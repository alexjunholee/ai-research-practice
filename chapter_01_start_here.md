# Ch.1 — AI 출력과 실행 경계

## 목적

AI가 낸 답을 연구 행동으로 옮기기 전에 확인할 경계를 정한다.
AI 출력은 후보이고, 연구 상태를 바꾸는 일은 실행이다. 후보를 실행으로 옮길 때는 대상 파일,
명령, 산출물, claim 범위를 먼저 정한다.

## 적용 상황

- ROS2, Docker, CUDA, dataset path 문제를 디버깅할 때
- 논문 코드에서 실제 실행 경로를 찾을 때
- 실험 숫자를 원고 문장으로 옮길 때
- reviewer comment에 답변할 때
- 이전 대화 요약을 이어서 작업할 때

## AI가 잘하는 일

- 로그에서 가능한 원인 후보를 빠르게 나열한다.
- 읽을 파일, 명령, 설정 후보를 좁힌다.
- reviewer comment를 실험, 설명, 한계 항목으로 분류한다.
- 긴 대화나 문서를 다음에 볼 항목으로 요약한다.

## 자주 생기는 실패

| 실패 | 설명 |
|---|---|
| 후보를 원인으로 취급 | QoS, namespace, Docker 권한 같은 후보가 확인 없이 원인이 된다. |
| 요약을 원문으로 취급 | compact summary나 handoff note가 source file을 대신한다. |
| 좁은 성공을 전체 성공으로 취급 | build pass, 일부 trajectory, plot 생성이 runtime 또는 실험 성공으로 올라간다. |
| 숫자를 claim으로 취급 | split, frame, metric script 확인 없이 성능 문장이 나온다. |
| 코드 존재를 실행 증거로 취급 | source에 factor나 config key가 있어도 runtime에서 쓰이지 않을 수 있다. |

## 실행 전 확인

AI 답변을 받은 뒤 바로 파일을 고치지 않는다. 먼저 아래 네 항목을 적는다.

```text
observed evidence:
candidate action:
expected artifact:
allowed claim after action:
```

예를 들어 subscriber callback이 비어 있으면 `observed evidence`는 topic list와
QoS 출력이다. `candidate action`은 launch 수정이나 QoS 변경이다. `expected artifact`는
수정 뒤의 callback log 또는 메시지 수신 기록이다. 이 기록이 없으면 수정 후에도 무엇이
달라졌는지 말하기 어렵다.

## 완료 기준

AI가 원인을 말한 것만으로 완료를 말하지 않는다. 완료 여부는 실행 뒤에 남은 artifact로 판단한다.

- 어떤 파일을 읽었는가
- 어떤 파일을 바꾸었는가
- 어떤 명령을 실행했는가
- 어떤 output path가 생겼는가
- 어떤 claim을 말할 수 있고, 어떤 claim은 아직 말할 수 없는가
