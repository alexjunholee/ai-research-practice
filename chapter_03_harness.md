# Ch.3 — 하네스 턴 절차

## 목적

한 번의 AI 작업을 research-state transition으로 처리하는 절차를 정한다. 목적은 실행, claim,
evidence, memory를 같은 층위에 놓지 않는 데 있다.

## Turn packet

비중 있는 작업은 아래 항목을 가진다.

```text
object_under_truth_control:
typed_action:
mode:
higher_order_dimension:
chain_link:
source_of_truth:
evidence_gate:
selected_action:
expected_artifact:
allowed_claim:
blocked_claim:
ledger_or_replay_update:
```

## Typed action

자주 쓰는 action은 다음과 같다.

| action | 적용 상황 |
|---|---|
| workspace_context_reconstruction | 이전 작업 상태를 이어야 할 때 |
| implementation_debug_loop | 코드, runtime, Docker, ROS2 문제가 있을 때 |
| experiment_design | 실험 조건을 새로 정할 때 |
| result_interpretation | 숫자와 표를 해석할 때 |
| paper_experiment_contract | 논문 claim에 실험을 연결할 때 |
| manuscript_argument_repair | 원고 claim과 evidence를 고칠 때 |
| reviewer_response | 심사 의견에 답할 때 |
| literature_positioning | 관련 연구와 novelty를 정리할 때 |

## Mode

mode를 먼저 정한다.

| mode | 허용되는 행동 |
|---|---|
| read-only | 파일 읽기와 분석만 허용 |
| proposal-only | 구조나 계획 제안만 허용 |
| run-allowed | 명령 실행 허용, 파일 수정은 별도 확인 |
| edit-allowed | 파일 수정 허용 |
| execution-requested | 실행과 결과 확인까지 요구 |

mode가 없으면 AI가 읽기 요청에서 편집을 하거나, 실행 요청에서 계획만 내놓는 일이 생긴다.

## Smallest permitted action

가장 작은 행동은 evidence boundary를 넘지 않고 연구 상태를 한 단계만 바꾸는 행동이다.

예시:

- runtime failure: stale process 정리 후 reproduction command 하나
- paper edit: 문장 수정 전 claim/evidence 표 작성
- result interpretation: best number 선택 전 metric protocol 확인
- code archaeology: 파일 요약 전 active code path 확인

## Narrowest proven outcome

마지막 보고는 좁게 쓴다.

| 잘못된 완료 보고 | 좁은 완료 보고 |
|---|---|
| 시스템을 고쳤다 | command X 뒤 warning signature Y가 사라졌다 |
| 성능이 좋아졌다 | protocol P에서 metric M이 baseline B보다 낮아졌다 |
| 논문 답변이 준비됐다 | Table 2 조건과 response scope를 맞췄다 |
| repo를 이해했다 | source of truth 파일 A/B/C와 open claim D를 확인했다 |

## Ledger / replay update

반복되는 실패는 설명으로 남기지 않는다. 다음 세션에서 같은 실패를 막는 형태로 남긴다.

| 반복 실패 | 남길 것 |
|---|---|
| summary를 source처럼 사용 | source 확인 전 claim 금지 rule |
| 코드 존재를 active method로 착각 | implementation status label |
| metric 조건 혼동 | experiment contract |
| reviewer comment를 문장 문제로 처리 | claim/evidence table |
| 사용자 반려 패턴 반복 | user reaction prior |
