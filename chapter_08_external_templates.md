# Ch.8 — Agent repo는 내 실패 옆에 놓고 읽는다

유명한 agent repo를 보면 마음이 급해진다. skill, memory, tool use, workflow, evaluation 같은
단어가 잘 정리되어 있고, 예제도 많다. [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)처럼
coding agent의 기본 습관을 모아 둔 repo도 있고, [`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)처럼
agent 개념을 넓게 정리한 자료도 있다. LangGraph, CrewAI, AutoGen, OpenAI Agents SDK는 오래 도는
workflow, role 분리, tool handoff, tracing을 각자 다른 방식으로 다룬다.

이 자료를 읽으면 agent 지도를 빨리 얻는다. 그대로 가져올 때 빠지는 자리도 있다. 대화 기록에서 자주 무너진 곳은
framework 선택보다 연구 증거 쪽이었다. 이 숫자가 같은 조건에서 나온 숫자인가. 이 코드는 실제
실행 경로에 들어가는가. 이 figure가 원고의 어느 claim을 받치는가. 이 요약은 원문을 대신할 수
있는가. 이 질문들이 닫히지 않은 채 agent framework만 좋아지면 틀린 방향으로 더 빨리 간다.

Karpathy식 skill repo에서 가져올 것은 coding agent의 기본 예절이다. 가정을 드러낸다. 작게 고친다.
요청 범위 밖의 파일을 건드리지 않는다. 실패한 명령을 성공한 일처럼 말하지 않는다. 이 규칙들은
AI가 엉뚱한 파일을 고치거나, 읽지 않은 repo를 읽은 것처럼 말하거나, plan만 내놓고 실행을
끝낸 척하는 일을 줄인다.

그러나 로보틱스 실험에는 그 앞뒤로 더 붙는 것이 있다. 어느 sequence로 돌렸는지, query와 database의
방향이 무엇인지, ground truth frame이 무엇인지, metric script가 지난번과 같은지. 이 항목들이 비어
있으면 코드 수정이 잘 끝나도 숫자는 아직 paper claim이 되지 않는다.

hello-agents 같은 자료는 agent 전체 지도를 얻을 때 좋다. model, memory, planning, tool use,
evaluation의 큰 이름을 빨리 익힐 수 있다. 처음 agent 논의를 따라갈 때 이런 지도는 시간을 줄여 준다.
하지만 연구실 책상 위의 질문은 더 좁다. 오늘 이 repo에서 AI에게 무엇을 읽게 할 것인가. 어떤 명령을
실행하게 할 것인가. 어느 출력이 나오기 전까지 말을 아낄 것인가.

[`alexjunholee/robotics-research-agent`](https://github.com/alexjunholee/robotics-research-agent)는
그 좁은 질문 쪽에 가까웠다. 특히 user reaction prior는 답을 쓰기 전에 이전에 자주 반려된 형태를
먼저 보게 만든다. 파일을 읽지 않았는가. 증거보다 큰 말을 했는가. 실행해야 할 때 계획만 말하고
있는가. 걸리는 항목이 있으면 문장을 덧붙이지 않고 다음 행동을 바꾼다.

외부 repo에서 가져올 것은 두 층이다. 하나는 agent가 파일을 고치고 명령을 실행할 때 쓰는 일반 규칙.
다른 하나는 로보틱스 연구가 요구하는 증거 규칙. 첫 번째는 유명한 repo들이 이미 많이 다룬다. 두 번째는
직접 쌓인 대화 기록에서 더 선명하게 보였다.

논문을 읽었는데 코드와 실험이 흩어져 있으면 paper-code-experiment map이 필요했다. 숫자가 나왔는데
조건이 흐리면 result provenance가 필요했다. 같은 실수가 되풀이되면 replay case가 필요했다. 답변
직전에 같은 지적이 예상되면 user-reaction-prior가 필요했다. 실제 연구 대화에서는 이런 작은
항목들이 일을 멈춰 세웠다.

GitHub star는 발견의 단서일 수 있다. 이식 기준은 내 연구가 자주 깨진 자리다. 그 자리 옆에 놓고,
그 자리를 고치는 규칙만 가져온다.
