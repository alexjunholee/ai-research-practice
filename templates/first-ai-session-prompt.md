# First AI Session Prompt

Use this template to draft your opening message in a new robotics or computer
vision research workspace. Replace every bracketed placeholder before sending
it to an AI agent.

## Session Target

- Workspace:
- Research object:
- Current task:
- First research loop target:
- Expected artifact:

## Read Order

Have the agent read these files in order before answering:

1. `AGENTS.md`
2. `project-memory.json`
3. `notes/first-day-workspace-checklist.md`
4. `notes/weekly-research-ledger.md`
5. target note or source file:
6. artifact or command output:

## First Research Loop Target

Pick one—and only one—target note before starting the first session, and name
both that note and the expected artifact in your opening message.

Common first targets:

- `notes/paper-code-experiment-map.md` with `notes/experiment-contract.md`
- `notes/stage-local-debugging.md`
- `templates/dataset-archaeology-sheet.md` copied into `notes/`
- `templates/claim-evidence-map.md` copied into `notes/`

## Before Answering

Start by mapping the workspace into its session, harness, and sandbox layers:

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

- Inspect primary source files and explicitly named artifacts.
- Separate primary source truth from secondary summaries.
- Call out any missing evidence before proposing a claim.
- Select a single, stage-local next action.
- Record the session update, controlling harness rule, sandbox action, and verification step.

## Blocked Claims

- Do not infer project truth from summaries when primary source files or
  artifacts are available.
- Do not claim experimental improvement until the dataset, split, metric,
  baseline, command, and artifact are all verified.
- Do not rewrite manuscript claims until you have clearly separated allowed
  wording from forbidden wording.
- Do not publish raw notes, reviewer material, credentials or secrets, or
  machine-specific storage paths.

## Promotion Requires

Move from initial orientation to active research only after filling in all of
the following fields:

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

Use source files, artifacts, and command outputs as your primary evidence, and
treat summaries as orientation only. If required evidence is missing, state
explicitly what is missing and propose the smallest inspection needed to verify
the claim. Do not open a second research loop in your first response.
```
