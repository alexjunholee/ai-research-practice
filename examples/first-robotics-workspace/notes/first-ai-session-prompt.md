# First AI Session Prompt

Use this example prompt to kick off a single paper-code-experiment loop for a
localization project.

## Session Target

- Workspace: example-localization-workspace
- Research object: one paper-code-experiment map for a localization paper
- Current task: connect the paper claim to code path candidates and missing
  experiment protocol fields
- Expected artifact: filled sections in `notes/paper-code-experiment-map.md`

## Read Order

Read these files in order before answering:

1. `AGENTS.md`
2. `project-memory.json`
3. `notes/first-day-workspace-checklist.md`
4. `notes/weekly-research-ledger.md`
5. `notes/paper-code-experiment-map.md`
6. `notes/experiment-contract.md`

## Before Answering

State these fields before giving any advice:

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
- Identify the paper's central claim and candidate code paths.
- Flag any missing dataset, split, metric, baseline, command, and artifact fields.
- Choose a single file or command output to inspect next.
- Record the session update, controlling harness rule, sandbox action, and verification step.

## Blocked Claims

- Do not claim any method performance gains yet.
- Do not declare reviewer readiness.
- Do not treat a filename alone as proof of an active implementation.
- Do not extrapolate manuscript claims from missing protocol fields.

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

My current task is to connect one localization paper's central claim to
candidate code paths and identify any missing experiment protocol fields.
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

Use source files, artifacts, and command outputs as your primary evidence, and
treat summaries as orientation only. If required evidence is missing, state
explicitly what is missing and propose the smallest inspection needed to verify
the claim. Do not open a second research loop in your first response.
```
