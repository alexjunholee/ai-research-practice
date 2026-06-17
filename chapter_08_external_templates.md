# Ch.8 — 외부 agent repo 이식 기준

## 목적

공개 agent repo에서 가져올 항목과 로보틱스 연구에 맞게 추가해야 할 항목을 분리한다.

## 참고할 repo 유형

| 유형 | 예 | 가져올 것 |
|---|---|---|
| coding-agent skill repo | `multica-ai/andrej-karpathy-skills` | 작은 수정, 가정 명시, 범위 제한, 실패 보고 |
| agent 개념 입문 repo | `datawhalechina/hello-agents` | agent, memory, tool use, evaluation 개념 지도 |
| framework 문서 | LangGraph, CrewAI, AutoGen, OpenAI Agents SDK | workflow, role 분리, tool handoff, tracing |
| local research agent repo | `alexjunholee/robotics-research-agent` | user reaction prior, 연구 증거 gate |

## 그대로 가져오면 부족한 항목

일반 agent repo는 보통 코드 변경과 tool use에 강하다. 로보틱스 연구에서는 다음 항목이 추가로
필요하다.

- dataset, split, sequence
- query/database direction
- ground-truth frame
- metric script
- failure policy
- implementation status
- result provenance
- claim/evidence boundary

## 이식 절차

1. 외부 repo의 규칙을 기능별로 나눈다.
2. Claude, Cursor, Codex 등 특정 도구에 묶인 호출법을 제거한다.
3. 남는 행동 규칙을 `AGENTS.md`나 template로 옮긴다.
4. 로보틱스/CV evidence gate를 추가한다.
5. user reaction prior로 반복 반려 패턴을 앞에 둔다.

## user reaction prior

답변 전에 아래 항목을 먼저 확인한다.

```text
읽지 않은 파일을 읽은 것처럼 말했는가:
증거보다 큰 claim을 썼는가:
실행해야 할 때 계획만 말했는가:
사용자가 싫어한 문체나 구조를 반복했는가:
공개 문서에 내부 작업 흔적을 남겼는가:
```

걸리는 항목이 있으면 문장을 덧붙이지 않는다. 다음 행동을 바꾼다.

## 이식 기준

GitHub star는 발견의 단서로만 쓴다. 이식 여부는 내 연구에서 반복된 실패를 줄이는지로 정한다.

| 반복 실패 | 이식할 규칙 |
|---|---|
| 코드 수정은 됐지만 숫자 의미가 비어 있음 | result provenance template |
| 논문 요약은 됐지만 실행 경로가 없음 | paper-code-experiment map |
| 같은 metric 혼동 반복 | experiment contract |
| reviewer 답변이 문장만 개선됨 | claim/evidence table |
| AI가 사용자의 반려 패턴을 반복 | user reaction prior |
