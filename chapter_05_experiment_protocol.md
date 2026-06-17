# Ch.5 — 실험과 metric protocol

## 목적

실험 숫자가 어떤 조건에서 나온 값인지 기록한다. 조건이 닫히지 않은 숫자는 원고 claim으로 쓰지
않는다.

## 최소 protocol

```text
dataset:
split:
sequence:
sensor/modality:
query/database direction:
ground-truth frame:
alignment:
metric:
threshold:
baseline:
command:
config:
output path:
timeout:
failure policy:
```

## SLAM/VIO 확인 항목

| 항목 | 확인 내용 |
|---|---|
| coverage | trajectory가 전체 bag을 덮는가 |
| pose count | 예상 pose 수와 출력 pose 수가 맞는가 |
| timestamp span | 시작/종료 시간이 맞는가 |
| tracking lost | 실패 구간을 어떻게 처리했는가 |
| alignment | SE(3), Sim(3), scale 처리 조건이 무엇인가 |
| failure policy | 실패 sequence를 평균에서 제외했는가 |

## VPR/retrieval 확인 항목

| 항목 | 확인 내용 |
|---|---|
| direction | camera-to-LiDAR인지 LiDAR-to-camera인지 |
| positive rule | exact frame인지 radius rule인지 |
| query count | invalid query 포함 여부 |
| feature source | backbone, projection head, teacher, student 구분 |
| cache version | feature cache가 현재 model에서 나온 것인지 |
| metric script | 지난번과 같은 script인지 |

## 허용되는 문장

좋은 문장은 조건을 포함한다.

> EuRoC MH_01-05에서 같은 alignment와 같은 metric script를 쓴 baseline 대비 ATE median이 줄었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

## 실패 결과 기록

성공 숫자만 남기지 않는다. 다음 항목도 결과에 포함한다.

- timeout
- OOM
- sensor dropout
- tracking lost
- missing sequence
- metric script failure
- invalid ground truth

실패 분포는 방법의 한계를 설명하는 자료다.
