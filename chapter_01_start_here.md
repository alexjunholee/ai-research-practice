# Ch.1 — AI 답변은 후보로 둔다

AI를 이용하면 오류 원인, 읽을 파일, 실험 조건, 고칠 문장처럼 먼저 확인할 대상을 빠르게 추릴 수 있다. 그 설명이 맞는지는 저장소와 실행 결과, 데이터셋, 평가지표, 원고의 주장을 대조해 판단한다.

우리 연구실에서 로보틱스 연구 대화의 사용자 입력 27,759개를 직접 분류해 보니 장점과 반복되는 실패가 함께 드러났다. 이 수는 내부 작업 기록을 돌아본 운영 감사의 규모이며, 다른 연구실이나 제품 사용자를 대표하는 표본 통계는 아니다. AI는 큰 저장소를 훑고 긴 로그를 나누며 논문 문장과 코드 경로를 맞춰 보는 데 도움이 됐다. 반면 현재 실행 상태를 보지 않은 채 원인을 단정하거나, 파일이 존재한다는 사실을 실제로 사용된다는 뜻으로 해석하는 일이 잦았다. 조건이 다른 수치를 비교하고 서로 다른 실패 단계를 한데 묶는 일도 뒤를 이었다. 실험 비용이나 심사 위험을 고려하지 않은 채 원고의 주장을 확대하는 경우는 적었지만, 한 번 발생했을 때의 부담은 컸다.

## 잘하는 일

AI는 주어진 텍스트와 파일을 빠르게 훑어 연구자가 직접 확인할 범위를 줄여 준다.

| 잘하는 일 | 연구에서의 쓰임 |
|---|---|
| 확인 대상 생성 | 에러 로그에서 확인할 원인을 여러 개 뽑는다 |
| 탐색 보조 | 파일, 함수, config, figure, table 위치를 찾는다 |
| 구조 정리 | 긴 log나 reviewer comment를 단계별로 나눈다 |
| 초안 작성 | rebuttal, README, command 설명의 첫 문장을 만든다 |
| 비교 정리 | 여러 repo, paper, 실험 조건의 차이를 표로 놓는다 |

확인 대상을 만드는 단계의 비용은 낮다. 틀린 설명이 섞여 있어도 이를 실행에 옮기기 전까지는 연구 상태가 바뀌지 않는다.

## 자주 틀리는 일

AI 답변은 확인할 후보를 제시한다. 현재 프로세스가 실행 중인지, config가 runtime에서 읽혔는지, metric script가 같은 조건을 썼는지, 심사자가 지적한 주장에 답할 만큼 근거가 있는지는 파일과 실행 결과로 확인해야 한다.

| 자주 틀리는 일 | 왜 문제가 되는가 |
|---|---|
| 보지 않은 현재 상태 확정 | 파일명, memory, 요약만으로 최신 repo나 runtime을 단정한다 |
| 코드 존재와 실행 사용 혼동 | source에 있는 module을 active method로 착각한다 |
| 숫자에서 주장으로의 과도한 확대 | metric 하나를 방법 개선이나 generalization 주장으로 올린다 |
| 실패 단계 혼합 | data loading, matching, optimization, evaluation 실패를 한 원인으로 합친다 |
| 위험 비용 무시 | 시간, compute, reviewer trust, 원고 주장 범위는 사람이 감당한다 |

제안받은 설명을 실제로 실행하는 순간부터 시간과 계산 자원이 든다. 후보와 확인된 원인을 구분하지 않으면 빠르게 답을 얻고도 같은 일을 다시 조사하게 된다.

## 왜 이런 일이 생기는가

반복되는 실패의 상당수는 작업을 나누는 방식에서 생긴다. AI는 대화와 일부 파일을 바탕으로 다음 설명을 제안하지만, 로보틱스 연구의 상태는 대화 밖에서도 계속 바뀐다. Docker container, ROS2 topic, CUDA process, dataset split, calibration file, metric script, TeX table의 현재 상태는 실제 파일과 실행 결과로 확인해야 한다.

AI에는 텍스트를 훑고 분류하는 일을 맡기고, 연구자는 실행 상태와 증거를 확인한다. 두 역할을 구분하지 않으면 같은 오류가 반복된다.

| 섞인 것 | 반복되는 오류 |
|---|---|
| 설명과 원인 | 그럴듯한 설명을 root cause로 쓴다 |
| 코드와 방법 | 구현되어 있는 코드를 논문 방법으로 쓴다 |
| 숫자와 주장 | 조건이 다른 숫자를 성능 주장으로 쓴다 |
| 문장과 답변 | reviewer가 요구한 실험 없이 rebuttal 문장만 고친다 |
| 요약과 증거 | handoff나 memory를 source로 쓴다 |

이 구분은 AI 도구에서 처음 생긴 문제가 아니다.

[Suchman의 *Plans and Situated Actions*](https://www.lancaster.ac.uk/humanities-arts-and-social-sciences/people/lucy-suchman)는 Xerox PARC에서 사람들이 복사기를 쓰는 장면에서 출발했다. 시스템이 예상한 절차와 사용자가 실제로 마주한 상황은 자주 어긋났다. 계획은 현장에서 다시 읽히고 고쳐 쓰였다. 연구에서도 prompt와 plan은 확인 지시서에 가깝다. `ros2 topic info`, CSV, TeX diff, rebuttal table 같은 자료를 보고 나서야 실제 행동을 판단할 수 있다.

[Hutchins의 *Cognition in the Wild*](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)는 해군 함정의 항법을 따라갔다. chart, 도구, 절차, 팀의 말 주고받기가 함께 항로를 만든다. 연구실의 판단도 repo, launch file, dataset, terminal output, paper table, 기억 노트에 흩어져 있다. AI가 말한 연결이 그럴듯해도, 이 자료들을 다시 대조해야 연구 상태를 판단할 수 있다.

[Bainbridge의 *Ironies of Automation*](https://doi.org/10.1016/0005-1098(83)90046-8)은 자동화 뒤에 operator에게 감시와 비정상 상황 개입이 남는다고 썼다. [Parasuraman & Riley](https://doi.org/10.1518/001872097778543886)는 use, misuse, disuse, abuse를 나누고, 신뢰와 workload가 자동화 사용을 바꾼다고 정리했다. AI가 후보 설명을 빨리 만들수록 연구자는 어느 설명을 실행할지, 어떤 숫자를 원고에 올릴지, reviewer에게 어디까지 말할지 판단해야 한다.

[Anthropic의 2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 2025년 10월부터 2026년 4월까지 약 40만 개 세션을 분석해 사람과 agent가 어떤 결정을 맡았는지 집계했다. 이 표본에서 사용자는 planning decision의 약 70%를, Claude는 execution decision의 약 80%를 맡았다. 사용자의 전문성은 문제 세팅, 검증 대상 지정, 잘못된 실행 방향 수정에서 드러났다. 이 수치를 모든 연구 작업의 고정 비율로 옮기기보다 역할 분담을 점검하는 관찰로 쓴다.

| 사용자가 가져오는 것 | 연구 작업에서의 의미 |
|---|---|
| 구체적 문제 세팅 | dataset, split, code path, metric, reviewer concern을 정확히 지목한다 |
| 검증 지점 지정 | 어느 config가 runtime에서 읽혔는지 보여 달라고 묻는다 |
| 오류 수정 방향 | AI가 제안한 원인 중 틀린 stage를 사용자가 걷어낸다 |

## 확인할 다섯 줄

AI를 연구에 쓰려면 설명과 확인 결과를 먼저 나눈다.

```text
AI가 만든 설명:
실제로 본 파일:
실행한 명령:
나온 결과:
그 결과로 말할 수 있는 범위:
```

이 다섯 줄이 있으면 AI의 빠른 탐색을 확인 가능한 연구 작업으로 옮길 수 있다. 이 기록이 없으면 답변은 그럴듯해도 다음 세션에서 같은 질문으로 되돌아가기 쉽다. 그다음에는 `실제로 본 파일`과 `나온 결과`를 어디에서 복원할지 정해야 한다.
