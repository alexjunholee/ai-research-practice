# Ch.6 — 실패 지점 찾기

AI에 오류를 물으면 QoS, calibration, cache, normalization 같은 원인 후보를 빠르게 얻을 수 있다. 이 답을 받아 바로 고치기 시작하면 지금 무엇이 돌고 있는지 보기 전에 원인이 정해진다. 답은 Ch.1의 다섯 줄 가운데 `AI가 만든 설명:` 칸에 적어 두고, 어느 단계에서 신호가 끊겼는지 눈으로 본 뒤에 꺼낸다.

[Endsley](https://doi.org/10.1518/001872095779049543)는 situation awareness를 시간과 공간의 한 범위 안에서 환경의 요소를 지각하는 것, 그 의미를 이해하는 것, 가까운 미래의 상태를 예측하는 것으로 정의했다. 확인된 것은 이 정의 한 문장까지다. 세 항목 각각을 원문이 어떻게 풀었는지는 못 봤다. 정의가 셋을 따로 세운 것처럼 이 책의 기록도 셋을 각각 다른 칸에 적는다. 눈으로 본 신호가 한 칸, 그 신호가 나온 단계가 한 칸, 아직 남은 원인 후보가 또 한 칸이다.

## 단계에 먼저 이름을 붙인다

복잡한 로보틱스 pipeline은 단계마다 다른 증상을 보인다. 어느 단계가 끊겼는지에 따라 볼 대상이 달라지므로 단계에 먼저 이름을 붙인다.

```text
input
preprocessing
representation
matching
geometry
optimization
evaluation
```

아래 두 목록은 이 일곱 이름을 그대로 쓴다. 앞의 목록은 한 단계 안에서 멈춘다. 뒤의 목록은 일곱을 처음부터 훑는다.

## 신호가 아예 안 올 때

받는 쪽 callback이 빈 채로 있으면 신호는 `input`에서 멈춘 상태다. 이어서 여섯 단계는 아직 입력을 받기 전이라 여기서 읽을 것은 `input` 하나다. 수정 전에 다음을 본다.

1. `ros2 topic list`로 topic 존재 확인
2. `ros2 topic info --verbose`로 QoS 확인
3. publisher/subscriber namespace 확인
4. `use_sim_time`과 `/clock` 확인
5. container device, network, volume 확인
6. 이어서 코드 또는 launch 수정

1부터 5까지 다섯 줄의 `stage:`는 모두 `input`이다. ROS2 기본 profile은 RELIABLE이고 sensor data profile은 BEST_EFFORT라 driver와 받는 쪽이 어긋나면 메시지가 안 온다. 2가 보는 것이 이 어긋남이다. topic이 오는 것을 눈으로 본 뒤에야 `next stage:`에 `preprocessing`을 적는다. 실행 환경 쪽 증상 하나하나를 어디서 볼지는 Ch.9에서 참조표로 세운다.

## 떨어진 숫자는 맨 위부터

성능 숫자 하나가 떨어졌을 때 그 값은 일곱 단계를 다 지나온 뒤에 나온 것이다. 어느 단계에서 떨어졌는지는 위에서부터 하나씩 짚어 본다. 수정 전에 다음을 본다.

1. dataset, split, sensor input 범위 확인
2. timestamp, frame, calibration 확인
3. preprocessing과 normalization 확인
4. cache, checkpoint, intermediate output 확인
5. matching, geometry, optimization의 입력과 출력 확인
6. metric script와 failure policy 확인
7. 그다음 model architecture, training 설정, control parameter 수정

1과 2는 `input`에 들어온 것과 거기 붙은 조건을 본다. 3은 `preprocessing`, 4는 `representation`, 5는 `matching`·`geometry`·`optimization`, 6은 `evaluation`이다. 앞 장에서 숫자마다 dataset과 split과 metric script를 적어 두었다면 1과 6은 그 기록을 다시 읽는 일이 된다. 7은 일곱 이름을 다 지나온 뒤에 남는다.

## 본 것을 적어 두는 형식

각 확인은 같은 형식으로 남긴다.

```text
stage:
command:
workdir:
observed signal:
changed file:
output path:
next stage:
```

`stage:`에는 위 일곱 이름 가운데 하나가 들어간다. `ros2 topic list`를 찍어 본 줄이면 `input`이고, metric script를 연 줄이면 `evaluation`이다. `observed signal:`에는 눈으로 본 것을, `next stage:`에는 이 확인 뒤에 옮겨 갈 이름을 적는다. 부록 D는 실행 중 문제의 시작점으로 `stage-local-debugging.md`를 둔다. 같은 부록이 적은 멈춤 조건 하나가 이 형식에서 바로 보인다. `next stage:`에 같은 이름이 두 번 이어서 들어가면 같은 단계에서 근거가 그대로인 상태다.

## 도구 탓인지 방법 탓인지

같은 `stage:`에 적힌 실패라도 종류가 갈리면 다음에 할 일이 갈린다.

| 실패 종류 | 예 |
|---|---|
| 실행 환경 실패 | `pip install`, CUDA driver, Docker volume, dataset path |
| runtime 실패 | callback 없음, tf lookup 실패, node crash |
| 평가 실패 | wrong frame, wrong split, wrong metric script |
| 방법 실패 | 조건을 맞춰 확인한 뒤에도 성능이 낮음 |

빌드 성공은 첫 줄에서 한 자리를 지운다. 소스가 컴파일됐다는 사실이 그 한 자리고, `pip install`과 CUDA driver와 Docker volume과 dataset path는 그대로 남는다. callback 없음과 tf lookup 실패는 둘째 줄에서 따로 본다. wrong metric script는 셋째 줄에서 따로 본다. output이 쓸 데에 맞는지는 `output path:`에 적은 파일을 열어 본다. 넷째 줄은 앞의 세 줄을 지운 뒤에 남는 자리다. 도구 실패와 방법 실패가 한 기록에 섞이면 부록 D가 적은 대로 멈춘다.

기록에 적힌 `stage:`와 실패 종류가 원고에 쓸 수 있는 문장의 어디까지를 정한다. 다음 장에서는 그 문장을 주장과 근거로 갈라 `claim-evidence-map.md`에 적는다.
