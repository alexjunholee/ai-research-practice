# Ch.6 — Stage-local debugging

## 목적

원인 이름을 맞히기 전에 pipeline의 어느 단계에서 신호가 끊겼는지 확인한다.

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

## ROS2 예시

subscriber callback이 비어 있으면 바로 launch file을 고치지 않는다.

1. `ros2 topic list`로 topic 존재 확인
2. `ros2 topic info --verbose`로 QoS 확인
3. publisher/subscriber namespace 확인
4. `use_sim_time`과 `/clock` 확인
5. container device, network, volume 확인
6. 그다음 코드 또는 launch 수정

## VPR 예시

성능이 갑자기 떨어졌을 때 model부터 바꾸지 않는다.

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
| 방법 실패 | 조건이 닫힌 뒤에도 성능이 낮음 |

build pass는 runtime success가 아니다. runtime success는 metric correctness가 아니다. 각 단계는
다른 증거를 요구한다.
