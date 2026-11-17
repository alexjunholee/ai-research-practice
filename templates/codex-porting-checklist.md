# Codex Porting Checklist

Use this checklist when migrating a project that already has `CLAUDE.md`,
`.claude/`, Cursor rules, or other tool-specific agent instructions.

## Source Files

Run a discovery sweep before filling in the table—do not rely on memory or only
on the files currently open in your editor.

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

Rules written for general coding agents often stop at passing unit tests.
Robotics research requires stricter gates:

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

Porting is complete only when all of the following conditions hold:

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
