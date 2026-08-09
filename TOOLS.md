# 부록 G — Claude의 Adaptive thinking과 Prompt caching (2026년 8월)

Claude 문서에 나온 버전과 수치를 정리해 둔다. 이 값들은 버전이 올라갈 때 함께 달라질 수 있으므로, 각 항목의 확인 날짜도 남긴다.

## Adaptive thinking

이전에는 답변 전에 모델이 사용할 thinking 분량을 `budget_tokens`로 직접 지정했다. Claude 4.7 이상에서는 이 방식이 400 오류로 거부된다.

이제는 `thinking: {"type": "adaptive"}`를 사용한다. 모델은 요청마다 thinking을 쓸지, 쓴다면 얼마나 쓸지 스스로 정한다. 실제 사용량은 응답의 `output_tokens_details.thinking_tokens`에서 확인할 수 있다.

생각한 내용을 다음 턴까지 이어 가는 방식은 모델에 따라 다르다. [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)에 따르면 Opus 4.5와 4.6 이상 모델은 이전 턴의 thinking block을 보존하며, 그 토큰은 입력 토큰으로 청구된다. Sonnet 4.5와 Haiku 4.5 및 그 이전 모델은 이를 지운다.

따라서 호출 코드가 같아도 어떤 모델을 고르느냐에 따라 두 가지가 달라진다. 모델이 이어받는 이전 맥락과 입력 토큰으로 청구되는 양이다.

## Prompt caching

호출할 모델을 고정해도 요청의 어느 부분을 바꾸는지에 따라 비용은 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)에 따르면 요청의 앞부분이 같으면 캐시에 저장된 부분을 다시 계산하지 않고 사용한다.

캐시는 tools, system, messages 순서로 쌓인다. 앞쪽이 바뀌면 뒤쪽 전체를 다시 쌓아야 한다. 예를 들어 도구 정의 하나를 고치면 캐시 전체가 처음부터 새로 저장된다.

저장 요금과 읽기 요금도 다르다. 5분 동안 저장할 때는 기본 입력 요금의 1.25배가 적용되고, `"ttl": "1h"`로 한 시간까지 늘리면 2배가 된다. 캐시에서 읽어 올 때는 0.1배다. 무효화된 구간에는 읽기 요금이 아니라 다시 저장하는 요금이 붙는다.

캐시가 적용되는 최소 토큰 수 역시 모델별로 다르다. Opus 5는 512, Sonnet 5는 1,024, Haiku 4.5는 4,096이다. 이보다 짧은 앞부분은 저장되지 않으므로 매번 다시 계산된다.
