# Ch.0 — 왜 작업 구조가 필요한가

AI는 연구 작업에서 유용하다. 큰 repo에서 관련 파일을 검색하고, 긴 로그에서 확인할 원인을 빠르게 찾아내고, 논문을 보고 코드를 프로토타입으로 구현하는 등 일반화 작업을 매우 빠르게 수행한다. 그러나 잘 못하는 부분도 분명 있다. 이것을 읽는 사용자는 AI 모델을 다그쳐도 보고, 꾸짖어도 보고, 달래도 보고 하면서 사람과 똑같이 대해가며 더 나은 결과를 이끌어냈을 것이다. 그런데 늘 이렇게 할 수는 없지 않은가. 우리가 AI를 어르고 달래기 위해서 일을 하는 게 아니지 않은가. 이 아티클은 이 상황을 타개하는 원리와 도구를 소개하기 위해 작성하였다.

## 비싼 구독 모델을 쓰면 해결되지 않나?

일단 우리 연구실에서는 200 USD짜리 구독을 6개월째 해오고 있다. 좋은 모델을 쓰면 성능이 더 좋아지는 부분이 있기 때문이다. 그러나 완벽하지는 않다. 구독 서비스는 기본적으로 폐쇄형 서비스다. 우리는 조작할 수 없는 모델에 프롬프트만 입력한다. 사용자는 실제 parameter 수, token limit, backend routing, system prompt, cache, thinking 처리가 언제 어떻게 바뀌는지 거의 알 수 없다. Anthropic의 [2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)은 reasoning effort 변경, thinking cache bug, 짧은 답변을 유도한 system prompt가 품질 저하 보고로 이어졌다고 설명했다. 공급자가 이런 항목을 바꿔도 우리는 알아채기조차 힘들다. 이 상태는 불안정하다. 연구는 장기 작업인데 이런 불안정성은 우리가 원하는 것이 아니다.

## 좋은 모델을 자체 서버에서 돌리면 어떤가?

좋은 모델을 자체 서버에 올리면 공급자의 routing이나 quota 변화에서는 조금 자유로워진다. 그러나 상용 서비스가 제공하는 것은 LLM 가중치 하나가 아니다. 모델 선택, routing, system prompt, context 압축, cache, tool 호출, retrieval, 권한, 실행 환경을 묶은 작업 하네스다. 연구실에서 같은 효과를 내려면 논문 PDF, code path, 실험 로그, dataset convention, reviewer comment를 검색 가능한 단위로 정리하고, 질문마다 어떤 근거를 쓸지 정해야 한다.

이 문제를 해결하기 위해 연구자들은 retrieval을 모델 구조 안으로 끌어들였다. [REALM](https://arxiv.org/abs/2002.08909)은 지식을 parameter 안에 암묵적으로 밀어 넣는 방식이 더 큰 모델을 요구한다고 보고, pre-training 단계부터 retriever를 붙여 문서를 검색하게 했다. [DPR](https://arxiv.org/abs/2004.04906)은 검색 단계 자체를 병목으로 보고, BM25 같은 sparse matching 대신 질문과 passage를 dense representation으로 맞추는 dual encoder를 학습했다. [RAG](https://arxiv.org/abs/2005.11401)는 generator가 사실을 더 정확히 다루고 provenance와 knowledge update 문제를 줄이기 위해 seq2seq model의 parametric memory와 Wikipedia dense index를 결합했다.

그다음 연구들은 generator가 검색된 자료를 어떻게 읽어야 하는지 물었다. [FiD](https://arxiv.org/abs/2007.01282)는 여러 passage를 따로 encode한 뒤 decoder에서 합쳐, 여러 근거를 조합하는 방식을 보였다. [RETRO](https://arxiv.org/abs/2112.04426)는 language model이 다음 token을 예측할 때 2 trillion token database에서 가까운 chunk를 같이 보게 했다. model 밖의 explicit memory를 실행 중에 참조하게 만든 것이다. [Atlas](https://arxiv.org/abs/2208.03299)는 few-shot 상황에서도 retrieval-augmented model이 knowledge-intensive task를 풀 수 있는지 보았고, index 내용을 바꾸면 knowledge source를 갱신할 수 있다는 점도 실험했다.

그러나 연구실에서 필요한 것은 이 논문들의 거대한 web-scale index가 아니다. 어느 논문 PDF, 어느 code path, 어느 실험 로그, 어느 reviewer comment를 어떤 단위로 잘라 두고, 질문이 들어왔을 때 무엇을 찾아 쓸지 정하는 일이다. 답의 품질은 모델의 parameter뿐 아니라 바깥 자료를 얼마나 정확히 찾아 쓰느냐에 달려 있다.

Anthropic의 [2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 이 분업을 실제 세션에서 관찰했다. 사용자는 목표, 접근 방식, 완료 기준을 정하는 쪽에 더 많이 개입했고, Claude는 파일을 고치고 명령을 실행하는 쪽을 더 많이 맡았다. 사용자의 전문성은 특히 문제를 구체적으로 세팅하고, 검증할 대상을 정확히 짚고, agent의 잘못된 판단을 바로잡는 능력으로 나타났다. 그래서 우리는 어떤 문제를 풀 것인지 좁히고, 무엇을 확인해야 하는지 정하고, 잘못된 실행 방향을 끊어 내는 능력을 키우려 한다.

## 그러면 우리가 해야 할 일은 무엇인가?

AI를 사람처럼 대하면 처음에는 잘 되는 것처럼 보인다. 더 자세히 설명하고, 다시 부탁하고, 틀렸다고 지적하면 답이 좋아질 때가 있다. 그러나 이것은 작업 방식으로는 불안정하다. 매번 사용자가 상황을 기억하고, 모델의 답을 의심하고, 빠진 맥락을 다시 채워 넣어야 하기 때문이다.

연구 작업에서는 이 방식이 금방 한계에 닿는다. 실험은 며칠씩 이어지고, 원고는 여러 번 바뀌고, reviewer comment는 과거 결과와 현재 코드 상태를 동시에 요구한다. 이때 필요한 것은 AI를 더 잘 달래는 능력이 아니라, AI가 틀리지 않게 만드는 작업 구조다.

그러려면 AI가 아니라 작업 환경을 바꿔야 한다. 어떤 파일을 봤는지, 어떤 command를 실행했는지, 어떤 결과를 근거로 삼았는지를 남겨야 한다. 그래야 AI가 바뀌어도 같은 일을 다시 이어갈 수 있다. 이렇게 하면 모델 성능이 낮아져도 작업이 완전히 무너지지 않는다. 좋은 모델은 더 빨리 찾고 더 잘 정리하겠지만, 성능이 낮은 모델도 같은 파일과 같은 로그를 보고 같은 절차를 따라갈 수 있다. 이 아티클에서 소개하는 도구들은 그 절차를 만들기 위한 것이다.
