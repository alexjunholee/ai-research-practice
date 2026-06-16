# First-Day Workspace Checklist

This file is filled enough for a first AI-assisted research loop. Replace every
example name before using it in a real project.

## Workspace Shape

- Workspace root: example-localization-workspace
- Main code repos: repos/localization-stack
- Dataset storage: datasets/public-sequence-sample
- Artifact storage: artifacts/first-pass
- Manuscript location: notes/claim-evidence-map.md when created
- Template location: templates/
- Public output location: README and sanitized notes

## Source Of Truth

| State | Primary source | Secondary source |
|---|---|---|
| project goal | AGENTS.md | project-memory.json |
| code truth | repos/localization-stack | recent command output |
| dataset truth | dataset inventory sheet | notes/experiment-contract.md |
| experiment truth | notes/experiment-contract.md | result provenance tuple |
| manuscript truth | notes/claim-evidence-map.md | paper notes |
| reviewer risk | notes/weekly-research-ledger.md | project-memory.json |
| durable corrections | project-memory.json | replay cases |

## Public / Private Boundary

Public:

- README
- sanitized notes
- empty templates
- public paper links

Private:

- raw experiment logs
- reviewer material
- unpublished result tables
- credential material
- machine-specific storage names

## First Agent Read Order

1. `AGENTS.md`
2. `project-memory.json`
3. `notes/first-day-workspace-checklist.md`
4. `notes/weekly-research-ledger.md`
5. current target note
6. artifacts named in the target note

## First Verification Commands

| Purpose | Command | Expected result |
|---|---|---|
| inspect project contract | `sed -n '1,160p' AGENTS.md` | project truth and boundary are visible |
| inspect memory | `python3 -m json.tool project-memory.json` | current truth parses as JSON |
| inspect first loop | `sed -n '1,180p' notes/paper-code-experiment-map.md` | claim/code/protocol fields are visible |
| inspect experiment gate | `sed -n '1,180p' notes/experiment-contract.md` | permitted and blocked claims are visible |

## First Research Action

- Object under truth control: one paper-code-experiment map for a localization paper
- Current evidence permits: identifying claim, code path candidates, and missing protocol fields
- Current evidence forbids: claiming method performance or reviewer readiness
- Smallest next action: fill the paper claim and active code path candidate
- Verification: cite the paper section, code file, or command output used for each filled field
