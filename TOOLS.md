# 부록 G — Claude의 Adaptive thinking과 Prompt caching (2026년 10월)

이 부록은 Claude API 공식 문서에 공개된 모델별 지원 범위와 요금 기준을 정리한 참고 메모다. 아래 항목은 모두 2026년 10월 23일에 원문 문서에서 확인한 값이며, 실제 지원 여부와 단가는 모델 세대와 제공 플랫폼에 따라 달라지므로 코드를 수정할 때는 링크한 공식 문서의 해당 모델 항목을 다시 대조해야 한다.

## Adaptive thinking

예전에는 모델이 답변을 내놓기 전에 쓸 추론 분량을 `thinking: {"type": "enabled", "budget_tokens": N}`처럼 토큰 상한으로 직접 지정했다. 그러나 [extended thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)에 따르면 Claude 4.6 모델에서는 이 방식이 deprecated 상태여서 요청 자체는 아직 처리되지만 권하지 않는다. 한 세대 뒤인 Claude 4.7 이상 모델에서는 아예 이 방식을 지원하지 않고 400 오류를 반환하며, 반대로 thinking을 지원하는 Claude 4.5 이하 모델에서는 여전히 이 방식만 쓸 수 있다.

새 세대 모델에서는 대신 `thinking: {"type": "adaptive"}`를 사용한다. 이 설정을 켜면 모델이 요청의 난이도에 따라 thinking을 사용할지, 쓴다면 얼마나 쓸지를 스스로 판단한다. 추론의 깊이를 조절하고 싶을 때도 `budget_tokens`가 아니라 `output_config`의 `effort` 값을 바꾼다. 실제로 소비한 추론 토큰 수는 API 응답의 `usage.output_tokens_details.thinking_tokens` 항목에서 확인할 수 있다.

멀티턴 대화에서는 이전 턴의 thinking block을 다음 턴까지 남기는지 여부도 모델마다 갈린다. [thinking 문서](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-block-preservation-by-model)에 따르면 Opus 4.5 이후 Opus 모델, Sonnet 4.6 이후 Sonnet 모델, 그리고 Haiku 5.5, Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Mythos Preview는 앞선 모든 턴의 thinking block을 기본으로 보존한다. 이때 보존된 block은 다음 요청의 입력 토큰에 포함되어 요금이 청구된다. 반면 그보다 앞선 Opus·Sonnet 모델과 Haiku 4.5까지의 Haiku 모델은 마지막 턴의 block만 남기고 나머지 이전 block은 API가 자동으로 지운다. 게다가 [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#caching-with-thinking-blocks)에 따르면 이들 이전 세대 모델은 도구 결과가 아닌 새 사용자 메시지가 들어오는 순간 앞의 thinking block을 비우면서 그 뒤 메시지의 캐시까지 함께 무효화한다.

## Prompt caching

호출할 모델을 하나로 고정해 두더라도 요청에서 어느 영역을 바꾸느냐에 따라 실제 API 비용은 크게 달라진다. [prompt caching 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)에서 설명하듯 요청의 앞부분 접두사(prefix)가 이전 호출과 일치하면, 서버는 캐시에 저장해 둔 중간 계산 결과를 다시 연산하지 않고 그대로 불러와 쓴다.

여기서 주의할 점은 캐시가 `tools`, `system`, `messages` 순서로 계층을 이루며 쌓인다는 사실이다. 앞쪽 구간이 조금이라도 달라지면 그 뒤에 이어지는 구간 전체를 처음부터 다시 쌓아야 한다. 예컨대 도구 정의 하나만 고쳐도 뒤에 붙은 system prompt와 messages 캐시 전체가 무효화되어 새로 저장되며, thinking 설정이나 `effort` 값을 바꾸는 경우에도 messages 캐시가 깨진다.

요금 역시 캐시에 기록하는 저장 요금과 꺼내 쓰는 읽기 요금을 따로 계산한다. 5분 TTL로 저장할 때는 기본 입력 토큰 요금의 1.25배가 붙고, `"ttl": "1h"`로 한 시간까지 늘리면 2배가 된다. 반대로 캐시에서 읽어 올 때는 대체로 기본 입력 요금의 0.1배만 내며, Claude Opus 5.5와 Claude Sonnet 5.5는 0.05배, Claude Fable 5.1과 Claude Mythos 5.1은 0.025배로 더 낮다. 따라서 캐시가 무효화되어 같은 구간을 자꾸 다시 저장하면 그때마다 1.25배 또는 2배의 저장 요금이 반복해서 붙는다.

마지막으로, 캐시가 작동하기 시작하는 최소 토큰 수도 모델마다 다르다. Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5는 512 토큰부터, Sonnet 5는 1,024 토큰부터, Haiku 4.5는 4,096 토큰부터 캐시가 적용된다. 요청의 앞부분이 이 기준보다 짧으면 캐시에 저장되지 않으므로 호출할 때마다 매번 새로 계산된다.
