# Ch.1 — AI가 잘하는 일과 자주 틀리는 일

AI는 먼저 확인 대상을 만든다. 에러 원인, 읽을 파일, 실험 조건, 원고 문장처럼 실제 작업 전에 좁혀 볼 목록을 빠르게 만든다. 그 설명이 맞는지는 repo, 실행 결과, dataset, metric, 원고 주장을 보고 판단한다.

로봇/CV 연구 대화에서 나온 사용자 입력 27,759개를 분류하면 장점과 실패가 함께 보인다. AI는 큰 repo를 훑고, 긴 log를 나누고, 논문 문장과 code path를 맞춰 보는 데 도움을 줬다. 반복 실패도 뚜렷했다. 현재 실행 상태를 보지 않은 단정, 파일 존재를 실제 사용으로 보는 착각, 조건이 다른 숫자의 비교였다.

## 잘하는 일

AI는 눈앞의 텍스트와 파일을 빠르게 훑는다. 연구자가 좁혀야 할 범위를 줄여 준다.

| 잘하는 일 | 연구에서의 쓰임 |
|---|---|
| 확인 대상 생성 | 에러 로그에서 확인할 원인을 여러 개 뽑는다 |
| 탐색 보조 | 파일, 함수, config, figure, table 위치를 찾는다 |
| 구조 정리 | 긴 log나 reviewer comment를 단계별로 나눈다 |
| 초안 작성 | rebuttal, README, command 설명의 첫 문장을 만든다 |
| 비교 정리 | 여러 repo, paper, 실험 조건의 차이를 표로 놓는다 |

확인 대상을 만드는 단계는 비용이 낮다. 틀린 설명이 섞여도 바로 실행하기 전까지는 연구 상태가 그대로다.

## 자주 틀리는 일

AI 답변은 확인할 후보를 준다. 현재 process가 살아 있는지, config가 runtime에서 읽혔는지, metric script가 같은 조건을 썼는지, reviewer가 공격한 주장에 답할 만큼 근거가 있는지는 파일과 실행 결과를 봐야 한다.

| 자주 틀리는 일 | 왜 문제가 되는가 |
|---|---|
| 보지 않은 현재 상태 확정 | 파일명, memory, 요약만으로 최신 repo나 runtime을 단정한다 |
| 코드 존재와 실행 사용 혼동 | source에 있는 module을 active method로 착각한다 |
| 숫자와 주장 거리 조절 실패 | metric 하나를 방법 개선이나 generalization 주장으로 올린다 |
| 실패 단계 혼합 | retrieval, geometry, optimization, evaluation 실패를 한 원인으로 합친다 |
| 위험 비용 무시 | 시간, compute, reviewer trust, 원고 주장 범위는 사람이 감당한다 |

AI가 내놓은 설명이 실행으로 넘어가는 순간부터 비용이 생긴다. 이 구분을 놓치면 연구자는 빠른 답을 얻고도 같은 일을 다시 확인한다.

## 왜 이런 일이 생기는가

반복 실패는 대체로 작업을 나누는 방식에서 나온다. AI는 대화와 파일 일부를 보고 다음 후보 설명을 만든다. 로보틱스/CV 연구의 상태는 대화 밖에서 바뀐다. Docker container, ROS2 topic, CUDA process, dataset split, calibration file, metric script, TeX table은 실제 파일과 실행 결과로 확인한다.

AI는 텍스트를 빠르게 훑고 나누는 데 강하다. 연구자는 실행과 증거를 확인한다. 이 둘을 섞으면 같은 오류가 반복된다.

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

[Anthropic의 2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 실제 세션에서 사람과 agent가 어떤 결정을 맡았는지 집계했다. 보고서는 사용자가 planning decision의 약 70%를, Claude가 execution decision의 약 80%를 맡는다고 분석했다. 사용자의 전문성은 문제 세팅, 검증 대상 지정, 잘못된 실행 방향 수정에서 드러났다. 연구 작업에서도 이 역할이 커진다.

| 사용자가 가져오는 것 | 연구 작업에서의 의미 |
|---|---|
| 구체적 문제 세팅 | dataset, split, code path, metric, reviewer concern을 정확히 지목한다 |
| 검증 지점 지정 | 어느 config가 runtime에서 읽혔는지 보여 달라고 묻는다 |
| 오류 수정 방향 | AI가 제안한 원인 중 틀린 stage를 사용자가 걷어낸다 |

## 확인할 다섯 줄

AI를 잘 쓰려면 먼저 일을 나눈다.

```text
AI가 만든 설명:
실제로 본 파일:
실행한 명령:
나온 결과:
그 결과로 말할 수 있는 범위:
```

이 다섯 줄이 있으면 AI의 빠른 탐색을 연구 작업으로 옮길 수 있다. 없으면 답변은 그럴듯해도 다음 세션에서 다시 같은 질문으로 돌아간다. 그 다음 문제는 `실제로 본 파일`과 `나온 결과`를 어디에서 복원할지다.
