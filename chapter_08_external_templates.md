# Ch.8 — 외부 agent repo와 템플릿은 하네스로 다시 읽는다

유명한 agent repo는 좋은 출발점이다. 연구 운영체제로 쓰려면 각 repo가
해결하는 층을 보고, 로보틱스 연구에 빠진 gate를 더해야 한다.

[`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)는 단일
`CLAUDE.md`, Cursor rule, skill package 형태로 coding agent 규칙을 제공한다.
현재 README는 assumption을 드러내고, 단순한 구현을 고르고, 필요한 줄만
고치고, 검증 가능한 성공 기준을 만들라는 네 원칙을 전면에 둔다. 이 원칙은
Codex에서도 유효하다. 옮길 때는 `CLAUDE.md`라는 파일명을 그대로 따르기보다
project `AGENTS.md`의 규칙으로 흡수한다.

[`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)는 agent를 배우는 사람이
개념에서 실습으로 이동하도록 만든 course repo다. 초보자가 builder로
넘어가는 흐름을 배울 수 있다. 그러나 일반 agent 교육만으로는 SLAM metric,
dataset archaeology, reviewer risk gate가 채워지지 않는다.

[`e2b-dev/awesome-ai-agents`](https://github.com/e2b-dev/awesome-ai-agents)와
[`kaushikb11/awesome-llm-agents`](https://github.com/kaushikb11/awesome-llm-agents) 같은 목록은
생태계를 빠르게 훑는 데 좋다. 특히 framework category, update discipline,
metadata를 보는 법을 배울 수 있다. 목록은 discovery tool로 쓰고, 연구
workflow 적합성은 dataset, metric, artifact, claim gate에서 다시 확인한다.

[`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph)는 long-running,
stateful agent workflow를 위한 낮은 층위의 orchestration을 전면에 둔다. 여기서
빌려올 것은 durable execution, human-in-the-loop, memory, tracing 같은 상태
관리 어휘다. 로보틱스 연구에서는 이 어휘를 `project-memory.json`, ledger,
replay case로 내려놓아야 한다. agent state가 이어진다는 사실만으로 실험
provenance가 닫히지는 않는다.

[`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI)는 role-playing autonomous
agent를 crew와 flow로 묶는 쪽에 무게가 있다. 역할과 task를 나누는 감각은
원고, 실험, 코드 점검을 분리할 때 유용하다. 다만 role이 나뉘어도 dataset,
metric, artifact, claim gate가 없으면 연구 증거는 여전히 비어 있다.

[`microsoft/autogen`](https://github.com/microsoft/autogen)은 multi-agent AI application
framework로 소개되지만, 현재 공개 README는 maintenance mode를 명시한다.
이 사례는 기능보다 lifecycle을 읽는 훈련에 가깝다. 유명했던 framework라도
유지 상태가 바뀌면 새 연구 하네스의 기반으로 삼기 전에 support surface와
대체 경로를 먼저 봐야 한다.

[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)는 agents,
tools, handoffs, guardrails, sessions, tracing, MCP integration, sandbox agents를
작은 primitive로 묶는다. 이 구분은 Codex-first 작업장에서도 유용하다. agent가
도구를 호출하는 일, session이 상태를 들고 있는 일, guardrail이 입력·출력을
검사하는 일, sandbox가 파일 상태를 격리하는 일을 분리해서 볼 수 있기
때문이다. 그래도 SDK runtime state는 연구 evidence gate를 대신하지 않는다.

## Claude 중심 자료를 Codex에서 쓰는 법

Claude용 repo에서 가져올 것과 버릴 것을 나눈다.

| Claude 중심 요소 | Codex에서의 대응 |
|---|---|
| `CLAUDE.md` 운영 규칙 | `AGENTS.md`로 옮긴다 |
| `.claude/skills`의 절차 지식 | Codex skill 또는 repo template으로 분리한다 |
| slash command | 반복 가능한 shell command, script, template으로 바꾼다 |
| plugin install 명령 | 공개 문서에는 링크와 개념만 두고, 로컬 설치는 별도 경계에 둔다 |
| coding-only rule | dataset, metric, artifact, claim gate를 추가한다 |
| "test passes" 성공 기준 | experiment protocol과 manuscript claim까지 확장한다 |

먼저 inventory를 만든다. `CLAUDE.md`만 열고 끝내면 slash command, `.claude/skills`,
Cursor rule, MCP/plugin 설정, workflow command가 빠진다. `codex-porting-checklist.md`
에는 discovery sweep과 keep/drop/destination 결정을 먼저 적는다.

이식할 때는 규칙의 payload를 본다. "작게 고쳐라"는 모든 coding agent에
통한다. "실험 claim은 metric protocol 뒤에 온다"는 로보틱스 연구 하네스가
추가해야 할 규칙이다.

이식 완료 조건은 파일 이름 변경이 아니다. `AGENTS.md`에 project goal, 공개
경계, read order, evidence gate, durable correction, verification command가
들어가고, `codex-porting-checklist.md`가 tool-specific command를 portable
script나 template으로 바꾸며, dataset·metric·artifact·claim·reviewer
risk·replay gate를 추가했을 때 첫 연구 행동으로 넘어간다.

## 연구용 하네스가 추가하는 것

일반 agent repo의 무게는 대개 code execution, memory, tool use, multi-agent
orchestration에 있다. 로보틱스 연구에는 다음 항목이 더 필요하다.

- dataset archaeology
- result provenance tuple
- SLAM/VIO/VPR metric contract
- code presence와 active method의 분리
- reviewer pressure와 claim/evidence map
- replay case
- public/private boundary

이 항목들이 없으면 agent는 일을 많이 한다. 연구자는 뒤에서 그 일이 어떤
claim을 허용하는지 다시 정리해야 한다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| 외부 repo 읽기 | 구조, 설치 방식, 반복 규칙, 빠진 gate를 분리했다 | 유명한 목록을 그대로 연구 방법으로 옮겼다 | agent repo의 품질과 로보틱스 연구 적합성은 다른 판단이다 |
| Claude 자료 이식 | payload를 `AGENTS.md`, script, template으로 나눴다 | `CLAUDE.md`와 slash command 이름을 보존했다 | 이름보다 중요한 것은 다음 세션이 같은 행동을 반복하는 능력이다 |
| Template 사용 | evidence gate가 닫히는 순간에 필요한 template만 붙였다 | 모든 template을 처음부터 채웠다 | 빈 문서는 새 유지비를 만든다 |
| 목록 탐색 | 발견 순서를 정하는 신호로만 썼다 | 목록의 크기를 연구 신뢰도로 읽었다 | 연구 claim은 dataset, metric, artifact에서 닫힌다 |

## 복사해서 시작하는 템플릿

이 repo의 `templates/`는 첫 프로젝트에 붙여 쓸 수 있는 최소 셋이다.

| 상황 | 템플릿 |
|---|---|
| 작업장 첫 화면을 만든다 | [`workspace-readme.md`](templates/workspace-readme.md) |
| 새 repo를 AI와 함께 쓴다 | [`AGENTS.template.md`](templates/AGENTS.template.md) |
| Claude 중심 규칙을 Codex로 옮긴다 | [`codex-porting-checklist.md`](templates/codex-porting-checklist.md) |
| 첫날 작업장을 만든다 | [`first-day-workspace-checklist.md`](templates/first-day-workspace-checklist.md) |
| 첫 AI 세션을 연다 | [`first-ai-session-prompt.md`](templates/first-ai-session-prompt.md) |
| 프로젝트의 현재 truth와 correction을 남긴다 | [`project-memory.template.json`](templates/project-memory.template.json) |
| 논문 한 편의 claim/evidence를 빠르게 남긴다 | [`paper-reading-note.md`](templates/paper-reading-note.md) |
| 논문 한 편을 code와 experiment로 연결한다 | [`paper-code-experiment-map.md`](templates/paper-code-experiment-map.md) |
| dataset provenance를 확인한다 | [`dataset-archaeology-sheet.md`](templates/dataset-archaeology-sheet.md) |
| 실험 숫자를 해석한다 | [`experiment-contract.md`](templates/experiment-contract.md) |
| 결과 숫자의 출처를 남긴다 | [`result-provenance-tuple.md`](templates/result-provenance-tuple.md) |
| stage-local debug를 진행한다 | [`stage-local-debugging.md`](templates/stage-local-debugging.md) |
| 원고 문장과 evidence를 묶는다 | [`claim-evidence-map.md`](templates/claim-evidence-map.md) |
| 반복 실패를 시험으로 만든다 | [`replay-case.md`](templates/replay-case.md) |
| 한 주의 연구 상태를 닫는다 | [`weekly-research-ledger.md`](templates/weekly-research-ledger.md) |
| 발행 URL을 직접 확인한다 | [`publication-browser-signoff.md`](templates/publication-browser-signoff.md) |

템플릿은 AI가 다음 행동을 할 수 있는 evidence gate를 닫는 데 쓴다.

## 첫 프로젝트에 붙이는 순서

1. `workspace-readme.md`를 `README.md`로 복사하고 시작 순서를 고정한다.
2. `AGENTS.template.md`를 프로젝트에 맞게 줄인다.
3. 기존 `CLAUDE.md`나 Cursor rule이 있으면 `codex-porting-checklist.md`의
   discovery sweep으로 source를 먼저 찾고, 옮길 규칙과 버릴 명령을 나눈다.
4. `first-day-workspace-checklist.md`로 공개/비공개 경계와 source of truth를
   닫는다.
5. `first-ai-session-prompt.md`를 채워 첫 세션의 읽기 순서와 evidence gate를
   고정한다.
6. `project-memory.template.json`에 현재 truth와 durable constraint를 쓴다.
7. 읽을 논문 하나를 `paper-code-experiment-map.md`로 정리한다.
8. 첫 실험 숫자는 `experiment-contract.md`와 `result-provenance-tuple.md`에
   같이 넣는다.
9. 원고 문장이 생기면 `claim-evidence-map.md`를 만든다.
10. AI가 같은 실수를 반복하면 `replay-case.md`로 승격한다.

이 순서가 지켜지면 AI 도구는 대화 상대에서 연구 운영체제의 일부로 내려온다.
