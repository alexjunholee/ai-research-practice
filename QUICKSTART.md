# 부록 B — 첫 연구 작업 공간 만들기

이 부록에서는 새 연구를 시작할 때 AI 도구와 작업 공간을 처음부터 차근차근 꾸리는 절차를 정리한다. 도구의 역할을 나눈 뒤 폴더 구조를 세우고, 기본 템플릿을 복사해 빈칸을 채우며, 첫 AI 세션을 하나의 작은 연구 루프로 여는 순서로 따라가면 된다.

## 도구의 역할부터 나눈다

새 작업 공간을 열 때는 어떤 모델을 쓸지부터 고르기보다, 연구가 지금 어느 단계에 있는지 살펴보고 도구마다 맡길 역할을 먼저 정하는 편이 낫다. 역할을 앞세워 구조를 짜 두면 그 역할을 수행하는 제품이나 모델은 나중에 얼마든지 바꿀 수 있다. 아래 표는 대표적인 연구 장면에 따라 먼저 열 도구와 첫 확인 기준을 정리한 것이다.

| 연구 장면 | 먼저 열 도구 | 첫 확인 |
|---|---|---|
| 저장소를 읽고 작은 수정을 한다 | 코딩 에이전트 | `AGENTS.md`와 원본 파일을 먼저 읽었는가 |
| 논문 주장을 코드와 실험에 연결한다 | 대화 모델 또는 코딩 에이전트 | 논문-코드-실험 표가 남는가 |
| ROS2, Docker, CUDA, 데이터셋 오류를 좁힌다 | 코딩 에이전트와 터미널 | 단계별 명령 출력이 있는가 |
| 외부 저장소나 논문을 찾는다 | 브라우저·검색 도구 | 출처 URL과 주장 범위가 분리됐는가 |
| 원고와 답변서를 고친다 | 원고 담당 역할 | 쓸 문장과 보류할 문장이 분리됐는가 |
| 반복 실패를 막는다 | 하네스 담당 역할 | 실패를 변경 기록이나 반복 확인 사례로 남겼는가 |

한 제품이 여러 역할을 겸할 수도 있지만, 같은 요청 안에서 역할이 바뀐다면 그에 맞춰 확인 기준도 다시 적어야 한다(→ 부록 A).

## 작업 공간을 만들고 파일을 설치한다

역할과 확인 기준을 머릿속에만 두면 다음 세션으로 넘어갈 때 맥락이 끊어진다. 따라서 작업 공간의 루트에는 AI가 가장 먼저 읽을 기준 파일을 배치하고, 나머지 자료는 성격에 따라 폴더로 나누어 둔다. 기본 구조는 다음과 같다.

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

여기서 다섯 하위 폴더를 반드시 같은 디스크에 둘 필요는 없다. 동기화 폴더나 외장 디스크, 원격 서버를 함께 쓰는 환경이라면 Git 저장소 메타데이터와 대용량 데이터셋을 어디에 저장할지 처음부터 정해 둔다. 코드 이력과 원시 데이터, 실험 결과물, 비공개 메모가 한 폴더에 뒤섞이지 않게 가르는 것이 핵심이다.

디렉터리 구조를 잡았으면 가이드 묶음의 `templates/` 아래에 있는 시작 파일을 새 작업 공간의 제자리에 복사한다. 구체적으로는 `workspace-readme.md`를 루트의 `README.md`로, `AGENTS.template.md`를 `AGENTS.md`로, `project-memory.template.json`을 `project-memory.json`으로 옮기고, 첫 요청을 작성할 `first-ai-session-prompt.md`를 비롯한 기록 양식을 `notes/`에 둔다. 주장과 근거를 대조할 `claim-evidence-map.md`는 나중에 원고 작업을 시작할 때 가져와도 무방하다. 복사한 뒤에는 `README.md`에 이 작업 공간의 목적과 공개·비공개 경계만 짧게 적고, 현재 상태 메모는 `project-memory.json`의 항목 형식에 맞춰 채운다.

가이드 번들을 내려받아 풀었다면 아래 명령으로 첫날 점검과 논문·실험 기록에 필요한 파일까지 한 번에 설치할 수 있다. 여기서 `GUIDE`는 가이드 묶음의 루트 경로이고, `WORKSPACE`는 새로 만들 연구 작업 공간의 경로다.

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

Windows PowerShell 환경에서는 같은 구성을 다음 명령으로 만든다.

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

복사를 마쳤다고 바로 세션을 열지 말고, 작업 공간 루트에서 필수 파일이 빠짐없이 놓였는지와 JSON 문법이 깨지지 않았는지 먼저 점검한다. POSIX 셸에서는 아래 확인 스크립트를 모두 통과한 뒤 첫 AI 세션을 연다.

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

Windows PowerShell에서는 같은 점검을 다음과 같이 실행한다.

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

파일 복사를 끝낸 직후에는 템플릿 곳곳에 아직 빈칸이 남아 있다. 우선 `project-memory.json`부터 열어 핵심 필드를 채워야 한다. `source_of_truth`에는 AI가 다시 확인해야 할 정본 파일을 적고, `tool_surface_map`에는 연구 장면별로 어떤 도구를 쓸지 정리한다. 지금 말할 수 있는 사실과 아직 보류해야 할 주장은 `current_evidence`에서 가르고, 이번에 시작할 연구 루프 하나를 `first_research_loop`에 고정한 뒤, 다음 세션에서 가장 먼저 취할 행동을 `next_smallest_actions`에 남긴다(→ 부록 A).

이어서 `notes/first-ai-session-prompt.md` 안의 `Prompt To Send` 블록에 세션·하네스·샌드박스의 경계를 채워 넣는다. 빈칸을 모두 채운 결과는 `artifacts/first-ai-session-message.txt`로 저장해 두고, 첫 AI 세션에 보낼 때는 이 파일의 내용을 그대로 입력한다.

## AGENTS.md에 프로젝트 규칙을 적는다

작업 공간 루트에 복사해 둔 `README.md`와 `AGENTS.md`에도 아직 프로젝트 고유 정보가 비어 있다. `README.md`에는 프로젝트 이름과 저장소·데이터셋·결과물의 위치만 간결하게 적고, 곧바로 루트의 `AGENTS.md`를 열어 아래 여섯 항목부터 채운다. 원본 서식은 [`templates/AGENTS.template.md`](templates.html#templates-agents-template)에서 확인할 수 있다.

- project truth
- public/private boundary
- managed agent boundary
- work modes
- evidence gate
- durable corrections

만약 기존 저장소에 이미 `CLAUDE.md`, `.claude/`, Cursor 규칙이 들어 있다면 옮겨 갈 원칙과 버릴 도구 전용 명령을 먼저 가려내야 한다. 구체적인 이관 절차는 `templates/codex-porting-checklist.md`에 정리되어 있다. 파일 이름이나 플러그인 호출 문법은 도구마다 다르므로 겉모습보다 규칙이 뜻하는 바를 기준으로 판단한다. 예컨대 "가정을 드러내라", "작게 고쳐라", "성공 기준을 검증 가능하게 만들어라" 같은 작업 원칙은 Codex 환경에서도 그대로 살려 쓴다(→ 부록 A).

## 현재 상태를 먼저 기록한다

앞선 `AGENTS.md`의 `project truth`와 `durable corrections` 항목을 채우려면 지금 연구가 어디까지 와 있는지 직접 확인하는 과정이 선행되어야 한다. 프로젝트의 목표, 현재 정본으로 삼는 코드 경로와 dataset, 실험과 원고의 진행 현황, 심사에서 지적받을 만한 약점, 그리고 계속 적용해야 할 교정 사항을 모두 원본 파일과 실제 실행 결과로 대조해 본다. 이렇게 눈으로 확인한 내용만을 추려 상태 메모에 적는다.

## 첫 AI 요청은 한 작업으로 좁힌다

이제 첫 AI 세션을 열 차례다. 답을 내기 전에 거치는 전체 점검 절차는 따로 마련되어 있으므로(→ 부록 C), 첫 요청은 [`templates/first-ai-session-prompt.md`](templates.html#templates-first-ai-session-prompt)를 채워 보내되 반드시 하나의 작업으로 범위를 좁혀야 한다. 가장 간결한 요청 형식은 다음과 같다.

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

이 첫 메시지는 `artifacts/first-ai-session-message.txt`처럼 파일로 남겨 두고, 이후 새 세션을 열 때도 똑같은 읽기 순서로 대화를 시작하면 작업 맥락이 흔들리지 않는다.

## 첫 연구 루프는 하나만 고른다

첫 요청에서 다룰 범위는 앞서 `project-memory.json`의 `first_research_loop`에 고정한 루프 하나로 정한다. 현재 가장 급한 상황에 따라 아래 표에서 시작 템플릿을 하나만 고르면 된다.

| 상황 | 시작 템플릿 |
|---|---|
| 논문 한 편을 읽는다 | [`paper-code-experiment-map.md`](templates.html#templates-paper-code-experiment-map) |
| 데이터셋 상태가 불명확하다 | [`dataset-archaeology-sheet.md`](templates.html#templates-dataset-archaeology-sheet) |
| 실험 숫자를 해석한다 | [`experiment-contract.md`](templates.html#templates-experiment-contract) |
| 오류를 좁힌다 | [`stage-local-debugging.md`](templates.html#templates-stage-local-debugging) |
| 원고 문장을 고친다 | [`claim-evidence-map.md`](templates.html#templates-claim-evidence-map) |

한 번의 요청에 여러 루프를 동시에 열면 질문과 답변이 금세 산만해지므로, 첫 요청에서는 성공 기준을 딱 하나만 둔다. 예컨대 표에서 「논문 한 편을 읽는다」를 골랐다면, "이 논문의 핵심 주장, 실제로 호출되는 코드 경로를 확인할 대상, 실험 절차의 빈칸을 분리하라."처럼 대상과 과제를 못 박아 요청한다.

## 세션을 닫기 전에 결과를 기록한다

작업을 마치고 세션을 닫기 전에는 `project-memory.json`이나 `weekly-research-ledger.md`에 세 가지를 반드시 남긴다. 지금 확인한 사실, 아직 말하면 안 되는 주장, 그리고 다음에 이어 갈 행동 하나다(→ 부록 D).

세션 도중 AI가 잘못된 가정을 세웠다면 그 사례를 `notes/` 아래 기록으로 남겨 두고, 똑같은 착오가 반복된다면 `AGENTS.md`의 규칙 한 줄로 끌어올려 다음 세션부터 미리 차단한다.

마지막으로, 세션 끝에 정리한 항목 가운데 아직 근거가 부족해 보류해야 하는 주장은 `claim_boundaries`로 옮긴다. 첫 세션이 끝나면 `project-memory.json`의 `current_evidence`, `first_research_loop`, `claim_boundaries`, `next_smallest_actions` 네 필드를 함께 갱신해 두어야 다음 세션이 곧바로 그 위에서 이어갈 수 있다.
