# 로보틱스 연구자를 위한 AI 활용법

> AI 출력은 후보로 두고, 실행과 claim은 증거로 닫는다.

[가이드 열기](guide.html)

AI를 로보틱스/CV 연구에 붙이면 산출물은 빨리 늘어난다. 에러 로그의 원인 후보, 논문에서 확인할
코드 경로, 실험 조건 초안, reviewer 답변 초안이 나온다. 이 산출물들은 아직 연구 결과가 아니다.
첫 장은 AI가 무엇을 잘하고 무엇을 못하는지, 그 차이가 왜 생기는지부터 설명한다.

하네스는 이 확인을 절차로 고정한다. 모든 요청을 research-state transition으로 바꾸고, 현재 상태,
evidence gate, 가장 작은 허용 action, 실행 뒤 artifact, allowed claim, ledger/replay update를 정한다.
이 문서는 그 개념 구조에서 시작해 코드 읽기, 실험, 디버깅, rebuttal, 외부 agent repo 이식으로
내려간다.

문서 범위는 코드 읽기, 디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response,
외부 agent repo 이식이다.

설치 순서와 템플릿은 부록에 둔다.

## 읽을 거리

- [Ch.1: AI 출력과 연구 상태](chapter_01_start_here.md)
- [Ch.2: 증거 흐름과 상태 복원](chapter_02_environment.md)
- [Ch.3: 하네스 턴 절차](chapter_03_harness.md)
- [Ch.4: 논문, 코드, 실험 매핑](chapter_04_research_workflows.md)
- [Ch.5: 실험과 metric protocol](chapter_05_experiment_protocol.md)
- [Ch.6: Stage-local debugging](chapter_06_stage_local_debugging.md)
- [Ch.7: 원고와 rebuttal의 claim/evidence 점검](chapter_07_manuscript_rebuttal.md)
- [Ch.8: 외부 agent repo 이식 기준](chapter_08_external_templates.md)

부록은 파일 목록이 아니라 상황별 도구 상자다. 지금 막힌 일에 맞춰 하나만 연다.

- 논문을 코드와 실험으로 읽을 때: [paper-code-experiment-map](templates/paper-code-experiment-map.md)
- 실험 숫자를 원고에 올릴 때: [experiment-contract](templates/experiment-contract.md)
- runtime 문제를 좁힐 때: [stage-local-debugging](templates/stage-local-debugging.md)
- reviewer 답변을 쓸 때: [claim-evidence-map](templates/claim-evidence-map.md)
- workspace를 처음 만들 때만: [빠른 시작 파일](QUICKSTART.md)
