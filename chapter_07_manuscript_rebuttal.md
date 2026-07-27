# Ch.7 — 주장과 근거를 먼저 본다

AI는 원고의 문장을 빠르게 다듬는다. 다듬고 나면 표현이 바뀐 원고가 남는다. 심사 의견은 손대기 전 원고를 읽고 돌아온다. 심사 의견이 짚은 근거는 다듬기 전 자리에 그대로 있다. 답변서는 원고의 어느 줄을 어떻게 바꿨는지 적어 함께 보내는 문서라서, 손댄 것이 표현뿐이면 답변서에 적을 것도 표현뿐이다. 의견 하나를 받으면 그것이 원고의 무엇을 짚었는지부터 가른다. 어조를 짚은 의견은 문장을 고치면 답이 된다. 실험 조건을 짚은 의견에는 실행이 한 번 더 든다. 주장이 어디까지 간다고 썼는지를 짚은 의견은 그 어디까지를 줄여 답한다.

의견이 무엇을 짚었는지 가르려면 주장과 근거가 어디서 붙는지 그 자리에 이름이 있어야 한다. [Toulmin은 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)에서 실제 논쟁에서 주장이 어떻게 성립하는지 뜯어 놓았다. claim은 주장된 명제이고(p.12), data는 "무엇을 근거로 하는가"에 대한 답이다(p.97). 둘을 잇는 자리에 필요한 것을 Toulmin은 "general, hypothetical statements, which can act as bridges, and authorise the sort of step to which our argument commits us"라고 적었다(p.98). 이 다리가 warrant다. 같은 책은 "data are appealed to explicitly, warrants implicitly"라고도 적었다(p.100). 원고에서 data는 표와 그림으로 이름을 갖고 본문에 나온다. 그 숫자가 왜 그 주장을 받치는지는 읽는 쪽이 채워 넣는 자리로 남는다. 다리를 문장으로 꺼내 적으면 의견이 어느 다리를 물었는지 짚을 자리가 생긴다. 주장이 어디까지 가는지는 다리와 다른 자리에 적힌다. Toulmin이 qualifier로 따로 둔 probably, generally, presumably 같은 양태 한정을 지우면 근거는 그대로인 채 주장만 멀리 간다.

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

warrant는 표에 따로 칸을 두지 않고 `현재 근거` 칸 안에 함께 적는다. 다리는 그 근거가 무엇을 받치는지를 말하는 것이라 근거와 떨어져 서면 읽을 데가 없다. figure와 table 이름을 적을 때 그 숫자가 주장을 어떻게 받치는지 한 줄을 함께 적으면 읽는 쪽이 채워 넣던 자리가 표 위로 올라온다. 의견이 그 한 줄을 물었으면 답에 드는 것은 새 숫자라서 `부족한 근거` 칸으로 넘어간다.

`답변 범위`에 쓸 말은 `현재 근거` 칸에서 나온다. 그 칸 밖에서 나온 말은 `남는 한계`로 내려간다.

표의 칸을 채우는 동안 심사 의견 원문, 겨냥된 문장, 표의 숫자, 새로 돌린 실행 결과가 한 세션에 쌓인다. Anthropic의 [context engineering 문서](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)는 창이 너무 커지면 compaction이 창 전체를 압축한다고 적었다. 압축이 무엇을 납작하게 만드는지를 같은 문서는 "user messages, assistant messages, tool calls, tool results, even prior compaction blocks are all flattened into the summary"라고 적었다. 문서가 돌린 실행에서 압축 한 번이 앞 대화를 약 2,783 토큰으로 줄였다. 요약이 한 번 지나간 뒤에도 `현재 근거` 칸이 가리키던 figure와 table 이름을 다시 집으려면 그 이름이 창 밖의 파일에 적혀 있어야 한다. 그 바깥 저장이 memory다. 문서는 memory가 정보를 창 밖으로 옮겨 세션을 건너 남긴다고 적었고, 이것을 "structured note-taking"이라 불렀다. 같은 실측에서 memory를 쓴 2세션은 5K 토큰으로 시작했고, memory를 안 쓴 2세션은 문서 여덟 개를 다시 읽어 332K까지 갔다. `claim-evidence-map.md`를 파일로 두는 까닭이 여기서 하나 더 선다.

파일에 옮겨 적는 일은 압축이 걸리기 전에 끝나 있어야 한다. 압축이 걸리는 시점은 context engineering 문서가 적어 둔 설정값이 잡는다. 기본 트리거는 150K 토큰이고 최소는 50K다. Claude Code의 [hooks 문서](https://code.claude.com/docs/en/hooks)에는 `PreCompact`와 `PostCompact`가 있어 압축 앞뒤에 무엇을 할지 정해 둘 수 있다. 표의 한 줄을 파일로 빼 두는 일을 `PreCompact`에 걸어 두면 세션이 압축을 지나도 같은 칸에서 다음 행동이 나온다.

## 답변 문장은 언제 써도 되나

부록 D는 멈춰야 하는 조건 하나로 "심사 위험이 남았는데 문장 다듬기만 반복한다"를 적었다. 답변 문장을 언제 써도 되는지가 아래 세 번째 줄에 걸려 있다.

1. reviewer comment에서 공격받은 주장을 뽑는다.
2. 해당 주장이 기대는 table, figure, experiment, citation을 찾는다.
3. 근거가 충분하면 답변 문장을 쓴다.
4. 근거가 부족하면 실험, 재계산, 주장 줄이기 가운데 하나를 고른다.
5. 원고를 고칠 자리를 답변서에 적는다.

reviewer가 겨냥한 문장이 표의 숫자를 가리키면 고칠 자리도 표가 된다. 표를 고칠 때도 이 다섯 단계를 그대로 밟는다. 뽑아 둔 주장이 표 하나에 걸려 있으면 둘째 단계는 그 표가 담은 칸을 세는 일이 된다. 무슨 칸을 세는지는 표가 무엇을 담았는지가 정한다. metric 표에는 낮은 error나 높은 success rate와 함께 그 수치가 어느 조건에서 나왔는지가 있어야 비교할 수 있다. 앞 장이 센 아홉 가운데 표 안에 자리를 갖는 것은 dataset, sensor, frame, failure policy 넷이고, split과 metric script와 baseline은 caption이나 본문이 받는다. 표와 caption에서 그 조건이 다 나오면 답변 문장에 그대로 적는다. 한 칸이 비면 넷째 단계로 가고, 그 칸이 기록에서 채워지는지 실험을 다시 돌려야 채워지는지가 갈린다.

event count 표는 같은 단계에서 다르게 걸린다. 표가 보여 주는 것은 센 횟수까지다. 그 횟수로 downstream task에 미친 영향까지 말하려면 센 것이 맞게 세어졌는지(precision), 틀리게 잡힌 것을 걸러 냈는지(outlier rejection), 그 처리가 downstream이 쓸 시간 안에 끝났는지(runtime)를 따로 대야 한다. 셋 다 표 밖에 있어서 넷째 단계에서 고를 것은 추가 실험이 된다. 표 밖의 셋을 본문 문장이 이미 말하고 있으면 그 문장도 고칠 자리에 들어간다. caption과 본문 문장은 표가 담은 데까지 쓴다. 고친 caption의 자리는 답변서에 적는다.

## 문장만 다듬은 답변서

이 순서를 건너뛰어도 답변서는 완성된다. 완성된 답변서가 원고에 무엇을 남기는지가 갈릴 뿐이다.

| 실패 | 결과 |
|---|---|
| comment를 어조 문제로만 처리 | 비교 조건이나 실험 공백이 남는다 |
| `robust`, `general`, `significant`를 추가 | 근거가 받치지 못하는 주장으로 커진다 |
| citation만 추가 | reviewer가 지적한 실험 조건 확인이 빠진다 |
| 공손한 문장부터 작성 | Table, Figure, Section 수정이 빠진다 |

첫째 줄은 의견을 가르는 자리에서 갈린다. 비교 조건을 물은 comment를 어조 문제로 받으면 문장이 정중해진 뒤에도 그 조건은 표에서 빈 칸으로 남는다. 둘째 줄이 qualifier를 지우는 손질이다. 같은 표를 그대로 두고 그 위의 문장만 더 멀리 간다. 셋째 줄의 citation은 남의 실행에 붙은 이름이라, 거기 적힌 조건은 그 논문 쪽 표에 남는다. reviewer가 물은 조건은 이쪽 기록에서 나오거나 한 번 더 돌려서 나온다.

답변의 예의는 필요하다. 정중한 문장이 답하는 것은 어조를 짚은 의견까지다. 실험 조건을 짚은 의견은 실행 하나를 더 받고서야 답이 된다. 그 실행이 앞의 숫자와 같은 조건에서 나왔는지를 reviewer가 짚어 볼 자리도 답변서에 있어야 한다. 같은 split과 metric script로 baseline을 다시 맞췄다면 그 세 이름을 답변서에 그대로 쓴다. 숫자를 다시 마주쳤을 때 던지라고 부록 D가 둔 여섯 줄에 그 셋이 들어 있다. 그 여섯 줄의 첫 줄에 적힌 dataset이 답변 문장이 갈 수 있는 어디까지를 정한다. cross-dataset generalization을 받치는 근거가 한 dataset에서 나왔다면 문장이 가는 어디까지도 그 dataset에 맞춘다. 줄여 낸 만큼은 `남는 한계` 칸으로 옮겨 적는다.
