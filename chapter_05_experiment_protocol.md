# Ch.5 — 실험 숫자는 조건 목록과 함께 읽는다

실험 숫자는 조건 없이 비교하지 않는다. ATE, RPE, Recall@K, precision-recall은 이름이 같아도 dataset, split, frame, alignment, query/database direction, positive rule, baseline이 다르면 다른 숫자다.

SLAM benchmark와 VPR tutorial 문헌도 숫자를 조건과 함께 읽어야 한다고 말한다. 낮은 RMSE나 높은 Recall@1을 원고에 쓰려면 그 숫자가 어떤 조건에서 나왔는지 같이 적어야 한다.

## 최소 기록

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

## SLAM/VIO에서 볼 항목

| 항목 | 확인 내용 |
|---|---|
| coverage | trajectory가 전체 bag을 덮는가 |
| pose count | 예상 pose 수와 출력 pose 수가 맞는가 |
| timestamp span | 시작/종료 시간이 맞는가 |
| tracking lost | 실패 구간을 어떻게 처리했는가 |
| alignment | SE(3), Sim(3), scale 처리 조건이 무엇인가 |
| failure policy | 실패 sequence를 평균에서 제외했는가 |

## VPR/retrieval에서 볼 항목

| 항목 | 확인 내용 |
|---|---|
| direction | camera-to-LiDAR인지 LiDAR-to-camera인지 |
| positive rule | exact frame인지 radius rule인지 |
| query count | invalid query 포함 여부 |
| feature source | backbone, projection head, teacher, student 구분 |
| cache version | feature cache가 현재 model에서 나온 것인지 |
| metric script | 지난번과 같은 script인지 |

원고 문장에는 조건을 넣는다.

> EuRoC MH_01-05에서 같은 alignment와 같은 metric script를 쓴 baseline 대비 ATE median이 줄었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

표 caption도 같은 규칙을 따른다. ATE 표는 dataset별 오차와 비교 조건을 말한다. loop closure 개수 표에는 탐지 수가 있다. precision, outlier rejection, pose graph 영향까지 말하려면 추가 근거가 필요하다. 표 아래 한 문장도 표가 직접 보여 준 범위 안에서만 쓴다.

실패도 결과다. timeout, OOM, sensor dropout, tracking lost, missing sequence, metric script failure, invalid ground truth는 다음 실험 조건을 정하는 자료가 된다.
