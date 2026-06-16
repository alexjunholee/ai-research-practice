# 로보틱스 연구자를 위한 AI 활용법

> AI가 만든 말은 싸다. 연구자의 행동은 비싸다.

[가이드 열기](guide.html)

이 글은 로보틱스/CV 연구에서 AI를 어디까지 믿고, 어디서 멈춰 세울지 다룬다.
대화 로그에서 반복된 성공과 실패를 바탕으로 썼다.

AI는 원인 후보를 늘리고, 논문을 빨리 훑고, 코드에서 볼 곳을 찾고, 원고 문장을
매끄럽게 만든다. 그 능력은 실제로 쓸모가 있다. 문제는 그다음이다. ROS2 노드를
다시 띄우고, bag을 돌리고, metric script를 확인하고, 원고의 주장을 줄이는 일은
사람이 한다. 그 행동에는 시간, compute, 파이프라인 안정성, 심사 신뢰가 붙는다.

그래서 이 글은 설치 순서로 시작하지 않는다. AI가 잘하는 일, 자주 무너지는 자리,
그 차이가 생기는 이유, 사람이 감당하는 연구 위험에서 출발한다. 하네스는 그 사이에
놓는 문턱이다. AI가 낸 말을 바로 행동으로 옮기기 전에, 지금 본 증거가 무엇을
허락하는지 묻는 형식이다.

## 읽을 거리

- [Ch.1 — AI의 답은 싸고, 연구자의 행동은 비싸다](chapter_01_start_here.md)
- [Ch.2 — 대화는 연구 상태를 보관하지 못한다](chapter_02_environment.md)
- [Ch.3 — 하네스는 말이 행동이 되기 전의 문턱이다](chapter_03_harness.md)
- [Ch.4 — 논문은 초록에서 끝나지 않는다](chapter_04_research_workflows.md)
- [Ch.5 — 숫자는 혼자 말하지 못한다](chapter_05_experiment_protocol.md)
- [Ch.6 — 디버깅은 한 단계에서만 시작한다](chapter_06_stage_local_debugging.md)
- [Ch.7 — 원고에서 먼저 고칠 것은 문장이 아니다](chapter_07_manuscript_rebuttal.md)
- [Ch.8 — 유명한 agent repo는 재료다](chapter_08_external_templates.md)

부록과 템플릿은 본문을 읽은 뒤 필요한 것만 가져가면 된다.

- [작업장 파일](QUICKSTART.md)
- [용어 경계](TERMS.md)
- [예시 작업장](EXAMPLE_WORKSPACE.md)
- [작업 리듬](PATH.md)
- [로드맵](ROADMAP.md)
