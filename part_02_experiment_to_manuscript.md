# 2부 — 실험에서 원고까지

저장소에 파일이 있다는 것과 그 파일이 실험에서 돌았다는 것은 서로 다른 사실이다. 논문에 적힌 방법까지 놓으면 갈라 볼 것이 셋이 된다. 논문에서 방법을 설명하는 문장은 저자의 주장이다. 그 주장이 어디까지 구현됐는지는 공개 코드를 열면 나온다. runtime 기록은 그 코드가 지금 환경에서 무엇을 내놓았는지까지 남긴다. 셋은 각각 따로 짚어 본다. 논문 한 편과 그 공개 저장소를 함께 열어 다시 돌려 보려 할 때 이 구분이 먼저 온다.

[NeurIPS 2019 Reproducibility Program 보고서](https://arxiv.org/abs/2003.12206)는 재현을 같은 code와 data로(구할 수 있을 때) 논문이나 발표에 실린 것과 비슷한 결과를 얻는 일로 적었다. 연구 결과의 신뢰성을 확인하려면 거쳐야 하는 단계로 두었다. 같은 프로그램의 ML Reproducibility checklist는 다섯 절로 나누어 물었고, 그중 셋의 제목이 이론적 주장, 공개한 코드, 보고한 실험 결과다. 눈으로 본 것은 절 제목까지다. 공개한 코드와 보고한 실험 결과가 다른 절에 놓였다는 것만 여기서 가져온다.

다시 돌려 보려면 어느 code와 어느 data인지부터 정한다. 그 둘은 셋을 갈라 둔 자리에서 나온다. 저장소에서 이름으로 찾아 나온 파일과 그 실행이 지나간 파일이 같은 것인지까지 정해야 어느 code인지가 하나로 선다. 논문에 적힌 component가 저장소에 있으면 config를 거쳐 실제로 호출되는지, 결과에 영향을 주는지를 이어서 짚어 본다.

논문 초록과 저장소 README에도 그 component의 이름과 하는 일이 적혀 있다. 초록과 README는 저자가 쓴 요약이다. 1부가 옮겨 둔 대로, 원문 파일이 손에 있으면 프로젝트의 참은 그 파일에서 정한다. 그 파일을 열고 눈으로 본 것을 남긴다.

## 위에서 아래로 채운다

적을 것은 위에서 아래로 순서가 있다. 논문 주장을 먼저 옮겨 오는데, 어느 table과 figure의 문장인지까지 적어 두면 다음에 그 자리를 바로 편다. 그다음 저장소에서 이름으로 찾은 code path를 적는다. 실제로 호출되는 경로는 돌려 봐야 아는 것이라 그다음이다. 둘이 같으면 같다고 적고 다르면 다르게 적는다. 이어서 다시 돌려 보는 데 쓴 command와 metric script를 적는다. 비교할 수 있는 범위는 앞이 다 채워진 뒤에 문장으로 적고, 원고에는 거기 적힌 데까지만 쓴다.

이 가운데 앞쪽에 남는 것은 이름과 경로다. Anthropic은 파일 경로나 질의나 링크처럼 가벼운 식별자만 들고 있다가 실행할 때 그 자리에서 불러오는 방식을 [`just in time`](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)이라고 적었다. 같은 문서는 맥락 창에 든 토큰이 늘수록 모델이 그 안의 내용을 정확히 되짚는 능력이 떨어진다고 적었다. 논문 전문과 저장소를 통째로 읽혀 넣으면 그 토큰이 모두 창에 남는다. 여섯 줄에 적힌 경로는 열기 전까지 한 줄이고, 그 줄을 열어 돌려 본 결과가 셋째 줄에 들어간다.

논문 쪽과 저장소 쪽에 각각 물어 둘 것이 있다.

## 논문에 묻고 코드에 묻고

물을 것에는 순서가 있고, 갈수록 열어 볼 데가 안으로 들어간다. 논문 주장이 어느 table과 figure와 section에 있는지 먼저 본다. 원고 주장의 범위가 여기서 선다. 공개 코드에서 해당 모듈이 어디 있는지 찾고, 그 모듈이 실제 예제에서 호출되는지 본다. config key가 runtime에 읽히는지도 본다. config에만 있고 쓰이지 않는 상태를 여기서 거른다. 앞 질문의 답이 나와야 다음 질문을 걸 자리가 생긴다. 모듈 경로가 손에 있어야 그 모듈이 예제에서 호출되는지를 물을 데가 정해진다. 뒤의 둘은 시간을 묻는다. 논문 표의 숫자를 만든 script가 지금 저장소에 공개되어 있는지, 논문 시점과 지금 branch 사이에 convention이 바뀌었는지다.

필요할 때 다음 층을 여는 짜임은 에이전트 쪽에도 있다. Anthropic의 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)는 지시와 script와 자료를 담은 폴더를 에이전트가 찾아 필요할 때 올려 쓰게 하고, 그 열림을 세 층으로 나눴다. 폴더마다 `SKILL.md` 한 장이 들어가고, 그 안에 이름과 언제 쓰는지가 적혀 있다. 1층에서는 그 이름과 description만 system prompt에 올라간다. 2층에서 관련 있다고 판단하면 `SKILL.md` 본문을 읽고, 3층에서 같은 폴더의 다른 파일을 필요할 때 연다. 목차로 시작해 장을 지나 자세한 부록으로 가는 잘 정리된 매뉴얼에 견주며, 필요한 만큼만 올린다고 적었다. 이쪽 질문들도 답이 나온 자리에서 다음으로 내려간다.

답이 모이면 그 모듈의 상태가 한 낱말로 선다. `저장소에 있다`에 다음 중 하나를 붙인다.

## 이 모듈, 지금 어느 상태인가

| 라벨 | 의미 |
|---|---|
| active | runtime에서 호출되고 결과에 영향을 준다 |
| disabled | 구현되어 있으나 꺼져 있다 |
| configured-unused | config에는 있으나 실행 경로 밖에 있다 |
| planned-only | 문서나 issue에만 있다 |
| tested-failed | 시도했으나 실패 기록이 있다 |
| dead | 남아 있으나 현재 경로 밖에 있다 |
| unknown | 확인 전 |

라벨은 두 자리에서 갈린다. planned-only와 tested-failed는 문서와 issue를 읽으면 붙는다. active와 configured-unused와 dead를 가르려면 실행 경로를 따라가야 한다. disabled는 flag를 읽으면 나온다. 켜서 돌려 본 뒤에는 다른 라벨로 옮겨 적는다. unknown은 물어 두고 답을 기다리는 자리다. 빈칸은 묻지 않았다는 뜻으로도 해당 없음이라는 뜻으로도 읽히므로, 물어 둔 자리에는 unknown을 적는다. 여기서 갈리는 것은 파일을 찾아 열면 그 자리에서 답이 나는 일과, 이 branch와 이 config로 돌려 본 출력이 있어야 답이 나는 일이다. AI에 맡길 몫도 이 선에서 나뉜다.

논문에서 방법의 구성요소를 뽑고, 저장소에서 관련 function, class, config를 찾고, issue thread와 README에 적힌 convention 변화를 모으는 일을 AI가 맡는다. 위 질문 가운데 script 공개와 convention 변화는 코드 본문 밖에 답이 있다. YAML, launch command, issue comment, 실패한 sequence, table caption까지 내려가게 한다. 실제로 호출됐는지, config가 runtime에 도달하는지, dataset과 metric 조건이 같은지, 원고에서 어디까지 말할 수 있는지는 실행 결과를 보고 사람이 적는다.

AI가 뽑아 오는 것은 구성요소 이름과 function과 config key와 convention 변화라 답이 들어갈 칸이 미리 정해져 있다. Claude API의 [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)는 constrained decoding으로 스키마에 맞는 답을 보장한다고 적었다. 칸 이름을 스키마로 걸어 두면 돌아온 답이 그대로 표의 한 줄이 된다. 스키마가 받는 것은 type과 properties, items와 required다. enum과 const, additionalProperties도 받는다. 객체를 중첩하거나 배열로 묶은 꼴도 그대로 받고, 칸 하나에는 boolean, number, integer, string, null이 온다. pattern(정규식)은 그 목록 밖에 있다. minimum과 maximum, minLength와 maxLength, uniqueItems, allOf, oneOf도 밖이다. 스키마는 그 칸이 채워졌다는 데까지 센다. 칸에 적힌 경로가 실행에서 지나갔는지는 앞의 라벨이 받는다.

논문이 말한 자리와 실행 경로의 라벨이 어긋나면 1부의 방식대로 한 번에 하나씩 바꾸며 좁힌다. 좁히는 동안 다시 여는 것은 라벨을 붙인 근거다. active로 적은 줄에는 그 라벨을 만든 command와 config가 함께 남는다. 다음에 그 줄을 열 때는 같은 command를 다시 걸어 라벨이 그대로인지 본다. command가 내놓는 숫자에는 조건이 붙어야 한다.

조건이 왜 붙어야 하는지는 로보틱스 metric의 생김에서 나온다. 로보틱스 metric은 이름 하나에 조건이 여럿 붙는다. dataset과 split, sensor와 frame, calibration과 alignment, metric script, failure policy, baseline 가운데 하나만 달라도 두 값은 서로 다른 조건을 잰 값이 된다. 두 수치를 나란히 놓는 일은 이 항목들이 같을 때 선다.

이 항목들이 같은지는 수치를 내놓은 쪽이 무엇을 함께 냈는지에서 갈린다. benchmark는 수치를 내면서 evaluation script와 dataset protocol, failure policy를 같이 낸다. 그 수치를 받아 쓰는 쪽이 같은 수를 다시 얻으려면 그것들이 있어야 하기 때문이다. Pineau 등은 [NeurIPS 2019 재현성 프로그램](https://arxiv.org/abs/2003.12206)에서, 같은 코드와, 구할 수 있으면 같은 데이터로 논문이나 발표에 제시된 것과 비슷한 결과를 다시 얻는 일을 연구 결과의 신뢰성을 확인하는 데 필요한 단계로 적었다. 로보틱스에서는 코드와 데이터에 sensor 입력, frame, calibration, alignment가 더 붙는다. error가 낮다거나 success rate가 높다거나 latency가 짧다고 원고에 쓰려면 그 수치가 나온 조건도 같이 적어야 한다.

조건을 숫자로 적어 둔 실행 환경도 있다. Anthropic의 [code execution tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)는 Claude가 Bash command를 돌리고 파일을 다루는 sandbox를 두고 그 경계를 숫자로 적었다. Python 3.11, 리눅스 컨테이너, x86_64, 메모리 5 GiB, 디스크 5 GiB, CPU 1개다. 코드를 셀 단위로 넘겨 돌리는 쪽에서는 셀 하나가 90초 벽시계 안에서 끝나야 한다. 어떤 수치를 이 sandbox에서 뽑았다면 latency를 재는 순간 이 값들이 그대로 그 수치의 조건이 되고, 셀 단위로 돌렸다면 90초도 함께 붙는다. 연구실 기계에서 잰 값에는 그 기계의 경계값이 같은 자리에 들어간다.

어느 기계에서 어느 dataset으로 잰 값인지를 수치마다 되짚으려면 물음이 한 벌 서 있어야 한다. 어느 dataset의 어느 split인지, 방향은 무엇인지, 어느 metric script와 어느 baseline인지, 실제로 읽은 output이 무엇인지다. 이 물음에 답이 붙은 수치가 원고에서 근거가 된다.

## 돌릴 때 그 자리에서 채운다

이 답은 실행을 걸 때 한 벌 적어 두면 그 자리에 남는다. 실행을 건 뒤에 같은 답을 맞추려면 command 이력과 config 파일과 결과 디렉터리를 각각 열어 봐야 한다. 그래서 command를 던지는 사람이 그 자리에서 적는다. 적을 것의 앞쪽은 수치의 조건이다. 어느 dataset의 어느 split과 sequence인지, 어느 sensor로 무엇을 받아 무엇을 내는지, ground-truth frame과 alignment는 무엇인지, metric과 threshold와 baseline은 무엇인지가 그 조건이다. 조건 뒤에는 같은 command를 다시 던지는 데 드는 것들이 이어진다. command와 config, output path, timeout, 그리고 실패 구간을 어떻게 처리했는지다. 결과 파일이 나오면 output path를 마저 채운다. 이 한 벌이 실행 하나의 최소 기록이다.

## 숫자 읽기 전에 결과물부터

실행이 끝나면 metric 값을 읽기 전에 결과물 자체를 짚는다. 최소 기록에 적은 것은 실행을 걸 때 정한 조건이다. 그 조건대로 돌았는지는 나온 파일을 열어야 안다. 아래 항목은 output 디렉터리를 처음 여는 사람이 하나씩 본다. 여기 오는 것은 실행 하나만 열어 놓고 답이 나오는 항목이다. `coverage`는 그 실행의 입력 구간과 출력 구간을 서로 대 보면 답이 나오므로 이 표에 선다.

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

metric script와 baseline과 output path는 앞의 물음이 묻던 것이다. 실행할 때 적어 둔 값과 지금 읽는 값이 같으면 두 수치가 한 표에 들어간다.

`metric script` 줄에는 script 이름 말고 그 script가 돌아간 라이브러리 판도 걸린다. 앞의 code execution tool 문서는 이 sandbox의 인터넷이 완전히 막혀 있다고 적었다. 그래서 도는 것은 미리 깔린 패키지뿐이고, 그 목록이 pandas, numpy, scipy, scikit-learn, matplotlib, pyarrow, pypdf 등이다. 문서가 적어 둔 것은 패키지 이름까지다. 같은 물음을 연구실 기계에서 돌린 script에 걸면, 그 판을 적은 줄이 같은 자리에 들어간다.

## 원고 문장에 조건을 단다

두 표를 짚고 나면 그 수치로 어디까지 말할 수 있는지가 선다. 원고 문장에는 조건을 넣는다.

> 같은 dataset, 같은 sensor 입력, 같은 metric script를 쓴 baseline 대비 main metric이 개선되었다.

조건이 빠진 문장은 보류한다.

> 성능이 향상되었다.

표 caption에도 같은 규칙을 건다. metric 표에는 수치와 비교 조건이 있어야 한다. caption이 받을 것은 그 표가 무엇을 센 표인지에 따라 갈린다. 로보틱스 원고에는 metric 표 말고 실행 중 일어난 사건을 센 event count 표도 들어간다. event count 표가 직접 보여 주는 것은 센 횟수까지다. 그 결과를 입력으로 받는 downstream task까지 영향이 갔다고 쓰려면 추가 근거가 필요하다. 표 아래의 설명도 그 표가 보여 준 데까지만 쓴다.

## 실패한 실행도 기록할 결과다

최소 기록은 결과 파일이 나온 실행을 받는다. output path와 metric이 결과 파일에서 채워지기 때문이다. 멈춘 실행에도 남길 것이 있다. timeout과 OOM, sensor dropout과 tracking lost, missing sequence, metric script failure, invalid ground truth는 다음 실험의 조건을 정하는 자료다. 최소 기록의 실패 처리 항목은 집계에서 실패 구간을 어떻게 다뤘는지를 받고, 멈춘 실행에는 그 한 벌을 따로 적어 어디까지 갔는지를 남긴다. 실패 하나가 실행의 어느 지점에서 나왔는지에 따라 다음에 고칠 자리가 갈린다. 어느 단계에서 끊겼는지는 이어서 가른다.

끊긴 단계를 AI에 물으면 QoS, calibration, cache, normalization 같은 원인 후보가 빠르게 나온다. 이 답을 받아 바로 고치기 시작하면 지금 무엇이 돌고 있는지 보기 전에 원인이 정해진다. 답은 1부의 방식대로 모델의 말로 적어 두고, 어느 단계에서 신호가 끊겼는지 눈으로 본 뒤에 꺼낸다.

[Endsley](https://doi.org/10.1518/001872095779049543)는 situation awareness를 시간과 공간의 한 범위 안에서 환경의 요소를 지각하는 것, 그 의미를 이해하는 것, 가까운 미래의 상태를 예측하는 것으로 정의했다. 눈으로 본 것은 이 정의 한 문장까지다. 세 항목 각각을 원문이 어떻게 풀었는지는 못 봤다. 여기서 가져다 쓰는 것은 셋을 갈라 세웠다는 짜임 하나다. 정의가 셋을 따로 세운 것처럼 이 책의 기록도 셋을 각각 다른 칸에 적는다. 눈으로 본 신호가 한 칸, 그 신호가 나온 단계가 한 칸, 아직 남은 원인 후보가 또 한 칸이다.

## 단계에 먼저 이름을 붙인다

복잡한 로보틱스 pipeline은 단계마다 다른 증상을 보인다. 어느 단계가 끊겼는지에 따라 볼 것이 달라지므로 단계에 먼저 이름을 붙인다.

```text
input
preprocessing
representation
matching
geometry
optimization
evaluation
```

아래 두 목록은 이 일곱 이름을 그대로 쓴다. 어느 목록을 여는지는 손에 든 증상이 정한다. 앞의 목록은 한 단계 안에서 멈춘다. 뒤의 목록은 일곱을 처음부터 훑는다.

## 신호가 아예 안 올 때

받는 쪽 callback이 빈 채로 있으면 신호는 `input`에서 멈춰 있다. 이어지는 여섯 단계는 아직 입력을 받기 전이라 여기서 읽을 것은 `input` 하나다. 수정 전에 다음을 본다.

1. `ros2 topic list`로 topic 존재 확인
2. `ros2 topic info --verbose`로 QoS 확인
3. publisher/subscriber namespace 확인
4. `use_sim_time`과 `/clock` 확인
5. container device, network, volume 확인
6. 이어서 코드 또는 launch 수정

1부터 5까지는 단계 이름에 모두 `input`을 적는다. 1에서 topic 이름이 목록에 보이는데도 callback이 빈 채로 있으면 다음에 볼 것은 profile이다. ROS2 기본 profile은 RELIABLE이고 sensor data profile은 BEST_EFFORT라 driver와 받는 쪽이 어긋나면 메시지가 안 온다. 2가 보는 것이 이 어긋남이다. topic이 오는 것을 눈으로 본 뒤에야 `next stage:`에 `preprocessing`을 적는다. 5가 보는 container device와 network와 volume은 실행 환경 쪽이다. 실행 환경 쪽 증상 하나하나를 어디서 볼지는 부록의 로봇 실험 참조표가 받는다.

1의 `ros2 topic list`를 AI가 대신 찍고 결과를 옮겨 줄 때는 자리가 하나 더 생긴다. 도구 응답에는 길이 제한이 걸린다. Anthropic의 [도구 작성 지침](https://www.anthropic.com/engineering/writing-tools-for-agents)은 도구가 high signal information만 에이전트에 돌려주게 하라고 적었다. 같은 글은 응답에 pagination과 범위 선택과 필터와 잘라내기를 두라고도 적었다. Claude Code는 도구 응답을 기본 25,000 토큰으로 제한한다. 이 제한이 걸린 응답은 뒤가 잘린 채로 온다. 짧게 온 목록을 그대로 적어 두기 전에 그것이 빈 목록인지 잘린 목록인지를 먼저 가른다. 잘린 것이면 topic 이름을 좁혀 다시 찍은 결과를 받는다.

## 떨어진 숫자는 맨 위부터

성능 숫자 하나가 떨어졌을 때 그 값은 일곱 단계를 다 지나온 뒤에 나온 것이다. 앞 절에서는 빈 callback 하나가 끊긴 자리를 `input`으로 좁혀 주었다. 다 지나온 값에는 일곱이 그대로 후보로 남는다. 뒤 단계는 앞 단계의 출력을 받아 돌기 때문에 앞이 어긋나면 뒤도 같이 어긋나 보인다. 어느 단계에서 떨어졌는지는 위에서부터 하나씩 짚어 본다. 수정 전에 다음을 본다.

1. dataset, split, sensor input 범위 확인
2. timestamp, frame, calibration 확인
3. preprocessing과 normalization 확인
4. cache, checkpoint, intermediate output 확인
5. matching, geometry, optimization의 입력과 출력 확인
6. metric script와 failure policy 확인
7. 그다음 model architecture, training 설정, control parameter 수정

일곱 이름은 데이터가 지나가는 차례다. `input`으로 들어온 것을 `preprocessing`이 손질하고, `representation`이 그것을 다루기 좋은 꼴로 바꿔 두면 `matching`이 짝을 찾고 `geometry`가 위치를 세우고 `optimization`이 전체를 맞춘다. 마지막 `evaluation`이 그 결과를 숫자로 잰다. 1과 2는 `input`에 들어온 것과 거기 붙은 조건을 본다. 3에서 여는 normalization은 `preprocessing` 안에서 도는 손질이다. 4가 여는 cache와 checkpoint와 중간 출력은 `representation`이 남겨 둔 것이다. 5는 `matching`과 `geometry`와 `optimization`의 입력과 출력을 한 줄에서 받고, 6이 metric script와 failure policy를 여는 자리가 `evaluation`이다. 앞 절에서 숫자마다 dataset과 split과 metric script를 적어 두었다면 1과 6은 그 기록을 다시 읽는 일이 된다. 7은 일곱 이름을 다 지나온 뒤에 남는다.

## 본 것은 같은 꼴로 적는다

앞의 두 목록은 항목마다 확인 하나를 만든다. 다음 세션에서 같은 자리를 다시 열려면 그 확인들이 한 파일에 같은 꼴로 쌓여 있어야 한다. 확인 하나에 적는 것은 이렇다. 어느 단계에서 본 것인지 위 일곱 이름 가운데 하나를 적는다. `ros2 topic list`를 찍어 봤으면 `input`이고 metric script를 열었으면 `evaluation`이다. 돌린 명령과 그 workdir를 적는다. 이 둘이 있어야 같은 신호를 다시 낸다. 눈으로 본 신호를 적고, 그 사이 건드린 파일과 결과가 간 자리를 적고, 이 확인 뒤에 옮겨 갈 단계를 적는다.

눈으로 본 신호와 그 신호가 나온 단계는 이렇게 확인 안에 남고, 아직 남은 원인 후보는 1부의 방식대로 모델의 말 자리에 남는다. 어느 확인을 열어도 눈으로 본 것과 AI가 댄 QoS나 calibration은 서로 다른 자리에서 나온다.

눈으로 본 신호 자리에 받는 것도 하나다. 앞 절에 든 도구 작성 지침은 오류 메시지를 코드나 traceback이 아니라 다음에 무엇을 하라는 말로 쓰라고 적었다. 이 자리도 같다. traceback을 통째로 옮겨 붙인 확인과, `input`에서 어느 topic이 빈 채로 있었는지를 적은 확인이 여기서 갈린다. 뒤쪽이면 다음에 옮겨 갈 단계가 그대로 이어진다.

이 확인들을 한 파일에 쌓아 두면, 멈춰야 할 자리 하나가 바로 보인다. 옮겨 갈 단계에 같은 이름이 두 번 이어서 들어가면 같은 단계에서 근거가 그대로라는 뜻이다.

## 도구 탓인지 방법 탓인지

같은 이름이 두 번 들어간 자리에서는 그 단계 안을 한 번 더 가른다. 같은 단계에 적힌 실패라도 종류가 다르면 다음에 할 일이 달라진다. 앞의 세 종류는 눈으로 본 신호로 갈린다.

| 실패 종류 | 예 |
|---|---|
| 실행 환경 실패 | `pip install`, CUDA driver, Docker volume, dataset path |
| runtime 실패 | callback 없음, tf lookup 실패, node crash |
| 평가 실패 | wrong frame, wrong split, wrong metric script |
| 방법 실패 | 조건을 맞춰 확인한 뒤에도 성능이 낮음 |

첫 줄은 여러 자리를 한꺼번에 받는다. 빌드 성공은 첫 줄에서 한 자리를 지운다. 소스가 컴파일됐다는 것까지가 그 한 자리다. `pip install`과 CUDA driver와 Docker volume과 dataset path는 그대로 남는다.

같은 확인을 AI가 code execution tool 안에서 돌렸다면 첫 줄이 받는 자리가 달라진다. Anthropic의 [code execution tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)는 그 컨테이너의 인터넷이 완전히 막혀 있어 런타임에 패키지를 받지 못한다고 적었다. 미리 깔린 것만 도는 자리라 `pip install`은 후보에서 빠지고, 대신 필요한 패키지가 그 목록에 있는지가 첫 줄의 자리로 들어온다. 같은 문서가 적은 두 가지는 첫 줄에 자리를 하나 더 붙인다. 컨테이너는 약 5분 놀면 체크포인트로 저장됐다가 같은 컨테이너 ID로 되살아난다. 도구 판을 `code_execution_20260120` 이후로 올리면 변수 바인딩까지 요청 사이에 남는다. 앞 실행의 상태가 남아 있는 것이 그 자리다.

첫 줄의 자리들을 지우고 나면 둘째 줄이 선다. callback 없음과 tf lookup 실패는 둘째 줄에서 따로 본다. wrong metric script가 걸리는 자리는 셋째 줄이다. output이 쓸 데에 맞는지는 결과가 간 자리에 적은 파일을 열어 본다. 넷째 줄은 앞의 세 줄을 지운 뒤에 남는 자리다. 도구 실패를 넷째 줄에 적으면 아직 남아 있는 자리가 지워진 것으로 기록되고, 다음 확인이 같은 단계로 돌아온다. 도구 실패와 방법 실패가 한 기록에 섞이면 부록 D가 적은 대로 멈춘다.

`evaluation`까지 지나온 줄은 성능 숫자를 두고 쓴 문장을 받쳐 준다. `input`에서 멈춘 줄이 받쳐 주는 것은 그 단계에서 눈으로 본 것까지다. 기록에 적힌 단계와 실패 종류가 원고에 쓸 수 있는 문장의 어디까지를 정한다. 그 문장은 주장과 근거로 갈라 `claim-evidence-map.md`에 적는다.

원고로 간 문장은 심사를 받는다. 심사를 기다리는 동안 AI는 원고의 문장을 빠르게 다듬고, 다듬고 나면 표현이 바뀐 원고가 남는다. 심사 의견은 손대기 전 원고를 읽고 돌아온다. 그 의견이 짚은 근거는 다듬기 전 자리에 그대로 있다. 답변서는 원고의 어느 줄을 어떻게 바꿨는지 적어 함께 보내는 문서다. 손댄 것이 표현뿐이면 거기 적을 것도 표현뿐이다. 의견 하나를 받으면 그것이 원고의 무엇을 짚었는지부터 가른다. 어조를 짚은 의견은 문장을 고치면 답이 된다. 실험 조건을 물었으면 실행이 한 번 더 든다. 주장이 어디까지 간다고 썼는지가 걸린 자리에서는 쓴 만큼을 줄여 답한다.

의견이 무엇을 짚었는지 가르려면 주장과 근거가 어디서 붙는지 그 자리에 이름이 있어야 한다. [Toulmin은 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)에서 실제 논쟁의 주장이 어떻게 서는지 뜯어 놓았다. claim은 주장된 명제다(p.12). "무엇을 근거로 하는가"에 답하는 것이 data다(p.97). 둘을 잇는 자리에 필요한 것을 Toulmin은 "general, hypothetical statements, which can act as bridges, and authorise the sort of step to which our argument commits us"(p.98)라고 적었다. 이 다리가 warrant다. 같은 책은 "data are appealed to explicitly, warrants implicitly"(p.100)라고도 적었다. 원고에서 data는 표와 그림으로 이름을 갖고 본문에 나온다. 그 숫자가 왜 그 주장을 받치는지는 읽는 쪽이 채워 넣는 자리로 남는다. 다리를 문장으로 꺼내 적으면 의견이 어느 다리를 물었는지 짚을 자리가 생긴다. 주장이 어디까지 가는지는 다리와 다른 자리에 적힌다. Toulmin이 qualifier로 따로 둔 probably, generally, presumably 같은 양태 한정을 지우면 근거는 그대로인 채 주장만 멀리 간다.

## 의견 하나를 한 줄로 옮긴다

부록 D는 원고 문장에서 시작할 때 `claim-evidence-map.md`를 쓰라고 적었다. 의견 하나를 이 표의 한 줄로 옮기면 다음 행동이 어느 칸에서 나오는지 보인다.

| 항목 | 내용 |
|---|---|
| 심사 의견 | 원문 또는 요약 |
| 문제가 된 주장 | reviewer가 겨냥한 문장 |
| 현재 근거 | figure, table, experiment, citation |
| 부족한 근거 | 새로 필요한 실험 또는 계산 |
| 원고 수정 위치 | 고칠 section, table, caption, paragraph |
| 답변 범위 | 답변서에서 말할 수 있는 범위 |
| 남는 한계 | 인정해야 할 한계 |

warrant는 표에 따로 칸을 두지 않고 `현재 근거` 칸 안에 함께 적는다. 다리는 그 근거가 무엇을 받치는지를 말하는 것이라 근거와 떨어져 서면 읽을 데가 없다. figure와 table 이름을 적을 때 그 숫자가 주장을 어떻게 받치는지 한 줄을 함께 적으면 읽는 쪽이 채워 넣던 자리가 표 안으로 들어온다. 의견이 그 한 줄을 물었으면 답에 드는 것은 새 숫자라서 `부족한 근거` 칸으로 넘어간다.

`답변 범위`에 쓸 말은 `현재 근거` 칸에서 나온다. 그 칸 밖에서 나온 말은 `남는 한계`로 내려간다.

표의 칸을 채우는 동안 심사 의견 원문, 겨냥된 문장, 표의 숫자, 새로 돌린 실행 결과가 한 세션에 쌓인다. Anthropic의 [context engineering 문서](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)는 창이 너무 커지면 compaction이 창 전체를 압축한다고 적었다. 같은 문서는 압축이 무엇을 납작하게 만드는지를 "user messages, assistant messages, tool calls, tool results, even prior compaction blocks are all flattened into the summary"라고 적었다. 문서가 돌린 실행에서 압축 한 번이 앞 대화를 약 2,783 토큰으로 줄였다. 요약이 한 번 지나간 뒤에도 `현재 근거` 칸이 가리키던 figure와 table 이름을 다시 집으려면 그 이름이 창 밖의 파일에 적혀 있어야 한다. 그 바깥 저장이 memory다. 문서는 memory가 정보를 창 밖으로 옮겨 세션을 건너 남긴다고 적었고, 이것을 "structured note-taking"이라 불렀다. 같은 실측에서 memory를 쓴 2세션은 5K 토큰으로 시작했고, memory를 안 쓴 2세션은 문서 여덟 개를 다시 읽어 332K까지 갔다. `claim-evidence-map.md`를 파일로 두는 까닭이 여기서 하나 더 선다.

파일에 옮겨 적는 일은 압축이 걸리기 전에 끝나 있어야 한다. 압축이 걸리는 시점은 context engineering 문서가 적어 둔 설정값이 잡는다. 기본 트리거는 150K 토큰이고 최소는 50K다. Claude Code의 [hooks 문서](https://code.claude.com/docs/en/hooks)에는 `PreCompact`와 `PostCompact`가 있어 압축 앞뒤에 무엇을 할지 정해 둘 수 있다. 표의 한 줄을 파일로 빼 두는 일을 `PreCompact`에 걸어 두면 세션이 압축을 지나도 같은 칸에서 다음 행동이 나온다.

표가 채워지면 의견 하나가 표의 한 줄이 되어, 겨냥된 주장과 현재 근거와 부족한
근거가 갈라져 있다. 그 줄을 답변서 문장으로 언제 옮겨도 되는지가 다음이다.

## 답변 문장은 언제 써도 되나

부록 D는 멈춰야 하는 조건 하나로 "심사 위험이 남았는데 문장 다듬기만 반복한다"를 적었다. 답변 문장을 언제 써도 되는지가 아래 세 번째 줄에 걸려 있다.

1. reviewer comment에서 공격받은 주장을 뽑는다.
2. 해당 주장이 기대는 table, figure, experiment, citation을 찾는다.
3. 근거가 충분하면 답변 문장을 쓴다.
4. 근거가 부족하면 실험, 재계산, 주장 줄이기 가운데 하나를 고른다.
5. 원고를 고칠 자리를 답변서에 적는다.

reviewer가 겨냥한 문장이 표의 숫자를 가리키면 고칠 자리도 표가 된다. 표를 고칠 때도 이 다섯 단계를 그대로 밟는다. 뽑아 둔 주장이 표 하나에 걸려 있으면 둘째 단계는 그 표가 담은 칸을 세는 일이 된다. 무슨 칸을 세는지는 표가 무엇을 담았는지가 정한다. metric 표에는 낮은 error나 높은 success rate와 나란히 그 수치가 어느 조건에서 나왔는지가 적혀 있어야 비교할 수 있다. 앞 절이 센 아홉 가운데 표 안에 자리를 갖는 것은 dataset, sensor, frame, failure policy 넷이다. split과 calibration과 alignment와 metric script와 baseline 다섯은 caption이나 본문이 받는다. 표와 caption에서 그 조건이 다 나오면 답변 문장에 그대로 적는다. 한 칸이 비면 넷째 단계로 가고, 그 칸이 기록에서 채워지는지 실험을 다시 돌려야 채워지는지가 갈린다.

event count 표는 같은 단계에서 다르게 걸린다. 표가 보여 주는 것은 센 횟수까지다. 그 횟수로 downstream task에 미친 영향까지 말하려면 제대로 세었는지(precision), 틀리게 잡힌 것을 걸러 냈는지(outlier rejection), 그 처리가 downstream이 쓸 시간 안에 끝났는지(runtime)를 따로 대야 한다. 셋 다 표 밖에 있어서 넷째 단계에서 고를 것은 추가 실험이 된다. 표 밖의 셋을 본문 문장이 이미 말하고 있으면 그 문장도 고칠 자리에 들어간다. caption과 본문 문장은 표가 담은 데까지 쓴다. 고친 caption의 자리는 답변서에 적는다.

## 문장만 다듬은 답변서

이 순서를 건너뛰어도 답변서는 완성된다. 완성된 답변서가 원고에 무엇을 남기는지가 갈릴 뿐이다.

| 실패 | 결과 |
|---|---|
| comment를 어조 문제로만 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | 근거가 받치지 못하는 주장으로 커진다 |
| citation만 추가 | reviewer가 지적한 실험 조건 확인이 빠진다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

첫째 줄은 의견을 가르는 자리에서 생긴다. 비교 조건을 물은 comment를 어조 문제로 받으면 문장이 정중해진 뒤에도 그 조건은 표에서 빈칸으로 남는다. 둘째 줄이 qualifier를 지우는 손질이다. 같은 표를 그대로 두고 그 위의 문장만 더 멀리 간다. 셋째 줄의 citation은 남의 실행에 붙은 이름이라, 거기 적힌 조건은 그 논문 쪽 표에 남는다. reviewer가 물은 조건은 이쪽 기록에서 나오거나 한 번 더 돌려서 나온다.

답변의 예의는 필요하다. 정중한 문장이 답하는 것은 어조를 짚은 의견까지다. 실험 조건을 짚은 의견은 실행 하나를 더 받고서야 답이 된다. 그 실행이 앞의 숫자와 같은 조건에서 나왔는지를 reviewer가 짚어 볼 자리도 답변서에 있어야 한다. 같은 split과 metric script로 baseline을 다시 맞췄다면 그 세 이름을 답변서에 그대로 쓴다. 숫자를 다시 마주쳤을 때 던지라고 부록 D가 둔 여섯 줄에 그 셋이 들어 있다. 그 여섯 줄의 첫 줄에 적힌 dataset이 답변 문장이 갈 수 있는 어디까지를 정한다. cross-dataset generalization을 받치는 근거가 한 dataset에서 나왔다면 답변 문장도 그 dataset에 맞춰 선다. 줄여 낸 만큼은 `남는 한계` 칸으로 옮겨 적는다.
