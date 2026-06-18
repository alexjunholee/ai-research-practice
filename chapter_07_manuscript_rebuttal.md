# Ch.7 — 원고와 답변서는 주장과 근거부터 본다

AI는 원고 문장을 매끄럽게 만든다. 원고와 답변서에서는 이 능력이 위험해질 수 있다. reviewer comment가 tone, 실험 조건, 주장 범위 중 무엇을 겨냥하는지 먼저 확인한다.

[Toulmin의 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)는 형식논리의 증명보다 실제 논쟁에서 주장이 어떻게 버티는지를 보았다. 이 모델에서는 claim, data, warrant, backing, qualifier, rebuttal이 따로 움직인다. 논문 답변도 비슷하게 읽힌다. reviewer comment는 주로 주장을 받치는 근거와 보증을 묻는다.

## 답변 전에 볼 것

| 항목 | 내용 |
|---|---|
| 심사 의견 | 원문 또는 요약 |
| 문제가 된 주장 | reviewer가 겨냥한 문장 |
| 현재 근거 | figure, table, experiment, citation |
| 부족한 근거 | 새로 필요한 실험 또는 계산 |
| 원고 수정 위치 | 고칠 section, table, caption, paragraph |
| 답변 범위 | 답변서에서 말할 수 있는 범위 |
| 남는 한계 | 인정해야 할 한계 |

## 처리 순서

1. reviewer comment에서 공격받은 주장을 뽑는다.
2. 해당 주장이 기대는 table, figure, experiment, citation을 찾는다.
3. 근거가 충분하면 답변 문장을 쓴다.
4. 근거가 부족하면 실험, 재계산, 주장 축소 중 하나를 선택한다.
5. 원고 수정 위치를 답변서에 명시한다.

## 자주 생기는 실패

| 실패 | 결과 |
|---|---|
| comment를 tone 문제로 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | 근거가 받치지 못하는 주장으로 커진다 |
| 새 citation만 추가 | reviewer가 지적한 실험 조건을 확인하지 않는다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

표를 고칠 때도 같은 순서다. ATE 표는 낮은 error를 보여 주지만 alignment, 실패 처리, sequence 범위가 함께 있어야 비교가 된다. loop closure 개수 표는 탐지 수를 보여 준다. trajectory 개선이나 제약 정확도까지 말하려면 precision, outlier rejection, pose graph 영향 근거가 필요하다. caption과 본문 문장은 표가 직접 보여 준 범위 안에서 쓴다.

예의는 필요하다. 정중한 문장은 실험 조건을 대신하지 못한다. 같은 split과 같은 metric script로 baseline을 다시 맞췄다면 그렇게 쓴다. cross-dataset generalization 근거가 없으면 해당 표현은 줄인다.
