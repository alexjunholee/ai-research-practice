# AI와 로봇 연구하기

[가이드 열기](guide.html)

AI는 연구 작업에서 유용하다. 큰 repo에서 관련 파일을 검색하고, 긴 로그에서 확인할 원인을 빠르게
찾아내고, 논문을 보고 코드를 프로토타입으로 구현하는 등 일반화 작업을 매우 빠르게 수행한다.
그러나 잘 못하는 부분도 분명 있다. 이것을 읽는 사용자는 AI모델을 다그쳐도 보고, 꾸짖어도 보고,
달래도 보고 하면서 사람과 똑같이 대해가며 더 나은 결과를 이끌어냈을 것이다. 그런데 늘 이렇게
할 수는 없지 않은가. 우리가 AI를 어르고 달래기 위해서 일을 하는게 아니지 않은가. 이 아티클은
이 상황을 타개하는 원리와 도구를 소개하기 위해 작성하였다.

- 많은 문제는 비싼 구독 모델을 쓰면 해결되지 않나?

일단 우리 연구실에서는 200USD짜리 구독을 6개월째 해오고 있다. 좋은 모델을 쓰면 성능이 더
좋아지는 부분이 있기 때문이다. 그러나 완벽하지는 않다. 그리고 이것은 기본적으로 폐쇄형 서비스로,
우리가 조작할 수 없는 모델에 프롬프트만 입력하는 식으로 작동한다. 사용자는 실제 parameter 수,
token limit, backend routing, system prompt, cache, thinking 처리가 언제 어떻게 바뀌는지 거의
알 수 없다. Anthropic의
[2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)은
reasoning effort 변경, thinking cache bug, 짧은 답변을 유도한 system prompt가 품질 저하 보고로
이어졌다고 설명했다. 이처럼 공급자가 마음대로 변화시키는 것을 우리는 알아채기조차 힘들다. 이런
것은 불안정하다. 연구는 장기 작업인데 이런 불안정성은 우리가 원하는 것이 아니다.

- 구독이 문제라면 직접 GPU에서 로컬로 돌리면 어떤가?

자체 서버도 완전한 답은 아니다. 모델을 직접 돌리면 공급자의 routing이나 quota 변화에서 조금
자유로워진다. 하지만 논문 PDF, code path, 실험 로그, dataset convention, reviewer comment를
가져오는 일은 여전히 남는다.

이 점은 retrieval-augmented language model 계열 연구에서 이미 정리됐다. [REALM](https://arxiv.org/abs/2002.08909)은
지식을 parameter 안에 암묵적으로 저장하는 대신, 대규모 corpus에서 문서를 검색해 attention에
올리는 구조를 보였다. [DPR](https://arxiv.org/abs/2004.04906)은 sparse keyword matching이 아니라
dense representation으로 passage를 찾는 방식을 학습했고, [RAG](https://arxiv.org/abs/2005.11401)는
seq2seq model의 parametric memory와 Wikipedia dense index라는 non-parametric memory를 결합했다.
[FiD](https://arxiv.org/abs/2007.01282)는 여러 retrieved passage를 generator가 합쳐 답할 수 있음을
보였고, [RETRO](https://arxiv.org/abs/2112.04426)는 2 trillion token database에서 가까운 chunk를
붙여 parameter가 25배 작은 모델로 GPT-3와 Jurassic-1 수준의 Pile 성능을 냈다. [Atlas](https://arxiv.org/abs/2208.03299)는
index 내용을 바꾸면 knowledge source를 갱신할 수 있다는 점도 보여 주었다.

연구실에서 필요한 것은 이 논문들의 거대한 web-scale index가 아니다. 어느 논문 PDF, 어느 code
path, 어느 실험 로그, 어느 reviewer comment를 가져와 답변 앞에 놓을 것인지 정하는 일이다. 답의
품질은 모델 안의 parameter만이 아니라 밖에서 어떤 자료를 찾아오느냐에 크게 묶인다.

- 그러면 우리가 해야 할 일은 무엇인가?

AI를 사람처럼 대하면 처음에는 잘 되는 것처럼 보인다. 더 자세히 설명하고, 다시 부탁하고,
틀렸다고 지적하면 답이 좋아질 때가 있다. 그러나 이것은 작업 방식으로는 불안정하다. 매번 사용자가
상황을 기억하고, 모델의 답을 의심하고, 빠진 맥락을 다시 채워 넣어야 하기 때문이다.

연구 작업에서는 이 방식이 금방 한계에 닿는다. 실험은 며칠씩 이어지고, 원고는 여러 번 바뀌고,
reviewer comment는 과거 결과와 현재 코드 상태를 동시에 요구한다. 이때 필요한 것은 AI를 더 잘
달래는 능력이 아니라, AI가 틀리지 않게 만드는 작업 구조다.

그러려면 AI가 아니라 작업 환경을 바꿔야 한다. 어떤 파일을 봤는지, 어떤 command를 실행했는지,
어떤 결과를 근거로 삼았는지를 남겨야 한다. 그래야 AI가 바뀌어도 같은 일을 다시 이어갈 수 있다.
이렇게 하면 모델 성능이 낮아져도 작업이 완전히 무너지지 않는다. 좋은 모델은 더 빨리 찾고 더 잘
정리하겠지만, 성능이 낮은 모델도 같은 파일과 같은 로그를 보고 같은 절차를 따라갈 수 있다. 이
아티클에서 소개하는 도구들은 그 절차를 만들기 위한 것이다.

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
