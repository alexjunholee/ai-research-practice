# Ch.2 — 현재 상태는 원 파일, 로그, 실행 결과에 있다

연구 상태를 이어받을 때는 원 파일, 로그, 실행 결과, 생성된 표와 figure부터 본다. 요약은 확인할 위치를 알려 주는 자료다.

[Endsley의 situation awareness 모델](https://doi.org/10.1518/001872095779049543)은 dynamic system에서 상황 인식을 세 단계로 나눈다. 현재 요소를 지각하고, 그 의미를 이해하고, 가까운 미래 상태를 예측하는 일이다. 연구 상태 복원도 이 순서를 따른다. 파일이 있는지 보는 것, 그 파일이 어떤 실행에서 나왔는지 이해하는 것, 그 결과로 어떤 말을 할 수 있는지 판단하는 것은 서로 다르다.

[Maynez et al. 2020](https://aclanthology.org/2020.acl-main.173/)은 abstractive summarization 출력이 자연스러워도 입력 문서와 맞지 않는 내용을 만들 수 있음을 보였다. [Ji et al. 2022](https://arxiv.org/abs/2202.03629)은 NLG hallucination을 원문이나 세계 지식과 어긋나는 생성으로 정리했다. 요약과 기억 기록은 방향을 잡는 자료다. 원 파일과 명령 출력은 다른 무게를 가진다.

## 증거의 무게

| 자료 | 예 | 말할 수 있는 범위 |
|---|---|---|
| 원 파일 | 소스 코드, config, TeX, CSV, log | 파일 안에서 직접 확인한 내용 |
| 실행 결과 | command output, generated figure, metric result | 해당 실행에서 나온 결과 |
| 조건을 확인한 결과 | dataset, split, metric, baseline을 확인한 숫자 | 같은 조건 안의 비교 |
| 요약 | handoff, compact summary, memory note | 다음에 확인할 위치 |
| AI 추정 | 원인 추정, 구조 해석, 요약 판단 | 확인해야 할 설명 |

요약만으로 논문 주장을 확정할 수는 없다. 명령 출력은 해당 실행의 결과를 말할 수 있다. dataset, split, metric을 확인하기 전에는 방법이 좋아졌다고 쓰지 않는다.

## 복원할 항목

로보틱스/CV 연구 상태는 여러 파일에 흩어져 있다.

| 상태 | 확인할 항목 |
|---|---|
| repo | branch, commit, modified file, build output |
| 실행 | process, container, device, environment, output path |
| 데이터 | dataset version, split, sequence, calibration |
| 결과 | metric output, plot, table, failed run |
| 원고 | TeX diff, figure 원본, table, paragraph |
| 기억 | project memory, handoff, durable correction |

## 복원 순서

1. 현재 repo와 공개/비공개 경계를 확인한다.
2. project memory나 handoff가 있으면 방향을 잡는 자료로 읽는다.
3. 원 파일을 찾는다.
4. 실행 결과가 필요한 경우 command와 output path를 확인한다.
5. 원고 작업이면 table, figure, paragraph를 함께 본다.
6. summary와 원 파일이 충돌하면 원 파일을 우선한다.
7. 다음 행동 하나만 정한다.

예를 들어 `final_results.csv`가 있어도 command와 config가 없으면 숫자가 있다는 말까지만 할 수 있다. 방법이 좋아졌다는 말에는 dataset, split, metric script, baseline 확인이 필요하다.

공개 문서에는 개인 대화 원문, 개인 경로, reviewer 원문, 미공개 숫자, 인증 정보가 들어가면 안 된다. 공개할 수 있는 것은 반복되는 실패 유형, 운영 규칙, 공개용 template이다.
