# Ch.6 — 디버깅은 신호가 끊긴 단계를 찾는 일이다

AI는 root cause를 빨리 말한다. QoS, calibration, cache, normalization 같은 단어가 바로 나온다. 도움이 될 때도 있다. 어느 단계에서 신호가 끊겼는지 확인하기 전까지는 후보 설명으로 둔다.

복잡한 로보틱스 pipeline은 단계마다 다른 실패를 낸다. data loading, representation, matching, geometry, optimization, evaluation이 각각 다른 증상을 만든다. 상황 인식 연구에서도 먼저 현재 신호를 보고, 그 신호가 어느 단계에서 나온 것인지 구분한 뒤, 다음 행동을 고른다.

## 기본 순서

```text
input
preprocessing
representation
matching/retrieval
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

## VPR 성능이 갑자기 떨어졌을 때

수정 전에 다음을 본다.

1. query/database split 확인
2. cached feature version 확인
3. normalization 확인
4. index order 확인
5. positive radius 확인
6. metric script 확인
7. 그다음 model architecture 또는 training 설정 수정

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

build pass로 알 수 있는 것은 소스가 컴파일됐다는 사실뿐이다. callback, tf lookup, metric correctness, trajectory validity는 따로 확인한다.
