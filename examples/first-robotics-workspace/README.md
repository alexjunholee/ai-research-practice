# First Robotics Workspace

이 폴더는 로보틱스·CV 연구 프로젝트를 시작하는 첫날에 작업 공간을 어떻게 채워 두어야 하는지 보여 주는 공개 예시다. 외부 공개용 예시이므로 실제 연구 파일이나 개인 로컬 경로, 원본 대화 로그는 포함하지 않았으며, 자신의 프로젝트에 적용할 때는 예시 이름과 경로만 실제 환경에 맞게 바꾸어 쓰면 된다.

## Start Here

작업 공간을 열었다면 파일들을 한꺼번에 읽으려 하지 말고 아래 순서대로 기본 규칙과 현재 상태부터 확인한다.

1. 루트의 `AGENTS.md`를 가장 먼저 읽어 작업 규칙과 경계를 파악한다.
2. `project-memory.json`을 열어 현재 확인한 사실과 `source_of_truth`, `current_evidence`, `first_research_loop`, `next_smallest_actions` 항목을 확인한다.
3. `notes/first-day-workspace-checklist.md`를 따라 정본으로 삼을 원본 파일과 실행 결과를 확정한다.
4. 기존에 쓰던 `CLAUDE.md`, `.claude/`, Cursor 규칙이 남아 있다면 `notes/codex-porting-checklist.md`를 참고해 행동 원칙만 추려 옮긴다.
5. 작업을 요청하기 전에 session, harness, sandbox의 경계부터 먼저 적는다.
6. 위 확인이 끝났으면 `notes/first-ai-session-prompt.md`의 빈칸을 채워 첫 AI 세션을 시작한다.

## First Run Check

첫 세션을 열기 전에 아래 아홉 개 파일이 작업 공간 안에 모두 제자리에 있는지부터 점검한다.

```text
AGENTS.md
README.md
project-memory.json
notes/first-day-workspace-checklist.md
notes/first-ai-session-prompt.md
notes/paper-code-experiment-map.md
notes/experiment-contract.md
notes/weekly-research-ledger.md
artifacts/first-ai-session-message.txt
```

파일 유무를 확인했다면 내용 검증으로 넘어간다. `project-memory.json`은 문법 오류 없이 JSON으로 파싱되어야 하며, `source_of_truth`, `tool_surface_map`, `current_evidence`, `first_research_loop`, `next_smallest_actions` 필드도 비어 있으면 안 된다. 또한 `artifacts/first-ai-session-message.txt`에 저장한 첫 메시지에는 `[task]`, `[target note]`, `[supporting note]`, `[expected artifact]` 같은 대괄호 빈칸이 남아 있지 않아야 바로 세션에 보낼 수 있다.

## Read Order

새 AI 세션을 열 때는 매번 자료를 찾는 순서를 새로 정하지 말고 아래 다섯 파일을 차례대로 읽히면 작업 맥락이 일정하게 유지된다.

```text
AGENTS.md
project-memory.json
notes/first-day-workspace-checklist.md
notes/weekly-research-ledger.md
notes/first-ai-session-prompt.md
```

이 순서대로 읽고 나면 에이전트는 프로젝트 규칙과 최근 주간 기록을 모두 파악한 상태에서 이번 세션의 질문으로 들어가게 된다.

## First Research Loop

첫 연구 루프는 한 번에 하나만 골라 성격에 맞는 기록 문서에 결과를 남긴다. 논문을 한 편 읽었다면 `notes/paper-code-experiment-map.md`에 주장과 코드 연결을 정리하고, 실험 숫자를 해석할 때는 `notes/experiment-contract.md`로 비교 프로토콜을 확인한 뒤에만 결론을 적으며, 실행 중 오류가 났다면 `notes/stage-local-debugging.md`에서 stage, signal, next check 순으로 원인을 좁힌다.

그리고 첫 세션에서 AI가 답을 내놓을 때는 항상 아래 아홉 가지 경계 항목을 먼저 채우도록 요구한다.

```text
session record to update:
harness rule that controls this action:
sandbox action allowed now:
sandbox action not allowed now:
object under truth control:
current evidence permits:
current evidence forbids:
smallest next action:
verification:
```

이 아홉 항목을 먼저 확인하게 하면 AI가 막연한 일반론 대신 지금 연구 상태와 허용된 범위 안에서 움직이게 된다. 세션을 마칠 때는 현재 확인한 사실과 아직 말하면 안 되는 주장, 그리고 다음에 실행할 행동 하나를 주간 기록에 남기고, 같은 경계를 `project-memory.json`의 `current_evidence`와 `next_smallest_actions`에도 반영해 두어야 다음 세션이 그 위에서 곧바로 이어갈 수 있다.
