# Ch.4 — 논문, 코드, 실험 매핑

## 목적

논문 요약을 실제 실행 경로와 연결한다. 논문에 적힌 method, 공개 코드, 내가 돌릴 실험을 분리해서
확인한다.

## 근거

논문 method는 주장이고, 공개 코드는 구현물이며, runtime은 별도의 상태다. computational
reproducibility 논의가 반복해서 가리키는 지점도 여기에 있다. 논문에 적힌 component가 repo에 있어도
그 component가 config를 통해 실행되고 결과 artifact에 영향을 줬는지는 따로 확인해야 한다.

그래서 이 장은 paper claim, code path, runtime path, experiment command를 한 줄로 합치지 않는다.
논문을 잘 읽는다는 말은 abstract를 요약하는 것이 아니라, claim이 어떤 코드와 실험 조건에 기대는지
찾는다는 뜻이다.

## 필요한 산출물

```text
paper claim:
code path:
runtime path:
experiment command:
metric script:
allowed comparison:
```

## 확인할 질문

| 질문 | 이유 |
|---|---|
| 논문 claim이 어느 table, figure, section에 있는가 | 원고 주장 범위를 확인한다. |
| 공개 코드에서 해당 모듈이 어디 있는가 | 코드 존재 여부를 확인한다. |
| 그 모듈이 실제 예제에서 호출되는가 | 실행 경로를 확인한다. |
| config key가 runtime에 읽히는가 | configured-unused 상태를 막는다. |
| 논문 표의 숫자를 만든 script가 공개되어 있는가 | 재현 가능성을 확인한다. |
| issue나 commit에서 convention이 바뀌었는가 | 현재 branch의 의미를 확인한다. |

## 구현 상태 라벨

코드에 존재한다는 말은 충분하지 않다. 다음 라벨 중 하나를 붙인다.

| 라벨 | 의미 |
|---|---|
| active | runtime에서 호출되고 결과에 영향을 준다 |
| disabled | 구현되어 있으나 꺼져 있다 |
| configured-unused | config에는 있으나 실행 경로에서 읽히지 않는다 |
| planned-only | 문서나 issue에만 있다 |
| tested-failed | 시도했으나 실패 기록이 있다 |
| dead | 남아 있으나 현재 경로에서 쓰이지 않는다 |
| unknown | 아직 확인하지 않았다 |

## AI에게 맡기기 좋은 일

- paper에서 method component 추출
- repo에서 관련 function, class, config 검색
- issue thread와 README의 convention 변화 수집
- paper-code 후보 연결 생성

## 사람이 닫아야 할 일

- 실제 호출 여부
- config가 runtime에 도달하는지
- 같은 dataset, split, metric 조건인지
- 내 원고 claim으로 올릴 수 있는 범위

논문 읽기는 abstract에서 끝나지 않는다. YAML, launch command, issue comment, failed sequence,
table caption까지 내려가야 한다.
