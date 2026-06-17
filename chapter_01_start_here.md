# Ch.1 — AI 출력과 연구 상태

## 개념

AI가 내는 것은 연구 결과가 아니라 후보 산출물이다. 원인 후보, 읽을 파일 후보, 실험 조건 후보,
원고 문장 후보가 나온다. 이 후보들은 빠르게 늘어난다. 그 자체로는 repo, runtime, dataset,
metric, paper claim을 바꾸지 않는다.

연구 상태는 다른 곳에 있다. 어떤 파일을 읽었는지, 어떤 command를 실행했는지, 어떤 artifact가
남았는지, 그 artifact로 어떤 claim을 말할 수 있는지가 연구 상태다. 로보틱스/CV 연구에서 AI를
쓸 때 첫 구분은 여기서 시작한다.

```text
AI output = candidate
research action = state transition
evidence = artifact that closes the transition
claim = statement allowed by that evidence
```

## AI가 잘하는 일

AI는 후보 공간을 넓히는 일에 강하다. 이미 보이는 텍스트, 코드, log, 논문 문장, reviewer comment를
빠르게 읽고 다음에 볼 지점을 제안한다.

| 잘하는 일 | 연구에서의 쓰임 |
|---|---|
| 후보 생성 | 에러 원인, 수정 방향, 실험 조건을 여러 갈래로 뽑는다 |
| 탐색 보조 | 파일, 함수, config, figure, table 위치를 좁힌다 |
| 구조화 | 긴 log나 comment를 stage, claim, evidence, action으로 나눈다 |
| 초안 작성 | rebuttal, README, template, command 설명의 첫 형태를 만든다 |
| 비교 정리 | 여러 repo, paper, 실험 조건의 차이를 표로 놓는다 |

이 일들은 비용이 낮다. 틀린 후보가 섞여도 바로 실행하지 않으면 연구 상태는 아직 바뀌지 않는다.

## AI가 못하는 일

AI는 후보를 만든 뒤 그 후보가 실제 연구 상태와 맞는지 자동으로 보증하지 못한다. 현재 process가
살아 있는지, config가 runtime에서 읽혔는지, metric script가 같은 protocol을 썼는지, reviewer가
공격한 claim이 정말 닫혔는지는 artifact를 봐야 한다.

| 못하는 일 | 왜 문제가 되는가 |
|---|---|
| 보지 않은 현재 상태 확정 | 파일명, memory, 요약만으로 최신 repo나 runtime을 단정한다 |
| 코드 존재와 실행 사용 구분 | source에 있는 module을 active method로 착각한다 |
| 숫자와 claim의 거리 조절 | metric 하나를 방법 개선이나 generalization claim으로 올린다 |
| 실패 단계 분리 | retrieval, geometry, optimization, evaluation 실패를 한 원인으로 합친다 |
| 위험 부담 | 시간, compute, reviewer trust, 원고 claim scope를 사람이 감당한다 |

그래서 AI 출력은 바로 행동이 되면 안 된다. 후보가 실행으로 넘어가는 순간부터 비용이 생기고,
연구 상태가 바뀐다.

## 구조적 이유

차이는 지능의 크기보다 작업 구조에서 나온다. AI는 context 안에서 가능한 다음 후보를 만든다.
로보틱스/CV 연구는 context 밖의 상태를 바꾼다. Docker container, ROS2 topic, CUDA process,
dataset split, calibration file, metric script, TeX table은 실제 파일과 실행 결과로 닫힌다.

AI가 강한 공간은 텍스트와 구조다. 연구자가 닫아야 하는 공간은 실행과 증거다. 이 둘을 섞으면
다음 오류가 반복된다.

| 섞인 것 | 반복되는 오류 |
|---|---|
| 후보와 원인 | 그럴듯한 설명을 root cause로 쓴다 |
| 코드와 방법 | 구현되어 있는 코드를 논문 방법으로 쓴다 |
| 숫자와 주장 | protocol이 다른 숫자를 성능 claim으로 쓴다 |
| 문장과 답변 | reviewer가 요구한 실험 없이 rebuttal 문장만 고친다 |
| 요약과 증거 | handoff나 memory를 source of truth로 쓴다 |

하네스는 이 섞임을 막기 위한 절차다.

## 이론적 근거

이 구분은 작업 이론과 human factors에 기대어 있다. Suchman의 situated action은 plan과 실제 행동의
거리를 다룬다. 연구에서도 prompt나 plan은 아직 행동이 아니다. `ros2 topic info`, CSV, TeX diff,
rebuttal table 같은 물체가 붙어야 행동이 된다.

Hutchins의 distributed cognition은 판단이 사람 머리 안에만 있지 않다고 본다. 연구실의 판단도
repo, launch file, dataset, terminal output, paper table, 기억 노트에 흩어져 있다. AI가 대화창 안에서
그럴듯한 연결을 만들 수 있어도, 흩어진 물체를 다시 묶어야 연구 상태가 닫힌다.

human factors 쪽의 automation 연구는 자동화가 일을 없애기보다 monitoring과 rare intervention을
남긴다고 본다. AI도 같다. 후보 작성은 쉬워지지만, 어느 후보를 실행할지, 어떤 숫자를 claim으로
올릴지, reviewer에게 어디까지 말할지는 연구자가 닫는다.

## 하네스가 다루는 것

하네스는 AI가 만든 후보가 어떤 연구 상태를 바꾸는지 묻는다. prompt, tool 목록, 문장 스타일은
보조 요소다. 주 대상은 연구 상태가 바뀌는 지점과 그 지점을 닫는 증거다.

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

예를 들어 SLAM metric을 다시 계산하는 일은 `experiment / metric` 전이에 해당한다. 그러나 frame
convention이 바뀌면 `state representation`까지 영향을 준다. 논문 문장을 고치는 일은 `paper claim`
전이지만, method를 실제보다 강하게 쓰면 `method` 전이를 몰래 바꾼 셈이 된다.

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
