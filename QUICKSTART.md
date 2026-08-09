# 부록 B — 첫 연구 작업 공간 만들기

본문에서 AI가 잘하는 일과 틀리는 일, 사람이 감당할 위험, 하네스가 확인할 경계를
먼저 읽는다. 그런 다음 이 부록에 모아 둔 파일을 새 연구 작업 공간으로 옮긴다.

## 도구의 역할부터 나눈다

처음에는 연구의 현재 상태와 도구의 역할을 함께 정한다. 모델명은 그다음에 다룰
문제다. 역할을 먼저 정해 두면 그 역할을 맡을 제품은 나중에 바꿔 끼울 수 있다.

| 연구 장면 | 먼저 열 도구 | 첫 확인 |
|---|---|---|
| 저장소를 읽고 작은 수정을 한다 | 코딩 에이전트 | `AGENTS.md`와 원본 파일을 먼저 읽었는가 |
| 논문 주장을 코드와 실험에 연결한다 | 대화 모델 또는 코딩 에이전트 | 논문-코드-실험 표가 남는가 |
| ROS2, Docker, CUDA, 데이터셋 오류를 좁힌다 | 코딩 에이전트와 터미널 | 단계별 명령 출력이 있는가 |
| 외부 저장소나 논문을 찾는다 | 브라우저·검색 도구 | 출처 URL과 주장 범위가 분리됐는가 |
| 원고와 답변서를 고친다 | 원고 담당 역할 | 쓸 문장과 보류할 문장이 분리됐는가 |
| 반복 실패를 막는다 | 하네스 담당 역할 | 실패를 변경 기록이나 반복 확인 사례로 남겼는가 |

같은 AI 제품이 여러 역할을 맡을 수 있다. 한 요청 안에서 역할이 바뀌면
확인 기준도 다시 적는다.

tool·resource·prompt와 sampling·elicitation·logging의 구분은 부록 A의 「MCP의 tool·resource·prompt」에서 확인한다.

## 작업 공간을 만들고 파일을 설치한다

역할과 확인 기준은 파일로 남겨야 다음 세션이 이어받을 수 있다.
루트에는 AI가 먼저 읽을 파일을 두고, 나머지는 용도별 폴더로 나눈다.

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

이 폴더들은 서로 다른 디스크에 둘 수 있다. 동기화 폴더, 외장 디스크, 원격 서버를
쓴다면 Git 메타데이터와 데이터셋을 어디에 저장할지 먼저 정한다. 코드 이력, 원시
데이터, 실험 결과물, 비공개 메모는 처음부터 나누어 둔다.

이 책의 공개 가이드 묶음에서는 `templates/`의 시작 파일을 정해진 자리로 옮긴다.
`workspace-readme.md`를 `README.md`로,
`AGENTS.template.md`를 `AGENTS.md`로, `project-memory.template.json`을
`project-memory.json`으로 복사하고, 첫 요청에 쓸 `first-ai-session-prompt.md`를
`notes/`에 둔다. 주장과 근거를 적을 `claim-evidence-map.md`는 원고 작업을 시작할 때
가져온다. `README.md`는 복사한 서식의 빈칸만 짧게 채우고, 상태 메모는 별도 서식 없이
직접 쓴다. 이 공간에 무엇을 두는지, 공개·비공개 경계를 어디에 두는지만 밝히면 된다.

번들을 내려받아 풀었다면 다음과 같이 시작한다. 아래 명령은 첫날 점검과 논문·실험
기록에 필요한 파일까지 한 번에 설치한다. `GUIDE`는 가이드 묶음의 루트이고,
`WORKSPACE`는 새 연구 작업 공간의 위치다.

```bash
GUIDE="$PWD"
WORKSPACE="$HOME/robotics-ai-workspace"
mkdir -p "$WORKSPACE"/repos "$WORKSPACE"/datasets "$WORKSPACE"/artifacts \
  "$WORKSPACE"/notes "$WORKSPACE"/templates
cp "$GUIDE/templates/workspace-readme.md" "$WORKSPACE/README.md"
cp "$GUIDE/templates/AGENTS.template.md" "$WORKSPACE/AGENTS.md"
cp "$GUIDE/templates/project-memory.template.json" "$WORKSPACE/project-memory.json"
cp "$GUIDE"/templates/*.md "$WORKSPACE/templates/"
cp "$GUIDE/templates/first-day-workspace-checklist.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/first-ai-session-prompt.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/paper-code-experiment-map.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/experiment-contract.md" "$WORKSPACE/notes/"
cp "$GUIDE/templates/weekly-research-ledger.md" "$WORKSPACE/notes/"
```

Windows PowerShell에서는 같은 구성을 다음과 같이 만든다.

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

복사가 끝나면 작업 공간 루트에서 파일이 제자리에 있는지 확인한다. POSIX 셸에서는
다음 확인을 모두 통과한 뒤 첫 AI 세션을 연다.

```bash
(
  set -eu
  cd "$WORKSPACE"
  for path in \
    AGENTS.md \
    README.md \
    project-memory.json \
    notes/first-day-workspace-checklist.md \
    notes/first-ai-session-prompt.md \
    notes/paper-code-experiment-map.md \
    notes/experiment-contract.md
  do
    if [ ! -f "$path" ]; then
      printf 'missing %s\n' "$PWD/$path" >&2
      exit 1
    fi
  done
  python3 -m json.tool project-memory.json >/dev/null
  mkdir -p artifacts
)
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

복사만 마친 파일에는 아직 빈칸이 남아 있다. `project-memory.json`에서는 먼저 다섯
묶음을 채운다. `source_of_truth`에는 AI가 다시 읽을 파일을, `tool_surface_map`에는
연구 장면별 도구 역할을 적는다. 지금 쓸 수 있는 말과 보류할 말은
`current_evidence`에서 가른다. 처음 시작할 연구 루프 하나는
`first_research_loop`에 고정하고, 다음 세션의 첫 행동은
`next_smallest_actions`에 남긴다.

session·harness·sandbox의 뜻과 파일 대응은 부록 A의 「세션·하네스·샌드박스」에서 확인한다.

`notes/first-ai-session-prompt.md`의 `Prompt To Send` 블록에 이 세 경계를 적는다.
빈칸을 모두 채운 뒤 `artifacts/first-ai-session-message.txt`에 저장하고, 첫 AI
세션에는 이 파일의 내용을 그대로 입력한다.

## AGENTS.md에 프로젝트 규칙을 적는다

루트의 `README.md`와 `AGENTS.md`에도 같은 빈칸이 남아 있다. `README.md`에는
프로젝트 이름과 저장소, 데이터셋, 결과물 위치만 직접 적는다. 그다음
[`templates/AGENTS.template.md`](templates.html#templates-agents-template)에서
다음 항목만 먼저 채운다.

- project truth
- public/private boundary
- managed agent boundary
- work modes
- evidence gate
- durable corrections

이미 `CLAUDE.md`, `.claude/`, Cursor 규칙이 있다면 옮길 규칙과 버릴 명령을
나눈다. 따라 할 절차는 `templates/codex-porting-checklist.md`에 있다. 파일 이름과
플러그인 명령은 도구마다 형식이 다르므로 규칙의 의미부터 본다. "가정을 드러내라", "작게
고쳐라", "성공 기준을 검증 가능하게 만들어라" 같은 규칙은 Codex에서도 그대로 쓴다.

한 작업에서만 쓰는 절차를 skill 폴더로 떼는 기준은 부록 A의 「작업 절차를 skill로 구성하는 기준」에서 확인한다.

## 현재 상태를 먼저 기록한다

`AGENTS.md`의 `project truth`와 `durable corrections`에 채울 내용은 여기에서 나온다.
프로젝트의 목표, 현재 정본으로 삼는 코드 경로와 dataset, 실험과 원고가 어디까지
왔는지, 심사에서 문제가 될 만한 부분, 계속 적용할 교정 사항을 원본 파일과 실행 결과로
확인해 상태 메모에 적는다.

## 첫 AI 요청은 한 작업으로 좁힌다

첫 요청에는 적어도 다음 다섯 항목을 넣는다. 답변 전 전체 점검은 부록 C의 아홉
항목으로 따로 한다. 첫 요청은
[`templates/first-ai-session-prompt.md`](templates.html#templates-first-ai-session-prompt)를
채워 보낸다. 가장 작은 형태는 이렇다.

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

AI의 답변을 연구 작업에 반영하기 전에 근거 상태부터 확인한다.
첫 메시지는 `artifacts/first-ai-session-message.txt`처럼 파일로 남겨 두고,
다음 세션도 같은 읽기 순서로 시작한다.

## 첫 연구 루프는 하나만 고른다

`project-memory.json`의 `first_research_loop`에 고정할 루프를 여기에서 고른다.

| 상황 | 시작 템플릿 |
|---|---|
| 논문 한 편을 읽는다 | [`paper-code-experiment-map.md`](templates.html#templates-paper-code-experiment-map) |
| 데이터셋 상태가 불명확하다 | [`dataset-archaeology-sheet.md`](templates.html#templates-dataset-archaeology-sheet) |
| 실험 숫자를 해석한다 | [`experiment-contract.md`](templates.html#templates-experiment-contract) |
| 오류를 좁힌다 | [`stage-local-debugging.md`](templates.html#templates-stage-local-debugging) |
| 원고 문장을 고친다 | [`claim-evidence-map.md`](templates.html#templates-claim-evidence-map) |

한 번에 여러 루프를 열면 요청이 다시 넓어지므로 첫 요청의 성공 기준은 하나만
둔다. 표의 첫 줄을 골랐다면 이렇게 요청한다. "이 논문의 핵심 주장, 실제로 호출되는 코드
경로를 확인할 대상, 실험 절차의 빈칸을 분리하라."

## 세션을 닫기 전에 결과를 기록한다

작업이 끝나면 `project-memory.json`이나 `weekly-research-ledger.md`에 현재 확인한
사실, 아직 말하면 안 되는 주장, 다음 행동 하나를 적는다. 이 세 줄을 어느 기록에 이어 적을지는
부록 D에서 다룬다.

AI가 잘못된 가정을 세웠다면 그 사례를 notes에 적어 두고, 같은 가정이 반복되면
`AGENTS.md`의 규칙 한 줄로 올린다. 다음 세션은 이렇게 남긴 기록을 읽고 시작한다.

세 줄 가운데 아직 말하면 안 되는 주장은 `claim_boundaries`에 옮긴다.
첫 세션이 끝난 뒤 `project-memory.json`의 `current_evidence`,
`first_research_loop`, `claim_boundaries`, `next_smallest_actions`를 함께 고친다.
이 기록을 갱신하면 다음 AI 세션이 같은 근거 범위를 이어받는다.
