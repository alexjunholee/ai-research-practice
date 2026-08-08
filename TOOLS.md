# 부록 — 도구 문서 요약 (2026-08 기준)

공급자 문서에서 옮겨 적은 버전과 수치를 여기 모은다. 버전이 올라가면 함께 바뀌는 값들이라, 항목마다 확인한 날짜를 적는다.

## thinking과 cache

공급자가 문서로 공개한 변경 가운데 thinking 처리가 있다. `budget_tokens`로 생각할 양을 직접 정하던 방식은 Claude 4.7 이상에서 400 오류로 거부된다. 그 자리를 `thinking: {"type": "adaptive"}`가 대신하고, 이번 요청에서 생각할지 말지는 모델이 스스로 정한다. 앞 턴의 thinking block을 남기는지 지우는지도 모델마다 다르다. [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)는 Opus 4.5, 그리고 4.6 이상이 이것을 남기고 입력 토큰으로 요금을 매긴다고 적었다. Sonnet 4.5·Haiku 4.5와 그 이전은 지운다. 이번 요청에 얼마나 생각했는지는 `response.usage.output_tokens_details.thinking_tokens`에 나온다. 우리 쪽 코드가 같아도 어느 모델을 부르느냐에 따라 모델이 이어받는 앞 맥락과 입력으로 청구되는 양이 달라진다.

부르는 모델을 고정해 두어도 우리 쪽에서 어디를 손대느냐에 따라 같은 앞 맥락을 보내는 데 드는 요금이 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)는 앞부분이 같은 요청이 오면 캐시에 저장해 둔 그 부분을 다시 계산하지 않고 쓴다고 적었다. 캐시는 tools, system, messages 순서로 쌓이고, 앞쪽이 바뀌면 그 뒤가 전부 다시 쌓인다. 도구 정의를 하나 고치면 캐시 전체가 처음부터 새로 쓰인다. 캐시에 저장하는 요금은 5분짜리가 기본 입력 요금의 1.25배다. `"ttl": "1h"`로 한 시간까지 늘리면 2배이고, 캐시에서 읽어 올 때는 0.1배다. 무효가 된 구간에는 읽기 요금 대신 다시 저장하는 요금이 붙는다. 캐시가 걸리는 최소 토큰 수도 모델마다 달라서 Opus 5는 512, Sonnet 5는 1,024, Haiku 4.5는 4,096이다.
