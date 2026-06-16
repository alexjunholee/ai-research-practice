# Paper-Code-Experiment Map

## Paper

- Title: Example visual place recognition paper
- Authors: Public authors
- Year / venue: 2024 / public venue
- Link: https://example.org/public-paper

## Central Claim

- What the paper claims: A representation improves place recognition under a defined evaluation.
- What problem pressure it responds to: visual change and cross-condition retrieval.
- What assumption it repairs or introduces: feature space should preserve place identity under appearance change.

## Method Map

| Paper concept | Code candidate | Status | Evidence |
|---|---|---|---|
| feature extractor | repos/localization-stack/src/features.py | unknown | file candidate only |
| retrieval index | repos/localization-stack/src/index.py | unknown | file candidate only |

## Experiment Contract

- Dataset: example urban route dataset
- Split / sequence: not verified
- Sensor / modality: camera
- Query -> database direction: not verified
- Ground truth: not verified
- Metric: R@K, definition not verified
- Threshold / alignment: not verified
- Baseline: not verified
- Artifact: not produced

## Issue / PR Notes

Only include issues that change how the method should be run, evaluated, or
cited.

- Build issue:
- Dataset convention issue:
- Metric issue:
- Sensor setup issue:
- Claim or limitation issue:

## Reusable Research Output

- Comparison I can reuse: blocked until protocol is verified.
- Claim this paper supports: candidate representation family for VPR.
- Claim this paper does not support: performance improvement in this workspace.
- Next artifact to inspect: evaluation script and dataset split file.
