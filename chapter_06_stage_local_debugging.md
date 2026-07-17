# Ch.6 — 실패 지점 찾기

AI에 오류를 물으면 QoS, calibration, cache, normalization 같은 원인 후보를 빠르게 얻을 수 있다. 다만 어느 단계에서 신호가 끊겼는지 확인하기 전까지는 그 답을 후보로 남겨 둔다.

복잡한 로보틱스 pipeline은 단계마다 다른 증상을 보인다. data loading, representation, matching, geometry, optimization, evaluation 중 어느 단계가 실패했는지에 따라 확인할 대상도 달라진다. [Endsley의 situation awareness 모델](https://doi.org/10.1518/001872095779049543)은 먼저 현재 신호를 지각하고, 그 의미를 이해한 뒤, 다음 상태를 예측하는 순서를 제시했다. 디버깅에서도 먼저 신호를 관찰하고 그 신호가 나온 단계를 구분한 뒤 다음 행동을 고른다.

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

## 로보틱스 과제의 성능이 갑자기 떨어졌을 때

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

빌드 성공은 소스가 컴파일됐다는 사실만 확인한다. callback, tf lookup, metric correctness, output validity는 각각 따로 확인해야 한다.
