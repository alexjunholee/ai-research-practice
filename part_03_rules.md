# 3부 — 규칙으로 만들기

공개된 agent 저장소에는 다시 쓸 만한 작업 습관이 있다. 작은 단위의 수정, 가정 명시, 실패 보고, 역할 분리, tool 호출 기록은 연구에도 쓸 데가 있다. 다만 그 규칙은 코드를 고치고 tool을 부르는 일을 중심으로 짜여 있다. 로봇 실험의 수치가 무엇을 가리키는지 말하려면 dataset, calibration, frame, metric, 실패 처리, reviewer risk까지 같은 자리에 적혀 있어야 한다.

tool 호출 쪽으로는 논문이 정해 둔 것이 있다. Yao 등은 reasoning trace와 action을 번갈아 내놓게 한 [ReAct](https://arxiv.org/abs/2210.03629)를 ALFWorld와 WebShop에서 쟀고, in-context example 한둘로 절대 성공률을 34%와 10% 올렸다. reasoning trace는 모델이 action plan을 세우고 따라가고 고치게 했고 예외도 그 자리에서 다루게 했다. action은 knowledge base나 environment 같은 외부 출처에서 정보를 더 모으는 통로였다. Schick 등의 [Toolformer](https://arxiv.org/abs/2302.04761)는 어느 API를 언제 부르고 무슨 argument를 넘기고 그 결과를 다음 token 예측에 어떻게 넣을지를 모델이 정하도록 훈련했다. 두 연구는 언제 부를지, 어떤 argument를 넘길지, 결과를 어떻게 다룰지를 정해 두었다. 그 호출이 어느 dataset의 어느 split으로 가고 어느 metric script로 재는지는 연구자 쪽에 남는다.

연구자 쪽에 남은 것을 어디에 적어 둘지는 그 작업이 돌아가는 구조에서 정해진다. Anthropic의 [Managed Agents](https://www.anthropic.com/engineering/managed-agents)는 자리를 셋으로 갈랐다. session은 일어난 일을 그대로 쌓는 append-only log, harness는 모델을 부르고 그 tool 호출을 그 infrastructure로 넘기는 loop, sandbox는 코드를 실행하고 파일을 고치는 실행 환경이다. harness는 loop를 한 바퀴 돌 때마다 지금 어느 도구를 부를지, 그 결과를 어디로 보낼지를 정한다. 연구 workspace에서는 사람이 그 판단을 미리 글로 적어 둔다. 어느 파일을 먼저 읽고 어떤 결과가 나오면 멈출지를 문장으로 남기면 agent가 걸음마다 그 문장을 본다. 그 문장 묶음이 harness에 해당한다. 다음 작업에서 다시 읽을 기록은 session에, 실제 파일과 command와 dataset이 놓인 경계는 sandbox에 대응한다.

연구 workspace로 옮겨 오는 것은 이 셋의 구분이다. 옮겨 올 규칙은 저장소마다 prompt 문구로 적혀 있다. 그 문구를 손보기 전에 이 셋부터 대응시킨다.

## 어느 저장소를 열어 보나

손볼 문구는 저장소를 열어야 나온다. 저장소를 처음 고를 때 가장 먼저 눈에 들어오는 수치는 GitHub star다. star는 그 저장소를 눈여겨본 사람 수를 알려 줄 뿐이다. 그다음 무엇을 볼지는 저장소의 유형에 따라 달라진다. 아래 이름은 유형을 가리키는 예다.

| 유형 | 예 | 볼 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 항목 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 확인 규칙 |

첫 줄의 skill repo는 그 습관이 주고받을 수 있는 단위로 묶인 꼴이다. Anthropic은 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)를 agent가 찾아 필요할 때 올려 쓰는, 지시와 스크립트와 자료가 든 폴더로 적었다. `SKILL.md`는 YAML frontmatter로 열고 `name`과 언제 쓰는지를 적는 `description`이 필수다. 언제 쓰는지가 폴더 안에 함께 적혀 있다. 그 칸에는 에이전트가 언제 이 폴더를 열지까지만 적힌다. 이쪽 연구 작업의 어디에서 걸리는지는 옮겨 오는 사람이 적는다.

표의 `볼 것` 칸을 세 자리에 나눠 보면 어느 줄이 무엇을 주는지 갈린다. 작은 수정과 가정 명시와 실패 보고, role 분리와 tool handoff는 agent가 단계마다 따를 문장이라 harness에 해당한다. tracing과 user reaction prior는 다음 작업에서 다시 읽을 것이라 session에 해당한다. 표의 `볼 것` 칸을 셋에 나눠 보는 일은 여기까지다.

## 남의 규칙에 없는 것

이 유형들이 적어 두는 규칙은 코드와 도구 쪽에 모여 있다. 로봇 실험 수치를 두고 말하려면 아래가 더 있어야 한다.

- dataset, split, sequence
- task input/output
- ground-truth frame
- metric script
- failure policy
- implementation status
- result provenance
- 원고에서 말할 수 있는 범위

여덟 항목은 1부와 2부가 이미 채워 본 이름이다. 위의 다섯은 실행을 걸 때 그 자리에서 채우는 최소 기록이다. 그것이 가리키는 것은 sandbox 자리에 놓인 파일과 script다. implementation status는 `저장소에 있다`에 붙이는 라벨이라 논문 주장과 실행 경로를 맞춰 봐야 정해진다. result provenance는 그 숫자가 어느 실행에서 나왔는지 적어 둔 기록에 남는다. 외부 저장소에서 가져온 문구 옆에 이 여덟 항목을 따로 단다.

부록 D(`PATH.md`)는 멈춰야 하는 조건 하나로 `실험 조건이 바뀌었는데 숫자를 비교하려 한다`를 적어 두었다. 조건이 바뀐 뒤에도 앞 조건에서 만들어 둔 cache를 그대로 읽거나 이름만 같은 metric script 둘을 한 표에 올려도 숫자는 그대로 나온다. 위 여덟 항목이 채워져 있으면 어긋난 것이 그 자리에서 눈에 보인다. 맨 아래 줄은 원고 문장 쪽으로 이어져 `claim-evidence-map.md`에서 주장과 근거로 나뉜다.

## 규칙을 쪼개서 옮겨 온다

옮기는 일은 외부 규칙을 쪼개는 데서 시작한다. 저장소 하나가 내놓는 prompt 문구에는 도구를 부르는 법과 다음 세션이 읽을 상태와 계속 걸어 둘 행동 규칙이 한 덩이로 적혀 있어, 통째로 옮기면 셋이 함께 따라온다. 조각마다 무엇인지를 먼저 묻는다. [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)은 server가 내놓는 것을 세 이름으로 갈라 두었다. tool은 AI 애플리케이션이 불러서 동작을 시키는 실행 가능한 함수이고, resource는 맥락 정보를 주는 자료 출처이며, prompt는 언어 모델과 주고받는 자리를 짜는 데 다시 쓰는 틀이다. 옮겨 올 줄에도 같은 것을 묻는다. 이 줄은 실행되는 것인가, 읽히는 자료인가, 다시 채워 쓰는 틀인가.

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 같은 도구에 묶인 호출법을 뗀다.
3. durable state는 `project-memory.json`, ledger, replay case로 옮긴다.
4. 남는 행동 규칙은 `AGENTS.md`나 template로 옮긴다.
5. 실제 실행 경계는 repo, dataset, artifact, command로 나눈다.
6. dataset, metric, 결과물, reviewer risk 항목을 더한다.
7. 사용자가 반복해서 반려한 패턴을 앞에 둔다.

첫째와 둘째 단계는 같은 문구를 두 번 손본다. 먼저 기능별로 갈라 놓고, 갈라 놓은 조각에서 도구 이름에 묶인 호출법을 뗀다. 잘게 갈라 두면 쓰는 쪽에서 다시 묶을 여지가 생긴다. Anthropic의 [도구 작성 지침](https://www.anthropic.com/engineering/writing-tools-for-agents)은 도구 하나가 여러 개별 동작이나 API 호출을 안에서 처리하며 기능을 묶을 수 있다고 적었고, 관련 있는 것을 같은 접두어 아래 모으는 namespacing이 도구가 많을 때 경계를 가르는 데 도움이 된다고 적었다. 같은 지침은 도구가 agent에 돌려주는 것을 high signal 정보로 두라고 했다. 옮겨 온 규칙에도 같은 손질이 필요하다. dataset 쪽 규칙과 원고 쪽 규칙을 각각 한 이름 아래 모아 두면 다음 요청에서 어디를 열지가 분명해진다.

셋째부터 다섯째 단계는 그 조각을 놓을 데를 정한다. 앞의 세 이름이 조각의 종류를 물었다면 이 셋은 실행 구조의 어디에 놓일지를 가른다. durable state는 다음 작업에서 다시 읽는 기록이니 session에 해당한다. 그 기록을 다시 읽는 사이에도 agent가 단계마다 보는 문장이 있고, 남는 행동 규칙이 harness에 해당한다. 그 문장이 실제로 손대는 repo와 dataset과 artifact와 command는 sandbox에 해당한다. 둘째 걸음에서 떼어 낸 도구별 호출법은 그 저장소의 도구에 남는다.

다섯째 단계의 실행 경계에는 로봇을 돌릴 때 하나가 더 붙는다. 로봇은 코드가 도는 기계 밖에서 움직인다. 장치와 시계와 네트워크의 현재 상태가 같은 경계 위에 놓인다. 그 상태를 적어 두는 일은 다음 절이 맡는다.

일곱 걸음을 마치면 그 규칙은 `AGENTS.md`와 template 안에 놓이고, 다음 요청부터 agent가 그것을 읽는다. 규칙이 지켜졌는지는 agent가 답을 내놓는 자리에서 드러난다. 부록 B(`QUICKSTART.md`)의 첫 AI 요청 블록도 마지막 줄에서 그 자리를 짚었다. 원문 파일이나 산출물이 손에 있으면 요약만 보고 프로젝트의 현재 상태를 단정하지 말라고 못 박았다. 그 블록은 답하기 전에 무엇을 밝힐지를 요청 안에 미리 적어 둔다. 옮겨 온 규칙에도 같은 대목을 하나 둔다. 그 대목은 agent가 답을 내놓기 직전이다. 그 직전에 다음 다섯을 짚는다. 읽지 않은 파일을 읽은 것처럼 말하지 않았는지, 근거 범위를 넘는 주장을 쓰지 않았는지, 실행해야 할 때 계획만 말하지 않았는지, 사용자가 싫어한 문체나 구조를 반복하지 않았는지, 공개 문서에 내부 작업 기록을 남기지 않았는지다.

걸리는 것이 하나라도 있으면 다음 행동을 바꾼다. 같은 항목이 두 번째로 걸리면 그 줄을 `AGENTS.md`의 규칙 한 줄이나 replay case로 옮겨 적는다. 무엇이 걸렸는지가 쌓이면, 어느 저장소에서 옮겨 온 규칙이 무엇을 줄였는지도 그 기록을 보고 알 수 있다.

GitHub star 수는 참고할 저장소를 처음 찾을 때만 본다. 그 규칙을 실제로 쓸지는 같은 metric 혼동과 cache 실수, 반복되는 reviewer comment가 줄어드는지가 정한다. 줄었는지를 보려면 규칙이 도는 자리, 곧 로봇이 실제로 움직이는 환경의 상태부터 적혀 있어야 한다.

## 로봇 실험에서 먼저 확인할 것

AI 코딩 에이전트(Claude, Copilot, ChatGPT 등)는 함수의 초안을 만들고 에러 메시지에서 원인 후보를 찾는 데 쓸 만하다. 로보틱스에서는 하드웨어, OS, 네트워크, 실시간 조건이 함께 맞물리므로 원인은 코드 밖에서도 찾아야 한다. 에이전트는 우리가 적어 준 코드와 오류 문구까지만 본다. 현재 장치와 실행 상태를 함께 보여 줘야 에이전트의 답이 지금 이 로봇을 가리킨다.

따라서 질문을 만들기 전에 토픽, 장치, 시계, 네트워크, 권한, 시스템 구조의 현재 상태를 기록한다. 이 관측값이 있어야 에이전트의 답도 바로 해 볼 확인 절차로 이어진다.

에이전트가 코드를 직접 돌리는 sandbox에서는 이런 조건을 문서가 숫자로 먼저 알려 준다. Anthropic의 [code execution tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)는 Python 3.11이 도는 x86_64 리눅스 컨테이너에 메모리 5 GiB, 디스크 5 GiB, CPU 1개가 걸리고 REPL 셀 하나가 실제 시간으로 90초 안에 끝난다고 적었다. 인터넷이 막혀 있다는 것도, 컨테이너가 30일 뒤 만료되고 약 5분을 놀면 체크포인트로 저장됐다가 같은 ID로 되살아난다는 것도 같은 문서에 있다. 로봇을 돌리는 자리에서는 같은 항목을 지금 이 기계에서 눈으로 본다. 어느 장치가 붙어 있는지, 시계가 맞는지, 네트워크가 어디까지 가는지는 현장에서 직접 읽어야 나오는 숫자다.

## 막히는 자리는 참조표에 모아 두었다

토픽이 안 오고, 컨테이너에서 장치가 안 보이고, 드라이버가 아무 반응도 없는
증상들은 저마다 먼저 돌려 볼 명령이 정해져 있다. 그 명령들을 증상별로 부록의 로봇 실험
참조표에 모아 두었다. 여기서는 그 표를 언제 어떻게 쓰는지를 다룬다. 어떤 증상이든
질문을 만들기 전에 참조표의 명령으로 지금 상태를 적고, 적은 것을 에이전트에게
준다.

## 에이전트에게 줄 정보

*논문 읽기와 글쓰기에서 에이전트를 쓰는 법은 [「연구노트」 Ch.7 — 논문을 세 번에 나누어 읽기](../research-notes/guide.html#chapter-7)와 [「연구노트」 Ch.16 — 마음가짐](../research-notes/guide.html#chapter-16)에 있다.*

### 환경과 증상을 함께 주기

에이전트의 답은 질문에 적어 준 환경 정보와 관측 자료를 따라간다.

정보가 부족한 예: "카메라가 안 돼요"

어디를 볼지 좁혀 주는 예: "Ubuntu 22.04, ROS2 Humble, Intel RealSense D435를 쓴다. `rs-enumerate-devices`에서는 보이지만 `ros2 launch realsense2_camera rs_launch.py`를 실행하면 `Could not open device` 오류가 난다. Docker 안에서 실행 중이고, `--device=/dev/video0`은 매핑했다."

**함께 줄 정보**:
- OS 버전, ROS 버전
- 하드웨어 플랫폼 (x86 vs ARM/Jetson)
- 센서 모델명
- 오류 메시지 전문
- `ros2 topic list`, `ros2 node list` 출력
- Docker 사용 여부와 실행 옵션 (`docker run` 명령 전체)
- 네트워크 구성 (유선/무선, IP 대역)

### 답을 실행 전에 검증하기

제안받은 명령이나 설정을 걸기 전에 다음을 짚는다.

- **패키지 설치** → 그 패키지가 지금 쓰는 ROS와 Ubuntu 버전을 지원하는지 `apt search ros-humble-PACKAGE_NAME` 등으로 짚는다.
- **설정 변경** → 지금 설정을 백업하고, 제안이 어떤 관측 결과를 설명하는지 살핀다.
- **환경 재설치** → 먼저 `pip show`, `dpkg -l | grep`, `apt policy` 등으로 지금 상태와 충돌이 어디까지 걸쳤는지 기록한다.
- **생성된 코드** → 하드코딩된 경로(`/home/user/...`), IP(`192.168.1.100`), x86 전용 패키지(`amd64` wheel)가 들어 있는지 본다.

### 맡길 일과 직접 잴 일

| 에이전트로 초안을 만들기 좋은 일 | 현장에서 측정값을 확보해야 하는 일 |
|---|---|
| 알고리즘 구현 (SLAM, detection 등) | 하드웨어 디버깅 |
| ROS2 노드/서비스 코드 작성 | QoS/DDS 설정의 실제 성능 확인 |
| Python/C++ 코드 리팩토링 | USB/시리얼 장치 상태 확인 |
| 논문 읽기/요약 | LiDAR 연결과 네트워크 패킷 확인 |
| CMakeLists.txt 작성 | 실시간 주기와 지터 측정 |
| 데이터 전처리 파이프라인 | Docker 안팎의 장치 접근 확인 |
| 시각화 코드 (matplotlib, Open3D) | 센서 간 시간 동기화 실전 |
| 일반적인 오류 메시지의 해석 | `dmesg`와 커널 로그를 현장 증상과 대조하는 일 |

에이전트는 코드 초안과 흔한 오류 메시지 해석에 쓸 데가 있다. 하드웨어와 소프트웨어가 맞닿는 자리에서는 장치 상태, 타이밍, 패킷처럼 현장에서만 나오는 숫자가 필요하다. 먼저 직접 재고, 그 결과를 분석 입력으로 준다.

## 논문·코드·실험·원고에 나누어 쓰기

같은 원칙이 논문 읽기, 코드 작성, 실험 설계, 원고 작성에서 각각 다른 모양으로 붙는다.

### 논문 읽기

*논문 읽기 워크플로우(3-pass + AI layer)는 [「연구노트」 Ch.7 — 논문을 세 번에 나누어 읽기](../research-notes/guide.html#chapter-7)에서 다룬다.*

중요한 논문은 3-pass로 읽으면서 에이전트의 요약을 곁에 둔다. 초록을 읽은 뒤 기여를 세 문장으로 정리하게 한다. 막히는 식은 단계를 나눠 유도해 달라고 한다.

### 코드 작성

- 프로토타이핑: "KITTI 데이터셋에서 ORB 특징점 뽑아서 매칭하는 코드 짜줘. OpenCV 쓰고, Lowe's ratio test 0.75로" — 이렇게 숫자까지 박아서 지시
- 디버깅: 오류 메시지와 관련 코드를 함께 주고 가능한 원인과 짚을 순서를 요청
- 리팩토링: "이 코드를 PyTorch Dataset 클래스로 바꿔줘" — 구조 변환에 강함
- 직접 볼 것: ROS QoS, 하드웨어 권한, 네트워크 설정, 실시간 타이밍

### 실험 설계

*실험 설계·ablation·결과 해석에 AI를 쓰는 방법은 [「연구노트」 Ch.32 — Revision/Rebuttal](../research-notes/guide.html#chapter-32)과 [「연구노트」 Ch.27 — Figures](../research-notes/guide.html#chapter-27)에서 다룬다.*

실험을 설계할 때는 baseline 비교 표를 주고 *내가 놓친 비교 축*을 묻는다.

### 논문 쓰기

- 초고 작성: 핵심 아이디어와 실험 결과를 건네고 Introduction의 논리 구조를 제안받기
- 문법·표현 교정: 영어 문장의 문법과 문맥을 함께 살펴보기
- 문체 검토: 생성된 문장을 자신의 논지와 어조에 맞게 고쳐 읽기
- BibTeX 생성: 서지 항목의 초안을 받은 뒤 논문 원문이나 출판사 페이지에서 연도, 학회·저널명, 권·호를 짚어 보기

### 일상 워크플로우 예시

다음은 이 작업들을 하루 일정에 배치한 예다.

```
09:00 — 새 논문 3편 arXiv에서 확인. AI에게 각각 1문장 요약 요청
09:30 — 흥미로운 1편 선택, 2패스 읽기. 모르는 수식은 AI에게 유도 요청
10:30 — 어제 학습 결과 분석. loss curve 캡처해서 AI에게 "이 패턴이 정상인가?" 확인
11:00 — 새 실험 코드 작성. AI에게 DataLoader 구조 생성 시킴. 수동으로 augmentation 로직 수정
14:00 — SLAM 코드 디버깅. ROS2 에러 → topic과 QoS 출력으로 원인 좁히기
16:00 — 논문 Related Work 섹션 초고. AI에게 비교 논문 5편의 차이점 표 만들게 시킴
17:00 — 표 검증. AI가 2편의 method를 혼동한 것 발견, 수동 수정
```
