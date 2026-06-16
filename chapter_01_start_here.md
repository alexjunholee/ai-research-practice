# Ch.1 — 로보틱스 연구에서 AI는 왜 자주 틀리는가

AI는 후보를 만든다. 이상한 로그 한 줄을 주면 가능한 원인이 늘어난다. 논문
abstract를 주면 관련 연구와 약점 후보가 붙는다. 코드 조각을 주면 고칠 수
있는 위치가 여럿 나온다. 이 능력은 연구자에게 실제로 유용하다. 혼자라면
놓쳤을 가지가 대화 몇 번 만에 생긴다.

문제는 그 다음이다. 연구자는 후보 중 하나를 행동으로 바꿔야 한다. bag을
다시 돌릴지, CUDA 환경을 건드릴지, baseline을 하나 더 세울지, 원고의 claim을
줄일지 정해야 한다. 그 선택에는 시간이 든다. GPU queue, 실험 마감,
깨지기 쉬운 launch file, reviewer에게 보낼 표가 걸린다.

AI가 만든 후보는 싸다. 사람의 행동은 비싸다.

로보틱스 연구에서 AI가 자주 미끄러지는 이유는 여기서 시작한다. AI는 가능한
말을 빠르게 늘린다. 연구는 어느 순간 그 말을 센서, 코드, dataset, metric,
원고 문장으로 내려야 한다. [March](https://doi.org/10.1287/orsc.2.1.71)가
말한 exploration과 exploitation의 긴장이 연구실 책상 위에서 반복된다.
search, variation, experimentation은 AI와 잘 맞는다. refinement, selection,
implementation, execution은 사람이 비용을 낸다.

LLM은 멀리 있는 연상을 잘 끌어온다. [Chen & Ding
2023](https://arxiv.org/abs/2310.11158)은 LLM이 divergent association 과제에서
높은 점수를 낼 수 있음을 보였다. 그러나 멀리 뻗은 연상이 곧 쓸모 있는
연구 판단은 아니다. [Nakajima et al.
2026](https://arxiv.org/abs/2601.20546)은 novelty와 contextual
appropriateness를 따로 보아야 한다고 지적했다. 로보틱스에서 맥락은 말보다
물체에 붙어 있다. sensor time, frame convention, calibration, container
권한, dataset split, metric script가 그 맥락이다.

AI는 연구자를 넓힐 수도 있고, 좁힐 수도 있다. [Wadinambiarachchi et al.
2024](https://arxiv.org/abs/2403.11164)는 생성 AI 예시가 ideation을 돕는 동시에
초기 예시에 고착을 만들 수 있음을 보였다. [Doshi & Hauser
2024](https://arxiv.org/abs/2312.00506)는 개인의 결과는 좋아졌지만 결과물
사이의 유사성이 커질 수 있음을 보고했다. 도움의 방향은 도구 자체보다
사용 장면에서 갈린다. 후보가 늘어도 판단이 깊어지지 않으면 넓어진 것이
아니다. 문장이 매끈해져도 claim이 잠기지 않으면 나아진 것이 아니다.

사람의 선택에는 확률표 바깥의 층이 있다. Simon의 bounded rationality는
사람이 제한된 정보와 시간 안에서 행동한다는 점을 설명한다. Kahneman과
Tversky의 prospect theory는 손실 프레임과 기준점이 위험 판단을 바꾼다는
언어를 준다. [Loewenstein et al.
2001](https://doi.org/10.1037/0033-2909.127.2.267)의 *Risk as Feelings*는
위험 판단에 즉각적인 감정이 들어온다는 점을 보탠다. 지금 고치면 하루를
잃을 수 있다는 감각, 간신히 돌아가는 pipeline을 건드릴 때의 불안, 비어
있는 rebuttal 표가 만드는 압박이 행동을 바꾼다.

카메라 토픽이 보이지 않는 ROS2 노드를 AI에게 던지면 답은 빠르게 나온다.
QoS가 맞지 않을 수 있다. namespace가 다를 수 있다. `use_sim_time`이 켜져
있을 수 있다. Docker 안에서 `/dev/video0` 권한이 빠졌을 수 있다. launch
파일이 다른 파라미터를 덮었을 수 있다.

다섯 가지 모두 그럴듯하다. 그중 하나가 실제 원인일 수도 있다. 그러나
연구자는 그 자리에서 하나를 골라 행동해야 한다. `ros2 topic info
--verbose`를 먼저 볼 것인지, container 권한을 다시 줄 것인지, bag replay를
멈추고 clock을 확인할 것인지 정해야 한다. 이 순간 긴 원인 목록은 도움과
부담을 함께 만든다.

Polanyi, Suchman, Hutchins, Weick의 오래된 논점이 이 장면에서 살아난다.
좋은 로보틱스 연구자는 prompt에 다 적히지 않는 상태를 안다. 어떤 bag은
timestamp가 수상하고, 어떤 USB hub는 오래 돌리면 끊기며, 어떤 reviewer는
metric 방향을 집요하게 본다. Suchman식으로 말하면 plan은 행동을 완전히
결정하는 script가 아니다. 상황 안에서 고쳐 쓰는 resource에 가깝다.

연구 상태는 사람과 artifact 사이에 흩어져 있다. shell history, bag file,
plot, commit diff, issue thread, calibration note가 함께 현재 상태를 만든다.
AI의 첫 일은 이 흩어진 상태를 대신 판단하는 것이 아니라, 지금 가능한
행동을 말로 붙이고 그 말을 다음 확인으로 되돌리는 것이다.

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
