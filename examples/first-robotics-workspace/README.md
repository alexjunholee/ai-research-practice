# First Robotics Workspace

이 폴더는 첫날 로보틱스/CV 연구 프로젝트를 어떻게 채우는지 보여 주는 공개
예시다. 실제 연구 파일, 개인 경로, 원 대화 로그는 들어 있지 않다.

## Start Here

1. `AGENTS.md`를 먼저 읽는다.
2. `project-memory.json`에서 현재 확인한 사실, source_of_truth, current_evidence,
   first_research_loop, next_smallest_actions를 확인한다.
3. `notes/first-day-workspace-checklist.md`로 원 파일과 실행 결과를 정한다.
4. 기존 `CLAUDE.md`, `.claude/`, Cursor rule이 있으면
   `notes/codex-porting-checklist.md`로 행동 원칙만 옮긴다.
5. session, harness, sandbox 경계를 먼저 쓴다.
6. 첫 AI 세션에는 `notes/first-ai-session-prompt.md`를 채워 보낸다.

## First Run Check

첫 세션 전에 다음 파일이 있어야 한다.

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

`project-memory.json`은 JSON으로 열려야 한다. 첫 메시지에는 `[task]`,
`[target note]`, `[supporting note]`, `[expected artifact]`가 남아 있으면 안 된다.
memory 안의 `source_of_truth`, `tool_surface_map`, `current_evidence`,
`first_research_loop`, `next_smallest_actions`도 비어 있으면 안 된다.

## Read Order

```text
AGENTS.md
project-memory.json
notes/first-day-workspace-checklist.md
notes/weekly-research-ledger.md
notes/first-ai-session-prompt.md
```

## First Research Loop

논문 한 편은 `notes/paper-code-experiment-map.md`에 남긴다. 실험 숫자는
`notes/experiment-contract.md`로 protocol을 확인한 뒤 말한다. 에러는
`notes/stage-local-debugging.md`에서 stage, signal, next check로 좁힌다.

첫 세션의 답은 항상 아래 경계를 포함해야 한다.

```text
session record to update:
harness rule:
sandbox action:
current evidence permits:
current evidence forbids:
next action:
verification:
record update:
```

이 다섯 줄이 채워지면 AI는 일반 조언 대신 연구 상태 안에서 움직인다.
세션이 끝나면 같은 경계를 `project-memory.json`의 `current_evidence`와
`next_smallest_actions`에 다시 남긴다.
