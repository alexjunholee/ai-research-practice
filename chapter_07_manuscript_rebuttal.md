# Ch.7 — 원고와 rebuttal에서 AI는 claim을 고친다

원고 작업에서 AI가 가장 쉽게 하는 일은 문장을 매끄럽게 만드는 것이다. 그
일은 마지막에 필요하다. 먼저 필요한 것은 claim 수리다. reviewer가 공격하는
지점은 대개 주장 권한이다.

```text
claim
-> evidence
-> assumption
-> limitation
-> reviewer risk
-> revised wording
```

이 순서가 바뀌면 문장은 좋아지고 논문은 약해진다.

## Claim inventory

원고 한 절을 고칠 때 AI에게 먼저 시킬 일은 claim inventory다.

| 항목 | 질문 |
|---|---|
| Central claim | 이 문단이 독자에게 믿게 하려는 말은 무엇인가 |
| Evidence | 그 말을 지탱하는 artifact, table, figure, theorem, ablation은 무엇인가 |
| Assumption | 어떤 dataset, sensor, metric, runtime 조건에 기대는가 |
| Scope | 어느 조건까지만 말할 수 있는가 |
| Risk | reviewer가 어디를 공격할 수 있는가 |
| Wording | 허용되는 표현과 금지되는 표현은 무엇인가 |

이 표가 없으면 AI는 stronger adjective를 넣는다. "robust", "general",
"significant" 같은 단어는 evidence가 올린 뒤에만 쓴다.

## Reviewer pressure를 action으로 바꾼다

좋은 rebuttal 초안은 공손한 문장으로 시작하지 않는다. reviewer pressure를
작업 단위로 바꾼다.

```text
reviewer pressure:
claim at risk:
missing evidence:
possible response:
required edit:
remaining limitation:
```

예를 들어 reviewer가 "comparison이 unfair하다"고 했다면 바로 "We thank the
reviewer"를 쓰지 않는다. 먼저 baseline protocol, dataset split, metric
definition, implementation status를 확인한다. 새 실험이 필요하면 실험으로
분리한다. 설명 부족이면 method clarification으로 분리한다. 실제 limitation이면
scope를 줄인다.

## AI가 잘하는 원고 일

AI는 다음 일을 잘한다.

- reviewer comment를 claim risk로 분해한다.
- 한 절 안에서 claim hierarchy를 정리한다.
- figure caption과 본문 claim을 맞춘다.
- 용어와 notation의 불일치를 찾는다.
- rebuttal 문장을 concession, evidence, revision, limitation으로 나눈다.

이 일들은 모두 구조 작업이다. 문체 작업은 구조가 맞은 뒤에 들어간다.

## AI가 자주 실패하는 원고 일

실패는 대체로 네 가지다.

| 실패 | 증상 | 하네스 gate |
|---|---|---|
| Overclaim | 실험보다 넓은 contribution을 쓴다 | allowed wording / forbidden wording |
| Citation patching | 관련 논문을 더 붙여 novelty를 만든다 | repaired assumption / prior-work contrast |
| Polish first | 문장은 좋아졌지만 reviewer 질문이 남는다 | claim/evidence map |
| Metric blur | 다른 protocol의 숫자를 한 표정으로 말한다 | experiment contract |

AI는 "더 설득력 있게"라는 요청을 받으면 문장을 키운다. 연구 하네스는 "어떤
증거가 있으면 어디까지 커질 수 있는가"를 먼저 묻는다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| Reviewer comment | pressure를 claim at risk와 missing evidence로 바꿨다 | 공손한 문장부터 만들었다 | reviewer risk는 예의보다 주장 권한에서 줄어든다 |
| 원고 polish | claim inventory 뒤에 문장을 고쳤다 | fluent paragraph를 먼저 만들었다 | 매끈한 문장은 열린 claim을 가릴 수 있다 |
| Citation 보강 | prior work와 assumption 차이를 분리했다 | 관련 논문을 더 붙여 novelty를 만들었다 | citation은 근거를 보태지만 실험 경계를 대신 닫지 못한다 |
| Scope 조정 | allowed wording과 forbidden wording을 나눴다 | robust, general, significant 같은 단어를 먼저 넣었다 | 형용사는 evidence tier보다 넓어지기 쉽다 |

## Rebuttal sentence pattern

rebuttal 문장은 네 조각으로 충분하다.

```text
concession:
evidence or new analysis:
manuscript revision:
remaining boundary:
```

예시는 이런 모양이다.

```text
We agree that the previous wording did not make the evaluation boundary clear.
We now report the result under the same sequence split and metric script as the
baseline. Section 4.3 and Table 2 have been revised to state this protocol
explicitly. The claim is limited to this setting and we do not claim
cross-dataset generalization.
```

공손함은 필요하다. 그러나 공손함만으로 reviewer risk가 줄지는 않는다.
rebuttal은 claim/evidence ledger를 reviewer에게 보이는 문장으로 바꾸는
작업이다.
