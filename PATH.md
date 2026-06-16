# 부록 D — 작업 리듬을 남기는 법

이 부록은 AI 사용의 기본 그림을 이해한 뒤 작업 기록을 남기는 방법을 정리한다.
본문의 중심 구조는 시간표가 아니다. AI가 만든 후보를 어떤 증거와 행동으로
좁힐지 이해한 다음, 그 판단을 다음 세션에 남기기 위해 이 리듬을 쓴다.

## 상태 복원

목표는 AI가 같은 출발점에서 작업하게 만드는 것이다.

완료 조건:

- `AGENTS.md`가 있다.
- `project-memory.json`에 현재 truth와 durable constraint가 있다.
- 공개/비공개 경계가 적혀 있다.
- 첫 research loop를 하나만 선택했다.
- 다음 AI 요청이 evidence gate를 요구한다.

처음 허용되는 claim은 작다.

```text
workspace can be resumed
first research loop is selected
next smallest action is known
```

아직 허용되지 않는 claim도 분명하다.

```text
method works
experiment improved
reviewer risk is resolved
```

## 하나의 루프를 artifact까지 보낸다

한 번에는 하나의 loop를 artifact까지 보낸다. 논문 읽기라면
paper-code-experiment map이 남아야 한다. 실험이라면 experiment contract와
result provenance tuple이 남아야 한다. 디버깅이라면 stage-local sheet에
command output이 붙어야 한다.

기본 루프는 다음 중 하나다.

| 시작점 | 남길 것 | 닫히는 gate |
|---|---|---|
| 논문 한 편 | `paper-code-experiment-map.md` | claim, code path, protocol 후보 |
| dataset 확인 | `dataset-archaeology-sheet.md` | split, count, frame, convention |
| 실험 숫자 | `experiment-contract.md`, `result-provenance-tuple.md` | protocol-bound result |
| runtime 문제 | `stage-local-debugging.md` | tool/runtime/data/method failure 분리 |
| 원고 문장 | `claim-evidence-map.md` | allowed wording, blocked wording |

좋은 상태는 다음 AI가 같은 실험 숫자를 보고 같은 질문을
먼저 묻는 상태다.

```text
Which dataset?
Which split?
Which direction?
Which metric script?
Which baseline?
Which artifact?
```

## 반복 실패를 replay로 바꾼다

반복되는 실수는 replay로 바꾼다. 같은 correction을 두 번 이상 했다면
memory를 지나 `replay-case.md`로 승격한다.

쌓을 durable surface:

- project memory
- weekly ledger
- experiment contract 목록
- result provenance tuple 목록
- claim/evidence map
- replay case
- public/private boundary update

이 단계에서 외부 agent repo도 다시 읽는다. coding discipline은
`AGENTS.md`로 옮기고, course repo는 학습 자료의 구성 방식만 참고하며,
awesome list는 도구 discovery에만 쓴다. 로보틱스 연구 하네스에는 dataset,
metric, artifact, claim, reviewer risk를 더한다.

## 운영 리듬

매주 마지막에는 세 줄을 닫는다.

```text
current truth:
blocked claim:
next smallest action:
```

이 세 줄을 남기면 다음 세션은 바로 이어진다. 없으면 다음 세션은 다시
요약부터 시작한다.

## 중단 기준

AI가 계속 답을 만들 수 있어도 연구는 멈춰야 할 때가 있다.

- 같은 stage에서 evidence가 늘지 않는다.
- tool failure와 method failure가 분리되지 않는다.
- protocol이 바뀌었는데 숫자를 비교하려 한다.
- reviewer risk가 남았는데 문장 polish만 반복한다.
- private material이 공개 문서로 넘어갈 위험이 있다.

중단 조건을 ledger에 남기면 다음 action이 더 작아진다.
