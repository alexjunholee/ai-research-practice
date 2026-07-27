# Ch.4 — 논문과 코드를 맞춰 본다

저장소에 파일이 있다는 것과 그 파일이 실험에서 돌았다는 것은 서로 다른 사실이다. 논문에 적힌 방법까지 놓으면 갈라 볼 것이 셋이다. 논문에서 방법을 설명하는 문장은 저자의 주장을 담는다. 공개 코드는 구현 상태를 보여 준다. runtime 기록은 현재 환경에서 나온 결과를 남긴다. 셋은 각각 따로 짚어 본다. 논문 한 편과 그 공개 저장소를 함께 열어 다시 돌려 보려 할 때 이 구분이 먼저 온다.

[NeurIPS 2019 Reproducibility Program 보고서](https://arxiv.org/abs/2003.12206)는 재현을 같은 code와 data로(구할 수 있을 때) 논문이나 발표에 실린 것과 비슷한 결과를 얻는 일로 적었다. 연구 결과의 신뢰성을 확인하려면 거쳐야 하는 단계로 두었다. 같은 프로그램의 ML Reproducibility checklist는 다섯 절로 나누어 물었고, 그중 셋의 제목이 이론적 주장, 공개한 코드, 보고한 실험 결과다. 확인된 것은 절 제목까지다. 공개한 코드와 보고한 실험 결과가 다른 절에 놓였다는 것만 여기서 가져온다.

다시 돌려 보는 일은 어느 code와 어느 data인지 정한 다음에 시작된다. 그 둘은 셋을 갈라 둔 자리에서 정해진다. 저장소에서 이름으로 찾아 나온 파일과 그 실행이 지나간 파일이 같은 것인지까지 정해야 어느 code인지가 하나로 선다. 논문에 적힌 component가 저장소에 있으면 config를 거쳐 실제로 호출되는지, 결과에 영향을 주는지를 이어서 짚어 본다.

논문 초록과 저장소 README에도 그 component의 이름과 하는 일이 적혀 있다. 초록과 README는 저자가 쓴 요약이다. 앞 장이 옮겨 둔 대로, 원문 파일이 손에 있는 자리에서 요약으로 프로젝트의 참을 정하지 않는다. 그 파일을 열고 눈으로 본 것을 여섯 줄에 남긴다.

## 줄마다 열어 볼 데가 다르다

```text
논문 주장:
관련 code path:
실제로 호출되는 경로:
실험 command:
metric script:
비교할 수 있는 범위:
```

줄마다 열어 볼 자리가 다르다. 첫 줄은 논문에서 옮겨 온다. 어느 table, 어느 figure의 문장인지까지 적어 두면 다음에 그 자리를 바로 편다. 둘째 줄은 저장소에서 이름으로 찾아 채우고, 셋째 줄은 그 이름이 실행에서 지나갔는지를 돌려 보고 채운다. 두 줄이 같으면 같다고 적고 다르면 다르게 적는다. 넷째 줄과 다섯째 줄에는 그 확인을 다시 거는 데 쓴 command와 script가 들어간다. 마지막 줄은 앞의 다섯 줄이 채워진 뒤에 문장으로 적고, 원고에는 그 줄에 적힌 어디까지만 쓴다.

이 여섯 줄 가운데 앞의 다섯에 남는 것은 이름과 경로다. Anthropic은 파일 경로나 질의나 링크처럼 가벼운 식별자만 들고 있다가 실행할 때 그 자리에서 불러오는 방식을 [`just in time`](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)이라고 적었다. 같은 문서는 맥락 창에 든 토큰이 늘수록 모델이 그 안의 내용을 정확히 되짚는 능력이 떨어진다고 적었다. 논문 전문과 저장소를 통째로 읽혀 넣으면 그 토큰이 모두 창에 남는다. 여섯 줄에 적힌 경로는 열기 전까지 한 줄이고, 그 줄을 열어 돌려 본 결과가 셋째 줄에 들어간다.

논문 쪽과 저장소 쪽에 각각 물어 둘 것이 있다.

## 논문에 묻고 코드에 묻고

| 질문 | 이유 |
|---|---|
| 논문 주장이 어느 table, figure, section에 있는가 | 원고 주장 범위를 확인한다 |
| 공개 코드에서 해당 모듈이 어디 있는가 | 코드 존재 여부를 확인한다 |
| 그 모듈이 실제 예제에서 호출되는가 | 실행 경로를 확인한다 |
| config key가 runtime에 읽히는가 | config만 있고 쓰이지 않는 상태를 막는다 |
| 논문 표의 숫자를 만든 script가 공개되어 있는가 | 재현 가능성을 확인한다 |
| issue나 commit에서 convention이 바뀌었는가 | 현재 branch의 의미를 확인한다 |

여섯 질문에는 순서가 있다. 논문 주장이 어느 table에 있는지에서 시작해 모듈이 저장소 어디에 있는지, 그 모듈이 예제에서 호출되는지, config key가 runtime에 읽히는지로 갈수록 열어 볼 데가 안으로 들어간다. 앞 질문의 답이 나와야 다음 질문을 걸 자리가 생긴다. 모듈 경로가 손에 있어야 그 모듈이 예제에서 호출되는지를 물을 데가 정해진다. 뒤의 두 질문은 시간을 묻는다. 논문 표의 숫자를 만든 script가 지금 저장소에 있는지, 논문 시점과 지금 branch 사이에 convention이 바뀌었는지다.

필요할 때 다음 층을 여는 짜임은 에이전트 쪽에도 있다. Anthropic의 [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)는 지시와 script와 자료를 담은 폴더를 에이전트가 찾아 필요할 때 올려 쓰게 하고, 그 열림을 세 층으로 나눴다. 폴더마다 `SKILL.md` 한 장이 들어가고, 그 안에 이름과 언제 쓰는지가 적혀 있다. 1층에서는 그 이름과 description만 system prompt에 올라간다. 2층에서 관련 있다고 판단하면 `SKILL.md` 본문을 읽고, 3층에서 같은 폴더의 다른 파일을 필요할 때 연다. 목차로 시작해 장을 지나 자세한 부록으로 가는 잘 정리된 매뉴얼에 견주며, 필요한 만큼만 올린다고 적었다. 여섯 질문도 답이 나온 줄에서 다음 줄로 내려간다.

답이 모이면 그 모듈의 상태를 한 낱말로 적을 수 있다. `저장소에 있다`에 다음 중 하나를 붙인다.

## 이 모듈, 지금 어느 상태인가

| 라벨 | 의미 |
|---|---|
| active | runtime에서 호출되고 결과에 영향을 준다 |
| disabled | 구현되어 있으나 꺼져 있다 |
| configured-unused | config에는 있으나 실행 경로 밖에 있다 |
| planned-only | 문서나 issue에만 있다 |
| tested-failed | 시도했으나 실패 기록이 있다 |
| dead | 남아 있으나 현재 경로 밖에 있다 |
| unknown | 확인 전 |

라벨은 두 자리에서 갈린다. planned-only와 tested-failed는 문서와 issue를 읽으면 붙는다. active와 configured-unused와 dead는 실행 경로를 따라가야 붙는다. disabled는 flag를 읽으면 붙는다. 켜서 돌려 본 뒤에는 다른 라벨로 옮겨 적는다. unknown은 물어 두고 답을 기다리는 자리다. 빈칸은 묻지 않았다는 뜻으로도 해당 없음이라는 뜻으로도 읽히므로, 물어 둔 자리에는 unknown을 적는다. 한쪽은 파일을 찾아 열면 그 자리에서 답이 나는 일이고, 다른 쪽은 이 branch와 이 config로 돌려 본 출력이 있어야 답이 나는 일이다. AI에 맡길 몫도 이 선에서 나뉜다.

논문에서 방법의 구성요소를 뽑고, 저장소에서 관련 function, class, config를 찾고, issue thread와 README에 적힌 convention 변화를 모으는 일을 AI가 맡는다. 앞의 표가 물은 것 가운데 script 공개와 convention 변화는 코드 본문 밖에 답이 있다. YAML, launch command, issue comment, 실패한 sequence, table caption까지 내려가게 한다. 실제 호출 여부, config가 runtime에 도달하는지, dataset과 metric 조건이 같은지, 원고에서 어디까지 말할 수 있는지는 실행 결과를 보고 사람이 적는다.

AI가 뽑아 오는 것은 구성요소 이름과 function과 config key와 convention 변화라 답이 들어갈 칸이 미리 정해져 있다. Claude API의 [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)는 constrained decoding으로 스키마에 맞는 답을 보장한다고 적었다. 칸 이름을 스키마로 걸어 두면 돌아온 답이 그대로 표의 한 줄이 된다. 스키마가 받는 것은 type, properties, items, required, enum, const, additionalProperties, 중첩 객체, 배열과 boolean·number·integer·string·null이다. pattern(정규식)과 minimum, maximum, minLength, maxLength, uniqueItems, allOf, oneOf는 그 목록 밖에 있다. 스키마는 그 칸이 채워졌다는 데까지 센다. 칸에 적힌 경로가 실행에서 지나갔는지는 앞의 라벨이 받는다.

논문이 말한 자리와 실행 경로의 라벨이 어긋나면 앞 장으로 돌아가 한 번에 하나씩 바꾸며 좁힌다. 좁히는 동안 다시 여는 것은 라벨을 붙인 근거다. active로 적은 줄에는 그 라벨을 만든 command와 config가 함께 남는다. 다음에 그 줄을 열 때는 같은 command를 다시 걸어 라벨이 그대로인지 본다. 이어지는 장에서는 그 command가 내놓은 숫자에 조건을 붙여 둔다.
