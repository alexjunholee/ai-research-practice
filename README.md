# AI와 로봇 연구하기

[가이드 열기](guide.html)

AI는 연구 작업에서 잘하는 일이 뚜렷하다. 큰 repo에서 관련 파일을 찾고, 긴 로그에서
확인할 원인을 정리하고, 논문과 코드가 만나는 지점을 빠르게 좁힌다. 약한 부분도 뚜렷하다.
현재 상태를 보지 않고 말하고, 파일 존재를 실제 방법 사용으로 보고, 조건을 확인하지 않은 숫자를
성능 주장처럼 다룬다.

그렇지만 모델은 연구자가 고정한 장비가 아니다. 폐쇄형 서비스에서 파라미터 수, 라우팅,
system prompt, cache, thinking 처리를 사용자가 온전히 검증하기는 어렵다. 공급자가 공개하는 것은
주로 모델 ID, [context window와 max output](https://platform.claude.com/docs/en/about-claude/models/overview),
[effort](https://platform.claude.com/docs/en/build-with-claude/effort) 같은 표면이다. Anthropic도
[모델 ID가 고정돼도 serving infrastructure는 달라질 수 있다](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)고
적고, [2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)에서는
기본 reasoning effort를 `high`에서 `medium`으로 낮춘 결정, thinking cache bug, 짧은 답변을
강제한 system prompt가 품질 저하 보고로 이어졌다고 설명했다. 공개
[Claude Code issue #42796](https://github.com/anthropics/claude-code/issues/42796)도
thinking depth 저하와 read-before-edit 감소를 사용자 로그로 추정했고,
[Max plan 사용량 소송 보도](https://www.thetimes.com/business/wsj/article/anthropic-sued-limits-ai-plans-f95f2wjcx)는
구독자가 기대한 사용량과 실제 limit 사이의 불투명성을 다뤘다. 그래서 장치는 낮은 effort,
짧은 context, 성능 낮은 모델에서도 동작해야 한다.

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
