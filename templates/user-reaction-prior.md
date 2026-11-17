# User Reaction Prior

Run this check before delivering any substantial research response, file edit,
command execution, or continuation.

The goal is not to second-guess the user personally, but to prevent the agent
from repeating known failure modes: shallow summaries, local pattern matching,
promoting weak evidence into claims, editing the wrong control layer, offering
non-operational advice, and drifting away from the core objective.

## When To Use

Apply this gate to robotics or computer vision research tasks involving code,
experiments, datasets, evaluation metrics, manuscript drafting, reviewer
responses, literature positioning, workspace handoffs, or durable project
memory.

Skip it for trivial one-line lookups or mechanical formatting changes that do
not affect the research state.

## Pre-Response Check

Before answering, ask:

```text
reaction_risk_check:
  likely_user_objection:
  violated_transition:
  required_revision:
  revised_action:
  remaining_risk:
```

If `likely_user_objection` is non-empty, change the underlying action before
responding—do not try to satisfy this gate by simply adding caveats, apologies,
or a printed checklist.

## Reaction Classes

| User correction cue | Likely agent failure | Required revision |
|---|---|---|
| "too shallow" | stopped at a surface-level summary | raise the level of abstraction and identify the reusable rule or transition |
| "too local" | focused on filenames, wording, or counts rather than research state | isolate the underlying failure mode and the right control surface |
| "did you read it?" | responded without grounding in retained artifacts | cite the source-of-truth artifact and bind every claim directly to it |
| "why this implementation surface?" | edited the wrong control layer | distinguish clearly between skill, rule, gate, workflow, and script |
| "can this be used immediately?" | gave descriptive advice instead of an actionable step | turn the advice into a concrete gate, checklist, replay case, schema field, or workflow step |
| "is that sufficiently analyzed?" | promoted weak evidence into a claim | downgrade the claim and specify exactly what evidence would promote it |
| "do you remember the goal?" | over-optimized a local subtask | restate the overarching objective and drop unrelated work |
| "stop making parallel documents" | scattered state across duplicate files | update the active canonical file instead of creating yet another summary |
| "proceed / resume / complete all" | stopped at a proposal instead of executing | follow through to implementation and verification |

## Real Revision

A genuine revision changes at least one concrete part of the plan:

- the selected skill or action type;
- the source-of-truth artifact inspected before acting;
- the evidence tier or blocked-claim boundary;
- the work or action mode;
- the narrowest next action;
- the verification gate;
- the durable control surface.

Merely softening the tone, adjusting length, or hedging confidence while leaving
the flawed action unchanged does not count as a revision.

## Stop Condition

Once the reaction-risk check passes, proceed through the active project
entrypoint—`AGENTS.md`, project memory, or the relevant research, issue, or paper
workflow. Whenever the same correction comes up twice, encode it as a reusable
gate, replay case, skill rule, project memory entry, or agent instruction.

Source model: [`alexjunholee/robotics-research-agent`](https://github.com/alexjunholee/robotics-research-agent).
