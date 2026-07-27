# Ch.8 — 남의 repo에서 습관만 가져온다

공개된 agent 저장소에는 다시 쓸 만한 작업 습관이 있다. 작은 단위의 수정, 가정 명시, 실패 보고, 역할 분리, tool 호출 기록은 연구에도 쓸 데가 있다. 다만 그 규칙은 코드를 고치고 tool을 부르는 자리를 가운데 두고 짜여 있다. 로봇 실험의 수치가 무엇을 가리키는지 말하려면 dataset, calibration, frame, metric, 실패 처리, reviewer risk까지 같은 자리에 적혀 있어야 한다.

tool 호출 쪽으로는 논문이 정해 둔 것이 있다. Yao 등은 reasoning trace와 action을 번갈아 내놓게 한 [ReAct](https://arxiv.org/abs/2210.03629)를 ALFWorld와 WebShop에서 쟀고, in-context example 한둘로 절대 성공률을 34%와 10% 올렸다. reasoning trace는 모델이 action plan을 세우고 따라가고 고치게 했고 예외도 그 자리에서 다루게 했다. action은 knowledge base나 environment 같은 외부 출처에서 정보를 더 모으는 통로였다. Schick 등의 [Toolformer](https://arxiv.org/abs/2302.04761)는 어느 API를 언제 부르고 무슨 argument를 넘기고 그 결과를 다음 token 예측에 어떻게 넣을지를 모델이 정하도록 훈련했다. 두 연구가 정해 둔 것은 호출의 시점과 argument와 결과 처리다. 그 호출이 어느 dataset의 어느 split으로 가고 어느 metric script로 재는지는 연구자 쪽에 남는다.

Anthropic의 [Managed Agents](https://www.anthropic.com/engineering/managed-agents)는 자리를 셋으로 갈랐다. session은 일어난 일을 그대로 쌓는 append-only log, harness는 모델을 부르고 그 tool 호출을 해당 infrastructure로 넘기는 loop, sandbox는 코드를 실행하고 파일을 고치는 실행 환경이다. harness가 loop를 한 바퀴 돌 때마다 정하는 것은 지금 어느 도구를 부르고 그 결과를 어디로 보낼지다. 연구 workspace에서는 사람이 그 판단을 미리 글로 적어 둔다. 어느 파일을 먼저 읽고 어떤 결과가 나오면 멈출지를 문장으로 남기면 agent가 걸음마다 그 문장을 본다. 그 문장 묶음이 harness 자리에 놓인다. 다음 작업에서 다시 읽을 기록은 session, 실제 파일과 command와 dataset이 놓인 경계는 sandbox에 대응한다.

연구 workspace로 옮겨 오는 것은 이 세 자리의 구분이다. 옮겨 올 규칙은 저장소마다 prompt 문구로 적혀 있다. 그 문구를 손보기 전에 세 자리부터 대응시킨다.

## 어느 저장소를 열어 보나

저장소를 처음 고를 때 손에 잡히는 수는 GitHub star다. 그다음 볼 자리는 유형이 정한다. 아래 이름은 유형을 가리키는 예다.

| 유형 | 예 | 볼 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 항목 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 확인 규칙 |

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

부록 D(`PATH.md`)는 멈춰야 하는 조건 하나로 `실험 조건이 바뀌었는데 숫자를 비교하려 한다`를 적어 두었다. 조건이 바뀐 뒤에도 앞 조건에서 만들어 둔 cache를 그대로 읽거나 이름만 같은 metric script 둘을 한 표에 올려도 숫자는 그대로 나온다. 위 여덟 줄이 채워져 있으면 그 자리에서 어긋난 항목이 눈에 보인다. 맨 아래 줄은 원고 문장 쪽으로 이어져 `claim-evidence-map.md`에서 주장과 근거로 나뉜다.

## 규칙을 쪼개서 옮겨 온다

옮기는 일은 외부 규칙을 쪼개는 데서 시작한다.

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 등 특정 도구에 묶인 호출법을 제거한다.
3. durable state는 `project-memory.json`, ledger, replay case로 옮긴다.
4. 남는 행동 규칙은 `AGENTS.md`나 template로 옮긴다.
5. 실제 실행 경계는 repo, dataset, artifact, command로 나눈다.
6. dataset, metric, 결과물, reviewer risk 항목을 더한다.
7. 사용자가 반복해서 반려한 패턴을 앞에 둔다.

다섯째 걸음의 실행 경계는 로봇을 돌리는 자리에서 하나 더 늘어난다. 장치와 시계와 네트워크의 현재 상태가 같은 경계 위에 놓인다.

일곱 걸음을 마치면 그 규칙은 `AGENTS.md`와 template 안에 놓이고, 다음 요청부터 agent가 그것을 읽는다. 규칙이 지켜졌는지는 agent가 답을 내놓는 자리에서 드러난다. 부록 B(`QUICKSTART.md`)의 첫 AI 요청 블록이 마지막 줄에서 요약으로 프로젝트의 참을 정하지 말라고 못 박은 것도 그 자리다. 답변 전에 아래 항목을 확인한다.

```text
읽지 않은 파일을 읽은 것처럼 말했는가:
근거 범위를 넘는 주장을 썼는가:
실행해야 할 때 계획만 말했는가:
사용자가 싫어한 문체나 구조를 반복했는가:
공개 문서에 내부 작업 기록을 남겼는가:
```

해당 항목이 하나라도 있으면 다음 행동을 바꾼다.

GitHub star 수는 참고할 저장소를 처음 찾을 때만 보조 지표로 쓴다. 실제 채택 여부는 같은 metric 혼동과 cache 실수, 반복되는 reviewer comment를 줄이는 데 도움이 되는지로 판단한다.
