# 로보틱스 연구자를 위한 AI 활용법

> AI 출력은 후보로 두고, 실행과 claim은 증거로 닫는다.

[가이드 열기](guide.html)

AI를 로보틱스/CV 연구에 붙이면 산출물은 빨리 늘어난다. 에러 로그의 원인 후보, 논문에서 확인할
코드 경로, 실험 조건 초안, reviewer 답변 초안이 나온다. 이 산출물들은 아직 연구 결과가 아니다.
각 후보가 어떤 연구 상태를 바꾸는지 확인해야 한다.

하네스는 이 확인을 절차로 고정한다. 모든 요청을 research-state transition으로 바꾸고, 현재 상태,
evidence gate, 가장 작은 허용 action, 실행 뒤 artifact, allowed claim, ledger/replay update를 정한다.
이 문서는 그 개념 구조에서 시작해 코드 읽기, 실험, 디버깅, rebuttal, 외부 agent repo 이식으로
내려간다.

문서 범위는 코드 읽기, 디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response,
외부 agent repo 이식이다.

설치 순서와 템플릿은 부록에 둔다.

## 읽을 거리

- [Ch.1: 하네스가 다루는 연구 상태](chapter_01_start_here.md)
- [Ch.2: 증거 흐름과 상태 복원](chapter_02_environment.md)
- [Ch.3: 하네스 턴 절차](chapter_03_harness.md)
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
