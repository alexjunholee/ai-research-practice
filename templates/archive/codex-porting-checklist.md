# Codex Porting Checklist

Use this when a project already has `CLAUDE.md`, `.claude/`, Cursor rules, or
tool-specific agent instructions.

## Source Files

Run a discovery sweep before filling the table. Do not rely on memory or on the
files already visible in the editor.

```bash
find . -maxdepth 4 \( -name 'CLAUDE.md' -o -path './.claude/*' -o -path './.cursor/*' -o -name '*command*' -o -name '*commands*' \) -print
```

Inventory result:

- Discovery command:
- Sources found:
- Sources intentionally ignored:
- Missing source types checked:

| Source | Exists? | Keep? | Destination |
|---|---|---|---|
| `CLAUDE.md` |  |  | `AGENTS.md` |
| `.claude/settings.local.json` |  |  | local notes only |
| `.claude/skills` |  |  | Codex skill or template |
| `.cursor/rules` |  |  | `AGENTS.md` or editor rule |
| slash commands |  |  | script or checklist |
| MCP/plugin config |  |  | local notes or install guide |
| CI/workflow commands |  |  | verification script |
| project memory |  |  | `project-memory.json` |

## Move Into AGENTS.md

- Project goal:
- Public/private boundary:
- Source-of-truth read order:
- Stage pipeline:
- Allowed commands:
- Forbidden commands:
- Evidence gate:
- Durable corrections:
- Build or verification commands:

## Convert Tool-Specific Commands

| Original command | Portable meaning | Codex replacement |
|---|---|---|
|  |  |  |

Examples:

- plugin install command -> source link plus manual install note
- slash command -> script, template, or checklist
- Claude-only setting -> Codex sandbox/approval note
- MCP/plugin config -> capability note plus local setup boundary
- CI/workflow command -> repo verification command
- coding rule -> project `AGENTS.md` rule

## Research Gates To Add

Claude or coding-agent rules often stop at test pass. Robotics research needs
more gates.

- Dataset provenance:
- Metric protocol:
- Artifact path:
- Result provenance:
- Claim/evidence boundary:
- Reviewer risk:
- Replay case:

## Do Not Publish

- private machine paths
- raw conversation records
- credential values
- private reviewer text
- unpublished result details

## Porting Result

Current evidence permits:

Current evidence forbids:

Promotion requires:

## Acceptance Gate

Porting is complete only when these artifacts agree.

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
