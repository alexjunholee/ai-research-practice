# First AI Session Prompt

This example starts one paper-code-experiment loop for a localization project.

## Session Target

- Workspace: example-localization-workspace
- Research object: one paper-code-experiment map for a localization paper
- Current task: connect the paper claim to code path candidates and missing
  experiment protocol fields
- Expected artifact: filled sections in `notes/paper-code-experiment-map.md`

## Read Order

Read these files before answering.

1. `AGENTS.md`
2. `project-memory.json`
3. `notes/first-day-workspace-checklist.md`
4. `notes/weekly-research-ledger.md`
5. `notes/paper-code-experiment-map.md`
6. `notes/experiment-contract.md`

## Before Answering

State these fields first.

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

- Inspect the paper-code-experiment map.
- Identify central claim and active code path candidates.
- Mark missing dataset, split, metric, baseline, command, and artifact fields.
- Choose one file or command output to inspect next.
- Leave a session record, harness rule, sandbox action, and verification record.

## Blocked Claims

- Do not claim method performance.
- Do not state reviewer readiness.
- Do not treat a file name as active implementation proof.
- Do not turn missing protocol fields into manuscript claims.

## Promotion Requires

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
Read AGENTS.md, project-memory.json, notes/first-day-workspace-checklist.md,
notes/weekly-research-ledger.md, notes/paper-code-experiment-map.md, and
notes/experiment-contract.md before answering.

My current task is to connect one localization paper's central claim to code path
candidates and missing experiment protocol fields.
First research loop target: notes/paper-code-experiment-map.md
Expected artifact: filled sections in notes/paper-code-experiment-map.md

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
