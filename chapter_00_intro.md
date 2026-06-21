# Ch.0 — 작업 구조를 남긴다

AI는 연구 작업에서 유용하다. 큰 repo에서 관련 파일을 검색하고, 긴 로그에서 확인할 원인을 빠르게 찾아내고, 논문을 보고 코드를 프로토타입으로 구현하는 등 일반화 작업을 매우 빠르게 수행한다. 그러나 잘 못하는 부분도 분명 있다. 이 글을 읽는 사용자는 AI 모델을 다그쳐도 보고, 꾸짖어도 보고, 달래도 보고 하면서 사람과 똑같이 대해가며 더 나은 결과를 이끌어낸 경험이 있다. 그런데 늘 이렇게 할 수는 없지 않은가. 우리가 AI를 어르고 달래기 위해서 일을 하는 게 아니지 않은가. 이 아티클은 이 상황을 타개하는 원리와 도구를 소개하기 위해 작성하였다.

## 비싼 구독 모델을 쓰면 해결되지 않나?

일단 우리 연구실에서는 200 USD짜리 구독을 6개월째 해오고 있다. 좋은 모델을 쓰면 성능이 더 좋아지는 부분이 있기 때문이다. 그래도 작업 품질은 일정하지 않다. 문제는 상용 구독이 폐쇄형 서비스라는 점이다. 사용자는 통제할 수 없는 모델에 프롬프트만 입력한다. 공급자는 실제 parameter 수, token limit, backend routing, system prompt, cache, thinking 처리의 변화 정보를 제한적으로만 공개한다. Anthropic의 [2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)은 reasoning effort 변경, thinking cache bug, 짧은 답변을 유도한 system prompt가 품질 저하 보고로 이어졌다고 적었다. 공급자가 이런 항목을 바꿔도 우리는 알아채기조차 힘들다. 장기 연구에는 안정적인 작업 조건이 필요하다.

## SOTA 모델을 자체 서버에서 돌리면 어떤가?

좋은 모델을 자체 서버에 올리면 공급자의 routing이나 quota 변화에서는 조금 자유로워진다. 그러나 상용 서비스가 제공하는 것은 LLM 가중치 하나가 아니다. 모델 선택, routing, system prompt, context 압축, cache, tool 호출, retrieval, 권한, 실행 환경을 묶은 작업 하네스다. 연구실에서 같은 효과를 내려면 논문 PDF, code path, 실험 로그, dataset convention, reviewer comment를 검색 가능한 단위로 정리하고, 질문마다 어떤 근거를 쓸지 정해야 한다.

이 문제를 부분적으로 해결하기 위해 retrieval을 모델 구조 안에 넣는 연구들이 이어졌다. [REALM](https://arxiv.org/abs/2002.08909)은 지식을 parameter에 모두 밀어 넣는 대신 pre-training 단계부터 retriever를 붙였다. [DPR](https://arxiv.org/abs/2004.04906)은 질문과 passage를 같은 dense representation 공간에서 맞추도록 dual encoder를 학습했다. [RAG](https://arxiv.org/abs/2005.11401)는 seq2seq model의 parametric memory와 Wikipedia dense index를 결합해 factuality, provenance, knowledge update 문제를 줄이려 했다. [FiD](https://arxiv.org/abs/2007.01282), [RETRO](https://arxiv.org/abs/2112.04426), [Atlas](https://arxiv.org/abs/2208.03299)도 retrieved passage를 generator가 읽는 방식, 큰 text database에서 chunk를 가져오는 방식, few-shot setting에서 retrieval을 쓰는 방식을 각각 밀고 갔다.

그러나 연구실에서 필요한 것은 이 논문들의 web-scale index가 아니다. 어느 논문 PDF, 어느 code path, 어느 실험 로그, 어느 dataset convention, 어느 reviewer comment를 어떤 단위로 잘라 둘지 정하는 일이다. 질문이 들어왔을 때 무엇을 찾아 붙일지도 정해야 한다. 답의 품질은 모델의 parameter뿐 아니라 바깥 자료를 얼마나 정확히 찾아 쓰느냐에 달려 있다.

Anthropic의 [2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 이 분업을 실제 세션에서 관찰했다. 사용자는 목표, 접근 방식, 완료 기준을 정하는 쪽에 더 많이 개입했고, Claude는 파일을 고치고 명령을 실행하는 쪽을 더 많이 맡았다. 사용자의 전문성은 특히 문제를 구체적으로 세팅하고, 검증할 대상을 정확히 짚고, agent의 잘못된 판단을 바로잡는 능력으로 나타났다. 그러나 이 일을 매번 사람이 즉석에서 해낼 수는 없다. 이 글의 목적은 agent에게 읽힐 수 있는 작업 지침을 제공하는 것이다. agent가 이 내용을 바탕으로 repo의 `AGENTS.md`, project memory, 실험 기록, 주장·근거 표를 만들 수 있어야 한다.

## 그러면 우리가 해야 할 일은 무엇인가?

AI를 사람처럼 대하면 처음에는 잘 되는 것처럼 보인다. 더 자세히 설명하고, 다시 부탁하고, 틀렸다고 지적하면 답이 좋아질 때가 있다. 이 방식은 작업 방식으로 불안정하다. 매번 사용자가 상황을 기억하고, 모델의 답을 의심하고, 빠진 맥락을 다시 채워 넣어야 하기 때문이다.

연구 작업에서는 이 방식이 금방 한계에 닿는다. 실험은 며칠씩 이어지고, 원고는 여러 번 바뀌고, reviewer comment는 과거 결과와 현재 코드 상태를 동시에 요구한다. 이때는 AI가 틀리지 않게 만드는 작업 구조가 필요하다.

그래서 작업 환경부터 바꿔야 한다. 어떤 파일을 봤는지, 어떤 command를 실행했는지, 어떤 결과를 근거로 삼았는지를 남겨야 한다. 그래야 AI가 바뀌어도 같은 일을 다시 이어갈 수 있다. 이렇게 하면 모델 성능이 낮아져도 작업을 계속 붙잡을 수 있다. 좋은 모델은 더 빨리 찾고 더 잘 정리하겠지만, 성능이 낮은 모델도 같은 파일과 같은 로그를 보고 같은 절차를 따라갈 수 있다. 이 아티클은 그 절차를 만드는 도구들을 소개한다.

이 글은 사람이 처음부터 모든 규칙을 손으로 옮겨 적으라고 쓴 문서가 아니다. 새 연구 workspace를 만들 때는 agent에게 이 글을 읽히고, 자기 repo의 `AGENTS.md`, project memory, 실험 기록, 주장·근거 표를 만들게 해야 한다. 사람은 목표와 공개/비공개 경계, 검증 기준을 정한다. agent는 그 기준을 파일과 절차로 옮긴다. 이 글의 쓰임은 거기에 있다.
