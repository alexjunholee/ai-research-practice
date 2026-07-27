# Ch.7 — 주장과 근거를 먼저 본다

AI는 원고의 문장을 빠르게 다듬는다. 다듬고 나면 표현이 바뀐 원고가 남는다. 심사 의견이 짚은 근거는 다듬기 전 자리에 그대로 있다. 답변서는 원고의 어느 줄을 어떻게 바꿨는지 적어 함께 보내는 문서라서, 손댄 것이 표현뿐이면 답변서에 적을 것도 표현뿐이다. 의견 하나를 받으면 그것이 원고의 무엇을 짚었는지부터 가른다. 어조를 짚은 의견은 문장을 고치면 답이 된다. 실험 조건을 짚은 의견에는 실행이 한 번 더 든다. 주장이 어디까지 간다고 썼는지를 짚은 의견은 그 어디까지를 줄여 답한다.

[Toulmin은 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)에서 실제 논쟁에서 주장이 어떻게 성립하는지 뜯어 놓았다. claim은 주장된 명제이고(p.12), data는 "무엇을 근거로 하는가"에 대한 답이다(p.97). 둘을 잇는 자리에 필요한 것을 Toulmin은 "general, hypothetical statements, which can act as bridges, and authorise the sort of step to which our argument commits us"라고 적었다(p.98). 이 다리가 warrant다. 같은 책은 "data are appealed to explicitly, warrants implicitly"라고도 적었다(p.100). 원고에서 data는 표와 그림으로 이름을 갖고 본문에 나온다. 그 숫자가 왜 그 주장을 받치는지는 읽는 쪽이 채워 넣는 자리로 남는다. 다리를 문장으로 꺼내 적으면 의견이 어느 다리를 물었는지 짚을 자리가 생긴다. Toulmin이 qualifier로 따로 둔 probably, generally, presumably 같은 양태 한정을 지우면 근거는 그대로인 채 주장만 멀리 간다.

## 의견 하나를 한 줄로 옮긴다

부록 D는 원고 문장에서 시작할 때 `claim-evidence-map.md`를 쓰라고 적었다. 의견 하나를 이 표의 한 줄로 옮기면 다음 행동이 어느 칸에서 나오는지 보인다.

| 항목 | 내용 |
|---|---|
| 심사 의견 | 원문 또는 요약 |
| 문제가 된 주장 | reviewer가 겨냥한 문장 |
| 현재 근거 | figure, table, experiment, citation |
| 부족한 근거 | 새로 필요한 실험 또는 계산 |
| 원고 수정 위치 | 고칠 section, table, caption, paragraph |
| 답변 범위 | 답변서에서 말할 수 있는 범위 |
| 남는 한계 | 인정해야 할 한계 |

`답변 범위`에 쓸 말은 `현재 근거` 칸에서 나온다. 그 칸 밖에서 나온 말은 `남는 한계`로 내려간다.

## 답변 문장은 언제 써도 되나

부록 D는 멈춰야 하는 조건 하나로 "심사 위험이 남았는데 문장 다듬기만 반복한다"를 적었다. 답변 문장을 언제 써도 되는지가 아래 세 번째 줄에 걸려 있다.

1. reviewer comment에서 공격받은 주장을 뽑는다.
2. 해당 주장이 기대는 table, figure, experiment, citation을 찾는다.
3. 근거가 충분하면 답변 문장을 쓴다.
4. 근거가 부족하면 실험, 재계산, 주장 줄이기 가운데 하나를 고른다.
5. 원고를 고칠 자리를 답변서에 적는다.

표를 고칠 때도 이 다섯 단계를 그대로 밟는다. 뽑아 둔 주장이 표 하나에 걸려 있으면 둘째 단계는 그 표가 담은 칸을 세는 일이 된다. metric 표에는 낮은 error나 높은 success rate와 함께 dataset, sensor, frame, failure policy가 있어야 비교할 수 있다. 네 칸이 다 있으면 그 조건을 답변 문장에 그대로 적는다. 한 칸이 비면 넷째 단계로 가고, 그 칸이 기록에서 채워지는지 실험을 다시 돌려야 채워지는지가 갈린다.

event count 표는 같은 단계에서 다르게 걸린다. 표가 보여 주는 것은 센 횟수까지다. 그 횟수로 downstream task에 미친 영향까지 말하려면 센 것이 맞게 세어졌는지(precision), 틀리게 잡힌 것을 걸러 냈는지(outlier rejection), 그 처리가 downstream이 쓸 시간 안에 끝났는지(runtime)를 따로 대야 한다. 셋 다 표 밖에 있어서 넷째 단계에서 고를 것은 추가 실험이 된다. caption과 본문 문장은 표가 담은 데까지 쓴다. 고친 caption의 자리는 답변서에 적는다.

## 문장만 다듬은 답변서

이 순서를 건너뛰어도 답변서는 완성된다. 완성된 답변서가 원고에 무엇을 남기는지가 갈릴 뿐이다.

| 실패 | 결과 |
|---|---|
| comment를 어조 문제로만 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | 근거가 받치지 못하는 주장으로 커진다 |
| citation만 추가 | reviewer가 지적한 실험 조건 확인이 빠진다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

둘째 줄이 qualifier를 지우는 손질이다. 같은 표를 그대로 두고 그 위의 문장만 더 멀리 간다.

답변의 예의는 필요하다. 정중한 문장이 답하는 것은 어조를 짚은 의견까지다. 실험 조건을 짚은 의견은 실행 하나를 더 받고서야 답이 된다. 같은 split과 metric script로 baseline을 다시 맞췄다면 그 세 이름을 답변서에 그대로 쓴다. 앞 장에서 채운 여섯 줄에 그 셋이 들어 있다. cross-dataset generalization을 받치는 근거가 한 dataset에서 나왔다면 문장이 가는 어디까지도 그 dataset에 맞춘다. 줄여 낸 만큼은 `남는 한계` 칸으로 옮겨 적는다.
