# Example Robotics Workspace AGENTS.md

This is a sanitized example file. Before using it in a real project, replace all
example names, paths, datasets, and commands with your own project details.

## Project Truth

- Current public artifact: project README and paper notes
- Current private state file: project-memory.json
- Source of truth for code: repos/localization-stack
- Source of truth for datasets: dataset inventory sheet
- Source of truth for experiments: notes/experiment-contract.md
- Source of truth for manuscript: notes/claim-evidence-map.md when created
- Source of truth for durable corrections: project-memory.json

## Public / Private Boundary

Public:

- README
- sanitized notes
- empty templates
- public paper links

Private:

- raw experiment logs
- reviewer material
- machine-specific storage names
- unpublished result tables

## Managed Agent Boundary

- Session: project-memory.json, weekly ledger, replay cases, and artifacts.
- Harness: AGENTS.md, evidence gate, work modes, and durable corrections.
- Sandbox: repos/localization-stack, dataset inventory, commands, and generated outputs.

Before starting work, state which session record you will update, which harness
rule governs the action, and which sandbox actions are currently allowed.

## Work Modes

### Workspace Resume

Read in this order:

1. AGENTS.md
2. project-memory.json
3. notes/first-day-workspace-checklist.md
4. notes/codex-porting-checklist.md if legacy AI rules exist
5. notes/weekly-research-ledger.md
6. current target note
7. artifacts named in the target note

### Experiment Interpretation

Required before any performance claim:

- dataset
- split or sequence
- query/database direction (for retrieval tasks)
- metric definition
- baseline
- artifact path
- failure condition

### Debugging

Follow stage-local debugging: identify the pipeline stage, expected signal,
observed signal, candidate causes, and lowest-risk diagnostic check before
naming a root cause.

## Evidence Gate

Before answering, state:

```text
current evidence permits:
current evidence forbids:
promotion requires:
```

## Durable Corrections

Whenever a user corrects an assumption, update project-memory.json before
continuing.

## Porting Acceptance

This example workspace includes a completed `notes/codex-porting-checklist.md`.
Active research begins only after the checklist confirms that:

- all tool-specific commands have portable replacements;
- local-only settings are kept separate from shared project rules;
- dataset, metric, artifact, claim, reviewer-risk, and replay gates are in place;
- the first AI session prompt points to this `AGENTS.md`, project memory, the
  first-day checklist, and the chosen target note.
