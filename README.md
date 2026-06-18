# AI와 로봇 연구하기

[가이드 열기](guide.html)

AI는 연구 작업에서 유용하다. 큰 repo에서 관련 파일을 검색하고, 긴 로그에서 확인할 원인을 빠르게
찾아내고, 논문을 보고 코드를 프로토타입으로 구현하는 등 일반화 작업을 매우 빠르게 수행한다.
그러나 잘 못하는 일도 분명 있다. AI가 만든 설명을 실제 연구 작업으로 옮기려면
기록과 확인 절차가 필요하다.

로보틱스 연구 대화에서 나온 사용자 입력 27,759개를 분류했다. 가장 자주 반복된 것은 요약을 현재
상태처럼 믿는 일과 코드 존재를 실제 사용으로 보는 일이었다. protocol이 다른 숫자를 한 줄에
올리는 일과 실패 단계를 섞는 일은 그다음으로 자주 나왔다. 원 파일, 로그, 실행 결과에서 현재
상태를 확인하고, 실험 조건, 구현 상태, 실행 시점, 원고 주장 범위를 함께 본다. 코드 읽기, 실험,
디버깅, 답변서, 외부 agent repo 이식에도
같은 기준을 쓴다.

문서 범위는 코드 읽기, 디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response,
외부 agent repo 이식이다.

설치 순서와 템플릿은 부록에 둔다.

## 읽을 거리

- [Ch.0: 왜 작업 구조가 필요한가](chapter_00_intro.md)
- [Ch.1: AI와 연구 상태](chapter_01_start_here.md)
- [Ch.2: 증거 흐름과 상태 복원](chapter_02_environment.md)
- [Ch.3: 하네스 턴 절차](chapter_03_harness.md)
- [Ch.4: 논문, 코드, 실험 매핑](chapter_04_research_workflows.md)
- [Ch.5: 실험과 metric protocol](chapter_05_experiment_protocol.md)
- [Ch.6: Stage-local debugging](chapter_06_stage_local_debugging.md)
- [Ch.7: 원고와 답변서의 주장·근거 점검](chapter_07_manuscript_rebuttal.md)
- [Ch.8: 외부 agent repo 이식 기준](chapter_08_external_templates.md)

부록은 상황별 참고 문서로 둔다. 필요한 항목만 본다.

- 논문을 코드와 실험으로 읽을 때: [paper-code-experiment-map](templates/paper-code-experiment-map.md)
- 실험 숫자를 원고에 올릴 때: [experiment-contract](templates/experiment-contract.md)
- runtime 문제를 좁힐 때: [stage-local-debugging](templates/stage-local-debugging.md)
- reviewer 답변을 쓸 때: [주장·근거 표](templates/claim-evidence-map.md)
- workspace를 처음 만들 때만: [빠른 시작 파일](QUICKSTART.md)
