# Project AGENTS.md Template

This project is operated Codex-first. If older `CLAUDE.md`, `.claude/`, or
Cursor rules exist, treat them as source material. Move durable project rules
into this `AGENTS.md` and keep tool-specific install commands separate.

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

- 비공개 대화 원문
- 심사 원문
- 인증 정보
- unpublished results
- 개인 경로
- raw dataset paths if they reveal private storage

## Managed Agent Boundary

This workspace follows the managed-agent pattern at the project level.

- Session: `project-memory.json`, weekly ledger, replay cases, and artifacts.
- Harness: this `AGENTS.md`, evidence gate, work modes, and durable corrections.
- Sandbox: code repos, datasets, commands, tools, and generated outputs.

Before starting work, state which session record will be updated, which harness
rule controls the action, and which sandbox action is currently allowed. Leave a
command result, file diff, or artifact path before promoting an observation into
a research claim.

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
- make paper claims from weak evidence

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
- compare numbers only inside a locked protocol

Required:

- dataset
- split or sequence
- query/database direction if retrieval
- ground-truth frame
- metric definition
- baseline
- artifact path

### Manuscript edit

Allowed:

- edit claim/evidence structure
- improve prose after argument is correct

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

When the user corrects an assumption, add it to project memory.

Record:

- wrong assumption:
- corrected fact:
- affected workflow:
- future gate:
- replay case:

## Porting Acceptance

If this file was created from `CLAUDE.md`, `.claude/`, Cursor rules, or another
tool-specific instruction set, do not start research action until the porting
checklist has confirmed:

- tool-specific commands have portable replacements;
- local-only settings are not treated as project rules;
- dataset, metric, artifact, claim, reviewer risk, and replay gates exist;
- first AI session prompt reads this `AGENTS.md`, project memory, first-day
  checklist, and the chosen target note.
