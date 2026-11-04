# 부록 G — Claude의 Adaptive thinking과 Prompt caching (2026년 10월)

Claude 문서에 나온 버전과 수치를 정리해 둔다. 아래 항목의 확인 날짜는 2026년 10월 23일이다. 모델과 제공 플랫폼에 따라 지원 범위와 요금이 다르므로, 코드를 바꿀 때는 링크한 문서의 해당 모델 항목을 다시 확인한다.

## Adaptive thinking

이전에는 답변 전에 모델이 쓸 thinking 분량을 `thinking: {"type": "enabled", "budget_tokens": N}`으로 직접 정했다. [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)에 따르면 Claude 4.6 모델에서는 이 방식이 deprecated지만 요청은 아직 처리된다. Claude 4.7 이상 모델은 이 방식을 지원하지 않고 400 오류를 돌려준다. thinking을 지원하는 Claude 4.5 이하 모델에서는 이 방식만 쓸 수 있다.

이제는 `thinking: {"type": "adaptive"}`를 쓴다. 모델은 요청마다 thinking을 쓸지, 쓴다면 얼마나 쓸지 스스로 정한다. 깊이는 `budget_tokens` 대신 `output_config`의 `effort`로 조절한다. 실제 사용량은 응답의 `usage.output_tokens_details.thinking_tokens`에 나온다.

앞 턴의 thinking block을 다음 턴까지 남기는지는 모델마다 다르다. [thinking 문서](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-block-preservation-by-model)에 따르면 Opus 4.5 이후 Opus 모델, Sonnet 4.6 이후 Sonnet 모델, Haiku 5.5, Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Mythos Preview는 앞선 모든 턴의 thinking block을 기본으로 남긴다. 남은 block은 입력 토큰으로 청구된다. 그보다 앞선 Opus·Sonnet 모델과 Haiku 4.5까지의 Haiku 모델은 마지막 턴의 block만 남기고 나머지는 API가 지운다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#caching-with-thinking-blocks)에 따르면 이 모델들은 도구 결과가 아닌 새 사용자 메시지가 들어오면 앞의 thinking block을 지우고, 그 뒤 메시지의 캐시도 무효가 된다.

## Prompt caching

호출할 모델을 고정해도 요청의 어느 부분을 바꾸는지에 따라 비용은 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)에 따르면 요청의 앞부분이 같으면 캐시에 저장된 부분을 다시 계산하지 않고 그대로 쓴다.

캐시는 tools, system, messages 순서로 쌓인다. 앞쪽이 바뀌면 뒤쪽 전체를 다시 쌓아야 한다. 예를 들어 도구 정의 하나를 고치면 캐시 전체가 처음부터 새로 저장된다. thinking 설정이나 `effort` 값을 바꿔도 messages 캐시는 무효가 된다.

저장 요금과 읽기 요금은 따로 매긴다. 5분 동안 저장할 때는 기본 입력 요금의 1.25배, `"ttl": "1h"`로 한 시간까지 늘리면 2배다. 캐시에서 읽어 올 때는 대체로 0.1배다. Claude Opus 5.5와 Claude Sonnet 5.5는 0.05배, Claude Fable 5.1과 Claude Mythos 5.1은 0.025배다. 무효가 된 구간을 다시 캐시에 저장하면 저장 요금이 다시 붙는다.

캐시가 적용되는 최소 토큰 수도 모델마다 다르다. Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5는 512, Sonnet 5는 1,024, Haiku 4.5는 4,096이다. 이보다 짧은 앞부분은 저장되지 않아 매번 다시 계산된다.
