# Ch.2 — 연구 상태 복원

## 목적

이전 대화나 오래된 작업을 이어서 할 때 현재 연구 상태를 복원한다. 복원의 목표는 요약문 작성이
아니다. 다음 행동이 의존할 source of truth를 정하는 것이다.

## 연구 상태를 이루는 항목

로보틱스/CV 연구 상태는 여러 파일과 artifact에 분산된다.

| 항목 | 예 |
|---|---|
| 코드 상태 | branch, commit, modified file, launch file, config |
| 실행 상태 | command, workdir, container, device 권한, environment variable |
| 데이터 상태 | dataset version, split, sequence, calibration, bag |
| 결과 상태 | result table, metric output, plot, failed run |
| 원고 상태 | TeX diff, figure source, claim/evidence map, reviewer memo |
| 기억 상태 | project memory, handoff note, previous summary |

## 증거 등급

모든 항목을 같은 무게로 다루지 않는다.

| 등급 | 예 | 허용되는 말 |
|---|---|---|
| 원본 파일 | source code, config, TeX, CSV | 파일 안에서 관찰한 내용 |
| 실행 출력 | command output, log, generated artifact | 해당 실행의 결과 |
| 요약 | handoff, compact summary, memory note | 다음에 확인할 위치 |
| 추론 | AI explanation, suspected cause | 확인해야 할 후보 |

## 복원 절차

1. repo의 현재 파일 상태를 본다.
2. README, AGENTS, project memory가 있으면 먼저 읽는다.
3. 최근 결과 폴더와 실행 로그를 확인한다.
4. 원고 작업이면 claim이 걸린 table, figure, paragraph를 찾는다.
5. 요약과 원본이 충돌하면 원본을 우선한다.
6. 다음 행동 하나만 정한다.

## 공개/비공개 경계

공개 문서에는 raw transcript, 개인 경로, reviewer 원문, 미공개 숫자, 인증 정보가 들어가면
안 된다. 공개할 수 있는 것은 반복된 실패 구조, 일반화된 운영 규칙, sanitized template이다.

## Claude 자료를 Codex로 옮길 때

옮길 것은 수행자 이름이 아니라 행동 규칙이다.

- 처음 읽을 파일의 순서
- 수정 가능한 범위
- 실행 전에 밝혀야 할 가정
- 완료를 말할 수 있는 증거
- 공개 문서에 남기면 안 되는 항목

특정 slash command, permission allowlist, UI 전제는 그대로 옮기지 않는다.
