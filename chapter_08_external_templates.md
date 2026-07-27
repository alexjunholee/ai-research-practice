# Ch.8 — 다른 저장소의 규칙

공개된 agent 저장소에는 다시 쓸 만한 작업 습관이 있다. 작은 단위의 수정, 가정 명시, 실패 보고, 역할 분리, tool 호출 기록은 연구에도 쓸 데가 있다. 다만 그 규칙은 코드를 고치고 tool을 부르는 자리를 가운데 두고 짜여 있다. 로봇 실험의 수치가 무엇을 가리키는지 말하려면 dataset, calibration, frame, metric, 실패 처리, reviewer risk까지 같은 자리에 적혀 있어야 한다.

tool 호출 쪽으로는 논문이 정해 둔 것이 있다. Yao 등은 reasoning trace와 action을 번갈아 내놓게 한 [ReAct](https://arxiv.org/abs/2210.03629)를 ALFWorld와 WebShop에서 쟀고, in-context example 한둘로 절대 성공률을 34%와 10% 올렸다. reasoning trace는 모델이 action plan을 세우고 따라가고 고치게 했고 예외도 그 자리에서 다루게 했다. action은 knowledge base나 environment 같은 외부 출처에서 정보를 더 모으는 통로였다. Schick 등의 [Toolformer](https://arxiv.org/abs/2302.04761)는 어느 API를 언제 부르고 무슨 argument를 넘기고 그 결과를 다음 token 예측에 어떻게 넣을지를 모델이 정하도록 훈련했다. 두 연구가 정해 둔 것은 언제 부르고 어떤 argument를 넘기고 결과를 어떻게 다룰지다. 그 호출이 어느 dataset의 어느 split으로 가고 어느 metric script로 재는지는 연구자 쪽에 남는다.

연구자 쪽에 남은 것을 어디에 적어 둘지는 그 작업이 도는 구조에서 정해진다. Anthropic의 [Managed Agents](https://www.anthropic.com/engineering/managed-agents)는 자리를 셋으로 갈랐다. session은 일어난 일을 그대로 쌓는 append-only log, harness는 모델을 부르고 그 tool 호출을 그 infrastructure로 넘기는 loop, sandbox는 코드를 실행하고 파일을 고치는 실행 환경이다. harness가 loop를 한 바퀴 돌 때마다 정하는 것은 지금 어느 도구를 부르고 그 결과를 어디로 보낼지다. 연구 workspace에서는 사람이 그 판단을 미리 글로 적어 둔다. 어느 파일을 먼저 읽고 어떤 결과가 나오면 멈출지를 문장으로 남기면 agent가 걸음마다 그 문장을 본다. 그 문장 묶음이 harness 자리에 놓인다. 다음 작업에서 다시 읽을 기록은 session에, 실제 파일과 command와 dataset이 놓인 경계는 sandbox에 대응한다.

연구 workspace로 옮겨 오는 것은 이 세 자리의 구분이다. 옮겨 올 규칙은 저장소마다 prompt 문구로 적혀 있다. 그 문구를 손보기 전에 세 자리부터 대응시킨다.

## 어느 저장소를 열어 보나

손볼 문구는 저장소를 열어야 나온다. 저장소를 처음 고를 때 손에 잡히는 수는 GitHub star다. star가 세는 것은 그 저장소를 눈여겨본 사람 수까지다. 그다음 볼 자리는 유형이 정한다. 아래 이름은 유형을 가리키는 예다.

| 유형 | 예 | 볼 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 항목 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 확인 규칙 |

첫 줄의 skill repo는 그 습관이 주고받을 수 있는 단위로 묶인 꼴이다. Anthropic은 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)를 agent가 찾아 필요할 때 올려 쓰는, 지시와 스크립트와 자료가 든 폴더로 적었다. `SKILL.md`는 YAML frontmatter로 열고 `name`과 언제 쓰는지를 적는 `description`이 필수다. 언제 쓰는지가 폴더 안에 함께 적혀 온다. 그 칸이 적는 것은 에이전트가 언제 이 폴더를 열지까지다. 이쪽 연구 작업의 어느 자리에서 걸리는지는 옮겨 오는 사람이 적는다.

표의 `볼 것` 칸을 세 자리에 나눠 보면 어느 줄이 무엇을 주는지 갈린다. 작은 수정과 가정 명시와 실패 보고, role 분리와 tool handoff는 agent가 걸음마다 따를 문장이라 harness 자리에 붙는다. tracing과 user reaction prior는 다음 작업에서 다시 읽을 것이라 session 자리로 간다. 표의 `볼 것` 칸이 세 자리에 닿는 데까지가 여기다.

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

여덟 줄은 앞선 장들이 이미 채워 본 이름이다. 위의 다섯 줄은 실행을 걸 때 그 자리에서 채우는 최소 기록 칸이다. 그 칸이 가리키는 것은 sandbox 자리에 놓인 파일과 script다. implementation status는 `저장소에 있다`에 붙이는 라벨이라 논문 주장과 실행 경로를 맞춰 봐야 정해진다. result provenance는 실험 숫자에서 시작할 때 남기는 `result-provenance-tuple.md`가 받는다. 외부 저장소에서 가져온 문구 옆에 이 여덟 줄을 따로 단다.

부록 D(`PATH.md`)는 멈춰야 하는 조건 하나로 `실험 조건이 바뀌었는데 숫자를 비교하려 한다`를 적어 두었다. 조건이 바뀐 뒤에도 앞 조건에서 만들어 둔 cache를 그대로 읽거나 이름만 같은 metric script 둘을 한 표에 올려도 숫자는 그대로 나온다. 위 여덟 줄이 채워져 있으면 그 자리에서 어긋난 항목이 눈에 보인다. 맨 아래 줄은 원고 문장 쪽으로 이어져 `claim-evidence-map.md`에서 주장과 근거로 나뉜다.

## 규칙을 쪼개서 옮겨 온다

옮기는 일은 외부 규칙을 쪼개는 데서 시작한다. 저장소 하나가 내놓는 prompt 문구에는 도구를 부르는 법과 다음 세션이 읽을 상태와 계속 걸어 둘 행동 규칙이 한 덩이로 적혀 있어, 통째로 옮기면 셋이 함께 따라온다. 조각마다 무엇인지를 먼저 묻는다. [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)은 server가 내놓는 것을 세 이름으로 갈라 두었다. tool은 AI 애플리케이션이 불러서 동작을 시키는 실행 가능한 함수이고, resource는 맥락 정보를 주는 자료 출처이며, prompt는 언어 모델과 주고받는 자리를 짜는 데 다시 쓰는 틀이다. 옮겨 올 줄에도 같은 물음을 건다 — 이 줄은 실행되는 것인가, 읽히는 자료인가, 다시 채워 쓰는 틀인가.

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 같은 도구에 묶인 호출법을 뗀다.
3. durable state는 `project-memory.json`, ledger, replay case로 옮긴다.
4. 남는 행동 규칙은 `AGENTS.md`나 template로 옮긴다.
5. 실제 실행 경계는 repo, dataset, artifact, command로 나눈다.
6. dataset, metric, 결과물, reviewer risk 항목을 더한다.
7. 사용자가 반복해서 반려한 패턴을 앞에 둔다.

첫째 걸음과 둘째 걸음은 같은 문구를 두 번 만진다. 먼저 기능별로 갈라 놓고, 갈라 놓은 조각에서 도구 이름에 묶인 호출법을 뗀다. 잘게 갈라 두면 쓰는 쪽에서 다시 묶을 자리가 나온다. Anthropic의 [도구 작성 지침](https://www.anthropic.com/engineering/writing-tools-for-agents)은 도구 하나가 여러 개별 동작이나 API 호출을 안에서 처리하며 기능을 묶을 수 있다고 적었고, 관련 있는 것을 같은 접두어 아래 모으는 namespacing이 도구가 많을 때 경계를 가르는 데 도움이 된다고 적었다. 같은 지침은 도구가 agent에 돌려주는 것을 high signal 정보로 두라고 했다. 옮겨 온 규칙에도 같은 손질이 든다. dataset 쪽 규칙과 원고 쪽 규칙을 각각 한 이름 아래 모아 두면 다음 요청에서 열 데가 하나로 선다.

셋째 걸음과 넷째 걸음과 다섯째 걸음은 그 조각을 놓을 데를 정한다. 앞의 세 이름이 조각의 종류를 물었다면 이 셋은 실행 구조의 어느 자리에 놓일지를 가른다. durable state는 다음 작업에서 다시 읽는 기록이니 session이 받는다. 그 기록을 다시 읽는 사이에도 agent가 걸음마다 보는 문장이 있고, 남는 행동 규칙이 harness를 채운다. 그 문장이 실제로 손대는 repo와 dataset과 artifact와 command는 sandbox 쪽 일이다. 둘째 걸음에서 떼어 낸 도구별 호출법은 그 저장소의 도구에 남는다.

다섯째 걸음의 실행 경계는 로봇을 돌리는 자리에서 하나 더 늘어난다. 로봇은 코드가 도는 기계 밖에서 움직인다. 장치와 시계와 네트워크의 현재 상태가 같은 경계 위에 놓인다. 그 상태를 적어 두는 일은 다음 장이 맡는다.

일곱 걸음을 마치면 그 규칙은 `AGENTS.md`와 template 안에 놓이고, 다음 요청부터 agent가 그것을 읽는다. 규칙이 지켜졌는지는 agent가 답을 내놓는 자리에서 드러난다. 부록 B(`QUICKSTART.md`)의 첫 AI 요청 블록도 마지막 줄에서 그 자리를 짚었다. 원문 파일이나 산출물이 손에 있는 자리에서는 요약으로 프로젝트의 참을 정하지 말라고 못 박았다. 그 블록은 답하기 전에 무엇을 밝힐지를 요청 안에 미리 적어 둔다. 옮겨 온 규칙에도 같은 자리를 하나 둔다. 연구자가 건 요청 하나에 agent가 답을 쓴다. 답을 내놓기 전에 아래를 짚는다.

```text
읽지 않은 파일을 읽은 것처럼 말했는가:
근거 범위를 넘는 주장을 썼는가:
실행해야 할 때 계획만 말했는가:
사용자가 싫어한 문체나 구조를 반복했는가:
공개 문서에 내부 작업 기록을 남겼는가:
```

걸리는 항목이 하나라도 있으면 다음 행동을 바꾼다. 같은 항목이 두 번째로 걸리면 그 줄을 `AGENTS.md`의 규칙 한 줄이나 replay case로 옮겨 적는다. 무엇이 걸렸는지가 쌓이면 어느 저장소에서 옮겨 온 규칙이 무엇을 줄였는지도 그 기록에서 갈린다.

GitHub star 수는 참고할 저장소를 처음 찾을 때만 본다. 그 규칙을 실제로 쓸지는 같은 metric 혼동과 cache 실수, 반복되는 reviewer comment가 줄어드는지가 정한다.
