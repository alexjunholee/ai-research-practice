# 부록 D — 작업 흐름을 남기는 법

AI와 연구할 때는 다음 세션이 같은 상태에서 시작할 만큼만 기록하면 된다. 파일, 명령, 숫자, 원고 문장이 어디에서 왔는지를 남긴다.

## 다시 시작할 때 필요한 것

- `AGENTS.md`
- 현재 상태와 계속 적용할 사용자 교정 사항을 적은 프로젝트 기억 기록
- 공개/비공개 경계
- 지금 이어갈 작업 하나
- 다음 AI 요청에서 확인해야 할 항목

처음에 말할 수 있는 것은 여기까지다.

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

한 번에는 하나의 작업만 결과물로 남긴다. 논문 읽기라면 주장, 코드 경로, 실험 조건 표가 그 결과물이다. 시작점이 달라지면 남길 파일과 확인할 항목도 달라진다.

| 시작점 | 남길 것 | 확인할 항목 |
|---|---|---|
| 논문 한 편 | `paper-code-experiment-map.md` | 주장, 코드 경로, 실험 조건 |
| 데이터셋 확인 | `dataset-archaeology-sheet.md` | split, count, frame, convention |
| 실험 숫자 | `experiment-contract.md`, `result-provenance-tuple.md` | 비교할 수 있는 조건 |
| 실행 중 문제 | `stage-local-debugging.md` | 도구/실행 환경/데이터/방법 실패 구분 |
| 원고 문장 | `claim-evidence-map.md` | 쓸 수 있는 문장과 보류할 문장 |

다음 AI 세션에서 같은 실험 숫자를 다시 보면 아래 질문부터 묻는다.

```text
Which dataset?
Which split?
Which direction?
Which metric script?
Which baseline?
Which output?
```

## 반복 실패를 다음 작업 전에 잡는다

같은 내용을 두 번 이상 바로잡았다면 프로젝트 기억 기록, 주간 기록, 실험 조건 목록, 결과 출처 기록, 주장·근거 표, 반복 확인 사례 중 하나에 남긴다.

외부 에이전트 저장소도 이 기준으로 본다. 코딩 규칙은 `AGENTS.md`로 옮긴다. 교육용 저장소에서는 학습 자료 구성만 참고한다. 도구 목록은 탐색에만 쓴다. 로보틱스 연구에는 데이터셋, 지표, 출력, 주장, 심사 위험을 더한다.

## 매주 남길 세 줄

```text
현재 확인한 사실:
아직 말하면 안 되는 주장:
다음 행동:
```

다음 세션에서는 이 세 줄을 읽고 확인된 사실에서 작업을 잇는다. 세 줄이 비어 있으면 연구 상태를 다시 세우는 일부터 한다.

## 멈출 때

AI가 계속 답할 수 있더라도 연구는 멈춰야 할 때가 있다.

- 같은 단계에서 근거가 그대로다.
- 도구 실패와 방법 실패가 섞여 있다.
- 실험 조건이 바뀌었는데 숫자를 비교하려 한다.
- 심사 위험이 남았는데 문장 다듬기만 반복한다.
- 비공개 자료가 공개 문서에 섞일 위험이 있다.

이 조건에서는 다음 행동을 어디까지 할지 좁혀 잡는다.
