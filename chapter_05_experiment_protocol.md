# Ch.5 — 숫자에는 조건이 붙는다

실험 수치는 조건과 함께 비교한다. 로보틱스 metric은 이름이 같아도 dataset, split, sensor, frame, calibration, alignment, metric script, failure policy, baseline이 다르면 같은 의미로 비교할 수 없다.

로보틱스 benchmark에는 수치뿐 아니라 evaluation script, dataset protocol, failure policy도 함께 제시된다. 낮은 error, 높은 success rate, 짧은 latency를 원고에 쓰려면 그 수치가 나온 조건도 함께 적어야 한다.

## 최소 기록

```text
dataset:
split:
sequence:
sensor/modality:
task input/output:
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

## 로보틱스 과제에서 볼 항목

| 항목 | 확인 내용 |
|---|---|
| coverage | 입력 구간과 출력 구간이 서로 맞는가 |
| output count | 예상 출력 수와 실제 출력 수가 맞는가 |
| timestamp span | 시작/종료 시간이 맞는가 |
| frame/calibration | frame convention과 calibration이 같은가 |
| preprocessing | resize, crop, filtering, normalization 조건이 같은가 |
| cache/checkpoint | 현재 model과 config에서 나온 결과물인가 |
| failure policy | 실패 구간을 평균이나 집계에서 어떻게 처리했는가 |

## 평가 조건에서 볼 항목

| 항목 | 확인 내용 |
|---|---|
| task input/output | 어떤 입력에서 어떤 출력을 평가하는가 |
| ground truth | 정답 파일, 좌표계, 시간 범위가 같은가 |
| threshold | success/failure를 가르는 기준이 같은가 |
| baseline | 같은 조건의 baseline인가 |
| metric script | 지난번과 같은 script인지 |
| output path | 실제로 읽은 결과 파일이 맞는지 |

원고 문장에는 조건을 넣는다.

> 같은 dataset, 같은 sensor 입력, 같은 metric script를 쓴 baseline 대비 main metric이 개선되었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

표 caption에도 같은 규칙을 적용한다. metric 표에는 수치와 비교 조건이 있어야 한다. event count 표가 직접 보여 주는 것은 센 횟수까지다. downstream task에 미친 영향까지 말하려면 추가 근거가 필요하다. 표 아래의 설명도 표가 직접 보여 주는 범위 안에서 쓴다.

실패한 실행도 기록할 결과다. timeout, OOM, sensor dropout, tracking lost, missing sequence, metric script failure, invalid ground truth는 다음 실험의 조건을 정하는 자료가 된다.
