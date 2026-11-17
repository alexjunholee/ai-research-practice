# Project AGENTS.md Template

This project follows a Codex-first workflow. If older `CLAUDE.md`, `.claude/`, or
Cursor rules still exist, treat them as reference material: move durable project
rules into this `AGENTS.md`, and keep tool-specific install commands separate.

## Project Truth

- Current public artifact:
- Current private state file:
- Source of truth for code:
- Source of truth for experiments:
- Source of truth for manuscript:
- Source of truth for reviewer response:
- Source of truth for durable corrections:

## Public / Private Boundary

Public:

- README
- guide or paper draft if already public
- templates
- sanitized examples

Private:

- raw private conversation logs
- raw reviewer material
- credentials and API keys
- unpublished results
- personal or machine-specific paths
- raw dataset paths that expose private storage locations

## Managed Agent Boundary

This workspace applies the managed-agent pattern at the project level:

- Session: `project-memory.json`, weekly ledger, replay cases, and artifacts.
- Harness: this `AGENTS.md`, evidence gate, work modes, and durable corrections.
- Sandbox: code repos, datasets, commands, tools, and generated outputs.

Before starting work, state which session record you will update, which harness
rule governs the action, and which sandbox actions are currently allowed. Always
record a command output, file diff, or artifact path before promoting an
observation into a research claim.

## Work Modes

### Read-only audit

Allowed:

- inspect files
- summarize current state
- identify missing evidence
- state what current evidence permits and forbids

Not allowed:

- edit files
- run destructive commands
- make paper claims based on weak or incomplete evidence

### Code execution

Allowed:

- run listed commands
- collect logs
- update run ledger

Required:

- command
- cwd
- expected artifact
- timeout
- verification step

### Experiment interpretation

Allowed:

- inspect configs, logs, tables, and metric scripts
- compare numbers only within a locked evaluation protocol

Required:

- dataset
- split or sequence
- query/database direction (for retrieval tasks)
- ground-truth frame
- metric definition
- baseline
- artifact path

### Manuscript edit

Allowed:

- edit claim/evidence structure
- refine prose once the underlying argument is sound

Required:

- target claim
- evidence source
- reviewer risk
- build or diff check

## Evidence Gate

Before answering, state:

```text
current evidence permits:
current evidence forbids:
promotion requires:
```

## Durable Corrections

Whenever a user corrects an assumption, log the correction in project memory
before moving on.

Record:

- wrong assumption:
- corrected fact:
- affected workflow:
- future gate:
- replay case:

## Porting Acceptance

If this file was ported from `CLAUDE.md`, `.claude/`, Cursor rules, or another
tool-specific instruction set, hold off on research tasks until the porting
checklist confirms that:

- all tool-specific commands have portable replacements;
- local-only settings are kept separate from shared project rules;
- dataset, metric, artifact, claim, reviewer-risk, and replay gates are in place;
- the first AI session prompt points to this `AGENTS.md`, project memory, the
  first-day checklist, and the chosen target note.
