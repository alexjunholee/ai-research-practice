# Ch.9 — 로봇은 코드 밖에서 실패한다

## 로봇 실험에서 먼저 확인할 것

AI 코딩 에이전트(Claude, Copilot, ChatGPT 등)는 함수의 초안을 만들고 에러 메시지에서 원인 후보를 찾는 데 유용하다. 로보틱스에서는 하드웨어, OS, 네트워크, 실시간 조건이 함께 작동하므로 코드만 보고 원인을 정하기 어렵다. 현재 장치와 실행 상태를 보여 주지 않으면 에이전트도 그럴듯하지만 맞지 않는 설명을 내놓기 쉽다.

따라서 질문을 만들기 전에 토픽, 장치, 시계, 네트워크, 권한, 시스템 구조의 현재 상태를 기록한다. 이 관측값이 있어야 에이전트의 답도 구체적인 확인 절차로 이어진다.

## ROS에서 자주 막히는 지점

### QoS 설정

[ROS2의 기본 publisher·subscription profile](https://docs.ros.org/en/humble/Concepts/Intermediate/About-Quality-of-Service-Settings.html)은 RELIABLE이고, sensor data profile은 BEST_EFFORT다. 카메라와 LiDAR driver가 sensor data profile을 쓰는데 subscriber가 기본 profile을 쓰면 reliability가 호환되지 않아 메시지가 전달되지 않을 수 있다. 이 상태를 토픽이나 driver 문제로 오인하지 않으려면 실제 QoS부터 확인한다.

```bash
# 토픽의 QoS 프로파일 확인
ros2 topic info /camera/image_raw --verbose
```

출력에서 `Reliability: BEST_EFFORT`, `Durability: VOLATILE` 같은 정보를 확인하고 subscriber의 QoS를 맞춘다.

```python
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

qos = QoSProfile(
    reliability=ReliabilityPolicy.BEST_EFFORT,
    durability=DurabilityPolicy.VOLATILE,
    depth=10
)
self.subscription = self.create_subscription(Image, '/camera/image_raw', self.callback, qos)
```

코드를 요청할 때는 "이 토픽의 QoS는 BEST_EFFORT / SENSOR_DATA다"처럼 확인한 profile을 함께 제공한다. 생성된 코드에서도 그 값이 반영됐는지 다시 확인한다.

### use_sim_time과 tf2 타이밍

rosbag을 재생하면서 `use_sim_time:=true`를 설정하지 않으면 tf lookup이 실패할 수 있다. `tf2 lookup failed`가 보인다고 바로 `static_transform_publisher`를 추가하기 전에 clock 설정을 확인한다.

이 경우에는 시뮬레이션 clock과 시스템 clock의 불일치가 원인이다. Bag 파일의 timestamp는 기록 시점을 가리키지만 노드가 현재 시스템 시간을 기준으로 tf를 조회하면 해당 변환을 찾을 수 없다.

```bash
# bag clock을 publish하는 재생 예
ros2 bag play my_bag --clock

# 노드 실행 시 sim_time 활성화
ros2 launch my_package my_launch.py use_sim_time:=true

# 실제 노드에 적용됐는지 확인
ros2 param get /my_node use_sim_time
```

생성된 tf2 lookup 코드에는 timeout과 예외 처리가 빠질 수 있으므로 두 항목을 확인한다.

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

### Workspace 소싱 순서

ROS2 workspace에서는 `/opt/ros/humble/setup.bash`를 먼저 source하고 `~/ros2_ws/install/setup.bash`를 이어서 source한다. 생성된 실행 절차가 base와 overlay workspace를 모두 포함하는지, 순서가 맞는지 확인한다.

```bash
# base를 먼저, overlay를 나중에 source
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

`.bashrc`에 경로를 넣었는데 새 terminal에서 package를 찾지 못한다면 재설치보다 source 상태를 먼저 살핀다. `echo $AMENT_PREFIX_PATH`로 현재 적용된 workspace를 확인한다.

### 커스텀 메시지와 빌드

`.msg` 파일을 생성할 때는 `CMakeLists.txt`와 `package.xml`의 dependency도 함께 수정해야 한다. 생성된 변경안에서 이 두 파일이 빠지지 않았는지 확인한다.

`rosidl_generate_interfaces` 설정이 빠지면 build 이후 Python import 단계에서 실패할 수 있다. Package 설치 문제로 판단하기 전에 interface 생성 설정을 확인한다.

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

`--symlink-install` 없이 build하면 Python 코드 수정이 바로 반영되지 않는다. 이를 cache 문제와 혼동하지 않도록 build option도 기록한다.

```bash
# Python 패키지 수정이 바로 반영되려면
colcon build --symlink-install
```

### 네임스페이스와 리매핑

`ros2 topic echo /camera/image_raw`에 데이터가 없더라도 driver 문제라고 바로 단정할 수는 없다. namespace가 적용되어 실제 topic이 `/robot1/camera/image_raw`일 수 있다.

```bash
# 토픽 목록부터 확인하라
ros2 topic list

# 특정 패턴으로 필터링
ros2 topic list | grep camera
```

디버깅을 요청할 때는 `ros2 topic list`와 `ros2 node list` 출력을 함께 제공한다. "토픽이 안 들어온다"는 설명만으로는 namespace와 node 상태를 구분할 수 없다.

### Launch 파일

생성된 ROS2 Python launch 파일에서는 다음 오류가 섞이지 않았는지 확인한다.

- ROS1 XML 문법과 ROS2 Python 문법의 혼용
- 노드 의존성을 고려하지 않은 `LaunchDescription` action 순서
- `ComposableNode`와 일반 `Node`의 혼동
- multi-robot 구성에서 `PushRosNamespace` 누락

```python
# multi-robot launch 파일에서 네임스페이스 적용
from launch.actions import GroupAction
from launch_ros.actions import Node, PushRosNamespace

robot1_group = GroupAction([
    PushRosNamespace('robot1'),
    Node(package='my_pkg', executable='my_node', name='sensor_node'),
])
```

Launch 파일을 요청할 때는 ROS2 Python 형식인지, multi-robot namespace가 필요한지, `ComposableNode`를 사용할지를 명시한다.

## Docker에서 자주 빠지는 설정

### GUI/시각화 문제

Docker 안에서 RViz나 Gazebo 같은 GUI 도구를 X11·XWayland 경로로 실행할 때는 display socket과 인증을 전달해야 한다. 흔히 제시되는 `xhost +local:docker`는 local X server 접근 범위를 넓히므로 그대로 쓰지 않는다.

다음은 X11 socket을 넘기는 최소 예다. X server 인증은 host 설정에 따라 별도로 연결해야 하며, 접근 제어를 끄는 `xhost +`는 쓰지 않는다.

```bash
docker run -it \
  --env DISPLAY=$DISPLAY \
  --env QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  my_image
```

각 옵션의 역할은 다음과 같다.
- `QT_X11_NO_MITSHM=1` — Docker 환경에서 MIT-SHM(공유 메모리) 확장 때문에 RViz가 종료되는 경우 이를 비활성화한다.
- `--ipc=host`가 필요한 프로그램도 있지만, 이 옵션은 host의 IPC namespace를 공유한다. 오류를 재현해 필요성을 확인한 경우에만 추가한다.
- Wayland session에서는 X11 socket mount만으로 부족할 수 있다. 로그인할 때 Xorg session을 선택하거나, host의 XWayland·Wayland 권한 설정에 맞춘다. `XDG_SESSION_TYPE` 환경 변수만 바꿔 현재 display server가 전환되지는 않는다.

### USB 디바이스 패스스루

카메라, LiDAR, IMU 같은 USB 장치를 Docker 안에서 쓰려면 device를 명시적으로 매핑해야 한다. Driver를 다시 설치하기 전에 container 안에 device가 보이는지 확인한다.

```bash
# 필요한 디바이스만 매핑
docker run -it --device=/dev/ttyUSB0 --device=/dev/video0 my_image

# 모든 디바이스 접근 허용 (보안상 비추, 디버깅용으로만)
docker run -it --privileged my_image
```

[Docker 문서](https://docs.docker.com/engine/containers/run/)에 따르면 `--privileged`는 모든 host device 접근과 확장된 capability를 컨테이너에 준다. 상시 운용할 때는 필요한 device만 `--device`로 매핑한다.

Container를 시작한 뒤 USB 장치를 연결하면 기존 device mapping에 반영되지 않을 수 있다. 이 경우 container를 다시 시작하거나, 디버깅할 때만 `--privileged`와 `-v /dev:/dev` 조합을 검토한다.

### ROS 네트워킹

Docker 컨테이너 간 ROS2 통신에서 `--network=host`는 설정이 단순하지만 [host의 network namespace를 공유해 network isolation을 없앤다](https://docs.docker.com/engine/network/drivers/host/). 포트 충돌과 노출 범위를 함께 확인한다.

ROS2가 bridge network에서 통신하지 못한다면 DDS(Data Distribution Service) discovery에 쓰이는 multicast가 container 경계를 통과하는지 확인한다. Docker bridge 설정에 따라 discovery packet이 전달되지 않을 수 있다.

```bash
# 가장 간단한 방법 (개발 환경에서)
docker run -it --network=host my_ros2_image

# ROS_DOMAIN_ID로 다른 사람과 충돌 방지
docker run -it --network=host -e ROS_DOMAIN_ID=42 my_ros2_image
```

같은 네트워크에서 `ROS_DOMAIN_ID`가 겹치면 다른 시스템의 ROS2 graph와 연결될 수 있다. 연구실에서 여러 명이 동시에 ROS2를 쓸 때 서로의 토픽이 보이는 이유다.

DDS 설정을 세밀하게 해야 할 때는 Cyclone DDS config XML로 특정 네트워크 인터페이스만 사용하게 제한한다:

```xml
<!-- cyclone_dds.xml -->
<CycloneDDS>
  <Domain>
    <General>
      <NetworkInterfaceAddress>eth0</NetworkInterfaceAddress>
    </General>
  </Domain>
</CycloneDDS>
```

```bash
export CYCLONEDDS_URI=file:///path/to/cyclone_dds.xml
```

### 파일 권한 문제

Docker 안에서 생성된 파일은 기본적으로 root 소유가 될 수 있다. 이 경우 호스트에서 편집하거나 삭제할 때 `sudo`가 필요하다.

```bash
# 호스트 사용자 권한으로 실행
docker run -it --user $(id -u):$(id -g) my_image
```

Device나 directory 권한 때문에 `--user` 옵션을 적용한 뒤 ROS package가 동작하지 않는 경우도 있다. 이때 `chmod 777`로 범위를 넓히기보다 Dockerfile에 non-root user를 만들고 필요한 group과 directory 권한만 부여한다.

```dockerfile
# Dockerfile에서 non-root 유저 설정
RUN useradd -m -s /bin/bash rosuser && \
    usermod -aG dialout rosuser
USER rosuser
```

## 하드웨어와 드라이버 신호

### 시리얼 포트 권한

`/dev/ttyUSB0` 접근 시 `Permission denied`가 뜨면 `sudo chmod 666 /dev/ttyUSB0` 같은 일회성 조치를 제안받기 쉽다. 이 설정은 재부팅하거나 장치를 다시 연결하면 사라진다.

재연결 뒤에도 유지할 설정은 udev rule로 만든다.

```bash
# 벤더/프로덕트 ID 확인
udevadm info -a -n /dev/ttyUSB0 | grep -E 'idVendor|idProduct'
```

```bash
# /etc/udev/rules.d/99-sensors.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="1546", ATTRS{idProduct}=="01a9", GROUP="dialout", MODE="0660", SYMLINK+="gps"
```

```bash
# udev rule 적용
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo usermod -aG dialout "$USER"  # 다시 로그인한 뒤 group 적용
```

이렇게 하면 해당 USB 장치를 `/dev/gps`라는 고정 이름으로 연결하고 권한도 자동으로 설정할 수 있다. 같은 모델의 장치를 여러 개 쓸 때도 시리얼 번호를 규칙에 넣으면 서로 구분할 수 있다.

### USB 대역폭

USB3 카메라 여러 대를 같은 허브에 연결했을 때 프레임이 끊긴다면 드라이버뿐 아니라 USB 컨트롤러의 대역폭도 확인해야 한다.

```bash
# 어떤 카메라가 어떤 USB 컨트롤러에 붙어있는지 확인
lsusb -t
```

컨트롤러의 대역폭이 원인이라면 설정 변경만으로는 해결되지 않는다. `lsusb -t`의 Bus 번호를 확인한 뒤 카메라를 서로 다른 USB 컨트롤러에 나누어 연결한다. 데스크톱 PC에서는 앞면과 뒷면 포트가 다른 컨트롤러에 연결된 경우도 있다.

### LiDAR 연결 (IP 설정)

Velodyne이나 Ouster LiDAR에서 데이터가 들어오지 않을 때는 드라이버를 다시 설치하기 전에 네트워크 설정부터 확인한다. 고정 IP와 서브넷 불일치는 이 증상의 흔한 원인이다.

많은 Ethernet LiDAR는 고정 IP나 지정된 subnet 설정을 사용한다. 장치가 예를 들어 `192.168.1.201/24`라면 host interface도 충돌하지 않는 `192.168.1.x/24` 주소로 맞춘다. 실제 주소와 UDP port는 장치 설정과 제조사 문서를 우선한다.

```bash
# 1단계: LiDAR에 ping이 되는지 확인
ping 192.168.1.201

# 2단계: 호스트 이더넷 인터페이스 IP 설정
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip link set eth0 up

# 3단계: UDP 패킷이 오는지 Wireshark로 확인
sudo tcpdump -i eth0 udp port 2368 -c 10
```

장치가 ICMP에 응답한다면 `ping`으로 연결을 확인하고, 응답하지 않더라도 Wireshark나 `tcpdump`로 지정된 UDP port의 패킷이 들어오는지 살핀다. 패킷은 들어오는데 ROS 토픽에서 보이지 않을 때 드라이버와 ROS 설정으로 조사 범위를 좁힌다.

### 카메라 드라이버 (v4l2)

간단한 예제는 흔히 `cv2.VideoCapture(0)`만 보여준다. 그러나 USB 카메라 하나가 영상과 메타데이터용으로 `/dev/video0`, `/dev/video1`을 함께 만들기도 하므로 장치 번호를 먼저 확인해야 한다.

```bash
# 카메라 디바이스 매핑 확인
v4l2-ctl --list-devices

# 지원하는 포맷과 해상도 확인
v4l2-ctl -d /dev/video0 --list-formats-ext

# 이 장치가 지원하는 control 확인
v4l2-ctl -d /dev/video0 --list-ctrls
```

자동 노출(auto exposure)과 자동 화이트밸런스가 frame 사이의 밝기를 크게 바꾸면 특징점 추출과 추적이 불안정해질 수 있다. 지원하는 control 이름과 범위는 driver마다 다르므로 먼저 확인한다.

```bash
# 수동 노출 설정 (SLAM용)
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto=1
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_absolute=100

# 화이트밸런스 고정
v4l2-ctl -d /dev/video0 --set-ctrl=white_balance_automatic=0
```

SLAM이 불안정하다고 해서 곧바로 알고리즘 매개변수만 조정하지는 않는다. 자동 노출과 화이트밸런스를 고정했을 때 영상 밝기와 특징점 추출이 안정되는지도 함께 확인한다.

### Jetson (ARM) 환경

생성된 코드나 Docker 설정에는 x86 환경을 전제로 한 의존성이 섞일 수 있다. NVIDIA Jetson은 ARM64와 JetPack의 버전 제약을 함께 고려해야 한다.

주의해야 할 점:
- package와 version 조합에 따라 ARM64 wheel이 없을 수 있다. 이때는 source build를 시작하기 전에 JetPack package, NVIDIA container, 배포판 package 중 호환되는 배포물이 있는지 확인한다.
- JetPack 버전에 따라 CUDA, cuDNN, TensorRT의 호환 범위가 정해진다. 개별 패키지를 최신 버전으로 올리기 전에 JetPack 호환표를 확인한다.
- Docker image는 장치의 L4T·JetPack release와 호환되는 ARM64 image를 고른다. [NVIDIA JetPack release notes](https://docs.nvidia.com/jetson/jetpack/release-notes/index.html)에서 현재 조합을 먼저 확인한다.

```bash
# JetPack 버전 확인
cat /etc/nv_tegra_release

# NVIDIA 문서의 r36.3 예시. 실제 장치에서는 확인한 L4T와 맞는 tag를 선택
docker pull nvcr.io/nvidia/l4t-jetpack:r36.3.0
```

코드를 요청할 때는 "Jetson Orin, JetPack 5.1.2, CUDA 11.4 환경이다"처럼 실제 장치에서 확인한 조합을 명시한다. 이 숫자는 형식 예시이며 최신 권장 버전을 뜻하지 않는다.

### 실시간 제어와 타이밍

`time.sleep(0.01)`을 넣었다고 해서 루프가 정확히 100Hz로 실행되는 것은 아니다. `time.sleep()` 이후 실제로 다시 실행되는 시점은 계산 시간과 운영체제 스케줄링의 영향을 받는다.

```python
# 주기 검증이 필요한 단순한 구현
import time
while True:
    do_control()
    time.sleep(0.01)  # 실제 주기는 계산 시간과 시스템 부하에 따라 달라진다
```

Python의 GIL(Global Interpreter Lock)과 운영체제 스케줄링도 멀티스레드의 실행 시점에 영향을 준다. 엄격한 실시간성이 필요하다면 C++과 RT(Real-Time) 커널(PREEMPT_RT) 같은 구성을 검토한다.

```bash
# 실제 퍼블리시 주파수 확인
ros2 topic hz /cmd_vel
```

목표 주파수를 코드에 적는 데서 끝내지 말고 `ros2 topic hz`로 실제 퍼블리시 주기를 측정한다. 기대한 주파수와 실제 주파수가 다르면 계산 시간, 스케줄링, 통신 지연을 차례로 점검한다.

## 반복해서 막히는 패턴

### "It works in simulation"

Gazebo에서 동작한 코드가 실제 로봇에서는 실패할 수 있다. 이때 코드와 하드웨어 중 하나만 탓하기보다 다음과 같은 시뮬레이션과 현실의 차이를 확인한다.

- **센서 노이즈**: 시뮬레이터에 넣은 노이즈 모델과 실제 센서의 분포가 다를 수 있다
- **통신 지연**: 시뮬레이션과 실제 시스템의 transport·queue·network 지연이 다르다
- **타이밍 불일치**: 시뮬레이터의 clock·timestamp 조건과 실제 센서 간 동기화 오차가 다르다
- **좌표계 불일치**: URDF와 실제 로봇의 센서 위치/각도가 미세하게 다르면 tf가 틀어진다

에이전트에게 질문할 때도 "시뮬레이션에서는 되지만 실제 로봇에서는 실패한다. 센서 노이즈 수준은 X이고, 통신 지연은 Y ms이며, 좌표계는 Z 방법으로 보정했다"처럼 관측한 차이를 구체적으로 제공한다.

### 하드웨어 문제를 소프트웨어로 고치려 함

케이블 불량, 접촉 불량, 전원 부족은 로그와 장치 상태를 직접 보지 않으면 판단하기 어렵다. 센서 데이터가 간헐적으로 끊길 때는 버퍼 크기, 타임아웃, QoS뿐 아니라 케이블과 USB 허브의 전원도 함께 점검한다.

```bash
# 커널 로그에서 하드웨어 문제 단서 찾기
dmesg | tail -20

# USB 연결 해제/재연결 이벤트 확인
dmesg | grep -i usb | tail -20
```

`dmesg`에 `USB disconnect`, `device descriptor read/64, error -71` 같은 메시지가 보이면 물리적 연결이나 전원 문제부터 확인한다. 케이블을 바꾸고, 유전원 USB 허브를 쓰거나, 다른 포트에 연결해 증상이 달라지는지 비교한다.

### 재설치 전에 충돌 범위 좁히기

라이브러리 버전 충돌이 복잡해도 곧바로 환경 전체를 다시 설치하지는 않는다. 먼저 `pip show package_name`으로 버전을 확인하고 충돌하는 패키지의 범위를 좁힌다.

OpenCV에서는 다음 패키지가 한 환경에 섞이면서 충돌하는 경우가 잦다.

- `opencv-python` (기본)
- `opencv-python-headless` (GUI 없는 서버용)
- `opencv-contrib-python` (추가 모듈 포함)
- `cv_bridge` (ROS 패키지, 자체 OpenCV를 참조)

세 PyPI package는 같은 `cv2` namespace를 제공하므로 한 환경에 함께 설치하지 않는다. `cv_bridge`는 system OpenCV와 연결될 수 있어 pip OpenCV를 섞으면 version·ABI 충돌이 생길 수 있다. 현재 ROS package와 Python import 경로를 확인한 뒤 한 배포 경로를 고른다.

```bash
# 현재 설치된 OpenCV 확인
pip show opencv-python opencv-python-headless opencv-contrib-python

# ROS Humble system package 상태와 실제 import 경로 확인
apt policy ros-humble-cv-bridge
python3 -c 'import cv2; print(cv2.__version__, cv2.__file__)'
```

ROS Humble의 system OpenCV와 `ros-humble-cv-bridge`를 쓰기로 했다면 별도의 pip OpenCV가 import 경로를 가로채지 않도록 구성한다. Package 제거는 의존하는 project를 확인한 뒤 한다.

### 반복 시도에서 원인 추적으로 전환하기

같은 처방을 반복해도 증상이 달라지지 않으면 접근법의 수를 늘리기보다 관측 수준을 낮춘다. 시스템 로그를 읽고, `strace`로 호출을 추적하며, 필요하면 패킷을 캡처한다.

더 나은 답을 얻으려면, 에러 메시지뿐 아니라 low-level 정보를 함께 줘야 한다:

```bash
# 시스템 로그
dmesg | tail -30
journalctl -u my_service --since "5 minutes ago"

# 프로세스 추적
strace -f -e trace=open,read,write ros2 run my_pkg my_node 2>&1 | head -100

# 네트워크 패킷 캡처
sudo tcpdump -i eth0 -w capture.pcap
```

이 정보를 에이전트에게 제공하면 일반적인 재설치 처방보다 현재 시스템의 증거에 맞춘 분석을 받기 쉽다.

## 에이전트에게 줄 정보

*논문 읽기와 글쓰기에서 에이전트를 쓰는 법은 [「연구노트」 Ch.7 — 논문을 세 번에 나누어 읽기](../research-notes/guide.html#chapter-7)와 [「연구노트」 Ch.16 — 마음가짐](../research-notes/guide.html#chapter-16)에서 다룬다. 여기서는 코드와 하드웨어를 다룰 때 필요한 입력에 집중한다.*

### 환경과 증상을 함께 제공한다

에이전트의 답은 질문에 포함된 환경 정보와 관측 자료에 크게 좌우된다.

정보가 부족한 예: "카메라가 안 돼요"

조사 범위를 좁힐 수 있는 예: "Ubuntu 22.04, ROS2 Humble, Intel RealSense D435를 쓴다. `rs-enumerate-devices`에서는 보이지만 `ros2 launch realsense2_camera rs_launch.py`를 실행하면 `Could not open device` 오류가 난다. Docker 안에서 실행 중이고, `--device=/dev/video0`은 매핑했다."

**함께 제공할 정보**:
- OS 버전, ROS 버전
- 하드웨어 플랫폼 (x86 vs ARM/Jetson)
- 센서 모델명
- 오류 메시지 전문
- `ros2 topic list`, `ros2 node list` 출력
- Docker 사용 여부와 실행 옵션 (`docker run` 명령 전체)
- 네트워크 구성 (유선/무선, IP 대역)

### 답을 실행하기 전에 검증하는 방법

제안받은 명령이나 설정을 적용하기 전에 다음을 확인한다.

- **패키지 설치** → 해당 패키지가 현재 ROS와 Ubuntu 버전을 지원하는지 `apt search ros-humble-PACKAGE_NAME` 등으로 확인한다.
- **설정 변경** → 현재 설정을 백업하고, 제안이 어떤 관측 결과를 설명하는지 확인한다.
- **환경 재설치** → 먼저 `pip show`, `dpkg -l | grep`, `apt policy` 등으로 현재 상태와 충돌 범위를 기록한다.
- **생성된 코드** → 하드코딩된 경로(`/home/user/...`), IP(`192.168.1.100`), x86 전용 패키지(`amd64` wheel)가 포함되어 있는지 확인한다.

### 맡기기 좋은 일과 직접 측정할 일

| 에이전트로 초안을 만들기 좋은 일 | 현장에서 측정값을 확보해야 하는 일 |
|---|---|
| 알고리즘 구현 (SLAM, detection 등) | 하드웨어 디버깅 |
| ROS2 노드/서비스 코드 작성 | QoS/DDS 설정의 실제 성능 확인 |
| Python/C++ 코드 리팩토링 | USB/시리얼 장치 상태 확인 |
| 논문 읽기/요약 | LiDAR 연결과 네트워크 패킷 확인 |
| CMakeLists.txt 작성 | 실시간 주기와 지터 측정 |
| 데이터 전처리 파이프라인 | Docker 안팎의 장치 접근 확인 |
| 시각화 코드 (matplotlib, Open3D) | 센서 간 시간 동기화 실전 |
| 일반적인 오류 메시지의 해석 | `dmesg`와 커널 로그를 현장 증상과 대조하는 일 |

에이전트는 코드 초안과 일반적인 오류 해석에 유용하다. 반면 하드웨어와 소프트웨어의 경계에서는 장치 상태, 타이밍, 패킷처럼 현장에서만 얻을 수 있는 정보가 필요하다. 먼저 직접 측정한 뒤 그 결과를 분석 입력으로 제공하는 편이 낫다.

## 연구 루틴에 붙이는 법

앞의 원칙은 논문 읽기, 코드 작성, 실험 설계, 원고 작성에 각각 다르게 적용된다.

### 논문 읽기

*논문 읽기 워크플로우(3-pass + AI layer)는 [「연구노트」 Ch.7 — 논문을 세 번에 나누어 읽기](../research-notes/guide.html#chapter-7)에서 다룬다.*

중요한 논문은 3-pass 방식으로 읽으면서 에이전트의 요약을 보조 자료로 쓴다. 초록을 읽은 뒤 기여를 세 문장으로 정리하게 하고, 이해하기 어려운 식은 단계별 유도를 요청한다.

### 코드 작성

- 프로토타이핑: "KITTI 데이터셋에서 ORB 특징점 뽑아서 매칭하는 코드 짜줘. OpenCV 쓰고, Lowe's ratio test 0.75로" — 이런 식으로 구체적으로 지시
- 디버깅: 오류 메시지와 관련 코드를 함께 주고 가능한 원인과 확인 순서를 요청
- 리팩토링: "이 코드를 PyTorch Dataset 클래스로 바꿔줘" — 구조 변환에 강함
- 직접 확인할 것: ROS QoS, 하드웨어 권한, 네트워크 설정, 실시간 타이밍

### 실험 설계

*실험 설계·ablation·결과 해석에 AI를 쓰는 방법은 [「연구노트」 Ch.32 — Revision/Rebuttal](../research-notes/guide.html#chapter-32)과 [「연구노트」 Ch.27 — Figures](../research-notes/guide.html#chapter-27)에서 다룬다.*

실험을 설계할 때는 baseline 비교 표를 제공하고 *내가 놓친 비교 축*을 묻는다.

### 논문 쓰기

- 초고 작성: 핵심 아이디어와 실험 결과를 제공하고 Introduction의 논리 구조를 제안받기
- 문법·표현 교정: 영어 문장의 문법과 문맥을 함께 검토하기
- 문체 검토: 생성된 문장을 그대로 쓰지 않고 자신의 논지와 어조에 맞게 다시 읽기
- BibTeX 생성: 서지 항목의 초안을 받은 뒤 논문 원문이나 출판사 페이지에서 연도, 학회·저널명, 권·호를 확인하기

### 일상 워크플로우 예시

다음은 이 작업들을 하루 일정에 배치한 예다.

```
09:00 — 새 논문 3편 arXiv에서 확인. AI에게 각각 1문장 요약 요청
09:30 — 흥미로운 1편 선택, 2패스 읽기. 모르는 수식은 AI에게 유도 요청
10:30 — 어제 학습 결과 분석. loss curve 캡처해서 AI에게 "이 패턴이 정상인가?" 확인
11:00 — 새 실험 코드 작성. AI에게 DataLoader 구조 생성 시킴. 수동으로 augmentation 로직 수정
14:00 — SLAM 코드 디버깅. ROS2 에러 → topic과 QoS 출력으로 원인 좁히기
16:00 — 논문 Related Work 섹션 초고. AI에게 비교 논문 5편의 차이점 표 만들게 시킴
17:00 — 표 검증. AI가 2편의 method를 혼동한 것 발견, 수동 수정
```
