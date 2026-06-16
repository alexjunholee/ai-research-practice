# Ch.3 — 하네스는 발산을 수렴시킨다

AI에게 실패 로그를 주면 원인이 늘어난다. 논문 초고를 주면 고칠 문장이
늘어난다. reviewer comment를 주면 반박 전략이 늘어난다. 늘어나는 것 자체는
문제가 아니다. 연구자는 혼자서는 보지 못한 가지를 보게 된다.

문제는 늘어난 가지가 모두 같은 무게로 보이는 순간에 생긴다. QoS 문제,
namespace 문제, Docker 권한 문제, dataset split 문제, metric script 문제,
원고 claim 문제는 모두 문장으로는 비슷한 길이다. 그러나 연구에서 각 문장은
다른 비용을 가진다. 어떤 문장은 명령 한 줄로 확인되고, 어떤 문장은 실험
하루를 요구하며, 어떤 문장은 원고의 contribution을 낮춘다.

하네스는 이 비용 차이를 보이게 하는 장치다. AI가 만든 후보를 바로 답으로
받지 않고, 현재 증거가 어디까지 허용하는지, 다음 행동이 무엇을 건드리는지,
그 행동 뒤에 어떤 artifact가 남아야 하는지를 묻는다.

## 좋은 세션은 먼저 좁아진다

로컬 대화 분석에서 잘 끝난 세션은 대부분 좁아졌다. 설명을 듣자마자 결론을
내리지 않고, 파일과 로그와 표를 먼저 보았다. 실험 숫자를 해석하기 전에
dataset, split, query/database direction, metric script를 잠갔다. 원고 문장을
고치기 전에 그 문장이 어떤 evidence에 기대는지 확인했다.

무너진 세션은 반대 방향으로 갔다. 파일명만 보고 구현 상태를 확정했고,
로그 일부를 전체 run의 원인처럼 다뤘고, 숫자 하나를 method improvement로
올렸다. reviewer comment는 문장 polish 문제로 축소됐다. AI가 못해서만 생긴
실패가 아니다. 사람이 무엇을 증거로 삼을지 정하지 않았을 때 AI는 가장
그럴듯한 문장을 먼저 만든다.

하네스가 묻는 질문은 길지 않다.

```text
무엇이 지금 truth control 아래 있는가.
현재 증거가 허용하는 말은 무엇인가.
현재 증거가 금지하는 말은 무엇인가.
다음 행동은 어떤 비용을 갖는가.
그 행동 뒤에 무엇을 확인해야 하는가.
```

이 다섯 줄은 AI를 느리게 만들기 위한 장치가 아니다. 오히려 빠르게 만든다.
묻지 않아도 될 후보를 일찍 버리고, 지금 확인할 수 있는 작은 행동으로
내려가기 때문이다.

## Evidence gate

증거는 한 층씩 올라간다. 파일 목록은 후보를 말할 수 있고, command output은
그 실행의 결과를 말할 수 있다. protocol이 닫힌 뒤에야 비교를 말할 수 있고,
claim/evidence map이 닫힌 뒤에야 원고 문장을 말할 수 있다.

| Evidence | 허용되는 말 | 금지되는 말 |
|---|---|---|
| 파일 목록 | 후보 artifact가 있다 | 결과가 검증됐다 |
| 로그 일부 | 특정 warning이 보인다 | 전체 run의 원인이 확정됐다 |
| 명령 실행 | 그 명령의 outcome | paper claim이 닫혔다 |
| protocol 확인 | 같은 조건 안의 비교 | 다른 조건과 일반 성능 비교 |
| claim/evidence map | 원고 문장 후보 | reviewer 방어 완료 |

AI가 자주 틀리는 자리는 이 층을 건너뛰는 곳이다. orientation을 claim처럼
쓰고, execution을 method improvement처럼 쓰고, observation을 전체 run의
원인처럼 말한다. 하네스는 그 건너뜀을 막는다.

## 연구 장면마다 닫히는 문이 다르다

논문 읽기에서는 central claim, active code path, experiment protocol이 닫혀야
한다. 코드 읽기에서는 실제 호출되는 함수와 dead code가 갈라져야 한다.
실험에서는 dataset, split, metric, baseline, artifact가 한 묶음으로 닫혀야
한다. 원고에서는 allowed wording과 blocked wording이 나뉘어야 한다.

같은 AI 도구를 쓰더라도 장면이 바뀌면 닫아야 할 문이 바뀐다. chat model이
논문 요약을 도울 수 있고, coding agent가 repo를 읽을 수 있으며, browser가
외부 repo를 찾을 수 있다. 그러나 도구 표면이 증거 계층을 대신하지는 않는다.

좋은 하네스는 도구 이름을 늘리지 않는다. 장면마다 어떤 문을 닫아야 하는지
적는다.

```text
paper -> claim / assumption / code path / experiment
runtime -> stage / command / output / next failure
experiment -> dataset / split / metric / baseline / artifact
manuscript -> claim / evidence / reviewer risk / allowed wording
```

## Replay는 같은 실패를 미래의 문턱으로 바꾼다

한 번 틀린 것은 correction이다. 두세 번 반복되면 gate가 되어야 한다. 같은
숫자를 보고 또 overclaim을 만들고, 같은 Docker 에러를 보고 또 driver 문제로
몰고 가고, 같은 reviewer comment를 보고 또 문장 polish부터 시작한다면
메모만으로는 부족하다.

replay case는 작은 시험이다. 다음 AI 세션이 같은 실패 앞에서 멈추는지 본다.

```text
trigger:
bad behavior:
required gate:
minimal test:
correct behavior:
durable constraint:
```

예를 들어 VPR 결과에서 `R@1` 숫자가 나왔다고 하자. 나쁜 행동은 exact-frame
retrieval과 radius-based retrieval을 섞어 성능을 비교하는 것이다. 필요한
gate는 query/database direction, radius threshold, feature space, evaluation
script를 확인하는 일이다. 다음 AI는 이 gate를 통과해야 같은 숫자에 대해 말할
수 있다.

하네스는 연구자의 판단을 대신하지 않는다. 대신 판단이 어디서 일어나야
하는지 표시한다. AI가 후보를 늘리는 일과 사람이 위험을 감당하는 일 사이에
놓인 표시다. 이 표시가 있으면 AI는 도구가 된다. 표시가 없으면 AI는 그럴듯한
문장으로 연구 상태를 덮는다.
