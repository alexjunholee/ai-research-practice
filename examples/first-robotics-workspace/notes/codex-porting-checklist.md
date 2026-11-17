# Codex Porting Checklist

This sanitized example walks through migrating older Claude- or Cursor-oriented
project rules into a Codex-first robotics research workspace.

## Source Files

Discovery sweep:

```bash
find . -maxdepth 4 \( -name 'CLAUDE.md' -o -path './.claude/*' -o -path './.cursor/*' -o -name '*command*' -o -name '*commands*' \) -print
```

- Discovery command: run against the legacy workspace root before copying rules
- Sources found: `CLAUDE.md`, `.claude/settings.local.json`, `.claude/skills`,
  slash commands, project memory
- Sources intentionally ignored: local plugin install notes, private machine
  paths, unsanitized conversation pointers
- Missing source types checked: `.cursor/rules`, MCP/plugin config,
  CI/workflow commands

| Source | Exists? | Keep? | Destination |
|---|---|---|---|
| `CLAUDE.md` | yes | yes | `AGENTS.md` |
| `.claude/settings.local.json` | yes | partial | local notes only |
| `.claude/skills` | yes | partial | template or Codex skill |
| `.cursor/rules` | no | no | none |
| slash commands | yes | partial | script or checklist |
| MCP/plugin config | no | no | none |
| CI/workflow commands | no | no | none |
| project memory | yes | yes | `project-memory.json` |

## Move Into AGENTS.md

- Project goal: maintain a localization research workspace with clear claim/evidence gates
- Public/private boundary: publish sanitized notes only
- Source-of-truth read order: AGENTS, memory, first-day checklist, target note, named artifacts
- Stage pipeline: resume context, choose one loop, run stage-local checks, and update the ledger
- Allowed commands: read files, inspect JSON, run documented verification checks
- Forbidden commands: delete datasets, publish raw logs, infer result quality from filenames
- Evidence gate: current evidence permits, forbids, and promotion requires
- Durable corrections: store repeated wrong assumptions in project memory
- Build or verification commands: commands listed in the target note

## Convert Tool-Specific Commands

| Original command | Portable meaning | Codex replacement |
|---|---|---|
| `/resume` | reconstruct current project state | read `AGENTS.md`, `project-memory.json`, and ledger |
| `/debug-topic` | isolate a ROS2 topic failure | fill `stage-local-debugging.md` |
| `/paper-map` | connect a paper to code and experiments | fill `paper-code-experiment-map.md` |
| `/claim-check` | stop unsupported manuscript claims | fill `claim-evidence-map.md` |
| plugin install command | install a local UI extension | keep as private setup note, not public guide content |
| CI/workflow command | run repeatable verification | keep as documented verification command if it exists |

## Research Gates To Add

- Dataset provenance: dataset inventory or archaeology sheet
- Metric protocol: experiment contract
- Artifact path: result provenance tuple
- Result provenance: command, timestamp, output file, failure condition
- Claim/evidence boundary: claim map before manuscript wording
- Reviewer risk: weekly ledger or claim map
- Replay case: repeated wrong assumption or metric mix-up

## Do Not Publish

- private machine paths
- raw conversation records
- credential values
- private reviewer text
- unpublished result details

## Porting Result

Current evidence permits:

- Existing Claude/Cursor operating rules can be adapted into Codex project rules.
- Tool-specific commands can be translated into portable scripts or checklist templates.

Current evidence forbids:

- Treating Claude-only settings as Codex permissions.
- Publishing local plugin install notes or private workspace paths.
- Claiming that the workspace or pipeline has been experimentally validated.

Promotion requires:

- Completing the first chosen research loop.
- Updating `project-memory.json` with any durable corrections.
- Adding a replay case if any mistaken assumption recurs.

## Acceptance Gate

- `AGENTS.md` includes the migrated project goal, public/private boundary, read
  order, evidence gate, durable corrections, and verification commands.
- The discovery sweep has been run, and every discovered Claude, Cursor,
  slash-command, or plugin file has an explicit keep/drop/destination decision.
- All tool-specific commands have portable replacements recorded in the command
  conversion table.
- Claude-only, editor-only, or machine-local settings are kept in local notes
  rather than shared project rules.
- Robotics research gates are in place for datasets, metrics, artifacts, claims,
  reviewer risk, and replay cases.
- `project-memory.json` records any durable corrections uncovered during
  porting.
- The first AI session prompt explicitly references `AGENTS.md`,
  `project-memory.json`, the first-day checklist, and the initial target note.

If any item above is missing, keep the first AI session limited to orientation
rather than starting active research.
