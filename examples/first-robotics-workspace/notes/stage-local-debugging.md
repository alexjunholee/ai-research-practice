# Stage-Local Debugging Sheet

## Debug Target

- Object under truth control: ROS2 camera image subscriber
- User-visible symptom: topic appears in graph, callback receives no image
- Current stage: runtime environment / ROS2 communication
- Expected signal: subscriber callback count increases during bag replay
- Observed signal: callback count remains zero

## Stage Selection

| Stage | In scope? | Evidence |
|---|---|---|
| data | no | bag presence not yet inspected |
| preprocessing | no | subscriber has no input |
| representation | no | no features computed |
| retrieval / matching | no | downstream stage |
| geometry / estimation | no | downstream stage |
| optimization | no | downstream stage |
| confidence / rejection | no | downstream stage |
| evaluation | no | downstream stage |
| runtime environment | yes | topic visible but callback absent |

## Candidate Causes

| Candidate | Stage | Evidence now | Lowest-risk check |
|---|---|---|---|
| QoS mismatch | runtime environment | publisher exists, callback absent | inspect topic QoS |
| namespace/remap mismatch | runtime environment | graph has image topic | inspect node subscriptions |
| simulated time issue | runtime environment | bag replay suspected | inspect clock and use_sim_time |

## Next Check

- Command: `ros2 topic info --verbose /camera/image_raw`
- Working directory: repo root
- Expected artifact: copied command output
- Timeout: 10 seconds
- Success signal: publisher/subscriber QoS is visible
- Failure signal: topic missing or command cannot query graph

## Result

- Command completed:
- Artifact produced:
- New evidence:
- Claim allowed:
- Claim forbidden:

## Stop Rule

- Stop if: two consecutive checks produce no new evidence.
- Escalate if: ROS graph cannot be queried.
- Record debt if: workaround is used before root cause is verified.
