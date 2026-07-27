# Ch.5 — 숫자에는 조건이 붙는다

실제로 도는 코드를 갈라내고 실행을 걸면 수치가 나온다. 로보틱스 metric은 이름 하나에 조건이 여럿 붙는다. dataset과 split, sensor와 frame, calibration과 alignment, metric script, failure policy, baseline 가운데 하나만 달라도 두 값은 서로 다른 조건을 잰 값이 된다. 두 수치를 나란히 놓는 일은 이 항목들이 같을 때 선다.

이 항목들이 같은지는 수치를 내놓은 쪽이 무엇을 함께 냈는지에서 갈린다. benchmark는 수치를 내면서 evaluation script와 dataset protocol, failure policy를 같이 낸다. 그 수치를 받아 쓰는 쪽이 같은 수를 다시 얻으려면 그것들이 있어야 하기 때문이다. Pineau 등은 [NeurIPS 2019 재현성 프로그램](https://arxiv.org/abs/2003.12206)에서, 같은 코드와, 구할 수 있으면 같은 데이터로 논문이나 발표에 제시된 것과 비슷한 결과를 다시 얻는 일을 연구 결과의 신뢰성을 확인하는 데 필요한 단계로 적었다. 로보틱스에서는 코드와 데이터에 sensor 입력, frame, calibration, alignment가 더 붙는다. error가 낮다거나 success rate가 높다거나 latency가 짧다고 원고에 쓰려면 그 수치가 나온 조건도 같이 적어야 한다.

조건을 숫자로 적어 둔 실행 환경도 있다. Anthropic의 [code execution tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)는 Claude가 Bash command를 돌리고 파일을 다루는 sandbox를 두고 그 경계를 숫자로 적었다. Python 3.11, 리눅스 컨테이너, x86_64, 메모리 5 GiB, 디스크 5 GiB, CPU 1개다. 코드를 셀 단위로 넘겨 돌리는 쪽에서는 셀 하나가 90초 벽시계 안에서 끝나야 한다. 어떤 수치를 이 sandbox에서 뽑았다면 latency를 재는 순간 이 값들이 그대로 그 수치의 조건이 되고, 셀 단위로 돌렸다면 90초도 함께 붙는다. 연구실 기계에서 잰 값에는 그 기계의 경계값이 같은 자리에 들어간다.

어느 기계에서 어느 dataset으로 잰 값인지를 수치마다 되짚으려면 물음이 한 벌 서 있어야 한다. 숫자를 다시 마주쳤을 때 던질 여섯 줄이 부록 D에 있다.

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

여섯 줄의 답은 실행을 걸 때 한 벌 적어 두면 그 자리에 남는다. 실행을 건 뒤에 같은 답을 맞추려면 command 이력과 config 파일과 결과 디렉터리를 각각 열어 봐야 한다. 아래 칸은 command를 던지는 사람이 그 자리에서 채우고, 결과 파일이 나오면 output path를 마저 채운다.

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

dataset과 split, baseline, output path 줄은 여섯 줄에 그대로 답한다. direction은 이름이 바뀌어 task input/output 칸으로 간다. metric script를 받는 칸은 metric이다. 나머지 칸이 남기는 것은 같은 command를 다시 던지는 데 드는 것들이다. 이 한 벌이 실행 하나의 최소 기록이다.

## 숫자 읽기 전에 결과물부터

실행이 끝나면 metric 값을 읽기 전에 결과물 자체를 짚는다. 최소 기록에 적은 칸은 실행을 걸 때 정한 조건이다. 그 조건대로 돌았는지는 나온 파일을 열어야 안다. 아래 항목은 output 디렉터리를 처음 여는 사람이 하나씩 본다. 여기 오는 것은 실행 하나만 열어 놓고 답이 나오는 항목이다. `coverage`는 그 실행의 입력 구간과 출력 구간을 서로 대 보면 답이 나오므로 이 표에 선다.

| 항목 | 확인 내용 |
|---|---|
| coverage | 입력 구간과 출력 구간이 서로 맞는가 |
| output count | 예상 출력 수와 실제 출력 수가 맞는가 |
| timestamp span | 시작/종료 시간이 맞는가 |
| frame/calibration | frame convention과 calibration이 같은가 |
| preprocessing | resize, crop, filtering, normalization 조건이 같은가 |
| cache/checkpoint | 현재 model과 config에서 나온 결과물인가 |
| failure policy | 실패 구간을 평균이나 집계에서 어떻게 처리했는가 |

`cache/checkpoint` 줄은 실행 환경이 요청 사이에 상태를 이어 줄 때 걸린다. 앞의 code execution tool 문서는 컨테이너가 약 5분 놀면 체크포인트로 저장됐다가 같은 컨테이너 ID로 되살아난다고 적었다. 도구 판을 `code_execution_20260120` 이후로 올리면 변수 바인딩까지 요청 사이에 남는다. 앞 요청에서 정한 값이 이번 요청에도 그대로 살아 있을 수 있으니, 결과물을 열어 그것이 지금의 model과 config에서 나온 것인지를 짚는다. 같은 문서는 컨테이너가 30일 뒤 만료된다고도 적었다.

한 항목이 어긋나면 그 수치는 보류하고, 어긋난 자리를 최소 기록에 적는다.

## 두 실행이 같은 걸 재고 있나

결과물이 맞으면 그 수치를 baseline이나 지난번 수치 옆에 놓는다. 그 직전에 두 실행이 같은 것을 재고 있는지를 아래 항목으로 짚는다. 아래에는 실행 둘을 맞대야 답이 나오는 항목만 세운다. `task input/output`이 그렇다 — 값은 한 실행의 파일에서 나오지만, 그 값이 옆에 놓을 실행의 값과 같은지는 둘을 대 봐야 갈린다.

| 항목 | 확인 내용 |
|---|---|
| task input/output | 어떤 입력에서 어떤 출력을 평가하는가 |
| ground truth | 정답 파일, 좌표계, 시간 범위가 같은가 |
| threshold | success/failure를 가르는 기준이 같은가 |
| baseline | 같은 조건의 baseline인가 |
| metric script | 지난번과 같은 script인지 |
| output path | 실제로 읽은 결과 파일이 맞는지 |

metric script, baseline, output path는 여섯 줄이 묻던 것이다. 실행할 때 적어 둔 값과 지금 읽는 값이 같으면 두 수치가 한 표에 들어간다.

`metric script` 줄에는 script 이름 말고 그 script가 돌아간 라이브러리 판도 걸린다. 앞의 code execution tool 문서는 이 sandbox의 인터넷이 완전히 막혀 있다고 적었다. 그래서 도는 것은 미리 깔린 패키지뿐이고, 그 목록이 pandas, numpy, scipy, scikit-learn, matplotlib, pyarrow, pypdf 등이다. 문서가 적어 둔 것은 패키지 이름까지다. 같은 물음을 연구실 기계에서 돌린 script에 걸면, 그 판을 적은 줄이 같은 자리에 들어간다.

## 원고 문장에 조건을 단다

두 표를 짚고 나면 그 수치로 어디까지 말할 수 있는지가 선다. 원고 문장에는 조건을 넣는다.

> 같은 dataset, 같은 sensor 입력, 같은 metric script를 쓴 baseline 대비 main metric이 개선되었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

표 caption에도 같은 규칙을 건다. metric 표에는 수치와 비교 조건이 있어야 한다. caption이 받을 것은 그 표가 무엇을 센 표인지에 따라 갈린다. 로보틱스 원고에는 metric 표 말고 실행 중 일어난 사건을 센 event count 표도 들어간다. event count 표가 직접 보여 주는 것은 센 횟수까지다. 그 결과를 입력으로 받는 downstream task까지 영향이 갔다고 쓰려면 추가 근거가 필요하다. 표 아래의 설명도 그 표가 보여 준 데까지만 쓴다.

## 실패한 실행도 기록할 결과다

최소 기록의 칸은 결과 파일이 나온 실행을 받는다. output path와 metric 칸이 결과 파일에서 채워지기 때문이다. 멈춘 실행에도 남길 것이 있다. timeout과 OOM, sensor dropout과 tracking lost, missing sequence, metric script failure, invalid ground truth는 다음 실험의 조건을 정하는 자료다. 최소 기록의 failure policy 칸은 집계에서 실패 구간을 어떻게 다뤘는지를 받고, 멈춘 실행에는 그 한 벌을 따로 적어 어디까지 갔는지를 남긴다. 실패 하나가 실행의 어느 지점에서 나왔는지에 따라 다음에 고칠 자리가 갈린다. 어느 단계에서 끊겼는지를 가르는 일은 다음 장이 맡는다.
