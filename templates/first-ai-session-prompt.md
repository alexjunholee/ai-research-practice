# First AI Session Prompt

Use this as the first message in a new robotics/CV research workspace. Fill the
brackets before sending it to an AI agent.

## Session Target

- Workspace:
- Research object:
- Current task:
- First research loop target:
- Expected artifact:

## Read Order

Read these files before answering.

1. `AGENTS.md`
2. `project-memory.json`
3. `notes/first-day-workspace-checklist.md`
4. `notes/weekly-research-ledger.md`
5. target note or source file:
6. artifact or command output:

## First Research Loop Target

Choose exactly one target note before the first session. The first message should
name that target note and the expected artifact.

Common first targets:

- `notes/paper-code-experiment-map.md` with `notes/experiment-contract.md`
- `notes/stage-local-debugging.md`
- `templates/dataset-archaeology-sheet.md` copied into `notes/`
- `templates/claim-evidence-map.md` copied into `notes/`

## Before Answering

Map the workspace into session, harness, and sandbox first.

```text
Session record to update:
Harness rule that controls this action:
Sandbox action allowed now:
Sandbox action not allowed now:
Object under truth control:
Current evidence permits:
Current evidence forbids:
Smallest next action:
Verification:
```

## Allowed First Action

- Inspect source files and named artifacts.
- Separate source truth from summary truth.
- Name missing evidence before proposing a claim.
- Choose one stage-local action.
- Leave a session record, harness rule, sandbox action, and verification record.

## Blocked Claims

- Do not infer project truth from summaries when source files or artifacts are
  available.
- Do not claim experiment improvement before dataset, split, metric, baseline,
  command, and artifact are known.
- Do not rewrite manuscript claims before allowed wording and forbidden wording
  are separated.
- Do not publish raw notes, reviewer material, secret material, or machine-specific
  storage names.

## Promotion Requires

The session can move from orientation to research action only after these fields
are filled.

```text
object under truth control:
primary evidence:
secondary evidence:
claim allowed:
claim blocked:
next command or file inspection:
ledger update:
```

## Prompt To Send

```text
Read AGENTS.md, project-memory.json, notes/first-day-workspace-checklist.md, and
notes/weekly-research-ledger.md, [target note], and [supporting note] before
answering.

My current task is: [task].
First research loop target: [target note]
Expected artifact: [expected artifact]

Before giving advice, state:
- Session record to update
- Harness rule that controls this action
- Sandbox action allowed now
- Sandbox action not allowed now
- Object under truth control
- Current evidence permits
- Current evidence forbids
- Smallest next action
- Verification

Use source files, artifacts, and command output as primary evidence. Treat
summaries as orientation only. If evidence is missing, say what is missing and
choose the smallest inspection that would promote the claim.
Do not open a second research loop in the first answer.
```
