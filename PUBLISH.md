# 발행 전 점검

이 repo는 정적 HTML로 발행할 수 있다. 원본은 Markdown chapter와 template이고,
`guide.html`은 생성물이다. 공개 전에는 생성, 검증, 수동 확인을 같은 순서로
반복한다.

## 1. 생성한다

```bash
python3 scripts/build_guide.py
```

이 명령은 `QUICKSTART.md`, `TERMS.md`, `EXAMPLE_WORKSPACE.md`, `PATH.md`,
`chapter_*.md`, `PUBLISH.md`, `SOURCES.md`를 읽어 `guide.html`을 다시 만든다.
`guide.html`을 손으로 수정하지 않는다.

## 2. 공개 경계를 검사한다

```bash
python3 scripts/smoke_runbook_toolchain_sync.py
python3 scripts/smoke_pages_workflow.py
python3 scripts/verify_public.py
python3 scripts/smoke_quickstart.py
python3 scripts/smoke_first_workspace_rehearsal.py
python3 scripts/smoke_example_research_loop.py
python3 scripts/smoke_templates.py
python3 scripts/smoke_sources.py
python3 scripts/smoke_log_analysis_coverage.py
python3 scripts/smoke_html_usability.py
python3 scripts/render_smoke.py
python3 scripts/style_smoke.py
```

검사는 다음 문제를 잡는다.

- 필요한 공개 파일이 빠진 경우
- `index.html`이 `guide.html`로 이어지는 meta refresh와 fallback link를 잃은 경우
- chapter 목록과 실제 chapter 파일이 맞지 않는 경우
- `guide.html`에 quickstart, 용어 경계, 예시 작업장, 운영 경로, 8장, 발행 점검,
  출처 목록이 빠진 경우
- 공개 파일에 개인 경로, 원 대화 원문, 오래된 제목, 미완성 표기가 들어간 경우
- 본문에서 호출한 template 파일이 빠진 경우
- 내부 anchor나 상대 링크가 깨진 경우
- 예시 작업장의 필수 파일과 evidence gate가 빠진 경우
- 복사용 template의 필수 섹션과 evidence gate field가 빠진 경우
- 본문 외부 URL을 `SOURCES.md`에 빠뜨렸거나, 생성 HTML 외부 링크에
  `target="_blank" rel="noopener"`를 빠뜨린 경우
- 렌더링 smoke가 Chrome/Chromium, Firefox, WeasyPrint fallback 중 어느 쪽으로도
  생성물을 만들지 못하는 경우
- 공개 산문에 챕터 메타 선언, 헤지 라벨, 홍보 어휘, vague attribution,
  부정 대조, 번역체 접속, 자기 작법 설명체가 들어간 경우

## 3. 브라우저에서 본다

파일을 직접 열 수 있다.

```text
index.html
guide.html
```

확인할 것은 다음 항목이다.

- 왼쪽 navigation에서 빠른 시작, 용어 경계, 8장, 발행 전 점검, Sources가 보이는가
- `index.html`을 열었을 때 `guide.html`로 이동하거나 fallback link가 보이는가
- 예시 작업장 섹션에서 `examples/first-robotics-workspace/` 구조가 보이는가
- 운영 경로가 첫날, 첫 주, 첫 달로 읽히는가
- 모바일 폭에서 본문과 표가 깨지지 않는가
- 외부 링크와 template 이름이 실제 파일과 맞는가

`scripts/render_smoke.py`는 자동 렌더링 smoke다. Chrome/Chromium headless가
동작하면 desktop/mobile screenshot과 PDF를 만든다. Chrome이 실패하면 Firefox
screenshot을 시도하고, 그마저 실패하면 WeasyPrint PDF fallback을 시도한다.
PDF가 생성되고 `pdftotext`가 있으면 제목, 빠른 시작, 용어 경계, 예시 작업장,
운영 경로, Ch.1, Ch.8 텍스트가 실제 렌더 산출물에 들어 있는지도 확인한다.
Firefox screenshot이 생성되면 desktop/mobile 폭을 눈으로 확인한다.

## 4. 발행 대상을 고른다

정적 호스팅에는 다음 파일만 필요하다.

```text
BUNDLE_MANIFEST.txt
BUNDLE_SHA256SUMS.txt
.nojekyll
README.md
QUICKSTART.md
TERMS.md
EXAMPLE_WORKSPACE.md
PATH.md
DEPLOY.md
PUBLISH.md
ROADMAP.md
SOURCES.md
index.html
guide.html
chapter_*.md
examples/
templates/
```

검증과 번들 생성을 위한 script는 source repo에 남긴다.

```text
scripts/build_guide.py
scripts/smoke_runbook_toolchain_sync.py
scripts/smoke_pages_workflow.py
scripts/smoke_no_git_dependency.py
scripts/verify_public.py
scripts/smoke_quickstart.py
scripts/smoke_first_workspace_rehearsal.py
scripts/smoke_example_research_loop.py
scripts/smoke_templates.py
scripts/smoke_sources.py
scripts/smoke_log_analysis_coverage.py
scripts/smoke_html_usability.py
scripts/render_smoke.py
scripts/style_smoke.py
scripts/build_publish_bundle.py
scripts/verify_publish_bundle.py
scripts/build_release_archive.py
scripts/verify_release_archive.py
scripts/smoke_archive_payload_only.py
scripts/smoke_release_archive_extract.py
scripts/build_publication_handoff.py
scripts/verify_publication_handoff.py
scripts/prepare_publication_signoff.py
scripts/verify_publication_signoff.py
scripts/smoke_publication_signoff.py
scripts/smoke_final_publication_check.py
scripts/smoke_local_http_bundle.py
scripts/smoke_published_url.py
scripts/smoke_published_url_contract.py
scripts/smoke_goal_readiness.py
scripts/verify_goal_readiness.py
scripts/build_local_readiness_report.py
scripts/verify_local_readiness_report.py
scripts/build_publication_operator_packet.py
scripts/verify_publication_operator_packet.py
scripts/final_publication_check.py
scripts/release_check.py
```

GitHub Pages, 정적 호스팅, 연구실 서버 중 어느 쪽이든 같은 파일을 올릴 수
있다. 비공개 작업 문서와 원 분석 자료는 발행 대상에서 제외한다.
이 발행 경로는 `.git` 디렉토리를 요구하지 않는다. 현재 파일 트리와
`dist/`/archive 산출물을 기준으로 검증한다.

발행 직전 번들은 다음 명령으로 만든다.

```bash
python3 scripts/build_publish_bundle.py
python3 scripts/verify_publish_bundle.py
python3 scripts/smoke_no_git_dependency.py
python3 scripts/build_release_archive.py
python3 scripts/verify_release_archive.py
python3 scripts/smoke_archive_payload_only.py
python3 scripts/build_publication_handoff.py
python3 scripts/verify_publication_handoff.py
python3 scripts/build_local_readiness_report.py
python3 scripts/verify_local_readiness_report.py
python3 scripts/build_publication_operator_packet.py
python3 scripts/verify_publication_operator_packet.py
```

출력은 `dist/`에 생긴다. `verify_publish_bundle.py`는 manifest, checksum,
필수 공개 파일, 내부 파일 혼입, 금지 패턴을 확인한다. `dist/`는 생성물이고
원본은 Markdown, template, example, script다. 업로드용 archive는
`artifacts/publication/ai-research-practice-dist.tar.gz`에 생기며, archive 안의
파일은 `dist/`와 같은 checksum을 가져야 한다. 업로드 담당자에게 넘길 handoff는
`artifacts/publication/PUBLICATION_HANDOFF.md`와
`artifacts/publication/publication-handoff.json`에 남는다.
source owner가 archive, checksum, handoff, local readiness report를 한 번에
넘길 때는 `artifacts/publication/ai-research-practice-publication-operator-packet.tar.gz`를
사용한다.
`smoke_archive_payload_only.py`는 archive를 임시 디렉토리에 풀어 source scripts
없이 payload root만으로 manifest, checksum, top-level hosting root, source-only
파일 부재를 확인한다.

업로드 담당자에게 archive만 전달되는 경우에는 archive를 풀어 나온 payload root를
호스팅 루트로 삼는다. 그 루트에는 `.nojekyll`, `BUNDLE_MANIFEST.txt`,
`BUNDLE_SHA256SUMS.txt`, `index.html`, `guide.html`, `examples/`, `templates/`가
같은 층위에 있어야 한다. source repo owner는 공개 URL을 받은 뒤
`final_publication_check.py`와 browser sign-off validator를 실행한다.

source scripts 없이 archive payload만 받은 사람은 payload root에서 최소한
checksum 파일을 확인한다. POSIX shell에서는 다음 명령을 쓴다.

```bash
test "$(wc -l < BUNDLE_MANIFEST.txt)" = "$(wc -l < BUNDLE_SHA256SUMS.txt)"
awk '{print $1 "  " $3}' BUNDLE_SHA256SUMS.txt | sha256sum -c -
while read -r digest size path; do
  actual=$(wc -c < "$path" | tr -d ' ')
  test "$actual" = "$size" || { echo "size mismatch: $path"; exit 1; }
done < BUNDLE_SHA256SUMS.txt
```

PowerShell에서는 `Get-FileHash`로 같은 sha256과 size를 확인한다.

```powershell
if ((Get-Content .\BUNDLE_MANIFEST.txt).Count -ne (Get-Content .\BUNDLE_SHA256SUMS.txt).Count) {
  throw "manifest/checksum count mismatch"
}
Get-Content .\BUNDLE_SHA256SUMS.txt | ForEach-Object {
  $parts = $_ -split '\s+', 3
  $expectedHash = $parts[0].ToLower()
  $expectedSize = [int64]$parts[1]
  $path = $parts[2]
  $item = Get-Item -LiteralPath $path
  if ($item.Length -ne $expectedSize) { throw "size mismatch: $path" }
  $actualHash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLower()
  if ($actualHash -ne $expectedHash) { throw "sha256 mismatch: $path" }
}
```

발행 직전 전체 게이트는 한 번에 실행할 수 있다.

```bash
python3 scripts/release_check.py
```

## 5. 발행 후 확인한다

공개 URL을 받은 뒤에는 다음 smoke를 먼저 실행한다.

```bash
python3 scripts/final_publication_check.py https://your-host/ai-research-practice/ \
  --write-receipt artifacts/publication/final-publication-receipt.json
```

`your-host`는 실제 공개 host로 바꾼다. 그대로 실행하면 최종 gate가 실패한다.
이 명령은 `file://`, localhost, private IP, placeholder host를 거부한 뒤
`release_check.py --url ... --url-retries 6 --url-delay 10`을 실행한다. 공개
URL의 파일, checksum, source-only 경로, `guide.html` 렌더를 같이 본다. 발행
URL에서 다음 항목을 확인한다.

- 공개 URL 루트가 `index.html` redirect 또는 guide 본문을 제공하는가
- `index.html`이 `guide.html`로 연결되고 첫 화면 제목이 `로보틱스 연구자를 위한 AI 활용법`인가
- `guide.html`이 404 없이 열린다
- 공개 URL의 manifest와 checksum이 원격 파일 크기와 sha256을 검증하고, 로컬
  `dist/` checksum과 정확히 일치하는가
- 공개 guide와 Markdown에 첫 작업장 preflight,
  `artifacts/first-ai-session-message.txt`, `project-memory.json`,
  `이식 완료 조건`, `dataset·metric·artifact·claim`,
  `publication-browser-signoff.md`가 남아 있는가
- manifest에 실린 공개 텍스트 파일 전체가 private boundary scan을 통과하는가
- 공개 `guide.html` render smoke가 통과하는가
- quickstart의 template 링크 이름과 실제 repo 파일 이름이 맞는다
- `templates/publication-browser-signoff.md`에 `Checksum files`,
  `First workspace preflight`, `Codex porting acceptance` 확인 행이 있다
- 외부 repo와 논문 링크가 새 탭에서 열린다
- 공개 문서에 개인 작업 흔적이 보이지 않는다
- source-only 경로가 공개 URL에서 열리지 않는다

브라우저 직접 확인은 `templates/publication-browser-signoff.md` 형식으로
`artifacts/publication/publication-browser-signoff.md`에 남긴다. 자동 receipt에서
초안을 먼저 만들 수 있다.

```bash
python3 scripts/prepare_publication_signoff.py \
  --receipt artifacts/publication/final-publication-receipt.json \
  --output artifacts/publication/publication-browser-signoff.md
```

이 초안은 자동 gate 결과만 채운다. `Checked at`, browser matrix, public boundary,
최종 publication claim은 실제 브라우저 확인 뒤에 사람이 채워야 한다. browser
matrix에는 공개 checksum 파일, 첫 작업장 preflight, Codex porting acceptance
확인 행도 들어간다. 자동 gate receipt와 수동 sign-off가 같은 URL을 가리키는지는
다음 명령으로 확인한다.

```bash
python3 scripts/verify_publication_signoff.py \
  artifacts/publication/publication-browser-signoff.md \
  --public-url https://your-host/ai-research-practice/ \
  --receipt artifacts/publication/final-publication-receipt.json
```

발행 URL을 확인하기 전까지 publication은 완료가 아니다.
