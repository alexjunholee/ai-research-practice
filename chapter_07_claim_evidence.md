# Ch.7 — 주장과 근거 잇기

AI는 원고의 문장을 빠르게 다듬는다. 다듬고 나면 표현이 바뀐 원고가 남는다. 심사 의견은 손대기 전 원고를 읽고 돌아온다. 그 의견이 짚은 근거는 다듬기 전 자리에 그대로 있다. 답변서는 원고의 어느 줄을 어떻게 바꿨는지 적어 함께 보내는 문서다. 손댄 것이 표현뿐이면 거기 적을 것도 표현뿐이다. 의견 하나를 받으면 그것이 원고의 무엇을 짚었는지부터 가른다. 어조를 짚은 의견은 문장을 고치면 답이 된다. 실험 조건을 물었으면 실행이 한 번 더 든다. 주장이 어디까지 간다고 썼는지가 걸린 자리에서는 쓴 만큼을 줄여 답한다.

의견이 무엇을 짚었는지 가르려면 주장과 근거가 어디서 붙는지 그 자리에 이름이 있어야 한다. [Toulmin은 *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)에서 실제 논쟁의 주장이 어떻게 서는지 뜯어 놓았다. claim은 주장된 명제다(p.12). "무엇을 근거로 하는가"에 답하는 것이 data다(p.97). 둘을 잇는 자리에 필요한 것을 Toulmin은 "general, hypothetical statements, which can act as bridges, and authorise the sort of step to which our argument commits us"(p.98)라고 적었다. 이 다리가 warrant다. 같은 책은 "data are appealed to explicitly, warrants implicitly"(p.100)라고도 적었다. 원고에서 data는 표와 그림으로 이름을 갖고 본문에 나온다. 그 숫자가 왜 그 주장을 받치는지는 읽는 쪽이 채워 넣는 자리로 남는다. 다리를 문장으로 꺼내 적으면 의견이 어느 다리를 물었는지 짚을 자리가 생긴다. 주장이 어디까지 가는지는 다리와 다른 자리에 적힌다. Toulmin이 qualifier로 따로 둔 probably, generally, presumably 같은 양태 한정을 지우면 근거는 그대로인 채 주장만 멀리 간다.

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

warrant는 표에 따로 칸을 두지 않고 `현재 근거` 칸 안에 함께 적는다. 다리는 그 근거가 무엇을 받치는지를 말하는 것이라 근거와 떨어져 서면 읽을 데가 없다. figure와 table 이름을 적을 때 그 숫자가 주장을 어떻게 받치는지 한 줄을 함께 적으면 읽는 쪽이 채워 넣던 자리가 표 안으로 들어온다. 의견이 그 한 줄을 물었으면 답에 드는 것은 새 숫자라서 `부족한 근거` 칸으로 넘어간다.

`답변 범위`에 쓸 말은 `현재 근거` 칸에서 나온다. 그 칸 밖에서 나온 말은 `남는 한계`로 내려간다.

표의 칸을 채우는 동안 심사 의견 원문, 겨냥된 문장, 표의 숫자, 새로 돌린 실행 결과가 한 세션에 쌓인다. Anthropic의 [context engineering 문서](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)는 창이 너무 커지면 compaction이 창 전체를 압축한다고 적었다. 같은 문서는 압축이 무엇을 납작하게 만드는지를 "user messages, assistant messages, tool calls, tool results, even prior compaction blocks are all flattened into the summary"라고 적었다. 문서가 돌린 실행에서 압축 한 번이 앞 대화를 약 2,783 토큰으로 줄였다. 요약이 한 번 지나간 뒤에도 `현재 근거` 칸이 가리키던 figure와 table 이름을 다시 집으려면 그 이름이 창 밖의 파일에 적혀 있어야 한다. 그 바깥 저장이 memory다. 문서는 memory가 정보를 창 밖으로 옮겨 세션을 건너 남긴다고 적었고, 이것을 "structured note-taking"이라 불렀다. 같은 실측에서 memory를 쓴 2세션은 5K 토큰으로 시작했고, memory를 안 쓴 2세션은 문서 여덟 개를 다시 읽어 332K까지 갔다. `claim-evidence-map.md`를 파일로 두는 까닭이 여기서 하나 더 선다.

파일에 옮겨 적는 일은 압축이 걸리기 전에 끝나 있어야 한다. 압축이 걸리는 시점은 context engineering 문서가 적어 둔 설정값이 잡는다. 기본 트리거는 150K 토큰이고 최소는 50K다. Claude Code의 [hooks 문서](https://code.claude.com/docs/en/hooks)에는 `PreCompact`와 `PostCompact`가 있어 압축 앞뒤에 무엇을 할지 정해 둘 수 있다. 표의 한 줄을 파일로 빼 두는 일을 `PreCompact`에 걸어 두면 세션이 압축을 지나도 같은 칸에서 다음 행동이 나온다.

표가 채워지면 의견마다 다음 행동이 어느 칸에서 나오는지가 서 있다. 그 행동을
답변서 문장으로 언제 옮겨도 되는지는 다음 장이 다룬다.
