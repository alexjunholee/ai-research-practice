# 부록 D — 작업 흐름을 남기는 법

AI와 연구할 때 기록은 길 필요가 없다. 다음 세션이 같은 상태에서 시작할 만큼만 남기면 된다. 파일, 명령, 숫자, 원고 문장이 어디에서 왔는지를 남긴다.

## 다시 시작할 때 필요한 것

- `AGENTS.md`
- 현재 상태와 durable correction을 적은 project memory
- 공개/비공개 경계
- 지금 이어갈 작업 하나
- 다음 AI 요청에서 확인해야 할 항목

처음 말할 수 있는 범위는 작다.

```text
workspace can be resumed
first research loop is selected
next small action is known
```

아직 말하면 안 되는 것도 적는다.

```text
method works
experiment improved
reviewer risk is resolved
```

## 하나의 작업을 결과물로 남긴다

한 번에는 하나의 작업만 결과물로 남긴다. 논문 읽기라면 주장, code path, 실험 조건 표가 남아야 한다. 실험이라면 조건과 결과 출처가 남아야 한다. 디버깅이라면 stage별 명령 출력이 남아야 한다.

| 시작점 | 남길 것 | 확인할 항목 |
|---|---|---|
| 논문 한 편 | `paper-code-experiment-map.md` | 주장, code path, 실험 조건 |
| dataset 확인 | `dataset-archaeology-sheet.md` | split, count, frame, convention |
| 실험 숫자 | `experiment-contract.md`, `result-provenance-tuple.md` | 비교할 수 있는 조건 |
| runtime 문제 | `stage-local-debugging.md` | tool/runtime/data/method failure 구분 |
| 원고 문장 | `claim-evidence-map.md` | 쓸 수 있는 문장과 보류할 문장 |

다음 AI가 같은 실험 숫자를 보고 아래 질문부터 묻는 상태가 좋다.

```text
Which dataset?
Which split?
Which direction?
Which metric script?
Which baseline?
Which output?
```

## 반복 실패를 다음 작업 전에 잡는다

같은 correction을 두 번 이상 했다면 project memory, 주간 기록, 실험 조건 목록, 결과 출처 기록, 주장·근거 표, 반복 확인 사례 중 하나에 남긴다.

외부 agent repo도 이 기준으로 본다. coding discipline은 `AGENTS.md`로 옮기고, course repo는 학습 자료 구성만 참고하며, awesome list는 도구 발견에만 쓴다. 로보틱스 연구에는 dataset, metric, output, 주장, reviewer risk를 더한다.

## 매주 남길 세 줄

```text
현재 확인한 사실:
아직 말하면 안 되는 주장:
다음 행동:
```

이 세 줄이 있으면 다음 세션은 바로 이어진다. 없으면 다음 세션은 다시 요약부터 시작한다.

## 멈출 때

AI가 계속 답을 만들 수 있어도 연구는 멈춰야 할 때가 있다.

- 같은 stage에서 근거가 그대로다.
- tool failure와 method failure가 섞여 있다.
- 실험 조건이 바뀌었는데 숫자를 비교하려 한다.
- reviewer risk가 남았는데 문장 다듬기만 반복한다.
- private material이 공개 문서에 섞일 위험이 있다.

중단 조건을 남기면 다음 행동이 작아진다.
