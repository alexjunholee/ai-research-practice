# Ch.0 — 작업 구조를 남긴다

AI는 큰 저장소에서 관련 파일을 찾고, 긴 로그에서 원인 후보를 좁히며, 논문의 방법을 prototype code로 옮기는 일을 빠르게 처리한다. 그러나 작업 맥락을 놓치거나 확인하지 않은 내용을 단정하기도 한다. 모델을 다그치거나 달래듯 요청을 거듭 고쳐 결과를 끌어낸 경험이 있더라도, 긴 연구 과정을 매번 이런 대화에만 의존할 수는 없다. 이 글은 작업 맥락과 검증 절차를 파일로 남기는 방법을 다룬다.

## 비싼 구독 모델을 쓰면 해결되지 않나?

이 글의 초고를 쓸 때 우리 연구실은 월 200 USD 구독을 6개월째 사용하고 있었다. 성능이 좋은 모델은 분명 도움이 되지만 작업 품질이 늘 일정한 것은 아니다. 상용 구독은 사용자가 모델의 동작 조건을 직접 통제할 수 없는 폐쇄형 서비스다. 공급자는 실제 parameter 수, token limit, backend routing, system prompt, cache, thinking 처리의 변화를 제한적으로만 공개한다. Anthropic의 [2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)은 reasoning effort 변경, thinking cache bug, 짧은 답변을 유도한 system prompt가 품질 저하 보고로 이어졌다고 적었다. 이런 변경은 사용자가 바로 알아차리기 어렵다. 장기 연구에는 모델 바깥에 안정적인 작업 조건을 마련해야 한다.

thinking 처리의 변화 하나는 문서에 적혀 있다. `budget_tokens`로 생각할 양을 직접 정하던 방식은 4.7 이상에서 400을 돌려주고, 그 자리를 `thinking: {"type": "adaptive"}`가 대신해 모델이 이번 요청에 생각할지 말지를 스스로 정한다. 앞 턴의 thinking block을 어떻게 하는지도 모델마다 갈린다. [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)는 Opus 4.5와 4.6 이상이 이것을 남기고 입력으로 과금하며, Sonnet 4.5·Haiku 4.5와 그 이전은 지운다고 적었다. 이번 요청에 얼마나 생각했는지는 `response.usage.output_tokens_details.thinking_tokens`에 나온다. 우리 쪽 코드가 같아도 어느 모델을 부르느냐에 따라 모델이 이어받는 앞 맥락과 입력으로 청구되는 양이 달라진다.

부르는 모델을 고정해 두어도 우리 쪽에서 어디를 손대느냐에 따라 같은 앞 맥락을 보내는 값이 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)는 앞부분이 같은 요청을 그 지점부터 이어 쓴다고 적었다. 캐시는 tools, system, messages 순서로 쌓이고, 앞 층이 바뀌면 그 아래가 전부 다시 쌓인다. 도구 정의를 하나 고치면 캐시 전체가 처음부터 새로 쓰인다. 캐시에 쓰는 값은 5분짜리가 기본 입력가의 1.25배, `"ttl": "1h"`로 한 시간까지 늘린 것이 2배이고, 읽어 오는 값은 0.1배다. 무효가 된 자리는 읽기 값 대신 다시 쓰는 값을 낸다. 도구 정의 한 줄이 그 차이를 만든다. 캐시로 잡히는 최소 토큰도 모델마다 갈려서 Opus 5는 512, Sonnet 5는 1,024, Haiku 4.5는 4,096이다.

## 최신 모델을 자체 서버에서 돌리면 어떤가?

성능이 좋은 모델을 자체 서버에 올리면 공급자의 routing이나 quota 변화의 영향은 덜 받는다. 다만 상용 서비스의 품질에는 LLM 가중치뿐 아니라 모델 선택, system prompt, context 압축, cache, tool 호출, retrieval, 권한, 실행 환경이 모두 관여한다. 연구실에서도 자료를 검색 가능한 단위로 정리하고 질문마다 사용할 근거를 정해야 일관된 작업 조건을 마련할 수 있다.

Retrieval을 모델 구조에 결합하는 연구는 이 문제의 일부를 다뤘다. [REALM](https://arxiv.org/abs/2002.08909)은 pre-training 단계부터 retriever를 붙였고, [DPR](https://arxiv.org/abs/2004.04906)은 질문과 passage를 같은 dense representation 공간에 맞추도록 dual encoder를 학습했다. [RAG](https://arxiv.org/abs/2005.11401)는 seq2seq model의 parametric memory와 Wikipedia dense index를 결합해 factuality, provenance, knowledge update 문제를 줄이려 했다. [FiD](https://arxiv.org/abs/2007.01282), [RETRO](https://arxiv.org/abs/2112.04426), [Atlas](https://arxiv.org/abs/2208.03299)는 retrieved passage를 generator가 읽거나, 큰 text database에서 chunk를 가져오거나, few-shot setting에 retrieval을 적용하는 방식을 탐구했다.

찾아온 자료를 모델이 읽는 자리는 맥락 창이다. 창에 넣은 토큰이 늘수록 모델이 그 안의 내용을 정확히 되짚는 능력은 떨어진다. Anthropic의 [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)는 이것을 `context rot`이라 부르고, 모델이 큰 맥락을 훑을 때 꺼내 쓰는 `attention budget`이 있다고 적었다. 토큰이 n개면 서로 짚어야 할 쌍이 n²개다. 그래서 좋은 맥락 관리는 원하는 결과가 나올 만한 가장 작은 고신호 토큰 묶음을 찾는 일이 된다.

연구실에서는 web-scale index를 만들기보다 먼저 자료의 경계를 정해야 한다. 어느 논문 PDF, code path, 실험 로그, dataset convention, reviewer comment를 어떤 단위로 나눌지 정하고 질문별로 찾아볼 자료를 연결한다. 답의 품질은 모델의 parameter뿐 아니라 외부 자료를 얼마나 정확히 찾아 쓰는지에도 달려 있다.

그 경계를 누가 긋고 그 안에서 누가 움직이는지는 실제 세션을 센 자료가 있다. Anthropic의 [2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 실제 세션에서 이런 분업을 관찰했다. 사용자는 목표, 접근 방식, 완료 기준을 정하는 데 더 많이 개입했고, Claude는 파일 수정과 명령 실행을 더 많이 맡았다. 이 판단을 매번 즉석에서 반복하지 않으려면 에이전트가 따라갈 작업 지침이 필요하다. 이 글의 절차는 저장소의 `AGENTS.md`, project memory, 실험 기록, 주장·근거 표로 옮겨 적을 수 있다.

## 무엇을 남겨야 하는가?

요청을 자세히 설명하고, 잘못을 지적하고, 빠진 맥락을 보충하면 답이 나아질 때가 있다. 다만 이 방식은 사용자가 매번 상황을 기억하고 같은 설명을 반복해야 하므로 장기 작업에 안정적이지 않다.

실험은 며칠씩 이어지고 원고는 여러 번 바뀐다. 심사 의견에 답하려면 과거 결과와 현재 코드 상태를 함께 확인해야 한다. 이때 필요한 것은 AI의 오류를 추적하고 다시 검증할 수 있는 작업 구조다.

읽은 파일과 실행한 command, 판단의 근거가 된 결과를 기록하면 모델이나 세션이 바뀌어도 작업을 이어갈 수 있다. 모델의 성능에 따라 탐색 속도와 정리 품질은 달라지지만, 같은 파일과 로그를 보며 같은 절차를 따를 수 있다는 조건은 남는다. 이어지는 장에서는 이 작업 구조를 하나씩 만든다.

장마다 만든 것은 파일로 남는다. 다음 연구를 시작하는 자리에서 사람과 에이전트가 그 파일을 함께 읽는다. 새 연구 workspace에서는 에이전트가 이 글을 참고해 저장소의 `AGENTS.md`, project memory, 실험 기록, 주장·근거 표의 초안을 만들 수 있다. 사람은 목표와 공개·비공개 경계, 검증 기준을 정하고, 에이전트는 그 기준을 파일과 절차로 옮긴다.
