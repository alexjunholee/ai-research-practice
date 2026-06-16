# 부록 A — 용어 경계

AI 연구 셋업은 단어가 섞이는 순간 흔들린다. agent를 model처럼 부르고,
skill을 prompt처럼 쓰고, memory를 증거처럼 믿으면 같은 실패가 돌아온다.
로보틱스 연구에서는 이 혼동이 실험 숫자와 원고 claim까지 올라간다.

## 기본 용어

| 용어 | 이 가이드에서의 뜻 | 경계 |
|---|---|---|
| Model | 텍스트, 코드, 이미지, 표를 생성하거나 판단하는 기반 모델 | 모델 성능은 workspace truth를 대신하지 못한다 |
| Tool | 파일 읽기, 명령 실행, 검색, 이미지 생성처럼 모델 밖의 행동 표면 | tool output은 해당 명령이나 API 범위 안의 증거다 |
| Agent | model과 tool을 묶어 목표를 향해 여러 step을 수행하는 실행자 | agent가 행동해도 claim 권한은 evidence gate가 정한다 |
| Skill | 특정 상황에서 agent가 따를 절차와 판단 기준 | skill은 언제 써야 하는지를 스스로 보장하지 않는다 |
| Harness | 상태, 증거, 행동, 검증, claim을 연결하는 운영 구조 | harness는 연구 상태 전이를 관리하는 규칙이다 |
| AGENTS.md | agent가 작업을 시작하기 전에 읽는 repo 규칙 | AGENTS는 prompt보다 오래 사는 project contract다 |
| Memory | durable correction, 현재 truth, 반복 위험을 보관하는 기록 | memory는 어디를 다시 볼지 정하는 orientation이다 |
| Ledger | 실험, claim, correction, replay의 변경 이력 | ledger는 다음 action을 제한할 때 의미가 있다 |
| Replay | 같은 실패가 다시 나는지 확인하는 작은 시험 | replay는 같은 실패를 future gate로 바꾸는 장치다 |
| Protocol | dataset, split, metric, baseline, artifact가 닫힌 실험 조건 | paper claim은 protocol 안의 숫자에서만 올라간다 |
| Artifact | 파일, 로그, 표, figure, checkpoint, command output | artifact는 provenance와 함께 읽어야 한다 |
| Claim | 원고, rebuttal, README, 발표에서 독자에게 믿게 하는 말 | claim은 evidence tier보다 넓어지면 안 된다 |

## Evidence tier

증거 tier마다 무게가 다르다.

| Tier | 예 | 허용되는 말 |
|---|---|---|
| Orientation | 이전 요약, memory, handoff note | 어디를 다시 볼지 정한다 |
| Candidate | 파일명, issue 제목, 검색 결과 | 후보 artifact나 후보 원인을 말한다 |
| Observation | 원 파일 일부, 로그 일부, config 일부 | 본 범위 안의 관찰을 말한다 |
| Execution | 명령 실행 결과, 생성된 artifact | 그 실행의 outcome을 말한다 |
| Protocol | dataset, split, metric, baseline, artifact가 닫힌 상태 | 같은 protocol 안의 비교를 말한다 |
| Claim | claim/evidence map과 reviewer risk가 닫힌 상태 | 원고 문장과 rebuttal 문장을 말한다 |

AI가 자주 무너지는 지점은 tier를 건너뛰는 곳이다. orientation을 claim처럼
쓰거나, execution을 method improvement처럼 쓰거나, observation을 전체 run의
원인처럼 말한다.

## Role boundary

한 turn 안에서 역할이 섞이면 결과가 흐려진다.

| Role | 맡길 일 | 끝낼 때 남길 것 |
|---|---|---|
| Code operator | repo 읽기, 작은 수정, build/test | command, diff, artifact, next failure |
| Experiment operator | protocol 작성, run 해석, result tuple | experiment contract, result provenance |
| Literature operator | 관련 연구 좌표, paper-code map | claim, assumption, code path, comparison |
| Manuscript operator | claim/evidence repair, rebuttal structure | allowed wording, blocked wording |
| Harness operator | AGENTS, memory, ledger, replay 관리 | durable correction, replay case |

같은 model이 여러 role을 수행할 수 있다. 그러나 같은 답변 안에서 role이
바뀌면 evidence gate도 다시 선언해야 한다.

## Tool surface map

도구 표면은 제품명보다 역할로 고른다.

| Tool surface | 좋은 용도 | 닫아야 할 gate |
|---|---|---|
| Chat model | 개념 정리, 논문 질문, claim 후보 분리 | primary evidence와 orientation을 구분한다 |
| Coding agent | repo 읽기, 작은 수정, script 실행, template 생성 | source file, command output, diff를 남긴다 |
| IDE assistant | 한 파일 안의 짧은 편집과 rename | 변경 범위와 formatter/test를 확인한다 |
| Browser/search tool | 외부 repo, 논문, 문서의 발견 | 링크, 확인일, claim boundary를 남긴다 |
| Terminal/script | build, metric, checksum 검증 | 실행 command와 artifact path를 남긴다 |
| Project memory | durable correction과 현재 truth 보관 | memory를 proof로 승격하지 않는다 |

도구를 바꾸면 증거 tier도 다시 확인한다. 검색 결과는 candidate이고, terminal
실행은 execution이며, protocol이 닫히기 전의 숫자는 manuscript claim이 아니다.

## Claim boundary

claim은 다섯 단계로 올라간다.

```text
observation
-> execution outcome
-> protocol-bound result
-> comparison
-> manuscript claim
```

예를 들어 `ros2 topic info --verbose`에서 QoS mismatch를 봤다면 허용되는 말은
"publisher와 subscriber의 QoS가 맞지 않는다"이다. 아직 허용되지 않는 말은
"시스템이 고쳐졌다"이다. 고쳐졌다는 말은 launch 수정, 재실행, callback
artifact가 있어야 한다.

실험에서도 같다. `R@1`이 높아졌다는 observation만으로 방법이 좋아졌다고
말하지 않는다. query/database 방향, positive rule, feature space, baseline,
metric script가 닫혀야 comparison을 말할 수 있다.

## Codex와 Claude 이식 경계

Claude용 규칙을 Codex에서 쓸 때는 행동 규칙과 evidence gate를 옮긴다.

| Claude 중심 자료 | 옮길 것 | 그대로 두면 안 되는 것 |
|---|---|---|
| `CLAUDE.md` | 행동 규칙, evidence gate, project boundary | Claude-only 명령 |
| `.claude/skills` | 절차 지식, routing rule | 파일 경로와 UI 전제 |
| Slash command | 반복 가능한 목적과 입력 형식 | 특정 도구의 호출 문법 |
| Cursor rule | 편집 원칙, style gate | editor 내부 설정을 universal rule처럼 쓰는 것 |

Codex에서는 `AGENTS.md`, `templates/`, project memory, 검증 스크립트가
이식된 규칙을 받는다. 이식 후에는 `codex-porting-checklist.md`로 빠진 gate를
확인한다.
