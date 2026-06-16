# Ch.2 — 연구 상태는 대화 안에 있지 않다

지난주에 돌린 실험을 다시 열었는데, AI는 자신 있게 말한다. "이 설정이면
baseline보다 좋아진 것 같습니다." 문장은 자연스럽다. 표도 그럴듯하다.
그러나 연구자의 손은 멈춘다. 그 숫자가 어느 dataset split에서 나왔는지,
query와 database 방향이 맞는지, 실행 중에 바뀐 config가 있었는지, 실패한
sequence를 제외했는지 아직 보지 않았기 때문이다.

대화 안에는 결과가 있다. 연구 상태는 다른 곳에 있다.

로보틱스 연구의 현재 상태는 한 파일에 들어 있지 않다. 코드 repo, bag,
calibration note, Dockerfile, launch file, shell history, 결과 표, figure,
원고 문장, reviewer memo, 지난번 correction이 서로 다른 표면에 흩어져 있다.
AI가 이 표면을 읽기 전에 답을 만들면, 빈칸은 문장으로 채워진다. 문장은
매끄럽고, 연구는 미끄러진다.

## 요약은 지도이지 증거가 아니다

긴 프로젝트를 다시 열 때 요약은 필요하다. 어디를 보아야 하는지 알려 주는
지도이기 때문이다. 그러나 지도는 땅이 아니다. compact summary, 이전 assistant
답변, project memory는 모두 방향을 주는 자료다. 그 자료가 현재 실행 상태를
증명하지는 못한다.

좋게 끝난 세션은 요약을 읽은 뒤 원래 표면으로 돌아갔다. 실제 파일을 열고,
command output을 다시 보고, artifact의 timestamp를 확인하고, protocol 빈칸을
잠갔다. 무너진 세션은 요약을 현재 truth로 승격했다. "지난번에 고쳤다"는
말이 active code path를 대신했고, "성능이 올랐다"는 요약이 dataset split을
대신했다.

이 차이는 작아 보이지만 원고에서는 커진다. 요약은 "개선됐다"고 말할 수
있다. 원고는 어느 조건에서 무엇이 얼마나 개선됐는지를 말해야 한다. 둘 사이에
dataset, split, metric script, baseline, artifact가 놓인다.

## AI가 먼저 읽어야 할 표면

AI에게 "여기서 뭐 하던 건지 파악해 봐"라고 맡길 때 필요한 것은 긴 설명이
아니다. 읽기 순서다. 어떤 repo에서는 `AGENTS.md`가 그 순서를 들고 있고,
어떤 프로젝트에서는 README, ROADMAP, experiment note, issue thread, result
folder가 그 역할을 나누어 가진다.

읽기 순서는 대체로 이렇게 내려간다.

```text
project rule
-> current status note
-> source file / config / script
-> command output / artifact
-> manuscript claim / reviewer risk
```

이 순서가 없으면 AI는 눈에 먼저 들어온 표면을 중심으로 이야기를 만든다.
파일명이 `final_results.csv`이면 최종 결과처럼 읽고, `fixed_launch.py`이면
고쳐진 launch처럼 읽는다. 로보틱스 연구에서는 이름과 활성 상태가 자주
어긋난다. 오래된 bag, 복사된 config, 쓰이지 않는 baseline script, 버려진
figure가 같은 폴더 안에 남아 있기 때문이다.

## 공개 경계도 연구 상태다

연구 상태를 복원할 때 공개와 비공개를 나누는 일은 행정 절차가 아니다.
AI가 어떤 문장을 만들 수 있는지를 정하는 연구 조건이다. 원 대화 로그,
개인 경로, reviewer 원문, 미공개 실험 결과, credential은 공개 문장으로
넘어가면 안 된다. 반대로 그 안에서 발견한 반복 패턴은 공개 지식이 될 수
있다.

공개로 옮길 수 있는 단위는 사건이 아니라 구조다. "어느 private repo에서
무슨 파일이 깨졌다"는 공개할 수 없다. "AI가 파일명만 보고 active method를
추정하면 틀린다"는 공개할 수 있다. 이 차이를 먼저 나누지 않으면 AI는 설명의
자연스러움을 위해 경계를 넘는다.

## 세 개의 오래 남는 표면

연구 상태를 매번 처음부터 복원할 수는 없다. 오래 남길 표면이 필요하다.
그 표면은 많을 필요가 없다.

```text
AGENTS.md
project-memory.json
weekly-research-ledger.md
```

`AGENTS.md`는 AI가 행동하기 전에 읽는 규칙이다. 공개 경계, 작업 모드,
검증 방식, 하면 안 되는 추론을 적는다. Claude 중심 repo에서 넘어온
`CLAUDE.md`, slash command, Cursor rule도 이름이 아니라 행동 원칙을 옮긴다.
"작게 고쳐라", "assumption을 말하라", "검증 기준을 먼저 말하라" 같은 규칙은
도구 이름이 바뀌어도 살아남는다.

`project-memory.json`은 현재 truth를 증명하는 파일이 아니다. 어디를 다시
보아야 하는지 알려 주는 표지다. memory가 proof가 되는 순간, 오래된 요약이
새 실험을 덮는다.

`weekly-research-ledger.md`는 이번 주에 닫힌 것과 아직 닫히지 않은 것을
나눈다. 닫힌 protocol, 막힌 claim, 다음 smallest action이 남아 있으면 다음
AI 세션은 같은 자리에서 다시 시작할 수 있다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| 프로젝트 재개 | 규칙, 상태 파일, 실제 artifact를 차례로 읽었다 | 이전 요약을 현재 상태로 확정했다 | 요약은 방향을 주지만 실행 상태를 증명하지 못한다 |
| Claude 규칙 이식 | 행동 원칙을 `AGENTS.md`와 template으로 옮겼다 | 파일명, slash command, 도구 이름을 그대로 복사했다 | 도구 이름보다 다음 세션이 같은 행동을 반복하는 능력이 중요하다 |
| 공개 경계 | 원문 로그와 private path를 로컬 전용으로 묶었다 | 설명을 만들다가 개인 경로를 공개 원고에 섞었다 | AI는 경계가 없으면 자연스러운 문장을 먼저 만든다 |
| 실험 재개 | artifact와 command output을 다시 확인했다 | memory를 proof처럼 사용했다 | 연구 상태는 대화보다 파일과 실행 결과에 더 많이 남는다 |

연구 상태 복원의 목표는 AI가 모든 것을 기억하게 만드는 일이 아니다. AI가
기억을 증거로 착각하지 않게 만드는 일이다. 이 차이를 지키면 다음 장의
하네스가 제 역할을 한다. 하네스는 기억을 늘리는 장치가 아니라, 기억이
어디까지 말할 수 있는지를 제한하는 장치다.
