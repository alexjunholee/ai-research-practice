# 부록 A — 헷갈리기 쉬운 말들

AI 도구를 연구에 쓰면 단어가 쉽게 섞인다. model, tool, agent, memory를 같은 종류로 부르면 실험 숫자와 원고 주장까지 흔들린다. 자주 섞이는 말을 구분하기 위한 최소 기준은 아래와 같다.

## 기본 용어

| 용어 | 뜻 | 조심할 점 |
|---|---|---|
| 모델 | 텍스트, 코드, 이미지, 표를 생성하거나 판단하는 기반 모델 | 모델 답변은 현재 workspace 상태를 대신하지 못한다 |
| 도구 | 파일 읽기, 명령 실행, 검색, 이미지 생성처럼 모델 밖에서 일어나는 행동 | 도구 결과는 해당 명령이나 API 범위 안에서만 근거가 된다 |
| 에이전트 | 모델과 도구를 묶어 여러 단계를 수행하는 실행자 | 에이전트가 행동해도 연구 주장은 실행 결과가 정한다 |
| 스킬 | 특정 상황에서 에이전트가 따를 절차와 판단 기준 | 언제 써야 하는지까지 자동으로 보장하지 않는다 |
| 하네스 | 상태, 근거, 행동, 확인, 주장을 연결하는 운영 구조 | 한 번의 AI 작업이 어디까지 말할 수 있는지 제한한다 |
| AGENTS.md | 에이전트가 작업 전에 읽는 repo 규칙 | 한 번의 prompt 뒤에도 남는 프로젝트 규칙이다 |
| 기억 기록 | 현재 상태, 반복 위험, 사용자의 durable correction을 보관하는 기록 | 다시 볼 위치를 알려 주는 자료다 |
| 변경 이력 | 실험, 주장, correction, 반복 확인의 변경 기록 | 다음 행동을 제한할 때 의미가 있다 |
| 반복 확인 | 같은 실패가 다시 나는지 확인하는 작은 시험 | 반복 실수를 다음 작업 전에 잡기 위해 쓴다 |
| 실험 조건 | dataset, split, metric, baseline, output path를 확인한 조건 | 숫자는 이 조건 안에서만 비교한다 |
| 결과물 | 파일, 로그, 표, figure, checkpoint, command output | 출처와 함께 읽어야 한다 |
| 주장 | 원고, 답변서, README, 발표에서 독자에게 믿게 하는 말 | 근거 범위를 넘으면 안 된다 |

## 근거의 무게

| 단계 | 예 | 말할 수 있는 범위 |
|---|---|---|
| 방향 잡기 | 이전 요약, memory, handoff note | 어디를 다시 볼지 정한다 |
| 확인 대상 | 파일명, issue 제목, 검색 결과 | 원인이나 다음 확인 대상을 제안한다 |
| 관찰 | 원 파일 일부, 로그 일부, config 일부 | 본 범위 안의 사실을 말한다 |
| 실행 결과 | 명령 실행 결과, 생성된 파일 | 그 실행의 결과를 말한다 |
| 실험 조건 확인 | dataset, split, metric, baseline, output path를 확인한 숫자 | 같은 조건 안에서 비교한다 |
| 원고 주장 | figure, table, citation, reviewer risk를 함께 확인한 문장 | 원고와 rebuttal에 쓴다 |

AI가 자주 틀리는 곳은 이 단계를 건너뛰는 자리다. 요약을 근거처럼 쓰거나, 실행 결과 하나를 방법 개선처럼 말하거나, 일부 로그를 전체 run의 원인처럼 말한다.

## 도구별로 볼 것

| 도구 | 좋은 용도 | 확인할 항목 |
|---|---|---|
| Chat model | 개념 정리, 논문 질문, 주장 분리 | 원 파일을 봤는지 구분한다 |
| Coding agent | repo 읽기, 작은 수정, script 실행 | 원 파일, 명령 출력, diff를 남긴다 |
| IDE assistant | 한 파일 안의 짧은 편집과 rename | 변경 범위와 formatter/test를 확인한다 |
| Browser/search tool | 외부 repo, 논문, 문서 발견 | 링크, 확인일, 주장 범위를 남긴다 |
| Terminal/script | build, metric 산출, checksum 확인 | 실행 command와 output path를 남긴다 |
| Project memory | durable correction과 현재 상태 보관 | 기억 기록을 증거로 쓰지 않는다 |

도구를 바꾸면 근거의 무게도 다시 본다. 검색 결과는 후보이고, terminal 실행은 실행 결과다. dataset, split, metric script를 확인하기 전 숫자는 원고에 올리지 않는다.

## Claude 규칙을 Codex에서 쓸 때

Claude용 규칙을 Codex에서 쓸 때는 행동 규칙과 확인 기준만 옮긴다.

| Claude 중심 자료 | 옮길 것 | 그대로 두면 안 되는 것 |
|---|---|---|
| `CLAUDE.md` | 행동 규칙, 확인 기준, project boundary | Claude-only 명령 |
| `.claude/skills` | 절차 지식, routing rule | 파일 경로와 UI 전제 |
| Slash command | 반복 가능한 목적과 입력 형식 | 특정 도구의 호출 문법 |
| Cursor rule | 편집 원칙, 문체 점검 | editor 내부 설정을 전체 규칙처럼 쓰는 것 |

Codex에서는 `AGENTS.md`, `templates/`, project memory가 이식된 규칙을 받는다. 이식 후에는 빠진 확인 항목을 따로 점검한다.
