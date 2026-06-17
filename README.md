# 로보틱스 연구자를 위한 AI 활용법

> AI 출력은 후보로 두고, 실행과 claim은 증거로 닫는다.

[가이드 열기](guide.html)

로보틱스/CV 연구에서 AI agent를 사용할 때 필요한 운영 기준을 정리한다. 범위는 코드 읽기,
디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response, 외부 agent repo 이식이다.

핵심 규칙은 하나다. AI가 낸 답은 후보로 두고, 연구 상태를 바꾸는 실행은 artifact로 확인한다.
숫자는 protocol이 닫힌 뒤에 해석하고, 원고 claim은 evidence 범위 안에서만 쓴다.

설치 순서와 템플릿은 부록에 둔다.

## 읽을 거리

- [Ch.1: AI 출력과 실행 경계](chapter_01_start_here.md)
- [Ch.2: 연구 상태 복원](chapter_02_environment.md)
- [Ch.3: 하네스 구조](chapter_03_harness.md)
- [Ch.4: 논문, 코드, 실험 매핑](chapter_04_research_workflows.md)
- [Ch.5: 실험과 metric protocol](chapter_05_experiment_protocol.md)
- [Ch.6: Stage-local debugging](chapter_06_stage_local_debugging.md)
- [Ch.7: 원고와 rebuttal의 claim/evidence 점검](chapter_07_manuscript_rebuttal.md)
- [Ch.8: 외부 agent repo 이식 기준](chapter_08_external_templates.md)

부록과 템플릿은 본문을 읽은 뒤 필요한 것만 가져가면 된다.

- [빠른 시작 파일](QUICKSTART.md)
- [용어 경계](TERMS.md)
- [예시 workspace](EXAMPLE_WORKSPACE.md)
- [운영 흐름](PATH.md)
