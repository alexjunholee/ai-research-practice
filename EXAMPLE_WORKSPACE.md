# 부록 C — 예시 workspace

`examples/first-robotics-workspace/`는 quickstart를 따라 만든 작은 공개 예시다.
공개할 수 있는 파일 이름과 기록 단위만 남겼다. 새 사용자는 이 예시를
보고 자기 workspace에 맞게 이름과 경로를 바꾸어 쓴다. 연구 상태는 다음 세션에서
다시 읽을 수 있게 파일로 남긴다. 예시는 session, harness, sandbox 경계도
함께 보여준다.

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

## 이 예시가 보여주는 것

| 파일 | 역할 |
|---|---|
| [`AGENTS.md`](examples/first-robotics-workspace/AGENTS.md) | AI가 먼저 읽는 project contract |
| [`README.md`](examples/first-robotics-workspace/README.md) | 예시 폴더만 열었을 때의 시작 순서 |
| [`project-memory.json`](examples/first-robotics-workspace/project-memory.json) | 현재 확인한 사실, 원 파일, 근거 범위, 연구 루프, 다음 행동 |
| [`first-ai-session-message.txt`](examples/first-robotics-workspace/notes/first-ai-session-message.txt) | AI 세션에 바로 넣는 메시지 |
| [`codex-porting-checklist.md`](examples/first-robotics-workspace/notes/codex-porting-checklist.md) | Claude/Cursor 중심 규칙을 Codex-first 규칙으로 옮기는 방식 |
| [`first-ai-session-prompt.md`](examples/first-robotics-workspace/notes/first-ai-session-prompt.md) | AI 세션에 넣는 읽기 순서와 확인 기준 |
| [`first-day-workspace-checklist.md`](examples/first-robotics-workspace/notes/first-day-workspace-checklist.md) | 원 파일과 작은 행동 경계 |
| [`paper-code-experiment-map.md`](examples/first-robotics-workspace/notes/paper-code-experiment-map.md) | 논문 읽기를 code path와 experiment protocol로 연결 |
| [`experiment-contract.md`](examples/first-robotics-workspace/notes/experiment-contract.md) | 숫자를 주장으로 쓰기 전 필요한 protocol |
| [`stage-local-debugging.md`](examples/first-robotics-workspace/notes/stage-local-debugging.md) | ROS2 topic 문제를 stage-local check로 좁히는 방식 |
| [`weekly-research-ledger.md`](examples/first-robotics-workspace/notes/weekly-research-ledger.md) | 한 주의 주장, protocol, risk, next action |

## 예시에서 배울 경계

이 예시는 AI가 어디서 시작해야 하는지 알 수 있을 만큼만 채운 상태다.

```text
session record to update:
harness rule:
sandbox action:
current evidence permits:
current evidence forbids:
next smallest action:
```

이 여섯 줄이 있으면 AI는 같은 연구 상태에서 시작한다. 이 줄들이 없으면 AI는
일반적인 조언으로 돌아간다.
