# 부록 C — 예시 작업 공간

앞선 부록 B의 절차를 실제로 채우면 어떤 모습이 되는지 살펴볼 수 있도록, `examples/first-robotics-workspace/`에 작은 공개 예시를 마련해 두었다. 여기에는 외부에 공개해도 무방한 파일과 기록 단위만 담았으므로, 처음 작업 공간을 꾸릴 때는 이 구조를 바탕으로 프로젝트 이름과 실제 경로만 바꿔 쓰면 된다. 특히 다음 세션을 열었을 때도 이전 연구 상태를 곧바로 되짚을 수 있도록 현재 확인한 사실을 파일에 남기고, 세션·하네스·샌드박스의 경계 역시 문서 안에서 분명하게 가르고 있다.

## 예시 작업 공간의 파일 구조

예시 폴더는 작업 공간 루트에 놓이는 핵심 기준 파일 세 개와, `notes/` 아래에 모인 여덟 개의 기록 양식으로 이루어져 있다. 전체 디렉터리 배치는 다음과 같다.

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

이 구성에서 루트의 세 파일은 세션의 시작점과 규칙·기억을 맡고, `notes/` 안의 문서들은 각 연구 단계에서 채워 넣을 구체적인 작업 기록을 담당한다.

## 각 파일이 맡는 일

실제 작업 공간에 파일을 옮길 때 어느 문서를 먼저 열고 어떤 내용을 적어야 하는지 헷갈리지 않도록, 예시 안의 열한 개 파일이 맡은 역할을 아래 표에 정리했다.

| 파일 | 역할 |
|---|---|
| [`AGENTS.md`](templates.html#examples-first-robotics-workspace-agents) | AI가 가장 먼저 읽는 프로젝트 작업 규칙 |
| [`README.md`](templates.html#examples-first-robotics-workspace-readme) | 예시 폴더만 열었을 때 따를 시작 순서 |
| [`project-memory.json`](templates.html#examples-first-robotics-workspace-project-memory-json) | 현재 확인한 사실, 원본 파일, 근거 범위, 연구 루프, 다음 행동 |
| [`first-ai-session-message.txt`](templates.html#examples-first-robotics-workspace-notes-first-ai-session-message-txt) | AI 세션에 바로 입력하는 메시지. 예시에서는 채운 결과를 한눈에 보이려고 `notes/`에 두었으며, 실제 자기 작업 공간에서는 부록 B의 안내대로 `artifacts/first-ai-session-message.txt`에 저장한다. |
| [`codex-porting-checklist.md`](templates.html#examples-first-robotics-workspace-notes-codex-porting-checklist) | Claude/Cursor 중심 규칙을 Codex 중심 규칙으로 옮기는 방법 |
| [`first-ai-session-prompt.md`](templates.html#examples-first-robotics-workspace-notes-first-ai-session-prompt) | AI 세션에서 지킬 읽기 순서와 확인 기준 |
| [`first-day-workspace-checklist.md`](templates.html#examples-first-robotics-workspace-notes-first-day-workspace-checklist) | 원본 파일과 작은 행동이 다루는 범위 |
| [`paper-code-experiment-map.md`](templates.html#examples-first-robotics-workspace-notes-paper-code-experiment-map) | 논문 읽기를 코드 경로와 실험 절차에 연결 |
| [`experiment-contract.md`](templates.html#examples-first-robotics-workspace-notes-experiment-contract) | 숫자를 주장에 쓰기 전에 확인할 실험 절차 |
| [`stage-local-debugging.md`](templates.html#examples-first-robotics-workspace-notes-stage-local-debugging) | ROS2 토픽 문제를 단계별 점검으로 좁혀 가는 방법 |
| [`weekly-research-ledger.md`](templates.html#examples-first-robotics-workspace-notes-weekly-research-ledger) | 한 주 동안의 주장, 실험 절차, 위험, 다음 행동 |

필요에 따라 위 파일들을 하나씩 열어 보면 빈 템플릿이 실제 로보틱스·CV 연구 맥락에서 어떻게 채워지는지 바로 가늠할 수 있다.

## 답변 전 점검과 세션 종료 기록

예시 작업 공간에는 AI가 성급한 결론을 내리지 않도록, 첫 답변을 출력하기 전에 반드시 짚고 넘어가야 하는 아홉 가지 점검 항목이 들어가 있다.

```text
session record to update:
harness rule that controls this action:
sandbox action allowed now:
sandbox action not allowed now:
object under truth control:
current evidence permits:
current evidence forbids:
smallest next action:
verification:
```

이 항목을 먼저 채우게 하면 AI가 막연하고 일반적인 조언을 늘어놓는 대신, 현재 연구 상태와 허용된 작업 범위 안에서만 다음 행동을 제안하게 된다. 그리고 한 세션을 마칠 때는 현재 확인한 사실, 아직 말하면 안 되는 주장, 다음 행동 하나를 기록에 남김으로써 다음 세션이 빈손으로 다시 시작하지 않게 한다.
