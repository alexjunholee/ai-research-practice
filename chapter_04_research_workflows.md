# Ch.4 — 논문과 코드를 맞춰 본다

저장소에 파일이 있다는 것과 그 파일이 실험에서 돌았다는 것은 서로 다른 사실이다. 논문에서 방법을 설명하는 문장은 저자의 주장을 담는다. 공개 코드는 구현 상태를 보여 준다. runtime 기록은 현재 환경에서 나온 결과를 남긴다. 셋은 각각 따로 짚어 본다.

[NeurIPS 2019 Reproducibility Program 보고서](https://arxiv.org/abs/2003.12206)는 재현을 같은 code와 data로(구할 수 있을 때) 논문이나 발표에 실린 것과 비슷한 결과를 얻는 일로 적었다. 연구 결과의 신뢰성을 확인하려면 거쳐야 하는 단계로 두었다. 같은 프로그램의 ML Reproducibility checklist는 다섯 절로 나누어 물었고, 그중 셋의 제목이 이론적 주장, 공개한 코드, 보고한 실험 결과다.

다시 돌려 보는 일은 어느 code와 어느 data인지 정한 다음에 시작된다. 그 둘은 셋을 갈라 둔 자리에서 정해진다. 논문에 적힌 component가 저장소에 있으면 config를 거쳐 실제로 호출되는지, 결과에 영향을 주는지를 이어서 짚어 본다.

초록과 README는 저자가 쓴 요약이다. 앞 장이 옮겨 둔 대로, 원문 파일이 손에 있는 자리에서 요약으로 프로젝트의 참을 정하지 않는다. 그 파일을 열고 눈으로 본 것을 여섯 줄에 남긴다.

## 줄마다 열어 볼 데가 다르다

```text
논문 주장:
관련 code path:
실제로 호출되는 경로:
실험 command:
metric script:
비교할 수 있는 범위:
```

줄마다 열어 볼 자리가 다르다. 논문 쪽과 저장소 쪽에 각각 물어 둘 것이 있다.

## 논문에 묻고 코드에 묻고

| 질문 | 이유 |
|---|---|
| 논문 주장이 어느 table, figure, section에 있는가 | 원고 주장 범위를 확인한다 |
| 공개 코드에서 해당 모듈이 어디 있는가 | 코드 존재 여부를 확인한다 |
| 그 모듈이 실제 예제에서 호출되는가 | 실행 경로를 확인한다 |
| config key가 runtime에 읽히는가 | config만 있고 쓰이지 않는 상태를 막는다 |
| 논문 표의 숫자를 만든 script가 공개되어 있는가 | 재현 가능성을 확인한다 |
| issue나 commit에서 convention이 바뀌었는가 | 현재 branch의 의미를 확인한다 |

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

라벨은 두 자리에서 갈린다. planned-only와 tested-failed는 문서와 issue를 읽으면 붙는다. active와 configured-unused와 dead는 실행 경로를 따라가야 붙는다. AI에 맡길 몫도 이 선에서 나뉜다.

논문에서 방법의 구성요소를 뽑고, 저장소에서 관련 function, class, config를 찾고, issue thread와 README에 적힌 convention 변화를 모으는 일을 AI가 맡는다. YAML, launch command, issue comment, 실패한 sequence, table caption까지 내려가게 한다. 실제 호출 여부, config가 runtime에 도달하는지, dataset과 metric 조건이 같은지, 원고에서 어디까지 말할 수 있는지는 실행 결과를 보고 사람이 적는다.

논문이 말한 자리와 실행 경로의 라벨이 어긋나면 앞 장으로 돌아가 한 번에 하나씩 바꾸며 좁힌다. active로 적은 줄에는 그 라벨을 만든 command와 config가 함께 남는다. 이어지는 장에서는 그 command가 내놓은 숫자에 조건을 붙여 둔다.
