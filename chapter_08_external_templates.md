# Ch.8 — Agent repo를 읽는 순서

대화 기록을 분류하면 앞줄에 같은 일이 반복해서 나온다. 구현 디버깅, reviewer response,
원고 수정, 실험 결과 해석. AI는 여기서 많은 일을 했다. 코드를 따라가고, 로그를 찾고,
LaTeX 문단을 고치고, 심사 의견을 실험·설명·한계로 나누었다. 읽을 파일과 판단 기준이
분명할 때는 속도도 빨랐다.

깨진 자리도 일정했다. 파일 이름을 현재 상태로 믿었다. 요약을 원문처럼 다뤘다. partial
trajectory, build pass, plot 생성 같은 좁은 성공을 전체 성공처럼 말했다. 숫자가 좋아졌을
때는 dataset split, frame, metric script, failure policy를 늦게 물었다. 코드에 어떤 factor가
있다는 사실을 optimizer가 그 factor를 쓰고 있다는 증거처럼 다룬 적도 있었다. 심사위원이
비교 조건을 물었는데 답변서 문장만 공손해진 경우도 있었다.

이 기록을 먼저 봐야 외부 agent repo의 자리가 보인다.
[`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)는
코딩 agent에게 필요한 기본 습관을 잘라 놓았다. 가정을 드러내기, 작게 고치기, 요청한 범위
밖의 파일을 건드리지 않기, 성공 기준을 확인하기. 이 규칙들은 AI가 엉뚱한 파일을 고치거나,
실패한 명령을 성공한 작업처럼 말하는 일을 줄인다.

그 규칙은 주로 코드 변경의 층위에 놓인다. 로보틱스 실험에서는 같은 줄의 코드보다 먼저 묶을
조건이 있다. 어느 sequence로 돌렸는지, query와 database의 방향이 무엇인지, ground truth
frame이 무엇인지, metric script가 지난번과 같은지. 이 항목들이 비어 있으면 코드 수정이 잘
끝나도 숫자는 아직 paper claim이 되지 않는다.

[`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)는 agent를
처음 공부할 때 필요한 개념을 넓게 모아 둔다. agent framework, memory, tool use, evaluation을
한 자리에서 훑을 수 있다. LangGraph, CrewAI, AutoGen, OpenAI Agents SDK도 각각 오래 도는
workflow, role 분리, tool handoff, tracing 같은 문제를 다룬다. 이런 자료를 읽으면 agent를
어떻게 굴릴지 먼저 보인다.

로보틱스 연구 대화에서 자주 돌아온 질문은 더 좁았다. 이 숫자가 같은 조건에서 나온 숫자인가.
이 코드는 실제 실행 경로에 들어가는가. 이 figure가 원고의 어느 claim을 받치는가. 이 요약은
원문을 대신할 수 있는가. 이 질문들 앞에서는 framework 이름보다 experiment contract,
implementation status, result provenance, claim calibration이 먼저 온다.

[`alexjunholee/robotics-research-agent`](https://github.com/alexjunholee/robotics-research-agent)는
그중 한 조각을 공개 repo로 떼어 놓았다. user reaction prior다. 답을 내기 전에 이전에 자주
반려된 형태를 먼저 본다. 너무 얕은가. 파일을 읽지 않았는가. 증거보다 큰 말을 했는가.
실행해야 할 때 계획만 말하고 있는가. 걸리는 항목이 있으면 문장을 덧붙이지 않고 다음 행동을
바꾼다.

외부 repo에서 가져올 것은 두 갈래다. 하나는 agent가 파일을 고치고 명령을 실행할 때 쓰는
일반 규칙이다. 다른 하나는 로보틱스 연구가 요구하는 증거 규칙이다. 일반 규칙은 좋은 repo가
이미 많이 다룬다. 증거 규칙은 직접 쌓인 대화 기록에서 더 선명하게 나왔다.

논문을 읽었는데 코드와 실험이 흩어져 있으면 paper-code-experiment map이 필요했다. 숫자가
나왔는데 조건이 흐리면 result provenance가 필요했다. 같은 실수가 반복되면 replay case가
필요했다. 답변 직전에 같은 지적이 예상되면 user-reaction-prior가 필요했다. 이름은 작지만,
실제 연구 대화에서는 이 작은 항목들이 자주 일을 멈춰 세웠다.
