# Ch.6 — 디버깅은 stage-local로 자른다

로보틱스 디버깅에서 "왜 안 되지?"는 너무 큰 질문이다. AI는 이 질문을 받으면
가능한 원인을 많이 만든다. driver, QoS, tf2, calibration, CUDA, dependency,
dataset path, metric script가 한꺼번에 나온다. 후보가 많아질수록 사람의
행동 비용은 커진다.

하네스는 원인을 바로 맞히려 하지 않는다. stage를 먼저 자른다.

```text
data
-> preprocessing
-> representation
-> matching / retrieval
-> geometry / estimation
-> optimization
-> confidence / rejection
-> evaluation
-> runtime environment
```

AI가 할 일은 각 stage의 후보 failure와 확인 명령을 붙이는 것이다. 사람은
가장 작은 위험의 action을 고른다.

## Stage table

| Stage | 흔한 failure | 먼저 볼 artifact |
|---|---|---|
| Data | 파일 누락, timestamp 불일치, bag clock | file count, metadata, first/last stamp |
| Preprocessing | resize, undistort, normalization 차이 | config, cached sample, transform log |
| Representation | feature space 혼동, projection head 사용 오류 | tensor shape, checkpoint key, feature dump |
| Retrieval/matching | query/database 방향, top-k, ratio test | index stats, match visualization |
| Geometry | wrong intrinsics, frame convention, PnP outlier | calibration, reprojection error |
| Optimization | residual scaling, bad initialization | loss curve, solver status |
| Confidence | threshold, rejection rule, fallback path | accepted/rejected count |
| Evaluation | ground truth frame, metric script, sequence filter | eval config, alignment log |
| Runtime | Docker device, CUDA, ROS2 QoS, permission | command output, topic info, container args |

이 표는 처음 볼 곳을 정하는 index다.

## 좋은 AI 디버깅 요청

나쁜 요청은 넓다.

```text
이거 왜 안 되는지 봐줘.
```

좋은 요청은 stage와 증거를 준다.

```text
Stage-local debug.
Object under truth control: camera image subscriber.
Observed artifact: ros2 topic list shows /camera/image_raw, node receives none.
Current evidence: publisher exists; subscriber callback not triggered.
Find the next three checks, ordered by lowest risk.
Do not claim root cause until a command output proves it.
```

이렇게 주면 AI는 바로 root cause를 쓰기 어렵다. 대신 QoS compatibility,
namespace/remap, callback executor, simulated time, container network 같은
후보를 check 단위로 나눈다.

## Tool failure와 method failure를 나눈다

명령 실패는 먼저 tool, runtime, data failure로 분리한다. `pip install` 실패,
CUDA driver mismatch, 빠진 Docker volume, 다른 dataset path는 method failure
전 단계에 있다. 반대로 명령이 성공해도 metric script가 다른 ground truth
frame을 읽었을 수 있다.

```text
tool failure:
runtime failure:
data failure:
method failure:
evaluation failure:
claim failure:
```

각 failure class가 다르면 다음 action도 다르다. AI가 이 층을 섞으면
"고쳐졌다"는 말이 너무 빨리 나온다.

## Stage-local loop

디버깅 turn은 다음 모양을 갖는다.

```text
stage:
expected signal:
observed signal:
candidate causes:
lowest-risk check:
command:
result:
next boundary:
```

예를 들어 VPR 성능이 갑자기 떨어졌다면 model을 바로 의심하지 않는다.
query/database split, cached feature version, normalization, index order,
positive radius, metric script를 먼저 자른다. 각 check는 하나의 artifact를
남겨야 한다. artifact가 없으면 다음 AI 세션은 같은 추측을 반복한다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| 첫 진단 | stage, observed signal, lowest-risk check를 정했다 | plausible cause 목록을 root cause처럼 읽었다 | 후보를 많이 만드는 일과 행동을 고르는 일은 비용 구조가 다르다 |
| Command failure | tool, runtime, data failure를 먼저 분리했다 | 설치 실패를 method 한계처럼 설명했다 | 실행 실패는 연구 결과가 되기 전에 환경 경계를 통과해야 한다 |
| 성능 하락 | split, cache, normalization, metric script를 stage별로 확인했다 | model architecture를 바로 바꿨다 | 큰 수정은 작은 artifact가 닫힌 뒤에야 위험을 감당할 수 있다 |
| Stop rule | evidence가 없는 stage를 접고 ledger에 debt를 남겼다 | 같은 추측을 새 표현으로 반복했다 | 멈추는 규칙이 없으면 AI의 발산이 디버깅 시간을 먹는다 |

## 언제 멈출 것인가

디버깅은 무한히 이어질 수 있다. 그래서 stop rule이 필요하다.

- 같은 stage에서 두 번 연속 evidence가 없으면 stage를 바꾼다.
- command failure를 세 번 반복하면 환경 문제로 분리한다.
- 결과가 좋아졌더라도 protocol이 바뀌었으면 성능 claim을 보류한다.
- root cause를 찾기 전에 workaround를 썼다면 ledger에 debt로 남긴다.

AI는 계속 후보를 낼 수 있다. 연구자는 멈추는 규칙을 가져야 한다.
