# 부록 F — 로봇 실험 문제 해결 안내서

로봇 실험에서 막혔을 때 원인을 추측으로 좁히려 들면 엉뚱한 설정을 고치기 쉽다. 이 안내서는 자주 부딪히는 증상마다 가장 먼저 실행해 볼 확인 명령과 점검 순서를 모아 둔 참고서다. 이 문서를 어느 단계에서 꺼내 쓰면 좋은지는 본문 3부 「증상에 맞는 첫 확인 명령을 찾는다」 절에 정리해 두었다.

## ROS 2에서 자주 막히는 문제

ROS 2 환경에서는 노드나 드라이버 코드 자체가 틀리기보다 QoS 설정, 시뮬레이션 시각 동기화, 작업 공간 소싱, 빌드 옵션, 네임스페이스처럼 실행 조건이 어긋나서 통신이 끊기는 일이 훨씬 잦다. 코드를 고치기 전에 아래 여섯 가지 조건부터 순서대로 짚어 본다.

### QoS 불일치로 토픽이 오지 않을 때

[ROS2의 기본 publisher·subscription profile](https://docs.ros.org/en/humble/Concepts/Intermediate/About-Quality-of-Service-Settings.html)은 reliability가 `RELIABLE`이지만, sensor data profile은 `BEST_EFFORT`를 쓴다. 카메라나 LiDAR 드라이버가 `BEST_EFFORT`로 데이터를 내보내는데 subscriber가 기본 profile(`RELIABLE`)로 받으려 하면 정책이 어긋나 처음부터 연결 자체가 맺어지지 않는다. 따라서 토픽이나 드라이버 내부를 의심하기 전에 먼저 양쪽의 실제 QoS 설정부터 확인한다.

```bash
# 토픽의 QoS 프로파일 확인
ros2 topic info /camera/image_raw --verbose
```

명령 출력에서 `Reliability: BEST_EFFORT`나 `Durability: VOLATILE` 같은 항목을 확인했다면, 아래처럼 subscriber의 QoS를 publisher 쪽에 맞추어 준다.

```python
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

qos = QoSProfile(
    reliability=ReliabilityPolicy.BEST_EFFORT,
    durability=DurabilityPolicy.VOLATILE,
    depth=10
)
self.subscription = self.create_subscription(Image, '/camera/image_raw', self.callback, qos)
```

에이전트에게 구독 코드를 요청할 때는 "이 토픽의 QoS는 BEST_EFFORT / SENSOR_DATA다"처럼 직접 확인해 둔 profile을 함께 적어 보내고, 돌려받은 코드에도 그 설정이 정확히 들어갔는지 다시 확인한다.

### use_sim_time과 tf2의 시간 불일치

rosbag을 `--clock` 옵션으로 재생할 때는 노드의 `use_sim_time:=true`도 함께 켜야 `tf` 조회가 현재 시각이 아니라 bag의 시각을 기준으로 동작한다. 실행 중에 `tf2 lookup failed` 오류가 뜬다면 `static_transform_publisher`를 급히 덧붙이기 전에 양쪽의 clock 설정이 맞물려 있는지부터 확인해야 한다. bag 파일의 timestamp는 데이터가 기록된 과거 시각인데, `use_sim_time`이 꺼진 노드는 현재 시스템 시각으로 transform을 찾기 때문이다. 아래와 같이 bag을 재생하면서 노드에 `use_sim_time`을 켜고, 파라미터가 실제로 반영됐는지까지 확인한다.

```bash
# bag clock을 publish하는 재생 예
ros2 bag play my_bag --clock

# 노드 실행 시 sim_time 활성화
ros2 launch my_package my_launch.py use_sim_time:=true

# 실제 노드에 적용됐는지 확인
ros2 param get /my_node use_sim_time
```

시각 동기화를 맞춘 뒤에도 예외 상황으로 노드가 죽지 않도록, `tf2` 조회 코드를 작성하거나 수정할 때는 아래와 같이 `timeout`과 예외 처리가 빠짐없이 들어갔는지 점검한다.

```python
from rclpy.duration import Duration

try:
    transform = tf_buffer.lookup_transform(
        'base_link', 'camera_link',
        rclpy.time.Time(),
        timeout=Duration(seconds=1.0)
    )
except tf2_ros.LookupException as e:
    self.get_logger().warn(f'TF lookup failed: {e}')
```

### ROS 2 작업 공간 소싱 순서

ROS 2 작업 공간을 불러올 때는 `/opt/ros/humble/setup.bash`를 먼저 `source`한 뒤, 그 위에 `~/ros2_ws/install/setup.bash`를 `source`해야 한다. 에이전트에게 실행 절차를 받았을 때도 base와 overlay workspace가 모두 들어 있는지, 그리고 불러오는 순서가 뒤바뀌지 않았는지 먼저 살펴야 한다.

```bash
# base를 먼저, overlay를 나중에 source
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

`.bashrc`에 경로를 적어 두었는데도 새 터미널에서 패키지가 보이지 않는다면, 패키지를 성급히 재설치하기 전에 현재 `source` 상태부터 점검한다. 이때 `echo $AMENT_PREFIX_PATH`를 실행하면 지금 셸에 어떤 workspace들이 어떤 순서로 적용되어 있는지 바로 드러난다.

### 커스텀 메시지 빌드와 반영

새 `.msg` 파일을 추가할 때는 메시지 파일만 만들지 말고 `CMakeLists.txt`와 `package.xml`의 의존성도 함께 고쳐야 한다. 에이전트가 낸 변경안을 검토할 때는 이 두 파일이 모두 빠짐없이 수정되었는지 확인한다. 특히 `rosidl_generate_interfaces` 설정이 빠져 있으면 `colcon build` 자체는 오류 없이 통과하더라도 막상 Python에서 `import`할 때 실패하게 되므로, 패키지 설치 상태를 의심하기에 앞서 인터페이스 생성 설정부터 짚어 본다.

```cmake
# CMakeLists.txt에 반드시 추가
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MyCustomMsg.msg"
  DEPENDENCIES std_msgs geometry_msgs
)
```

```xml
<!-- package.xml에 반드시 추가 -->
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<depend>std_msgs</depend>
<depend>geometry_msgs</depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

메시지나 Python 노드를 고친 뒤에는 `--symlink-install` 옵션을 붙여 빌드해야 수정한 Python 코드가 실행 환경에 곧바로 반영된다. 코드를 고쳤는데도 예전 동작이 그대로 나온다면, 빌드 캐시를 지우기에 앞서 빌드 옵션부터 확인한다.

```bash
# Python 패키지 수정이 바로 반영되려면
colcon build --symlink-install
```

### 네임스페이스와 리매핑

`ros2 topic echo /camera/image_raw`를 실행했을 때 아무 메시지도 뜨지 않는다면, 드라이버를 뜯어보기 전에 네임스페이스가 붙어 실제 토픽 이름이 `/robot1/camera/image_raw`처럼 바뀌지 않았는지부터 확인해야 한다. 먼저 현재 그래프에 올라온 토픽과 노드 이름을 대조하는 일이 우선이다.

```bash
# 토픽 목록부터 확인하라
ros2 topic list

# 특정 패턴으로 필터링
ros2 topic list | grep camera
```

문제를 좁히기 위해 에이전트에게 디버깅을 요청할 때도 `ros2 topic list`와 `ros2 node list`의 출력을 함께 넘겨주어야, 단순한 네임스페이스 불일치인지 노드 실행 자체의 문제인지를 단번에 가려낼 수 있다.

### ROS 2 launch 파일

에이전트가 작성한 ROS 2 Python `launch` 파일에서는 다음 네 가지 실수가 자주 섞여 나오므로, 실행하기 전에 먼저 훑어본다.

- ROS 1 XML 문법과 ROS 2 Python 문법의 혼용
- 노드 의존성을 놓친 `LaunchDescription` action 순서
- `ComposableNode`와 일반 `Node`의 혼동
- multi-robot 구성에서 `PushRosNamespace` 누락

여러 대의 로봇을 동시에 띄우는 구성이라면 아래처럼 `GroupAction` 안에 `PushRosNamespace`를 넣어 각 로봇 그룹의 노드마다 네임스페이스가 일관되게 붙도록 만든다.

```python
# multi-robot launch 파일에서 네임스페이스 적용
from launch.actions import GroupAction
from launch_ros.actions import Node, PushRosNamespace

robot1_group = GroupAction([
    PushRosNamespace('robot1'),
    Node(package='my_pkg', executable='my_node', name='sensor_node'),
])
```

따라서 에이전트에게 `launch` 파일 작성을 맡길 때는 ROS 2 Python 형식인지, multi-robot 네임스페이스가 필요한지, 그리고 `ComposableNode`를 쓰는지까지 조건을 분명히 밝혀 주어야 한다.

## Docker에서 자주 빠지는 설정

ROS 2 노드가 호스트에서는 멀쩡히 돌다가 Docker 컨테이너 안에서만 멈춘다면, 디스플레이 소켓이나 USB 장치 매핑, 네트워크 격리, 파일 소유권 가운데 하나가 막혀 있을 가능성이 크다. 컨테이너 안팎의 경계에서 자주 빠뜨리는 네 가지 설정을 차례로 확인한다.

### Docker GUI와 디스플레이 권한

Docker 안에서 RViz나 Gazebo 같은 GUI 도구를 띄우려면 X11이나 XWayland를 통해 display socket과 인증 정보를 컨테이너 안으로 넘겨주어야 한다. `xhost +local:docker`처럼 local X server를 모든 로컬 사용자에게 열어 두는 방법도 있지만, 보안 범위를 줄이려면 필요한 소켓만 골라 연결하는 편이 안전하다. 아래는 X11 socket을 넘기는 가장 기본적인 실행 예다. X server 인증 정보는 호스트 환경에 맞게 따로 넘기고, 접근 제어 자체는 켠 상태로 유지한다.

```bash
docker run -it \
  --env DISPLAY=$DISPLAY \
  --env QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  my_image
```

위 옵션만으로 GUI가 뜨지 않거나 바로 종료된다면 아래 세 가지 설정을 함께 확인한다.

- `QT_X11_NO_MITSHM=1` — Docker 안에서 MIT-SHM(공유 메모리) 확장 때문에 RViz가 죽는 현상을 막기 위해 이 확장을 끈다.
- `--ipc=host`가 있어야 돌아가는 프로그램도 있지만, 이 옵션은 호스트의 IPC namespace를 컨테이너와 그대로 공유한다. 따라서 무작정 붙이지 말고 실제 오류를 재현해 확인한 뒤에만 사용한다.
- Wayland session에서는 X11 socket mount만으로 화면이 열리지 않을 수 있다. 로그인할 때 Xorg session을 선택하거나 호스트의 XWayland·Wayland 권한 설정에 맞추어야 하며, 단순히 `XDG_SESSION_TYPE` 환경 변수만 바꾼다고 해서 이미 실행 중인 display server가 바뀌지는 않는다.

### USB 장치 연결

카메라, LiDAR, IMU 같은 USB 장치를 Docker 안에서 쓰려면 호스트의 device 파일을 컨테이너에 직접 매핑해야 한다. 장치 인식이 안 될 때 드라이버를 다시 설치하기에 앞서, 컨테이너 내부에서 해당 장치 노드가 실제로 보이는지부터 확인한다.

```bash
# 필요한 디바이스만 매핑
docker run -it --device=/dev/ttyUSB0 --device=/dev/video0 my_image

# 모든 디바이스 접근 허용 (보안상 비추, 디버깅용으로만)
docker run -it --privileged my_image
```

[Docker 문서](https://docs.docker.com/engine/containers/run/)에 따르면 `--privileged` 옵션은 모든 호스트 장치에 대한 접근 권한과 확장된 capability를 컨테이너에 한꺼번에 부여한다. 따라서 상시 운용 환경에서는 필요한 장치만 `--device`로 골라 매핑하는 것이 원칙이다. 또한 컨테이너를 띄운 뒤에 뒤늦게 꽂은 USB 장치는 기존 device mapping에 잡히지 않으므로, 이때는 컨테이너를 새로 띄우거나 디버깅 중에 한해서만 `--privileged`와 `-v /dev:/dev`를 함께 쓴다.

### Docker의 ROS 네트워크

Docker 컨테이너 사이에서 ROS 2 토픽을 주고받을 때 `--network=host`를 붙이면 설정이 간편해지지만, [호스트의 network namespace를 그대로 공유해 네트워크 격리(network isolation)를 없앤다](https://docs.docker.com/engine/network/drivers/host/). 따라서 포트 충돌이 생기지 않는지, 그리고 외부에 네트워크가 열려도 괜찮은 환경인지 함께 따져 보아야 한다. 반면 기본 bridge network 위에 올린 ROS 2 노드들이 서로를 찾지 못한다면, DDS(Data Distribution Service) discovery에 쓰이는 multicast 패킷이 컨테이너 경계를 넘는지부터 확인해야 한다. Docker bridge 설정에 따라 discovery packet이 컨테이너 바깥으로 나가지 못하고 갇히기 때문이다.

```bash
# 가장 간단한 방법 (개발 환경에서)
docker run -it --network=host my_ros2_image

# ROS_DOMAIN_ID로 다른 사람과 충돌 방지
docker run -it --network=host -e ROS_DOMAIN_ID=42 my_ros2_image
```

같은 네트워크 대역에서 `ROS_DOMAIN_ID`가 겹치면 다른 장비의 ROS 2 graph와 자동으로 연결된다. 연구실처럼 여러 사람이 한 네트워크에서 동시에 ROS 2를 돌리는 환경이라면 도메인 ID를 나누어 서로의 토픽이 섞이지 않게 막아야 한다.

여러 네트워크 인터페이스가 붙어 있는 환경에서 DDS 트래픽을 더 세밀하게 제어해야 할 때는 Cyclone DDS 설정 XML에 사용할 네트워크 인터페이스를 하나만 콕 집어 적는다. [현재 Cyclone DDS 설정 문서](https://github.com/eclipse-cyclonedds/cyclonedds/blob/master/docs/manual/options.md)에서는 인터페이스를 `General/Interfaces` 아래 `NetworkInterface` 요소로 지정한다.

```xml
<!-- cyclone_dds.xml -->
<CycloneDDS>
  <Domain id="any">
    <General>
      <Interfaces>
        <NetworkInterface name="eth0"/>
      </Interfaces>
    </General>
  </Domain>
</CycloneDDS>
```

작성한 설정 파일은 아래와 같이 `CYCLONEDDS_URI` 환경 변수로 지정해 적용한다.

```bash
export CYCLONEDDS_URI=file:///path/to/cyclone_dds.xml
```

### Docker 안팎의 파일 소유권

컨테이너를 기본값인 `root` 사용자로 실행해 마운트된 볼륨에 파일을 생성하면, 호스트 쪽에서도 파일이 `root` 소유로 남는다. 그 결과 호스트에서 파일을 고치거나 지울 때마다 `sudo`를 붙여야 하는 불편이 생긴다. 실행할 때 호스트 사용자의 `uid`와 `gid`를 그대로 넘겨주면 컨테이너 안에서 만든 파일도 호스트 사용자 소유로 남는다.

```bash
# 호스트 사용자 권한으로 실행
docker run -it --user $(id -u):$(id -g) my_image
```

다만 `--user` 옵션만으로 실행하면 컨테이너 내부의 장치 노드나 특정 디렉터리 권한이 맞지 않아 ROS 패키지가 제대로 동작하지 않을 수 있다. 이때 `chmod 777`로 권한을 모두 열어 두기보다, 아예 `Dockerfile` 안에서 non-root 사용자를 만들고 시리얼 포트 접근 등에 필요한 그룹과 디렉터리 권한만 부여해 두는 편이 깔끔하다.

```dockerfile
# Dockerfile에서 non-root 유저 설정
RUN useradd -m -s /bin/bash rosuser && \
    usermod -aG dialout rosuser
USER rosuser
```

## 센서·하드웨어·실시간 조건

컨테이너와 ROS 2 설정을 맞췄는데도 센서 데이터가 들쭉날쭉하거나 제어 주기가 흔들린다면, 한 층 아래의 하드웨어·커널·아키텍처 조건을 살펴볼 차례다. 시리얼 포트 권한과 USB 대역폭, LiDAR 네트워크, 카메라 노출, Jetson ARM 환경, 그리고 제어 루프 주기까지 여섯 지점을 차례대로 점검한다.

### 시리얼 포트 권한

`/dev/ttyUSB0`에 연결하려 할 때 `Permission denied` 오류가 뜨면 `sudo chmod 666 /dev/ttyUSB0`으로 당장 접근을 열 수는 있다. 하지만 이렇게 임시로 풀어 둔 권한은 시스템을 재부팅하거나 USB 케이블을 뺐다 다시 꽂는 순간 초기화된다. 장치를 다시 연결해도 이름과 권한이 그대로 유지되게 하려면 아래 순서대로 `udev` 규칙을 등록해야 한다. 먼저 장치의 벤더 ID와 프로덕트 ID를 조회한다.

```bash
# 벤더/프로덕트 ID 확인
udevadm info -a -n /dev/ttyUSB0 | grep -E 'idVendor|idProduct'
```

조회한 ID를 바탕으로 `/etc/udev/rules.d/99-sensors.rules` 파일에 규칙을 작성한다.

```bash
# /etc/udev/rules.d/99-sensors.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="1546", ATTRS{idProduct}=="01a9", GROUP="dialout", MODE="0660", SYMLINK+="gps"
```

규칙 파일을 저장한 뒤에는 `udevadm`으로 규칙을 다시 불러오고 현재 계정을 `dialout` 그룹에 추가한다.

```bash
# udev rule 적용
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo usermod -aG dialout "$USER"  # 다시 로그인한 뒤 group 적용
```

이 설정을 마치고 다시 로그인하면 해당 USB 장치는 포트 번호가 바뀌더라도 항상 `/dev/gps`라는 고정 심볼릭 링크로 잡히고 권한도 자동으로 적용된다. 만약 같은 모델의 센서를 여러 대 동시에 꽂아 쓴다면, 각 장치의 시리얼 번호(`ATTRS{serial}`)까지 규칙에 함께 넣어 서로 뒤섞이지 않게 구분한다.

### USB 대역폭

USB 3 카메라 여러 대를 하나의 허브에 물렸을 때 프레임이 중간중간 끊긴다면, 드라이버 설정을 만지기 전에 USB 컨트롤러의 대역폭 포화부터 의심해 보아야 한다. 아래 명령으로 장치들이 어느 컨트롤러에 몰려 있는지 확인한다.

```bash
# 어떤 카메라가 어떤 USB 컨트롤러에 붙어있는지 확인
lsusb -t
```

만약 여러 카메라가 같은 버스(Bus) 아래 몰려 있어 대역폭이 원인인 것으로 드러났다면, 소프트웨어 설정이 아니라 물리적 배선부터 바꾸어야 한다. `lsusb -t` 출력의 `Bus` 번호를 보면서 카메라들을 서로 다른 USB 컨트롤러에 분산해 꽂는다. 데스크톱 PC에서는 본체 앞면 포트와 뒷면 포트가 서로 다른 컨트롤러에 연결되어 있는 경우도 많으므로 포트를 옮겨 보며 대역폭을 나눈다.

### LiDAR의 IP와 UDP 연결

Velodyne이나 Ouster 같은 이더넷 LiDAR에서 데이터가 들어오지 않을 때도, 드라이버를 지웠다 다시 깔기 전에 네트워크 설정부터 확인해야 한다. 고정 IP나 서브넷 마스크가 어긋나 있어도 드라이버 쪽에서는 똑같이 연결 실패로 보이기 때문이다. 대부분의 이더넷 LiDAR는 공장에서 정한 고정 IP나 특정 서브넷 대역을 쓰므로, 장치가 예컨대 `192.168.1.201/24`라면 호스트의 이더넷 인터페이스 역시 겹치지 않는 `192.168.1.x/24` 주소로 맞추어 주어야 한다. 물론 실제 IP 주소와 UDP 포트 번호는 사용 중인 장치 설정과 제조사 문서를 따른다. 연결 상태는 아래 세 단계로 차례차례 좁혀 나간다.

```bash
# 1단계: LiDAR에 ping이 되는지 확인
ping 192.168.1.201

# 2단계: 호스트 이더넷 인터페이스 IP 설정
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip link set eth0 up

# 3단계: UDP 패킷이 오는지 tcpdump로 확인
sudo tcpdump -i eth0 udp port 2368 -c 10
```

장치가 ICMP 응답을 허용한다면 `ping`으로 물리적 연결을 바로 확인할 수 있다. 설령 보안을 위해 ICMP를 막아 둔 장치라 하더라도, Wireshark나 `tcpdump`를 걸어 지정된 UDP 포트로 패킷이 실제로 들어오는지는 확인된다. 만약 패킷은 정상적으로 들어오는데 ROS 토픽만 비어 있다면, 그때 비로소 네트워크가 아니라 드라이버와 ROS 설정 쪽으로 확인 범위를 좁힌다.

### 카메라 드라이버와 v4l2

간단한 예제 코드에는 흔히 `cv2.VideoCapture(0)`처럼 인덱스 `0`만 적혀 있다. 하지만 실제 USB 카메라 한 대가 영상 스트림과 메타데이터용으로 `/dev/video0`과 `/dev/video1`을 동시에 만들어 내는 경우가 흔하므로, 코드를 돌리기 전에 장치 번호와 지원 포맷부터 확인하는 습관이 필요하다.

```bash
# 카메라 디바이스 매핑 확인
v4l2-ctl --list-devices

# 지원하는 포맷과 해상도 확인
v4l2-ctl -d /dev/video0 --list-formats-ext

# 이 장치가 지원하는 control 확인
v4l2-ctl -d /dev/video0 --list-ctrls
```

또한 카메라의 자동 노출(auto exposure)과 자동 화이트밸런스가 켜져 있으면 프레임마다 밝기가 출렁여 특징점 추출과 추적이 쉽게 흔들린다. 다만 제어 항목 이름과 허용 값의 범위는 드라이버와 Linux 커널 버전에 따라 달라지므로, 먼저 `--list-ctrls` 출력에서 정확한 이름을 확인해야 한다. 아래 명령은 최신 Linux 커널에서 쓰이는 이름이며, 구형 커널에서는 `exposure_auto`, `exposure_absolute`처럼 다른 이름으로 표시되기도 한다.

```bash
# 수동 노출 설정 (SLAM용)
v4l2-ctl -d /dev/video0 --set-ctrl=auto_exposure=1
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_time_absolute=100

# 화이트밸런스 고정
v4l2-ctl -d /dev/video0 --set-ctrl=white_balance_automatic=0
```

따라서 SLAM이나 시각 주행계(VO)가 자꾸 추적을 놓친다면 알고리즘 매개변수를 조정하기에 앞서 자동 노출과 화이트밸런스부터 고정해 본다. 그 상태에서 영상 밝기가 일정해지고 특징점 추적이 안정되는지를 먼저 확인해야 원인을 섞지 않는다.

### Jetson의 ARM·JetPack 환경

에이전트가 제안한 코드나 Docker 설정에는 x86 데스크톱 환경을 암묵적으로 전제한 의존성이 섞여 들어오기 쉽다. NVIDIA Jetson 보드에서 작업할 때는 ARM64 아키텍처와 JetPack 버전에서 비롯하는 제약을 반드시 함께 따져 보아야 한다.

- 패키지와 버전 조합에 따라 PyPI에 ARM64용 wheel이 아예 없을 수 있다. 이럴 때 무작정 소스 빌드로 넘어가기 전에 JetPack 패키지, NVIDIA 공식 컨테이너, 배포판 패키지 가운데 호환되는 배포물이 있는지부터 찾아본다.
- JetPack 버전이 CUDA, cuDNN, TensorRT의 호환 범위를 함께 결정한다. 개별 패키지만 최신 버전으로 올리면 라이브러리가 어긋나기 쉬우므로, 변경 전에 JetPack 호환표를 먼저 읽는다.
- Docker 이미지 역시 보드에 설치된 L4T·JetPack 릴리스와 맞물리는 ARM64 이미지를 골라야 한다. [NVIDIA JetPack release notes](https://docs.nvidia.com/jetson/jetpack/release-notes/index.html)에서 현재 조합을 대조해 본다.

실제 보드에 올라간 L4T 릴리스는 아래 명령으로 확인할 수 있으며, 확인한 태그에 맞추어 컨테이너 이미지를 내려받는다.

```bash
# L4T release 확인 (JetPack 버전은 이 L4T 번호로 NVIDIA 표에서 찾는다)
cat /etc/nv_tegra_release

# NVIDIA 문서의 r36.3 예시. 실제 장치에서는 확인한 L4T와 맞는 tag를 선택
docker pull nvcr.io/nvidia/l4t-jetpack:r36.3.0
```

에이전트에게 빌드 오류나 패키지 설치 문제를 물을 때도 "Jetson Orin, JetPack 5.1.2, CUDA 11.4 환경이다"처럼 장치에서 직접 확인한 버전 조합을 함께 적어 준다. (여기서 적은 숫자는 보고 형식을 보이기 위한 예시다.)

### 실시간 제어 주기

제어 루프 끝에 `time.sleep(0.01)`을 넣더라도 이는 최소 대기 시간만 보장할 뿐이다. 실제로 루프가 다음 회차를 시작하는 시점은 `do_control()`의 계산 시간과 운영체제의 스케줄링 상태가 함께 결정한다.

```python
# 주기 검증이 필요한 단순한 구현
import time
while True:
    do_control()
    time.sleep(0.01)  # 실제 주기는 계산 시간과 시스템 부하에 따라 달라진다
```

여기에 Python의 GIL(Global Interpreter Lock)과 일반 커널 스케줄링까지 겹치면 멀티스레드 환경에서 실행 시점이 더 크게 흔들린다. 엄격한 실시간성이 요구되는 제어기라면 C++ 구현과 RT(Real-Time) 커널(`PREEMPT_RT`) 같은 구성을 함께 검토해야 한다. 또한 코드에 목표 주기를 적어 두는 것만으로는 충분하지 않으므로, 아래 명령으로 실제 토픽의 관측 주파수를 재어 보아야 한다.

```bash
# 실제 퍼블리시 주파수 확인
ros2 topic hz /cmd_vel
```

코드에 적은 값은 어디까지나 목표치이고, `ros2 topic hz`가 찍어 주는 숫자가 실제로 관측된 수신 주파수다. 두 숫자 사이에 간극이 벌어진다면 연산 시간, OS 스케줄링, 통신 지연 세 가지 가운데 어디서 병목이 생기는지 차례로 짚어 나간다.

## 반복 실패의 원인을 좁히는 법

개별 설정을 하나씩 손봤는데도 같은 문제가 되풀이된다면, 증상을 표면에서만 덮지 말고 시뮬레이션과의 차이, 물리적 배선, 패키지 충돌, 그리고 커널·시스템 호출 수준까지 한 층씩 내려가며 원인을 분리해야 한다.

### 시뮬레이션에서만 동작하는 경우

Gazebo에서는 매끄럽게 돌던 코드가 실제 로봇 위에서만 실패한다면, 먼저 시뮬레이션 환경과 실제 하드웨어 환경이 어긋난 네 지점부터 대조해 본다.

- **센서 노이즈**: 시뮬레이터에 넣은 노이즈 모델이 실제 센서의 잡음 분포와 어긋난다.
- **통신 지연**: 시뮬레이션 내부 루프와 실제 시스템의 transport·queue·network 지연이 다르다.
- **타이밍 불일치**: 시뮬레이터의 clock·timestamp 조건과 실제 센서들 사이의 동기화 오차가 다르다.
- **좌표계 불일치**: URDF에 적은 센서 위치·각도와 실제 로봇에 장착된 위치가 미세하게 다르면 `tf`가 틀어진다.

에이전트에게 원인을 묻거나 수정안을 요청할 때도 막연히 "실제 로봇에서 안 된다"라고 쓰지 말고, "시뮬레이션에서 성공한 동작이 실제 로봇에서 실패한다. 센서 노이즈 수준은 X다. 통신 지연은 Y ms다. 좌표계는 Z 방법으로 보정했다"처럼 직접 측정한 차이를 수치로 적어 보내야 한다.

### 소프트웨어를 고치기 전에 하드웨어부터 확인한다

케이블 단선이나 접촉 불량, 전원 부족 같은 물리적 문제는 아무리 코드를 고쳐도 풀리지 않으며, 커널 로그와 장치 상태를 직접 들여다보아야 비로소 소프트웨어 오류와 가려낼 수 있다. 센서 데이터가 간헐적으로 끊길 때는 버퍼 크기나 타임아웃, QoS 설정만 살피지 말고 케이블과 USB 허브의 전원 상태도 함께 점검한다.

```bash
# 커널 로그에서 하드웨어 문제 단서 찾기
dmesg | tail -20

# USB 연결 해제/재연결 이벤트 확인
dmesg | grep -i usb | tail -20
```

`dmesg` 출력에 `USB disconnect`나 `device descriptor read/64, error -71` 같은 줄이 찍혀 나온다면 소프트웨어 문제가 아니라 물리적 연결이나 전원 불안정일 가능성이 크다. 이때는 설정을 건드리지 말고 케이블을 교체하거나, 외부 전원이 따로 들어가는 유전원 USB 허브를 물리고, 다른 포트에 옮겨 꽂아 증상이 달라지는지부터 비교한다.

### OpenCV 재설치 전 패키지·ABI 충돌 확인

라이브러리 버전이 꼬여 오류가 날 때도 가상환경이나 시스템 전체를 밀고 다시 설치하기 전에, 먼저 `pip show package_name`으로 버전을 확인해 어느 패키지끼리 부딪히는지부터 좁혀야 한다. 특히 OpenCV는 아래 네 패키지가 한 환경에 섞여 들어올 때 충돌이 잦다.

- `opencv-python` (기본)
- `opencv-python-headless` (GUI 없는 서버용)
- `opencv-contrib-python` (추가 모듈이 포함된 배포판)
- `cv_bridge` (ROS 패키지, 자체 OpenCV를 참조)

앞의 세 PyPI 패키지는 모두 똑같은 `cv2` 네임스페이스를 차지하므로 한 Python 환경에는 하나만 남겨 두어야 한다. 게다가 ROS의 `cv_bridge`는 시스템 OpenCV와 링크되는 경우가 많아, 여기에 `pip`로 깐 OpenCV를 섞어 두면 버전이나 ABI 충돌이 발생하기 쉽다. 따라서 먼저 현재 설치된 ROS 패키지와 Python이 실제로 불러오는 `cv2` 경로를 확인한 뒤 한쪽 배포 경로로 통일해야 한다.

```bash
# 현재 설치된 OpenCV 확인
pip show opencv-python opencv-python-headless opencv-contrib-python

# ROS Humble system package 상태와 실제 import 경로 확인
apt policy ros-humble-cv-bridge
python3 -c 'import cv2; print(cv2.__version__, cv2.__file__)'
```

만약 ROS Humble의 시스템 OpenCV와 `ros-humble-cv-bridge`를 기준으로 삼기로 결정했다면 Python의 import 경로가 그쪽을 먼저 가리키도록 정리한다. 반대로 불필요한 패키지를 지우기 전에는 그 패키지에 의존하는 다른 프로젝트가 남아 있지 않은지 먼저 확인한다.

### 반복 처방을 멈추고 원인을 추적한다

같은 처방을 두세 번 되풀이했는데도 증상이 그대로라면 추측을 멈추고 한 층 아래의 원시 신호를 직접 관측해야 한다. 커널·서비스 로그를 확인하고, `strace`로 시스템 호출을 따라가며, 네트워크 문제라면 실제 패킷까지 잡아 본다. 에이전트에게 디버깅을 요청할 때도 에러 메시지 한 줄만 던지지 말고 아래처럼 저수준 관측 결과를 함께 첨부해야 정확한 진단을 끌어낼 수 있다.

```bash
# 시스템 로그
dmesg | tail -30
journalctl -u my_service --since "5 minutes ago"

# 프로세스 추적
strace -f -e trace=open,openat,read,write ros2 run my_pkg my_node 2>&1 | head -100

# 네트워크 패킷 캡처
sudo tcpdump -i eth0 -w capture.pcap
```

이처럼 어느 계층에서 실패가 일어났는지 로그와 패킷으로 먼저 좁힌 다음, 그 결과는 `stage-local-debugging.md`에 남겨 같은 시행착오가 다음 세션으로 이어지지 않게 정리해 둔다.
