# Ch.7 — 원고와 rebuttal의 claim/evidence 점검

## 목적

AI가 만든 매끄러운 문장을 바로 쓰지 않는다. reviewer가 공격한 claim, 그 claim을 받치는 evidence,
수정해야 할 원고 위치를 먼저 분리한다.

## 근거

Toulmin의 argument model은 claim, grounds, warrant, backing, rebuttal을 나눈다. 논문 답변도 같은
구조를 갖는다. reviewer가 묻는 것은 보통 문장 취향이 아니라 claim을 떠받치는 grounds와 warrant다.

그래서 rebuttal 초안은 공손한 문장보다 claim/evidence map에서 시작한다. evidence가 없으면 새 실험,
재계산, claim 축소 중 하나가 먼저다.

## 기본 표

| 항목 | 내용 |
|---|---|
| reviewer comment | 원문 또는 요약 |
| attacked claim | 공격받은 주장 |
| current evidence | 현재 figure, table, experiment, citation |
| missing evidence | 새로 필요한 실험 또는 계산 |
| manuscript change | 고칠 section, table, caption, paragraph |
| response scope | 답변서에서 말할 수 있는 범위 |
| remaining limitation | 인정해야 할 한계 |

## 처리 순서

1. reviewer comment에서 공격받은 claim을 뽑는다.
2. 해당 claim이 기대는 table, figure, experiment, citation을 찾는다.
3. evidence가 충분하면 답변 문장을 쓴다.
4. evidence가 부족하면 실험, 재계산, claim 축소 중 하나를 선택한다.
5. 원고 수정 위치를 답변서에 명시한다.

## 자주 생기는 실패

| 실패 | 결과 |
|---|---|
| comment를 tone 문제로 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | claim이 evidence보다 커진다 |
| 새 citation만 추가 | reviewer가 지적한 실험 조건이 닫히지 않는다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

## 답변서 문장 기준

답변서는 다음 네 요소를 분리한다.

```text
concession:
evidence:
revision:
remaining limitation:
```

예의는 필요하다. 그러나 예의는 실험 조건을 대신하지 않는다. 같은 split과 같은 metric script로
baseline을 다시 맞췄다면 그렇게 쓴다. cross-dataset generalization을 보이지 않았다면 해당 claim을
줄인다.
