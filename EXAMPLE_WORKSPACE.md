# 부록 C — 예시 작업 공간

`examples/first-robotics-workspace/`는 빠른 시작 절차에 따라 만든 작은 공개 예시로,
공개 가능한 파일 이름과 기록 단위만 담았다. 새 사용자는 자신의 작업 공간에 맞게
이름과 경로를 바꾸어 쓴다. 다음 세션에서 다시 읽을 수 있도록 연구 상태를 파일로
남기고 세션·하네스·샌드박스의 경계도 구분한다.

## 파일 구조

```text
examples/first-robotics-workspace/
├── AGENTS.md
├── README.md
├── project-memory.json
└── notes/
    ├── codex-porting-checklist.md
    ├── experiment-contract.md
    ├── first-ai-session-message.txt
    ├── first-ai-session-prompt.md
    ├── first-day-workspace-checklist.md
    ├── paper-code-experiment-map.md
    ├── stage-local-debugging.md
    └── weekly-research-ledger.md
```

## 파일별 역할

| 파일 | 역할 |
|---|---|
| [`AGENTS.md`](templates.html#examples-first-robotics-workspace-agents) | AI가 먼저 읽는 프로젝트 작업 규칙 |
| [`README.md`](templates.html#examples-first-robotics-workspace-readme) | 예시 폴더만 열었을 때의 시작 순서 |
| [`project-memory.json`](templates.html#examples-first-robotics-workspace-project-memory-json) | 현재 확인한 사실, 원본 파일, 근거 범위, 연구 루프, 다음 행동 |
| [`first-ai-session-message.txt`](templates.html#examples-first-robotics-workspace-notes-first-ai-session-message-txt) | AI 세션에 바로 넣는 메시지 |
| [`codex-porting-checklist.md`](templates.html#examples-first-robotics-workspace-notes-codex-porting-checklist) | Claude/Cursor 중심 규칙을 Codex 중심 규칙으로 옮기는 방식 |
| [`first-ai-session-prompt.md`](templates.html#examples-first-robotics-workspace-notes-first-ai-session-prompt) | AI 세션에 넣는 읽기 순서와 확인 기준 |
| [`first-day-workspace-checklist.md`](templates.html#examples-first-robotics-workspace-notes-first-day-workspace-checklist) | 원본 파일과 작은 행동의 범위 |
| [`paper-code-experiment-map.md`](templates.html#examples-first-robotics-workspace-notes-paper-code-experiment-map) | 논문 읽기를 코드 경로와 실험 절차로 연결 |
| [`experiment-contract.md`](templates.html#examples-first-robotics-workspace-notes-experiment-contract) | 숫자를 주장에 쓰기 전에 확인할 실험 절차 |
| [`stage-local-debugging.md`](templates.html#examples-first-robotics-workspace-notes-stage-local-debugging) | ROS2 토픽 문제를 단계별 점검으로 좁히는 방식 |
| [`weekly-research-ledger.md`](templates.html#examples-first-robotics-workspace-notes-weekly-research-ledger) | 한 주의 주장, 실험 절차, 위험, 다음 행동 |

## 예시에서 확인할 경계

이 예시에는 AI가 시작 지점을 찾는 데 필요한 내용만 채워 두었다.

```text
session record to update:
harness rule:
sandbox action:
current evidence permits:
current evidence forbids:
next smallest action:
```

이 여섯 줄을 남기면 AI는 다음 세션에서도 같은 연구 상태에서 시작하고, 남기지 않으면
일반적인 조언부터 되풀이한다.
