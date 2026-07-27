# Ch.5 — 숫자에는 조건이 붙는다

실제로 도는 코드를 갈라내고 실행을 걸면 수치가 나온다. 로보틱스 metric은 이름이 같아도 dataset, split, sensor, frame, calibration, alignment, metric script, failure policy, baseline이 다르면 서로 다른 조건을 잰 값이다. 두 수치를 나란히 놓는 일은 이 항목들이 같을 때 선다.

benchmark는 수치와 함께 evaluation script, dataset protocol, failure policy를 낸다. 그 수치를 받아 쓰는 쪽이 같은 수를 다시 얻으려면 그것들이 있어야 하기 때문이다. Pineau 등은 [NeurIPS 2019 재현성 프로그램](https://arxiv.org/abs/2003.12206)에서, 논문이나 발표에 제시된 것과 비슷한 결과를 같은 코드와, 구할 수 있으면 같은 데이터로 다시 얻는 일을 연구 결과의 신뢰성을 확인하는 데 필요한 단계로 적었다. 로보틱스에서는 코드와 데이터에 sensor 입력, frame, calibration, alignment이 더 붙는다. 낮은 error, 높은 success rate, 짧은 latency를 원고에 쓰려면 그 수치가 나온 조건도 함께 적어야 한다.

부록 D에 숫자를 다시 마주쳤을 때 던질 물음이 여섯 줄로 있다.

```text
Which dataset?
Which split?
Which direction?
Which metric script?
Which baseline?
Which output?
```

이 여섯 줄에 답이 붙은 수치가 원고에서 근거가 된다.

## 돌릴 때 그 자리에서 채운다

여섯 줄의 답은 실행을 걸 때 한 벌 적어 두면 그 자리에 남는다. 아래 칸은 command를 던지는 사람이 그 자리에서 채우고, 결과 파일이 나오면 output path를 마저 채운다.

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

dataset, split, baseline, output path 줄이 여섯 줄에 그대로 답한다. 나머지 칸은 같은 command를 다시 던지는 데 필요한 것을 남긴다.

## 숫자 읽기 전에 결과물부터

실행이 끝나면 metric 값을 읽기 전에 결과물 자체를 짚는다. 아래 항목은 output 디렉터리를 처음 여는 사람이 하나씩 본다.

| 항목 | 확인 내용 |
|---|---|
| coverage | 입력 구간과 출력 구간이 서로 맞는가 |
| output count | 예상 출력 수와 실제 출력 수가 맞는가 |
| timestamp span | 시작/종료 시간이 맞는가 |
| frame/calibration | frame convention과 calibration이 같은가 |
| preprocessing | resize, crop, filtering, normalization 조건이 같은가 |
| cache/checkpoint | 현재 model과 config에서 나온 결과물인가 |
| failure policy | 실패 구간을 평균이나 집계에서 어떻게 처리했는가 |

한 항목이 어긋나면 그 수치는 보류하고, 어긋난 자리를 최소 기록에 적는다.

## 두 실행이 같은 걸 재고 있나

결과물이 맞으면 그 수치를 baseline이나 지난번 수치 옆에 놓는다. 그 직전에 두 실행이 같은 것을 재고 있는지를 아래 항목으로 짚는다.

| 항목 | 확인 내용 |
|---|---|
| task input/output | 어떤 입력에서 어떤 출력을 평가하는가 |
| ground truth | 정답 파일, 좌표계, 시간 범위가 같은가 |
| threshold | success/failure를 가르는 기준이 같은가 |
| baseline | 같은 조건의 baseline인가 |
| metric script | 지난번과 같은 script인지 |
| output path | 실제로 읽은 결과 파일이 맞는지 |

metric script, baseline, output path는 여섯 줄이 묻던 것이다. 실행할 때 적어 둔 값과 지금 읽는 값이 같으면 두 수치가 한 표에 들어간다.

## 원고 문장에 조건을 단다

두 표를 짚고 나면 그 수치로 말할 수 있는 어디까지가 정해진다. 원고 문장에는 조건을 넣는다.

> 같은 dataset, 같은 sensor 입력, 같은 metric script를 쓴 baseline 대비 main metric이 개선되었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

표 caption에도 같은 규칙을 적용한다. metric 표에는 수치와 비교 조건이 있어야 한다. 로보틱스 원고에는 metric 표와 함께 실행 중 일어난 사건을 센 event count 표가 들어간다. event count 표가 직접 보여 주는 것은 센 횟수까지다. 그 결과를 입력으로 받는 downstream task까지 영향이 갔다고 쓰려면 추가 근거가 필요하다. 표 아래의 설명도 표가 직접 보여 주는 데까지 쓴다.

## 실패한 실행도 기록할 결과다

최소 기록의 칸은 결과 파일이 나온 실행을 받는다. 실패한 실행도 기록할 결과다. timeout, OOM, sensor dropout, tracking lost, missing sequence, metric script failure, invalid ground truth는 다음 실험의 조건을 정하는 자료가 된다. 목록의 failure policy 칸은 집계에서 실패 구간을 어떻게 다뤘는지를 받고, 멈춘 실행에는 목록을 한 벌 따로 적어 어디까지 갔는지를 남긴다. 어느 단계에서 끊겼는지를 가르는 일은 다음 장이 맡는다.
