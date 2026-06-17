# Ch.3 — 하네스 구조

## 목적

하네스는 AI 답변을 연구 행동으로 옮길 때 쓰는 운영 구조다. 목적은 자동화가 아니라 경계
관리다. 어떤 증거를 봤고, 무엇을 바꾸며, 실행 뒤 어디까지 말할 수 있는지 기록한다.

## 기본 구조

```text
state:
evidence:
candidate actions:
selected action:
expected artifact:
allowed claim:
blocked claim:
ledger update:
```

## 각 항목의 의미

| 항목 | 의미 |
|---|---|
| state | 현재 repo, 실험, 원고, reviewer 상태 |
| evidence | 실제로 읽은 파일이나 실행 출력 |
| candidate actions | AI가 제안한 원인, 수정, 실험 후보 |
| selected action | 지금 실제로 할 하나의 행동 |
| expected artifact | 행동 뒤 남아야 할 파일, 로그, 표, diff |
| allowed claim | 현재 증거로 말할 수 있는 범위 |
| blocked claim | 아직 말하면 안 되는 범위 |
| ledger update | 다음 세션에서 반복을 막기 위한 기록 |

## 하네스가 막는 오류

- warning 한 줄을 전체 실패 원인으로 올리는 것
- `R@1` 증가를 곧바로 방법 개선으로 쓰는 것
- build 성공을 runtime 성공으로 쓰는 것
- generated summary를 source truth로 쓰는 것
- reviewer comment를 paragraph polish 문제로만 처리하는 것

## 좋은 실행 단위

실행 단위는 작아야 한다.

- topic이 보이는지 확인한다.
- subscriber가 받는지 확인한다.
- clock과 namespace를 확인한다.
- 그다음 launch file을 수정한다.

VPR에서는 다음 순서를 우선한다.

- query/database 방향
- cached feature version
- normalization
- index order
- positive radius
- metric script

model architecture 수정은 위 항목이 닫힌 뒤에 한다.

## 반복 실패 기록

같은 실패가 반복되면 조언으로 남기지 않고 gate로 남긴다.

| 반복 실패 | 다음 gate |
|---|---|
| Docker error에서 driver만 의심 | device 권한, volume, user group 확인 |
| retrieval metric 혼동 | metric 이름 옆에 positive definition 기록 |
| reviewer comment를 문체 문제로 처리 | 답변서 앞에 claim/evidence 표 작성 |
| summary를 원문처럼 사용 | 원본 artifact 확인 전 claim 금지 |
