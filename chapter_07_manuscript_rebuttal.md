# Ch.7 — 주장과 근거를 먼저 본다

AI는 원고의 문장을 빠르게 다듬지만, 매끄러운 표현이 근거의 빈틈까지 메워 주지는 않는다. 원고와 답변서를 고칠 때는 reviewer comment가 어조, 실험 조건, 주장 범위 가운데 무엇을 지적하는지 먼저 확인한다.

[Toulmin의 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)는 실제 논쟁에서 주장이 어떻게 성립하는지 분석했다. claim, data, warrant, backing, qualifier, rebuttal은 서로 다른 역할을 맡는다. 논문 답변서에서도 주장을 뒷받침하려면 근거와 보증이 필요하다. reviewer comment는 주로 이 연결이 충분한지를 묻는다.

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
| comment를 어조 문제로만 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | 근거가 받치지 못하는 주장으로 커진다 |
| citation만 추가 | reviewer가 지적한 실험 조건 확인이 빠진다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

표를 고칠 때도 같은 순서를 따른다. metric 표에는 낮은 error나 높은 success rate와 함께 dataset, sensor, frame, failure policy가 있어야 비교할 수 있다. event count 표가 보여 주는 것은 센 횟수까지다. downstream task에 미친 영향까지 말하려면 precision, outlier rejection, runtime에 관한 추가 근거가 필요하다. caption과 본문 문장은 표가 담은 범위 안에서 쓴다.

답변의 예의는 필요하지만 정중한 표현이 실험 조건을 대신할 수는 없다. 같은 split과 metric script로 baseline을 다시 맞췄다면 그 사실을 구체적으로 쓴다. cross-dataset generalization을 뒷받침할 근거가 없다면 해당 표현의 범위를 줄인다.
