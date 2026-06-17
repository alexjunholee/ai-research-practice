# User Reaction Prior

Use this before a substantial research-agent response, edit, command, or
continuation.

The purpose is not to predict the user as a person. The purpose is to stop the
agent from repeating known transition failures: shallow summary, local pattern
matching, weak evidence promotion, wrong implementation surface, non-operational
advice, and drift from the original goal.

## When To Use

Use this gate for robotics/CV research work involving code, experiments,
datasets, metrics, paper writing, reviewer response, literature positioning,
workspace continuation, or durable project memory.

Do not use it for trivial one-line facts or mechanical formatting with no
research-state consequence.

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

If `likely_user_objection` is nonempty, change the action itself before
answering. Do not pass this gate by adding caveats, apologies, or a displayed
checklist.

## Reaction Classes

| User correction cue | Likely agent failure | Required revision |
|---|---|---|
| "too shallow" | stopped at first-order summary | raise abstraction and name the reusable transition |
| "too local" | followed files, words, or counts instead of research state | extract invariant failure mode and control surface |
| "did you read it?" | detached from retained artifacts | name the source-of-truth artifact and bind the claim to it |
| "why this implementation surface?" | used the wrong control layer | separate skill, rule, gate, workflow, and script |
| "can this be used immediately?" | descriptive but not operational | convert to a gate, checklist, replay case, schema field, or workflow entry |
| "is that sufficiently analyzed?" | promoted weak evidence | demote the claim and state what would promote it |
| "do you remember the goal?" | optimized a local subtask | restate the higher-order objective and discard irrelevant work |
| "stop making parallel documents" | scattered state | patch the active surface instead of creating another summary |
| "proceed / resume / complete all" | stopped at proposal | continue through implementation and verification |

## Real Revision

A real revision changes at least one of:

- selected skill or typed action;
- source-of-truth artifact inspected before acting;
- evidence tier or blocked claim;
- action mode;
- narrowest next action;
- verification gate;
- durable control surface.

A non-revision only changes tone, length, or confidence language while leaving
the same flawed action intact.

## Stop Condition

After the reaction-risk check, continue through the active project entrypoint:
`AGENTS.md`, project memory, research-turn skill, issue workflow, or paper
workflow. When a correction recurs, turn it into a reusable gate, replay case,
skill rule, project memory entry, or bot instruction.

Source model: [`alexjunholee/robotics-research-agent`](https://github.com/alexjunholee/robotics-research-agent).
