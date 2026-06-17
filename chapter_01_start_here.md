# Ch.1 — 하네스가 다루는 연구 상태

## 목적

하네스가 무엇을 통제하는지 먼저 정한다. 하네스는 AI가 만든 후보가 연구 상태를 어떻게 바꾸는지
묻는다. prompt, tool 목록, 문장 스타일은 그 통제를 돕는 요소다. 주 대상은 연구 상태가 바뀌는
지점과 그 지점을 닫는 증거다.

## 기본 전이

하네스는 모든 입력을 아래 흐름 안에 둔다.

```text
surface request
-> current research state
-> candidate transition
-> smallest permitted action
-> artifact
-> allowed claim
-> ledger or replay update
```

표면 요청이 "이 코드 고쳐줘"여도 실제 전이는 다를 수 있다. runtime state를 바꾸는 일일 수 있고,
experiment protocol을 바꾸는 일일 수 있으며, paper claim을 바꾸는 일일 수도 있다. 전이를 잘못
잡으면 결과가 국소적으로 맞아도 연구 상태는 틀어진다.

## Robotics/CV chain

로보틱스/CV 연구에서는 입력을 다음 chain 안에 놓는다.

```text
world
-> observation model
-> state representation
-> method
-> experiment / metric
-> paper claim
-> reviewer risk
```

예를 들어 SLAM metric을 다시 계산하는 일은 `experiment / metric` 전이에 해당한다. 그러나 frame convention이
바뀌면 `state representation`까지 영향을 준다. 논문 문장을 고치는 일은 `paper claim` 전이지만,
method를 실제보다 강하게 쓰면 `method` 전이를 몰래 바꾼 셈이 된다.

## Object under truth control

작업 전에는 truth control 대상 하나를 정한다.

| 대상 | 예 |
|---|---|
| runtime state | ROS2 node, Docker container, CUDA process, bag replay |
| implementation state | active code path, config consumption, disabled module |
| experiment state | dataset, split, metric script, output path |
| manuscript state | claim, figure, table, paragraph, reviewer response |
| memory state | project memory, handoff note, user correction |

한 turn에서 여러 대상을 건드릴 수는 있다. 그래도 주 대상은 하나로 둔다. 주 대상이 없으면 AI는
파일 수정, 설명, 원고 문장, 실험 claim을 같은 층위에서 섞는다.

## 시작 질문

하네스는 매번 같은 질문으로 시작한다.

```text
이 행동이 틀리면 어떤 연구 상태가 무효가 되는가?
```

이 질문에 답해야 action mode와 evidence gate가 정해진다. 예를 들어 metric script를 바꾸는 행동이
틀리면 result table과 paper claim이 무효가 된다. launch file을 바꾸는 행동이 틀리면 runtime
state와 이후 로그 해석이 무효가 된다. reviewer 답변 문장을 바꾸는 행동이 틀리면 reviewer risk가
커진다.

## 하네스가 필요한 이유

AI는 후보를 빠르게 만든다. 로보틱스 연구에서는 후보 하나를 실행하는 순간 코드, 데이터, 실행 로그,
metric, 원고 claim이 같이 움직인다. 하네스는 후보를 실행으로 옮기기 전에 전이 대상, 증거 등급,
허용 claim, 남길 기록을 정한다.

나머지 장은 같은 구조를 적용한다. 상태를 복원하고, evidence gate를 닫고, 작은 action을 실행하고,
artifact로 claim을 제한한다.
