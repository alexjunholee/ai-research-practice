# Ch.3 — 로그 분석은 성공 조건과 실패 조건을 나눈다

하네스는 AI가 연구 상태를 바꿀 때 거치는 검문소다. 무엇을 읽었는지, 어떤
행동을 해도 되는지, 어떤 검증이 끝났는지, 어떤 주장을 아직 하면 안 되는지
남긴다.

로컬 대화 분석에서 가장 두드러진 요청은 구현과 디버깅이었다. 그다음으로
reviewer response, 원고 수정, 실험 결과 해석, build/test 검증, 문헌
positioning이 반복됐다. 실패 신호는 네 방향으로 모였다. 문장이 너무
얕거나, 이미 준 맥락을 놓치거나, 엄밀성이 부족하거나, argument보다 polish를
먼저 했다.

이 결과는 하나의 결론으로 모인다. AI는 연구자의 일을 대신하는 사람이
되기 전에 연구 상태 전이를 다뤄야 한다.

```text
surface request
-> object under truth control
-> current evidence
-> permitted action
-> verification
-> claim / ledger / replay update
```

## 잘되는 조건

### Artifact-first

좋은 세션은 설명을 듣자마자 결론을 내리지 않는다. 파일, 로그, 표, figure,
command output, raw config를 먼저 본다. 논문도 마찬가지다. abstract 요약보다
method section, experiment table, code path, issue discussion이 더 강한
증거가 되는 경우가 많다.

### Protocol-locked

실험 숫자는 protocol 밖에서 의미가 없다.

```text
dataset -> split -> query/database direction -> metric -> baseline -> artifact
```

이 체인이 닫히면 AI는 비교를 말할 수 있다. 하나라도 비면 AI는 관찰만 말할
수 있다.

### Stage-local

디버깅은 data loading, timestamp, transform, retrieval, matching, PnP,
optimizer, evaluation, runtime 중 어느 stage가 깨졌는지 좁히는 일이다. AI는
후보를 빠르게 나열할 수 있다. 하네스는 그 후보를 stage와 command로 묶는다.

### Claim-calibrated

원고 수정은 어떤 문장이 어떤 artifact에 기대는지, reviewer가 어느 claim을
공격하는지, 어떤 evidence가 남아 있는지부터 본다. claim이 좁아지면 문장도
좁아진다.

### Correction-to-constraint

사용자가 "그게 아니다"라고 말한 내용은 다음 turn의 기억으로만 남기면
다시 실패한다. durable constraint로 바뀌어야 한다.

```text
wrong assumption
-> corrected fact
-> affected workflow
-> future gate
-> replay case
```

## 잘 안되는 조건

| 실패 패턴 | 겉모습 | 실제 문제 |
|---|---|---|
| filename inference | 파일명만 보고 구현 완료처럼 말한다 | code presence와 active method가 다르다 |
| partial read finality | 일부 로그를 전체 run처럼 해석한다 | 샘플과 전체 artifact가 분리되지 않았다 |
| metric overclaim | 숫자 하나로 method 개선을 말한다 | protocol과 comparison target이 없다 |
| memory-as-truth | 이전 요약을 현재 상태로 쓴다 | 2차 자료를 primary evidence로 승격했다 |
| tool failure attribution | 명령 실패를 연구 결과처럼 설명한다 | execution failure와 method failure가 섞였다 |
| prose-before-argument | 원고 문장을 먼저 다듬는다 | claim/evidence 구조가 아직 열려 있다 |

## Evidence gate

evidence gate는 현재 증거가 허용하는 말과 금지하는 말을 나눈다.

| Evidence | 허용되는 말 | 금지되는 말 |
|---|---|---|
| 파일 목록 | 후보 artifact가 있다 | 결과가 검증됐다 |
| 로그 일부 | 특정 warning이 보인다 | 전체 run의 원인이 확정됐다 |
| 명령 실행 | 그 명령의 outcome | paper claim이 닫혔다 |
| protocol 확인 | 같은 조건 내 비교 | 다른 논문과 일반 성능 비교 |
| claim/evidence map | 원고 문장 후보 | reviewer 방어 완료 |

이 표가 하네스의 중심이다. AI가 대답하기 전에 이 표의 어느 줄에 서 있는지
정해야 한다.

## Replay

같은 실패가 세 번 반복되면 replay가 필요하다. replay case는
작은 시험이다.

```text
trigger:
bad behavior:
required gate:
minimal test:
correct behavior:
durable constraint:
```

예를 들어 VPR 결과에서 `R@1`이 나왔다고 하자. bad behavior는 exact-frame
retrieval과 radius-based retrieval을 섞어 성능을 비교하는 것이다. required
gate는 query/database direction, radius threshold, feature space, evaluation
script를 확인하는 일이다. 다음 AI는 이 replay를 통과해야 같은 숫자에 대해
말할 수 있다.
