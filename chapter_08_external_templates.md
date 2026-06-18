# Ch.8 — 유명한 agent repo에서는 습관만 골라 온다

공개 agent repo에는 가져올 습관이 있다. 작은 수정, 가정 명시, 실패 보고, 역할 분리, tool 호출 기록 같은 습관은 연구에도 도움이 된다. 그 규칙을 로봇 연구에 그대로 옮기면 빠지는 항목이 많다.

일반 agent repo는 코드 변경과 tool use에 강하다. 로보틱스/CV 연구에서는 dataset, calibration, frame, metric, 실패 처리, reviewer risk가 실험 숫자의 의미를 정한다.

## 참고할 repo 유형

| 유형 | 예 | 볼 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 항목 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 확인 규칙 |

## 그대로 가져오면 빠지는 항목

- dataset, split, sequence
- query/database direction
- ground-truth frame
- metric script
- failure policy
- implementation status
- result provenance
- 원고에서 말할 수 있는 범위

## 옮길 때 볼 것

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 등 특정 도구에 묶인 호출법을 제거한다.
3. 남는 행동 규칙을 `AGENTS.md`나 template로 옮긴다.
4. dataset, metric, 결과물, reviewer risk 항목을 더한다.
5. 사용자가 반복해서 반려한 패턴을 앞에 둔다.

답변 전에 아래 항목을 확인한다.

```text
읽지 않은 파일을 읽은 것처럼 말했는가:
근거 범위를 넘는 주장을 썼는가:
실행해야 할 때 계획만 말했는가:
사용자가 싫어한 문체나 구조를 반복했는가:
공개 문서에 내부 작업 기록을 남겼는가:
```

해당 항목이 하나라도 있으면 다음 행동을 바꾼다.

GitHub star 수는 발견의 단서다. 기준은 연구에서 같은 metric 혼동, 같은 cache 실수, 같은 reviewer comment를 줄일 수 있는지다.
