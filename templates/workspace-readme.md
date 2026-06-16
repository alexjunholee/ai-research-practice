# [PROJECT_NAME] Research Workspace

이 파일은 새 로보틱스/CV 연구 작업장의 첫 화면이다. 프로젝트 이름, 주요
repo, dataset 위치, 첫 AI 세션 경계만 채운 뒤 시작한다.

## Start Here

1. `AGENTS.md`를 먼저 읽는다.
2. `project-memory.json`에서 현재 truth, source_of_truth, current_evidence,
   first_research_loop, next_smallest_actions를 확인한다.
3. `notes/first-day-workspace-checklist.md`로 source of truth를 잠근다.
4. 기존 `CLAUDE.md`, `.claude/`, Cursor rule이 있으면
   `notes/codex-porting-checklist.md`로 행동 원칙만 옮긴다.
5. 첫 AI 세션에는 `notes/first-ai-session-prompt.md`를 채워 보낸다.

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
current evidence permits:
current evidence forbids:
next smallest action:
verification:
ledger update:
```

Fill these lines before asking for a broad answer.

After the first session, copy the same boundary back into `project-memory.json`
under `current_evidence` and `next_smallest_actions`.
