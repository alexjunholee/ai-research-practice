# Ch.8 — 별 많은 저장소에서 절반을 버린다

별 수가 많은 agent 저장소를 열면 마음이 빨라진다. 누군가 이미 정리해 둔 규칙, skill,
prompt, 작업 흐름이 보인다. 그대로 가져오면 연구실의 AI 사용도 정리될 것 같다. 새 도구를
설치할 때의 감각과 비슷하다. 파일이 늘고, 규칙이 생기고, 진척이 있는 것처럼 보인다.

[`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)는
가정을 드러내고, 작게 고치고, 요청한 줄만 만지고, 성공 기준을 검증 가능하게 두라는 식의
규칙을 앞세운다. 코딩 agent가 옆 코드를 건드리거나 잘못된 가정을 밀고 갈 때 도움이 되는
규칙들이다. 도구가 바뀌어도 이런 습관은 남는다. 다만 SLAM metric이나 답변서의 비교
조건은 이 규칙만으로 정리되지 않는다.

[`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)는 agent를
처음 배우는 사람이 개념에서 실습으로 넘어가게 만든다. framework, memory, tool use,
evaluation 같은 말을 큰 지도 안에 놓는다. 그 지도는 쓸모가 있다. 연구실의 bag,
calibration, dataset split, metric script, failed run은 따로 올려놓아야 한다.

`awesome-ai-agents`나 `awesome-llm-agents` 같은 목록도 쓸 곳이 있다. 생태계를 훑고,
어떤 framework가 오래 움직이는지 보는 데 좋다. LangGraph에서는 오래 도는 stateful
workflow와 human-in-the-loop가 먼저 보이고, CrewAI에서는 role과 flow를 나누는 방식이
눈에 들어온다. OpenAI Agents SDK는 agents, tools, handoffs, guardrails, sessions,
tracing, MCP를 작은 primitive로 나누어 둔다. 여기까지는 도구의 풍경이다.

로보틱스 연구실 책상에는 그 풍경 옆에 다른 물건이 더 놓인다. 데이터셋의 출처, 결과
숫자의 주소, SLAM/VIO/VPR 평가 조건, 코드가 있다는 사실과 실제 방법으로 쓰였다는 사실의
차이, 심사 압박, 공개와 비공개 경계. 이 물건들이 빠지면 agent는 일을 많이 한다. 사람이
뒤에서 그 일이 어떤 주장을 만들 수 있는지 다시 치워야 한다.

다른 도구에서 쓰던 규칙을 옮길 때도 같은 방식으로 본다. 예전 파일에는 저장소의 행동
원칙이 들어 있고, skill 폴더에는 반복 절차가 들어 있다. slash command에는 사람이 자주
부르던 작업 단위가 남아 있고, 편집기 규칙에는 그 편집기 안에서만 살던 관습이 섞인다.
도구 설정에는 실제 호출 경계와 인증 정보 경계가 같이 들어 있을 수 있다.

옮길 때는 이름보다 행동을 먼저 본다. "작게 고쳐라"는 작업 원칙으로 남는다. "성공 기준을
검증 가능하게 두라"는 실행 뒤 산출물을 남기는 습관으로 남는다. 특정 명령 한 줄은 새
도구에서 쓸 수 있는 script, template, 읽기 순서로 바뀐다. 다음 세션이 같은 행동을 반복할
수 있으면 이식된 것이다.

템플릿은 늦게 붙인다. 많이 복사하면 운영체제가 생기는 것처럼 보이지만, 빈 문서는 유지비가
된다. 논문을 읽었는데 코드와 실험이 흩어져 있을 때 paper-code-experiment map을 만든다.
숫자가 나왔는데 주소가 흐릴 때 result provenance를 붙인다. 같은 실수가 반복될 때 replay
case를 남긴다. 문서가 앞서가고 연구가 뒤따르는 순서는 오래가지 않는다.

유명한 저장소는 좋은 재료다. 연구실 책상 위에 올라오면 절반은 버려야 한다. 도구의 규칙은
남기고, 도구의 허세는 버린다. 그 뒤에야 AI 사용법이 연구의 물건 앞에 붙는다.
