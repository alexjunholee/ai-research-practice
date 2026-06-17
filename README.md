# 로보틱스 연구자를 위한 AI 활용법

> AI는 후보를 빨리 만든다. 연구자는 그중 하나를 실행하며 비용을 낸다.

[가이드 열기](guide.html)

로보틱스/CV 연구 대화에는 비슷한 압력이 자주 남아 있었다. AI는 코드를 따라가고, 로그를
찾고, 원고 문장을 고친다. 읽을 파일과 판단 기준이 분명할 때 속도도 빠르다. 그러나 숫자가
좋아졌다는 말은 split, frame, metric script, failure policy가 붙기 전까지 원고 문장이 되지
못한다.

ROS2 노드를 다시 띄우고, bag을 돌리고, metric script를 확인하고, 원고의 claim을 줄이는
일은 사람이 한다. 그 행동에는 시간, compute, pipeline 안정성, reviewer 신뢰가 붙는다. 이
가이드는 AI 답변이 연구 행동으로 내려가는 순간을 다룬다.

설치 순서와 템플릿은 부록에 둔다. 먼저 볼 것은 AI가 잘하는 일, 자주 실패하는 일, 그리고
그 실패를 줄이는 하네스다.

## 읽을 거리

- [Ch.1: 싼 답과 비싼 실행](chapter_01_start_here.md)
- [Ch.2: 현재 상태는 파일 하나에 없다](chapter_02_environment.md)
- [Ch.3: 하네스는 실행 전에 묻는다](chapter_03_harness.md)
- [Ch.4: 논문은 실행 경로로 읽는다](chapter_04_research_workflows.md)
- [Ch.5: 숫자는 조건을 달고 나온다](chapter_05_experiment_protocol.md)
- [Ch.6: 디버깅은 멈춘 지점부터 본다](chapter_06_stage_local_debugging.md)
- [Ch.7: 답변서는 표에서 시작한다](chapter_07_manuscript_rebuttal.md)
- [Ch.8: Agent repo는 내 실패 옆에 놓고 읽는다](chapter_08_external_templates.md)

부록과 템플릿은 본문을 읽은 뒤 필요한 것만 가져가면 된다.

- [빠른 시작 파일](QUICKSTART.md)
- [용어 경계](TERMS.md)
- [예시 workspace](EXAMPLE_WORKSPACE.md)
- [운영 흐름](PATH.md)
