# 부록 C — 예시 작업장

`examples/first-robotics-workspace/`는 quickstart를 따라 만든 작은 공개 예시다.
실제 연구 파일, 개인 경로, 원 대화는 들어 있지 않다. 새 사용자는 이 예시를
보고 자기 workspace에 맞게 이름과 경로를 바꾸어 쓴다. 핵심은 순서가 아니라
AI가 다시 읽을 수 있는 연구 상태의 표면이다.

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
| [`project-memory.json`](examples/first-robotics-workspace/project-memory.json) | 현재 truth, source of truth, evidence boundary, 연구 루프, 다음 행동 |
| [`first-ai-session-message.txt`](examples/first-robotics-workspace/notes/first-ai-session-message.txt) | AI 세션에 바로 붙일 수 있는 메시지 |
| [`codex-porting-checklist.md`](examples/first-robotics-workspace/notes/codex-porting-checklist.md) | Claude/Cursor 중심 규칙을 Codex-first 규칙으로 옮기는 방식 |
| [`first-ai-session-prompt.md`](examples/first-robotics-workspace/notes/first-ai-session-prompt.md) | AI 세션에 그대로 붙이는 읽기 순서와 evidence gate |
| [`first-day-workspace-checklist.md`](examples/first-robotics-workspace/notes/first-day-workspace-checklist.md) | source of truth와 작은 action 경계 |
| [`paper-code-experiment-map.md`](examples/first-robotics-workspace/notes/paper-code-experiment-map.md) | 논문 읽기를 code path와 experiment protocol로 연결 |
| [`experiment-contract.md`](examples/first-robotics-workspace/notes/experiment-contract.md) | 숫자를 claim으로 올리기 전 필요한 protocol |
| [`stage-local-debugging.md`](examples/first-robotics-workspace/notes/stage-local-debugging.md) | ROS2 topic 문제를 stage-local check로 좁히는 방식 |
| [`weekly-research-ledger.md`](examples/first-robotics-workspace/notes/weekly-research-ledger.md) | 한 주의 claim, protocol, risk, next action |

## 예시에서 배울 경계

이 예시는 AI가 어디서 시작해야 하는지 알 수 있을 만큼만 채운 상태다.

```text
current evidence permits:
current evidence forbids:
next smallest action:
```

세 줄이 있으면 AI는 연구 상태 안에서 움직인다. 세 줄이 없으면 AI는 일반적인
조언으로 돌아간다.
