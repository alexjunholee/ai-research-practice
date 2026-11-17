# [PROJECT_NAME] Research Workspace

이 파일은 새 로보틱스·CV 연구 프로젝트 작업 공간을 열었을 때 가장 먼저 확인하는 안내 화면이다. 프로젝트 이름과 주요 저장소·데이터셋 위치, 그리고 첫 AI 세션을 시작하기 위한 최소 경계만 채워 둔 뒤 작업을 시작한다.

## Start Here

새 작업 공간에서 첫 세션을 열기 전에 아래 여섯 단계를 순서대로 밟아 기본 규칙과 작업 맥락을 고정한다.

1. 루트의 `AGENTS.md`를 가장 먼저 읽어 프로젝트 규칙과 경계를 확인한다.
2. `project-memory.json`을 열어 현재 확인한 사실과 `source_of_truth`, `current_evidence`, `first_research_loop`, `next_smallest_actions` 항목을 확인한다.
3. `notes/first-day-workspace-checklist.md`를 따라 정본으로 삼을 파일(`source of truth`)을 잠근다.
4. 기존 `CLAUDE.md`, `.claude/`, Cursor 규칙이 남아 있다면 `notes/codex-porting-checklist.md`를 참고해 행동 원칙만 추려 옮긴다.
5. 요청을 보내기 전에 session, harness, sandbox의 경계를 먼저 적는다.
6. 위 준비가 끝나면 `notes/first-ai-session-prompt.md`의 빈칸을 채워 첫 AI 세션을 시작한다.

## First Run Check

Before the first AI session, the workspace should have these files.

```text
AGENTS.md
README.md
project-memory.json
notes/first-day-workspace-checklist.md
notes/first-ai-session-prompt.md
notes/paper-code-experiment-map.md
notes/experiment-contract.md
artifacts/first-ai-session-message.txt
```

`project-memory.json` must parse as JSON. The first message in
`artifacts/first-ai-session-message.txt` should have no bracket placeholders
left before it is sent.

`project-memory.json` should also include `source_of_truth`, `tool_surface_map`,
`current_evidence`, `first_research_loop`, and `next_smallest_actions`. These
fields keep the next AI session from treating memory as proof.

Use the workspace as a managed-agent harness.

- Session: `project-memory.json`, ledger, replay cases, and artifacts.
- Harness: `AGENTS.md`, prompt templates, evidence gates, and work modes.
- Sandbox: repos, datasets, commands, tools, and generated outputs.

## Workspace Shape

```text
workspace/
├── AGENTS.md
├── README.md
├── project-memory.json
├── repos/
├── datasets/
├── artifacts/
├── notes/
└── templates/
```

## Project Pointers

- Main repo:
- Dataset root:
- Artifact root:
- Paper or manuscript:
- Current experiment:

## First Research Loop

| Situation | Start With |
|---|---|
| Read one paper | `notes/paper-code-experiment-map.md` |
| Check a dataset | `templates/dataset-archaeology-sheet.md` |
| Interpret a number | `notes/experiment-contract.md` |
| Narrow an error | `notes/stage-local-debugging.md` |
| Repair a claim | `templates/claim-evidence-map.md` |

## Evidence Gate

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

Fill these lines before asking for a broad answer.

At the end of the session, write the currently confirmed fact, the claim that is
not yet safe to make, and one next action in the weekly ledger. Reflect the same
boundary under `current_evidence` and `next_smallest_actions` in
`project-memory.json`.
