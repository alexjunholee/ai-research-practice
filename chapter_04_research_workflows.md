# Ch.4 — 논문과 코드를 맞춰 본다

논문 요약은 시작일 뿐이다. 로봇 논문을 실제 연구에 쓰려면 논문 문장, 공개 코드, 현재 환경에서 돌릴 실험을 따로 확인해야 한다.

논문에서 방법을 설명하는 문장은 저자의 주장을 담고, 공개 코드는 구현 상태를 보여 주며, runtime 기록은 현재 환경에서 나온 결과를 남긴다. 이 셋은 따로 확인한다. [NeurIPS 2019 Reproducibility Program 보고서](https://arxiv.org/abs/2003.12206)도 결과의 신뢰성을 확인하려면 같은 code와 data, 실행 조건으로 다시 돌려 보는 일이 필요하다고 썼다. 논문에 적힌 component가 저장소에 있더라도 config를 거쳐 실제로 호출되고 결과에 영향을 주는지는 별도로 확인해야 한다.

논문을 연구에 활용하려면 초록을 요약하는 데서 그치지 않고 각 주장이 성립하는 실험 조건을 찾아야 한다.

## 남길 항목

```text
논문 주장:
관련 code path:
실제로 호출되는 경로:
실험 command:
metric script:
비교할 수 있는 범위:
```

## 확인할 질문

| 질문 | 이유 |
|---|---|
| 논문 주장이 어느 table, figure, section에 있는가 | 원고 주장 범위를 확인한다 |
| 공개 코드에서 해당 모듈이 어디 있는가 | 코드 존재 여부를 확인한다 |
| 그 모듈이 실제 예제에서 호출되는가 | 실행 경로를 확인한다 |
| config key가 runtime에 읽히는가 | config만 있고 쓰이지 않는 상태를 막는다 |
| 논문 표의 숫자를 만든 script가 공개되어 있는가 | 재현 가능성을 확인한다 |
| issue나 commit에서 convention이 바뀌었는가 | 현재 branch의 의미를 확인한다 |

## 구현 상태 라벨

코드에 존재한다는 말로는 부족하다. 다음 중 하나로 적는다.

| 라벨 | 의미 |
|---|---|
| active | runtime에서 호출되고 결과에 영향을 준다 |
| disabled | 구현되어 있으나 꺼져 있다 |
| configured-unused | config에는 있으나 실행 경로 밖에 있다 |
| planned-only | 문서나 issue에만 있다 |
| tested-failed | 시도했으나 실패 기록이 있다 |
| dead | 남아 있으나 현재 경로 밖에 있다 |
| unknown | 확인 전 |

AI에는 논문에서 방법의 구성요소를 뽑고, 저장소에서 관련 function, class, config를 찾으며, issue thread와 README에 기록된 convention 변화를 모으는 일을 맡기기 좋다. 실제 호출 여부, config가 runtime에 도달하는지, dataset과 metric 조건이 같은지, 원고에서 어디까지 말할 수 있는지는 실행 결과로 확인한다.

초록을 읽은 뒤에는 YAML, launch command, issue comment, 실패한 sequence, table caption까지 내려가 주장을 뒷받침하는 실행 조건을 찾는다.
