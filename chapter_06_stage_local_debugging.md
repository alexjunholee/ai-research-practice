# Ch.6 — 디버깅은 신호가 끊긴 단계를 찾는 일이다

AI는 root cause를 빨리 말한다. QoS, calibration, cache, normalization 같은 단어가 바로 나온다. 도움이 될 때도 있다. 어느 단계에서 신호가 끊겼는지 확인하기 전까지는 후보 설명으로 둔다.

복잡한 로보틱스 pipeline은 단계마다 다른 실패를 낸다. data loading, representation, matching, geometry, optimization, evaluation이 각각 다른 증상을 만든다. [Endsley의 situation awareness 모델](https://doi.org/10.1518/001872095779049543)은 먼저 현재 신호를 지각하고, 그 의미를 이해한 뒤, 다음 상태를 예측하는 순서를 잡았다. 디버깅도 먼저 신호를 보고, 그 신호가 어느 단계에서 나온 것인지 구분한 뒤, 다음 행동을 고른다.

## 기본 순서

```text
input
preprocessing
representation
matching
geometry
optimization
evaluation
```

## ROS2 callback이 비어 있을 때

수정 전에 다음을 본다.

1. `ros2 topic list`로 topic 존재 확인
2. `ros2 topic info --verbose`로 QoS 확인
3. publisher/subscriber namespace 확인
4. `use_sim_time`과 `/clock` 확인
5. container device, network, volume 확인
6. 그다음 코드 또는 launch 수정

## 일반적인 로보틱스 task에서 성능이 갑자기 떨어졌을 때

수정 전에 다음을 본다.

1. dataset, split, sensor input 범위 확인
2. timestamp, frame, calibration 확인
3. preprocessing과 normalization 확인
4. cache, checkpoint, intermediate output 확인
5. matching, geometry, optimization의 입력과 출력 확인
6. metric script와 failure policy 확인
7. 그다음 model architecture, training 설정, control parameter 수정

## 기록 형식

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

## 구분해야 할 실패

| 실패 종류 | 예 |
|---|---|
| 실행 환경 실패 | `pip install`, CUDA driver, Docker volume, dataset path |
| runtime 실패 | callback 없음, tf lookup 실패, node crash |
| 평가 실패 | wrong frame, wrong split, wrong metric script |
| 방법 실패 | 조건을 맞춰 확인한 뒤에도 성능이 낮음 |

build pass는 소스 컴파일을 확인한다. callback, tf lookup, metric correctness, output validity는 따로 확인한다.
