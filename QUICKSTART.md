# 부록 B — 빠른 시작 파일

본문을 읽은 뒤 새 연구 workspace에 옮길 파일을 정리한다. AI가 잘하는 일과 자주 틀리는 일,
사람이 감당하는 위험, 하네스가 확인하는 경계를 먼저 이해하고 이 부록을 쓴다.

## 도구 역할을 먼저 나눈다

처음에는 연구 상태와 도구 표면을 함께 정한다. 모델명은 그다음 문제다.

| 연구 장면 | 먼저 열 도구 표면 | 첫 확인 |
|---|---|---|
| repo를 읽고 작은 수정을 한다 | coding agent | `AGENTS.md`와 원 파일을 먼저 읽었는가 |
| 논문 주장을 code와 experiment에 연결한다 | chat model 또는 coding agent | 논문-코드-실험 표가 남는가 |
| ROS2, Docker, CUDA, dataset 오류를 좁힌다 | coding agent와 terminal | stage별 command output이 있는가 |
| 외부 repo나 논문을 찾는다 | browser/search tool | 출처 URL과 주장 범위가 분리됐는가 |
| 원고와 답변서를 고친다 | manuscript operator role | 쓸 문장과 보류할 문장이 분리됐는가 |
| 반복 실패를 막는다 | harness operator role | 변경 기록이나 반복 확인 사례로 남겼는가 |

같은 AI 제품이 여러 역할을 할 수 있다. 한 turn 안에서 역할이 바뀌면
확인 기준도 다시 적는다.

## Workspace를 나눈다

처음에는 단순하게 둔다.

```text
workspace/
├── AGENTS.md
├── README.md
├── project-memory.json
├── repos/
├── datasets/
├── artifacts/
├── notes/
└── templates/
```

동기화 폴더, 외장 디스크, 원격 서버를 쓰면 git metadata와 dataset 저장 위치를
먼저 정한다. 코드 이력, raw data, 실험 결과물, 비공개 메모를 한 덩어리로
섞지 않는다.

새 workspace를 처음 만들 때는 공개 번들에서 다음 파일을 먼저 복사한다.

| 공개 번들 | 새 workspace |
|---|---|
| [`templates/workspace-readme.md`](templates/workspace-readme.md) | `README.md` |
| [`templates/AGENTS.template.md`](templates/AGENTS.template.md) | `AGENTS.md` |
| [`templates/project-memory.template.json`](templates/project-memory.template.json) | `project-memory.json` |
| `templates/*.md` | `templates/` |
| 필요한 research loop template | `notes/` |

번들을 내려받아 풀어 둔 상태라면 다음처럼 시작할 수 있다. `GUIDE`는 이 가이드
bundle의 루트, `WORKSPACE`는 새 연구 workspace 위치다.

```bash
GUIDE="$PWD"
WORKSPACE="$HOME/robotics-ai-workspace"
mkdir -p "$WORKSPACE"/repos "$WORKSPACE"/datasets "$WORKSPACE"/artifacts \
  "$WORKSPACE"/notes "$WORKSPACE"/templates
cp "$GUIDE/templates/workspace-readme.md" "$WORKSPACE/README.md"
cp "$GUIDE/templates/AGENTS.template.md" "$WORKSPACE/AGENTS.md"
cp "$GUIDE/templates/project-memory.template.json" "$WORKSPACE/project-memory.json"
cp "$GUIDE/templates/"*.md "$WORKSPACE/templates/"
cp "$GUIDE/templates/first-day-workspace-checklist.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/first-ai-session-prompt.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/paper-code-experiment-map.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/experiment-contract.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/weekly-research-ledger.md" "$WORKSPACE/notes/"
```

Windows PowerShell에서는 같은 작업을 이렇게 한다.

```powershell
$Guide = (Get-Location).Path
$Workspace = "$HOME\robotics-ai-workspace"
New-Item -ItemType Directory -Force -Path `
  "$Workspace\repos", "$Workspace\datasets", "$Workspace\artifacts", `
  "$Workspace\notes", "$Workspace\templates" | Out-Null
Copy-Item "$Guide\templates\workspace-readme.md" "$Workspace\README.md"
Copy-Item "$Guide\templates\AGENTS.template.md" "$Workspace\AGENTS.md"
Copy-Item "$Guide\templates\project-memory.template.json" "$Workspace\project-memory.json"
Copy-Item "$Guide\templates\*.md" "$Workspace\templates\"
Copy-Item "$Guide\templates\first-day-workspace-checklist.md" "$Workspace\notes\"
Copy-Item "$Guide\templates\first-ai-session-prompt.md" "$Workspace\notes\"
Copy-Item "$Guide\templates\paper-code-experiment-map.md" "$Workspace\notes\"
Copy-Item "$Guide\templates\experiment-contract.md" "$Workspace\notes\"
Copy-Item "$Guide\templates\weekly-research-ledger.md" "$Workspace\notes\"
```

복사 직후에는 workspace 루트에서 첫 실행 전 확인을 한다. POSIX shell에서는
다음 항목만 통과하면 첫 AI 세션을 열 수 있다.

```bash
cd "$WORKSPACE"
test -f AGENTS.md
test -f README.md
test -f project-memory.json
python3 -m json.tool project-memory.json >/dev/null
test -f notes/first-day-workspace-checklist.md
test -f notes/first-ai-session-prompt.md
test -f notes/paper-code-experiment-map.md
test -f notes/experiment-contract.md
mkdir -p artifacts
```

Windows PowerShell에서는 같은 확인을 이렇게 한다.

```powershell
Set-Location $Workspace
@(
  "AGENTS.md",
  "README.md",
  "project-memory.json",
  "notes\first-day-workspace-checklist.md",
  "notes\first-ai-session-prompt.md",
  "notes\paper-code-experiment-map.md",
  "notes\experiment-contract.md"
) | ForEach-Object {
  if (-not (Test-Path $_)) { throw "missing $_" }
}
Get-Content .\project-memory.json | ConvertFrom-Json | Out-Null
New-Item -ItemType Directory -Force -Path .\artifacts | Out-Null
```

`project-memory.json`에는 다섯 묶음이 있어야 한다. `source_of_truth`는 AI가
다시 읽을 파일을 가리키고, `tool_surface_map`은 연구 장면별 도구 역할을
나눈다. `current_evidence`는 지금 쓸 수 있는 말과 보류할 말을 분리한다.
`first_research_loop`는 처음 열 루프 하나만 고정하고, `next_smallest_actions`는
다음 세션의 첫 행동을 남긴다.

그다음 `notes/first-ai-session-prompt.md`의 `Prompt To Send` 블록에서 빈칸을
채우고 `artifacts/first-ai-session-message.txt`에 저장한다. 이 파일이 첫 AI
세션의 실제 입력이다.

## AGENTS.md 작성

[`templates/workspace-readme.md`](templates/workspace-readme.md)를 `README.md`로
복사하고, 프로젝트 이름과 repo, dataset, artifact 위치만 채운다. 그다음
[`templates/AGENTS.template.md`](templates/AGENTS.template.md)에서
다음 항목만 먼저 채운다.

- project truth
- public/private boundary
- work modes
- evidence gate
- durable corrections

이미 `CLAUDE.md`, `.claude/`, Cursor rule이 있으면
[`templates/codex-porting-checklist.md`](templates/codex-porting-checklist.md)로
옮길 규칙과 버릴 명령을 나눈다. 파일 이름과 plugin 명령은 도구별 형식이다.
먼저 볼 것은 규칙의 의미다. assumption을 드러내라, 작게 고쳐라, 성공 기준을 검증 가능하게
만들어라 같은 규칙은 Codex에서도 그대로 쓴다.

## 첫 상태 체크리스트를 채운다

[`templates/first-day-workspace-checklist.md`](templates/first-day-workspace-checklist.md)는
현재 연구 상태의 원 파일과 실행 결과를 정한다.

```text
project goal:
code truth:
dataset truth:
experiment truth:
manuscript truth:
reviewer risk:
durable corrections:
```

이 표가 비어 있으면 AI는 현재 상태를 복원하지 못한다. README만으로는
실험 protocol, reviewer risk, dataset convention을 알 수 없다.

## 첫 AI 요청을 좁힌다

첫 요청은 [`templates/first-ai-session-prompt.md`](templates/first-ai-session-prompt.md)를
채워서 보낸다. 가장 작은 형태는 이렇다.

```text
Read AGENTS.md and the first-day workspace checklist.
Before answering, state:
- object under truth control
- current evidence permits
- current evidence forbids
- smallest next action
- verification
Do not infer project truth from summaries when source files or artifacts are
available.
```

이 요청은 가능한 설명이 연구 행동으로 바뀌기 전에 증거 상태를 확인한다.
첫 메시지는 `artifacts/first-ai-session-message.txt`처럼 파일로 남겨 두면
다음 세션에서 같은 읽기 순서를 다시 쓸 수 있다.

## 연구 루프를 하나만 고른다

처음에는 하나만 고른다.

| 상황 | 시작 템플릿 |
|---|---|
| 논문 한 편을 읽는다 | [`paper-code-experiment-map.md`](templates/paper-code-experiment-map.md) |
| dataset 상태가 불명확하다 | [`dataset-archaeology-sheet.md`](templates/dataset-archaeology-sheet.md) |
| 실험 숫자를 해석한다 | [`experiment-contract.md`](templates/experiment-contract.md) |
| 에러를 좁힌다 | [`stage-local-debugging.md`](templates/stage-local-debugging.md) |
| 원고 문장을 고친다 | [`claim-evidence-map.md`](templates/claim-evidence-map.md) |

한 번에 여러 루프를 열면 AI는 다시 넓어진다. 시작 지점에서는 작은 성공 하나가
좋다. 예를 들어 "논문 요약" 대신 "이 논문의 central claim, active code
path 확인 대상, experiment protocol 빈칸을 분리하라"처럼 요청한다.

## 결과를 기록에 남긴다

작업이 끝나면 `project-memory.template.json`이나
`weekly-research-ledger.md`에 세 줄을 남긴다.

```text
현재 확인한 사실:
아직 말하면 안 되는 주장:
다음 행동:
```

AI가 틀린 assumption을 했다면 `replay-case.md`에 반복 확인 사례로 적는다. 같은 실수를
다음 세션에서 다시 설명하지 않기 위해서다.

첫 세션이 끝난 뒤 `project-memory.json`의 `current_evidence`,
`first_research_loop`, `claim_boundaries`, `next_smallest_actions`를 함께 고친다.
memory가 바뀌지 않으면 다음 AI 세션은 같은 근거 범위를 이어받지 못한다.
