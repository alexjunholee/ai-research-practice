# Ch.8 — 남의 repo에서 습관만 가져온다

공개된 agent 저장소에는 재사용할 만한 작업 습관이 있다. 작은 단위의 수정, 가정 명시, 실패 보고, 역할 분리, tool 호출 기록은 연구에도 도움이 된다. 다만 그 규칙을 로봇 연구에 그대로 옮기면 실험에 필요한 항목이 빠질 수 있다.

일반적인 agent 저장소는 코드 변경과 tool use를 중심으로 규칙을 구성한다. 로보틱스 연구에서는 dataset, calibration, frame, metric, 실패 처리, reviewer risk까지 알아야 실험 수치의 의미를 판단할 수 있다.

Anthropic의 [Managed Agents](https://www.anthropic.com/engineering/managed-agents)는 session을 사건의 append-only log, harness를 모델 호출과 tool routing을 맡는 loop, sandbox를 코드 실행과 파일 편집이 일어나는 환경으로 구분한다. 이 가이드는 구현을 그대로 복제하지 않고 역할만 연구 workspace에 옮긴다. 다음 작업에서 다시 읽을 기록은 session, agent가 따를 규칙은 harness, 실제 파일·command·dataset이 놓인 경계는 sandbox에 대응한다. 외부 저장소를 참고할 때는 먼저 이 세 경계를 대응시키고 prompt 문구는 그다음에 조정한다.

## 참고할 repo 유형

| 유형 | 예 | 볼 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 항목 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 확인 규칙 |

## 그대로 가져오면 빠지는 항목

- dataset, split, sequence
- task input/output
- ground-truth frame
- metric script
- failure policy
- implementation status
- result provenance
- 원고에서 말할 수 있는 범위

## 옮길 때 볼 것

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 등 특정 도구에 묶인 호출법을 제거한다.
3. durable state는 `project-memory.json`, ledger, replay case로 옮긴다.
4. 남는 행동 규칙은 `AGENTS.md`나 template로 옮긴다.
5. 실제 실행 경계는 repo, dataset, artifact, command로 나눈다.
6. dataset, metric, 결과물, reviewer risk 항목을 더한다.
7. 사용자가 반복해서 반려한 패턴을 앞에 둔다.

답변 전에 아래 항목을 확인한다.

```text
읽지 않은 파일을 읽은 것처럼 말했는가:
근거 범위를 넘는 주장을 썼는가:
실행해야 할 때 계획만 말했는가:
사용자가 싫어한 문체나 구조를 반복했는가:
공개 문서에 내부 작업 기록을 남겼는가:
```

해당 항목이 하나라도 있으면 다음 행동을 바꾼다.

GitHub star 수는 참고할 저장소를 처음 찾을 때만 보조 지표로 쓴다. 실제 채택 여부는 같은 metric 혼동과 cache 실수, 반복되는 reviewer comment를 줄이는 데 도움이 되는지로 판단한다.
