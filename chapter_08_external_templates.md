# Ch.8 — 유명한 agent repo는 재료다

별 수가 많은 agent 저장소를 열면 마음이 빨라진다. 이미 누군가 정리해 둔 규칙,
skill, prompt, 작업 흐름이 보인다. 그대로 가져오면 지금 연구실의 AI 사용도 정리될
것 같다. 여기서 한 번 멈춰야 한다. 저장소의 품질을 묻는 일과 로보틱스 연구에 맞는지
묻는 일은 다른 판단이다.

[`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)는
Claude Code가 잘못된 가정을 밀고 가거나, 코드를 과하게 키우거나, 옆 코드를 건드리는
문제를 줄이려는 규칙을 한곳에 모은다. 가정을 드러내라, 단순하게 고쳐라, 요청한
줄만 만져라, 성공 기준을 검증 가능하게 두라. 이 원칙은 Codex에서도 그대로 쓸 수
있다. 하지만 그 자체가 SLAM metric이나 심사 위험을 닫아 주지는 않는다.

[`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)는 agent를
처음 배우는 사람이 개념에서 실습으로 넘어가게 만든다. framework, memory, tool use,
evaluation 같은 말을 큰 지도로 잡는 데 좋다. 다만 일반 agent 교육은 연구실의
bag, calibration, dataset split, metric script, failed run까지 대신 보지 않는다.

목록형 저장소도 쓸모가 있다. `awesome-ai-agents`나 `awesome-llm-agents` 같은 목록은
생태계를 훑고, 어떤 framework가 오래 움직이는지 보는 출발점이 된다. LangGraph는
long-running, stateful agent workflow의 durable execution과 human-in-the-loop를
앞세운다. CrewAI는 role과 flow를 나누어 multi-agent 작업을 조직한다. AutoGen처럼
유명했던 framework도 유지 상태가 바뀔 수 있다. OpenAI Agents SDK는 agents, tools,
handoffs, guardrails, sessions, tracing, MCP를 작은 primitive로 나누어 보여 준다.

이것들은 모두 좋은 재료다. 그러나 연구 주장은 여전히 데이터셋, metric, 산출물,
원고 문장에서 닫힌다. agent 상태가 이어진다고 실험 출처가 닫히지는 않는다.
guardrail이 있다고 심사위원이 공격할 범위가 줄어드는 것도 아니다.

## 무엇을 빌릴 것인가

외부 repo에서 빌릴 것은 대개 다섯 가지다. 읽기 순서, 가정을 드러내는 방식, 작은
변경을 강제하는 규칙, 실행 뒤 산출물을 남기는 습관, 반복 실패를 다음 세션의 문턱으로
남기는 장치. 이 다섯 가지는 도구가 바뀌어도 살아남는다.

로보틱스 연구에는 거기에 몇 가지가 더 붙는다. 데이터셋의 출처 확인, 결과 숫자의
출처, SLAM/VIO/VPR 평가 조건, 코드가 있다는 사실과 실제 방법으로 쓰였다는 사실의
분리, 심사 압박과 주장-근거 지도, 공개와 비공개 경계. 이 항목들이 없으면 agent는
일을 많이 한다. 연구자는 뒤에서 그 일이 어떤 주장을 허락하는지 다시 정리해야 한다.

## Claude 자료를 Codex로 옮길 때

Claude 중심 저장소를 Codex에서 쓰려면 먼저 목록을 만든다. `CLAUDE.md`,
`.claude/skills`, slash command, Cursor rule, MCP나 plugin 설정, shell command,
template, permission rule, verifier command를 한 번에 훑는다. `CLAUDE.md`만 열고
끝내면 중요한 절차가 빠진다.

그다음 알맹이를 본다. "작게 고쳐라"는 `AGENTS.md`의 작업 원칙이 된다. "성공 기준을
검증 가능하게 두라"는 실행 뒤 산출물을 남기는 규칙이 된다. "이 명령을 실행하라"는
Codex에서 쓸 수 있는 script, template, read order, 증거 문턱으로 바꾼다. 다음
세션이 같은 행동을 반복할 수 있으면 이식된 것이다.

| Claude 중심 요소 | Codex에서 남길 것 |
|---|---|
| `CLAUDE.md` 운영 규칙 | 저장소의 `AGENTS.md`에 읽기 순서와 행동 원칙으로 흡수 |
| `.claude/skills` 절차 지식 | Codex skill, template, 또는 저장소 안 checklist로 분리 |
| slash command | 반복 가능한 script, 명령 묶음, 산출물 template으로 변환 |
| Cursor rule | editor에 묶인 표현을 빼고 보편 규칙만 유지 |
| MCP/plugin 설정 | 실제로 쓰는 도구 경계와 인증 정보 경계를 따로 기록 |
| 검증 통과 기준 | dataset, metric, 산출물, 원고 주장까지 확장 |

## 템플릿은 마지막에 붙는다

템플릿을 많이 복사하면 연구 운영체제가 생기는 것처럼 보인다. 실제로는 빈 문서가
유지비가 되기도 한다. 템플릿은 문턱이 보일 때만 붙인다. 논문을 읽었는데 코드와
실험이 흩어져 있으면 paper-code-experiment map을 쓴다. 숫자가 나왔는데 출처가
흐리면 result provenance를 쓴다. 같은 실수가 반복되면 replay case를 쓴다.

AI를 잘 쓰는 연구실은 prompt가 많은 곳이 아니다. 어느 말이 어떤 행동으로 내려가도
되는지, 내려간 뒤 무엇을 남겨야 하는지 정해 둔 곳이다. 유명한 repo는 그 결정을
도와주는 재료다. 판단은 연구의 물건 앞에서 다시 해야 한다.
