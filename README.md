# 로보틱스 연구자를 위한 AI 활용법

> AI 출력은 후보로 두고, 실행과 claim은 증거로 닫는다.

[가이드 열기](guide.html)

AI agent를 로보틱스/CV 연구에 쓰면 초반 효율은 바로 올라간다. 에러 로그에서 가능한 원인이
나오고, 논문에서 확인할 코드 경로가 나오며, reviewer comment에서 필요한 실험과 수정 위치가
정리된다. 이 단계의 출력은 좋은 출발점이다.

그 출력은 아직 연구 결과가 아니다. ROS2 launch를 고치고, bag을 다시 돌리고, metric script를
확인하고, 원고 claim을 바꾸는 순간 연구 상태가 바뀐다. 이 문서는 그 경계에서 쓸 기준을
정리한다. 후보, 실행, artifact, claim을 분리하고, 각 장은 그 분리를 코드 읽기, 실험, 디버깅,
rebuttal, 외부 agent repo 이식에 적용한다.

문서 범위는 코드 읽기, 디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response,
외부 agent repo 이식이다.

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
