# 부록 — 도구 문서 요약 (2026-08 기준)

공급자 문서에서 옮겨 적은 버전과 수치를 여기 모은다. 버전이 올라가면 함께 바뀌는 값들이라, 항목마다 확인한 날짜를 적는다.

## thinking과 cache

그 가운데 thinking 처리의 변화는 문서에 적혀 있다. `budget_tokens`로 생각할 양을 직접 정하던 방식은 4.7 이상에서 400 오류로 거부된다. 그 자리는 `thinking: {"type": "adaptive"}`가 대신하고, 이번 요청에 생각할지 말지는 모델이 스스로 정한다. 앞 턴의 thinking block을 어떻게 하는지도 모델마다 갈린다. [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)는 Opus 4.5와 4.6 이상이 이것을 남기고 입력으로 과금한다고 적었다. Sonnet 4.5·Haiku 4.5와 그 이전은 지운다. 이번 요청에 얼마나 생각했는지는 `response.usage.output_tokens_details.thinking_tokens`에 나온다. 우리 쪽 코드가 같아도 어느 모델을 부르느냐에 따라 모델이 이어받는 앞 맥락과 입력으로 청구되는 양이 달라진다.

부르는 모델을 고정해 두어도 우리 쪽에서 어디를 손대느냐에 따라 같은 앞 맥락을 보내는 값이 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)는 앞부분이 같은 요청을 그 지점부터 이어 쓴다고 적었다. 캐시는 tools, system, messages 순서로 쌓이고, 앞 층이 바뀌면 그 아래가 전부 다시 쌓인다. 도구 정의를 하나 고치면 캐시 전체가 처음부터 새로 쓰인다. 캐시에 쓰는 값은 5분짜리가 기본 입력가의 1.25배다. `"ttl": "1h"`로 한 시간까지 늘리면 2배, 읽어 오는 값은 0.1배다. 무효가 된 자리는 읽기 값 대신 다시 쓰는 값을 낸다. 캐시로 잡히는 최소 토큰도 모델마다 갈려서 Opus 5는 512, Sonnet 5는 1,024, Haiku 4.5는 4,096이다.
