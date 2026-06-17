# AI와 로봇 연구하기

[가이드 열기](guide.html)

AI는 연구 작업에서 잘하는 일이 뚜렷하다. 큰 repo에서 관련 파일을 찾고, 긴 로그에서
확인할 원인을 정리하고, 논문과 코드가 만나는 지점을 빠르게 좁힌다. 약한 부분도 뚜렷하다.
현재 상태를 보지 않고 말하고, 파일 존재를 실제 방법 사용으로 보고, 조건을 확인하지 않은 숫자를
성능 주장처럼 다룬다.

그러면 좋은 모델을 자체 서버에 올려 돌리면 해결될까. 공급자 쪽 routing이나 quota 변화에서는
조금 벗어날 수 있다. 그러나 그 모델이 연구실의 현재 상태를 저절로 아는 것은 아니다. 논문 PDF,
code path, 실험 로그, dataset convention, reviewer comment가 앞에 놓이지 않으면 자체 서버의
모델도 추측한다.

frontier model을 직접 만드는 길도 있다. 그러나 대부분 연구실에서 그 길은 첫 병목이 아니다.
Lewis et al.의 RAG는 Wikipedia index를 검색해 open-domain QA와 지식 집약 생성에서
parametric-only baseline을 앞섰다. DeepMind의 RETRO도 2 trillion token database를 붙여
parameter가 25배 적은 모델로 GPT-3와 Jurassic-1 수준의 Pile 성능을 냈다. 연구실에서는 어떤
자료를 모으고, 어떻게 찾아오고, 찾은 자료를 어떻게 근거로 남기는지가 더 직접적인 병목이다.

2026년 4월 Anthropic은 [Claude Code 품질 저하 보고](https://www.anthropic.com/engineering/april-23-postmortem)를
설명하며 세 가지를 들었다. 기본 reasoning effort를 `high`에서 `medium`으로 낮춘 일, 오래된
thinking을 계속 지운 cache bug, 짧은 답변을 강제한 system prompt였다. 사용자 쪽에서도
[Claude Code issue #42796](https://github.com/anthropics/claude-code/issues/42796)에
thinking depth 감소와 read-before-edit 감소를 로그로 추정한 기록이 남았다.
[Max plan 사용량 소송 보도](https://www.thetimes.com/business/wsj/article/anthropic-sued-limits-ai-plans-f95f2wjcx)는
구독자가 기대한 사용량과 실제 limit 사이의 간격을 다뤘다.

좋은 모델이 계속 온다고 가정할 수 없다. 낮은 effort, 짧은 context, 성능 낮은 모델이 와도
원 파일, 로그, 실행 결과로 일을 잘라 확인해야 한다.

로봇/CV 연구 대화에서 나온 사용자 입력 27,759개를 분류했다. 같은 실패가 반복됐다. 요약을 현재
상태처럼 믿는 일, 코드 존재를 method 사용으로 보는 일, protocol이 다른 숫자를 한 줄에 올리는
일이었다. 원 파일, 로그, 실행 결과에서 현재 상태를 확인하고, 실험 조건, 구현 상태,
실행 시점, 원고 주장 범위를 함께 본다. 코드 읽기, 실험, 디버깅, 답변서, 외부 agent repo 이식도
그 기준에서 다룬다.

문서 범위는 코드 읽기, 디버깅, 실험 protocol, metric 해석, 원고 수정, reviewer response,
외부 agent repo 이식이다.

설치 순서와 템플릿은 부록에 둔다.

## 읽을 거리

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
