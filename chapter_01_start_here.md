# Ch.1 — 로보틱스 연구에서 AI는 왜 자주 틀리는가

카메라 토픽이 보이지 않는 ROS2 노드를 AI에게 던지면 답은 빠르게 나온다.
QoS가 맞지 않을 수 있다. namespace가 다를 수 있다. `use_sim_time`이 켜져
있을 수 있다. Docker 안에서 `/dev/video0` 권한이 빠졌을 수 있다. launch
파일이 다른 파라미터를 덮었을 수 있다.

다섯 가지 모두 그럴듯하다. 그중 하나가 실제 원인일 수도 있다. 그러나
연구자는 그 자리에서 하나를 골라 행동해야 한다. `ros2 topic info
--verbose`를 먼저 볼 것인지, container 권한을 다시 줄 것인지, bag replay를
멈추고 clock을 확인할 것인지 정해야 한다. 그 선택에는 시간이 든다. GPU
queue, 실험 마감, reviewer에게 보낼 표, 이미 깨지기 쉬운 launch script가
걸려 있다.

AI가 만든 후보는 싸다. 사람의 행동은 비싸다.

이 차이가 로보틱스 연구에서 AI가 자주 틀리는 첫 이유다. [March
1991](https://doi.org/10.1287/orsc.2.1.71)의 표현을 빌리면 AI는 exploration 쪽으로
일을 밀어붙인다. search, variation, risk taking, experimentation, discovery를
싸게 만든다. 연구는 곧 exploitation으로 넘어가야 한다. refinement, selection,
implementation, execution에는 사람이 시간을 낸다.

LLM은 텍스트 상황에서 가능한 후보를 잘 늘린다. [Chen & Ding
2023](https://arxiv.org/abs/2310.11158)은 LLM이 divergent association 과제에서 높은 점수를 낼 수
있음을 보였다. 동시에 [Nakajima et al.
2026](https://arxiv.org/abs/2601.20546)은 새롭거나 멀리 떨어진 연상과 유용한 창의성이
곧바로 이어지지 않으며, 맥락에 맞는지를 따로 검증해야 한다고 지적했다.
로보틱스의 맥락성은 센서
시간, frame convention, calibration, container 권한, dataset split, metric
정의에서 드러난다.

AI 도움은 사고를 넓히기도 하고 좁히기도 한다. [Wadinambiarachchi et al.
2024](https://arxiv.org/abs/2403.11164)는 생성 이미지 도움을 받은 ideation에서 초기 예시에 더
고착되고 아이디어 수와 다양성이 줄어든 사례를 보고했다. [Doshi & Hauser
2024](https://arxiv.org/abs/2312.00506)는 생성 AI 아이디어가 개인의 글쓰기 품질을 올리면서도
결과물 사이의 유사성을 키울 수 있음을 보였다. [Holzner et al.
2025](https://arxiv.org/abs/2505.17241)의 meta-analysis도 인간-AI 협업이 창의 성과를 올릴 수
있지만 아이디어 다양성은 줄일 수 있음을 보인다.

연구 로그에서도 같은 모양이 반복해서 보인다. AI가 첫 번째 plausible cause를 잡고
root cause처럼 말하거나, 숫자 하나를 보고 방법 전체가 개선됐다고 쓰거나,
evidence가 잠기기 전에 원고 문장을 매끈하게 만든다.

사람의 선택에는 다른 층이 있다. Simon의 bounded rationality는 사람이 모든
경우를 최적화하지 않고 제한된 정보와 시간 속에서 행동한다는 점을 설명한다.
Kahneman과 Tversky의 prospect theory는 손실 프레임과 기준점이 위험 판단을
바꾼다는 언어를 준다. [March & Shapira
1987](https://doi.org/10.1287/mnsc.33.11.1404)는 조직 안의 risk taking을 평균과 분산 계산보다
성과 기준, 주의 배분, gambling과 risk taking의 구분 속에서 보았다.
[Loewenstein et al. 2001](https://doi.org/10.1037/0033-2909.127.2.267)의
*Risk as Feelings*는 한 가지 층을 더 보탠다. 위험 판단은 확률표만 보고
움직이지 않는다. 지금 망가지면 하루를 잃는다는 감각, 이미 간신히 돌아가는
pipeline을 건드릴 때의 불안, reviewer에게 보낼 표가 비어 있다는 압박이
행동을 바꾼다.

마감 직전의 연구자는 작은 gain보다 큰 loss를 피하려고 더 위험한 추가
실험을 받아들이기도 하고, 반대로 fragile한 pipeline을 건드리지 않으려고
명백한 구조 수정을 미루기도 한다. Sarasvathy의 effectuation은 예측 가능한
최적 경로보다 지금 가진 수단과 감당 가능한 손실에서 행동이 시작되는
경우를 설명한다. [Ecological rationality](https://en.wikipedia.org/wiki/Ecological_rationality)는
여기에 한 가지를 더 보탠다. 정보가 부족한 환경에서 긴 원인 목록은 행동을
늦춘다. 현재 환경에 맞는 작은 heuristic이 더 나은 선택이 될 수 있다. `ros2
topic info --verbose` 한 줄이 긴 원인 목록보다 값비싼 순간이 있다.

Polanyi, Dreyfus, Suchman의 오래된 논점도 여기서 살아난다. 좋은 로보틱스
연구자는 prompt로 다 말하지 못하는 상태를 안다. 어떤 bag은 timestamp가
수상하고, 어떤 USB hub는 오래 돌리면 끊기며, 어떤 reviewer는 metric
방향을 집요하게 본다. Suchman식으로 말하면 plan은 행동을 완전히 결정하는
script보다 상황 안에서 고쳐 쓰는 resource에 가깝다. bag이 실패하고 GPU가
OOM을 내고 dataset count가 README와 다르면 plan은 그 자리에서 바뀐다.

연구 상태는 사람과 artifact 사이에 흩어진다. [Distributed
cognition](https://en.wikipedia.org/wiki/Distributed_cognition)의 관점에서 보면 연구실의
인지 상태는 shell history, bag file, plot, commit diff, issue thread,
calibration note를 함께 포함한다. [Sensemaking](https://en.wikipedia.org/wiki/Sensemaking)의
언어를 빌리면, AI의 첫 일은 지금 어떤 행동이 가능한 상황인지 말로 붙이고
그 말을 다음 확인으로 되돌리는 쪽에 가깝다.

하네스가 필요한 이유가 여기에 있다. 하네스는 발산한 후보를 연구 행동으로
바꾸기 전에 증거 상태와 위험을 붙이는 장치다.

```text
candidate branches
-> evidence state
-> smallest risky action
-> artifact check
-> claim / ledger / replay update
```

## 로그에서 반복된 모양

로컬 연구 대화 분석에서 많이 나온 요청은 일반적인 생산성 질문이 아니었다.
구현과 디버깅, reviewer response, 원고 수정, 실험 결과 해석, build와 test,
문헌 positioning이 반복됐다. 도메인은 SLAM, VIO, localization, robotics
general, paper publication에 집중됐다.

성공한 대화는 대체로 좁았다. 원 파일을 읽고, 명령 출력을 확인하고, dataset
protocol을 잠그고, 원고 claim을 evidence에 묶었다. 실패한 대화는 넓었다.
파일명만 보고 구현 상태를 추정하고, compact summary를 원 자료처럼 믿고,
metric 방향을 확인하기 전에 성능을 해석하고, reviewer 문장을 문장 polish
문제로만 다뤘다.

| 반복 패턴 | 잘되는 경우 | 잘 안되는 경우 | 이유 |
|---|---|---|---|
| ROS2/Docker/CUDA 디버깅 | stage를 좁히고 command outcome을 본다 | 처음부터 root cause를 단정한다 | 물리적 실행 상태는 prompt에 들어 있지 않다 |
| SLAM/VPR 결과 해석 | dataset, split, direction, metric을 잠근다 | 숫자만 보고 claim을 만든다 | 같은 숫자도 protocol이 다르면 뜻이 바뀐다 |
| 논문 읽기 | paper, code, experiment를 함께 본다 | abstract 요약으로 novelty를 판단한다 | 연구 기여는 구현과 평가에서 검증한다 |
| 원고/rebuttal | claim, evidence, reviewer risk를 나눈다 | 문장만 매끄럽게 만든다 | reviewer는 문체보다 주장 권한을 본다 |
| 긴 프로젝트 재개 | AGENTS, status, artifact를 다시 읽는다 | 이전 요약을 현재 상태로 착각한다 | memory는 orientation이지 proof가 아니다 |

## 첫 규칙

AI에게 바로 답을 요구하지 않는다. 먼저 현재 행동이 어느 위험을 건드리는지
말하게 한다.

```text
object under truth control:
current evidence permits:
current evidence forbids:
smallest next action:
verification:
```

이 다섯 줄이 있으면 AI의 발산은 작업 후보로 좁아진다. 이 다섯 줄이 없으면
AI의 발산은 drift로 흐른다.
