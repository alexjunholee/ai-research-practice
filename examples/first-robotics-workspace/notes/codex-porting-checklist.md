# Codex Porting Checklist

This is a sanitized example of moving older Claude/Cursor-oriented project
rules into a Codex-first robotics research workspace.

## Source Files

Discovery sweep:

```bash
find . -maxdepth 4 \( -name 'CLAUDE.md' -o -path './.claude/*' -o -path './.cursor/*' -o -name '*command*' -o -name '*commands*' \) -print
```

- Discovery command: ran against the old workspace root before copying rules
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
- Stage pipeline: resume, choose one loop, run stage-local check, update ledger
- Allowed commands: read files, inspect JSON, run documented smoke checks
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
| CI/workflow command | run repeatable verification | keep as documented smoke command if it exists |

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

- Claude/Cursor-era operating rules can be reused as Codex project rules.
- Tool-specific commands have portable meanings that can become scripts or templates.

Current evidence forbids:

- Treating Claude-only settings as Codex permissions.
- Publishing local plugin install notes or private workspace paths.
- Claiming the workspace is experimentally validated.

Promotion requires:

- Run the first chosen research loop.
- Update `project-memory.json` with any durable correction.
- Add a replay case if the same mistaken assumption recurs.

## Acceptance Gate

- `AGENTS.md` contains the moved project goal, boundary, read order, evidence
  gate, durable corrections, and verification commands.
- Discovery sweep was run and every found Claude/Cursor/slash-command/plugin
  source has a keep/drop/destination decision.
- tool-specific commands have portable replacements in the command conversion
  table.
- Claude-only, editor-only, or local-only settings are recorded as local notes, not public
  project rules.
- Robotics research gates were added for dataset, metric, artifact, claim,
  reviewer risk, and replay.
- `project-memory.json` contains any durable correction discovered during
  porting.
- First AI session prompt names `AGENTS.md`, `project-memory.json`, first-day
  checklist, and the first target note.

If one item is missing, the first AI session remains orientation only.
