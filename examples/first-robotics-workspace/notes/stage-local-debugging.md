# Stage-Local Debugging Sheet

## Debug Target

- Object under truth control: ROS2 camera image subscriber
- User-visible symptom: topic appears in the ROS graph, but the subscriber callback receives no images
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
| runtime environment | yes | topic is visible, but callbacks do not fire |

## Candidate Causes

| Candidate | Stage | Evidence now | Lowest-risk check |
|---|---|---|---|
| QoS mismatch | runtime environment | publisher exists, but callbacks do not fire | inspect topic QoS |
| namespace/remap mismatch | runtime environment | graph has image topic | inspect node subscriptions |
| simulated time issue | runtime environment | bag replay suspected | inspect clock and use_sim_time |

## Next Check

- Command: `ros2 topic info --verbose /camera/image_raw`
- Working directory: repo root
- Expected artifact: copied command output
- Timeout: 10 seconds
- Success signal: publisher and subscriber QoS profiles are visible
- Failure signal: topic is missing or the command cannot query the ROS graph

## Result

- Command completed:
- Artifact produced:
- New evidence:
- Claim allowed:
- Claim forbidden:

## Stop Rule

- Stop if: two consecutive checks produce no new evidence.
- Escalate if: the ROS graph cannot be queried.
- Record debt if: a workaround is applied before the root cause is verified.
