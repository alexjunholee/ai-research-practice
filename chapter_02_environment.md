# Ch.2 — AI에게 맡기기 전에 연구 상태를 복원한다

새 연구 환경의 첫날은 AI가 읽을 수 있는 작업장을 만드는 데 쓴다. 로보틱스
연구의 상태는 코드 repo, bag, calibration, Dockerfile, 실험 로그, 원고,
reviewer memo, 이전 correction으로 흩어져 있다. 이 상태를 복원하지 못한
AI는 빈칸을 문장으로 채운다.

작업장은 네 층으로 나누면 오래 간다.

```text
workspace/
├── AGENTS.md              # AI가 먼저 읽는 운영 규칙
├── repos/                 # code and paper repos
├── datasets/              # raw data, bag, sequences, indexes
├── artifacts/             # logs, tables, figures, checkpoints
├── notes/                 # paper notes, claim maps, ledgers
└── templates/             # reusable harness files
```

Dropbox, network drive, external SSD처럼 동기화가 끼는 환경에서는 git metadata
충돌 처리를 먼저 분리한다. 공개 가이드는 특정 사용자의 파일 구조를 강제하지
않는다. 원칙은 고정해 둔다. 코드 이력, dataset, artifact, private note의
수명주기를 섞지 않는다.

## AGENTS.md가 첫 진입점이다

Codex 기준의 진입점은 `AGENTS.md`다. Claude 중심 repo에서 쓰던 `CLAUDE.md`,
`.claude/skills`, Cursor rule도 내용 자체는 버릴 필요가 없다. 수행자 이름과
tool-specific command를 걷어내고 다음 항목을 `AGENTS.md`로 옮긴다.

- 이 프로젝트의 공개 산출물
- 로컬 전용 자료와 공개 금지 경계
- stage pipeline과 한 번에 수행할 수 있는 단계
- 실행 가능한 검증 명령
- destructive command와 credential 처리 규칙
- 반복된 사용자 correction
- AI가 evidence 없이 하면 안 되는 주장

`CLAUDE.md`에 있던 "assumption을 말하라", "작게 고쳐라", "검증 기준을
정하라" 같은 규칙은 Codex에서도 그대로 유효하다. `/plugin install`,
Claude-specific slash command, 특정 UI 동작은 버리고, 행동 원칙과 evidence
gate를 옮긴다.

## 현재 상태를 읽는 순서

AI에게 "여기서 뭐 하던 건지 파악해 봐"라고 맡길 때는 읽기 순서가 있어야
한다.

1. 상위 `AGENTS.md`와 repo 안의 `AGENTS.md`
2. `README.md`, `ROADMAP.md`, `project-memory.json` 같은 공개/운영 상태 파일
3. `notes/`, `templates/`, evidence map, ledger 같은 로컬 작업 문서
4. 실제 파일 목록과 최근 생성물
5. build script, test script, run script
6. 결과 artifact와 command output

대화 요약, compact summary, 이전 assistant 답변은 2차 자료다. 방향을 잡는 데
쓸 수는 있다. claim은 원 파일, artifact, 실행 결과, protocol이 닫을 때만
올라간다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| 첫 진입 | 상위 규칙, repo 규칙, 상태 파일, 실제 파일 목록을 차례로 읽었다 | 이전 요약을 현재 상태로 확정했다 | 요약은 방향을 주지만 생성물과 공개 경계를 증명하지 못한다 |
| Claude 규칙 이식 | 행동 원칙을 `AGENTS.md`와 template으로 옮겼다 | 파일명, slash command, 도구 이름을 그대로 복사했다 | 도구 이름은 실행 환경이 바뀌면 동작하지 않는다 |
| 공개 경계 | 원문 로그, private path, reviewer memo를 로컬 전용으로 묶었다 | 설명을 만들다가 개인 경로를 공개 원고에 섞었다 | AI는 경계가 없으면 문장의 자연스러움을 먼저 최적화한다 |
| 연구 상태 재개 | artifact와 command output을 다시 확인했다 | memory를 proof처럼 사용했다 | 연구 상태는 대화 안보다 파일과 실행 결과에 더 많이 남는다 |

## 공개와 비공개를 먼저 나눈다

연구용 AI 셋업에는 공개 가능한 지식과 공개하면 안 되는 상태가 함께
생긴다.

| 공개 가능 | 로컬 전용 |
|---|---|
| 일반화된 절차 | 비공개 대화 원문 |
| 빈 템플릿 | 개인 프로젝트 경로 |
| 공개 repo와 논문 링크 | reviewer 원문 |
| sanitized 예시 | 미공개 실험 결과 |
| 빌드된 가이드 | credential, token, machine path |

이 경계가 없으면 AI가 좋은 설명을 만들다가 private path를 그대로 공개
문서에 넣는다. 반대로 경계가 너무 엄격하면 로컬 경험에서 배운 규칙이
공개 지식으로 바뀌지 못한다. 공개로 옮길 수 있는 단위는 패턴이다.

## 첫날에 남길 세 파일

처음부터 거대한 하네스를 만들 필요는 없다. 세 파일이면 연구 상태가
흘러가기 시작한다.

```text
AGENTS.md
project-memory.json
weekly-research-ledger.md
```

`AGENTS.md`는 AI의 행동 규칙이다. `project-memory.json`은 반복 correction과
durable constraint를 담는다. 여기에 source_of_truth, tool_surface_map,
current_evidence, first_research_loop, next_smallest_actions가 있어야 다음 AI
세션이 memory를 proof로 착각하지 않는다. `weekly-research-ledger.md`는 이번
주에 닫힌 protocol, 아직 닫히지 않은 claim, 다음 smallest action을 적는다.

첫날의 성공 기준은 단순하다. 새 AI 세션이 와도 같은 private boundary를
지키고, 같은 현재 상태에서 시작하며, 같은 검증 명령을 찾을 수 있어야 한다.
