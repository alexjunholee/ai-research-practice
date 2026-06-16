# 배포 — dist/만 공개한다

발행 대상은 source repo 전체가 아니다. 공개 호스팅에는 `dist/` 안의 파일만
올린다. `scripts/`, 내부 작업 메모, 원 분석 자료, 상태 파일은 source repo에
남긴다.

## 공통 순서

어느 호스팅을 쓰든 순서는 같다.

```bash
python3 scripts/release_check.py
```

통과하면 `dist/`를 정적 발행 단위로 삼는다. 같은 내용의 업로드용 archive는
`artifacts/publication/ai-research-practice-dist.tar.gz`에 만든다. 업로드
handoff는 `artifacts/publication/PUBLICATION_HANDOFF.md`에 만든다.
`scripts/smoke_archive_payload_only.py`는 이 archive를 임시 디렉토리에 풀고
source script 없이 payload root만으로 manifest, checksum, source-only 파일
부재를 확인한다.

```text
dist/
├── .nojekyll
├── BUNDLE_MANIFEST.txt
├── BUNDLE_SHA256SUMS.txt
├── index.html
├── guide.html
├── README.md
├── QUICKSTART.md
├── TERMS.md
├── EXAMPLE_WORKSPACE.md
├── PATH.md
├── PUBLISH.md
├── DEPLOY.md
├── ROADMAP.md
├── SOURCES.md
├── chapter_*.md
├── examples/
└── templates/
```

호스팅 루트는 `dist/` 안쪽 파일들이 놓이는 위치다. 공개 URL에서
`index.html`과 `guide.html`이 바로 열려야 한다.

## archive만 받은 경우

업로드 담당자가 source repo 없이
`ai-research-practice-dist.tar.gz`만 받았다면 archive를 풀고, 풀린 디렉토리의
안쪽 파일들을 호스팅 루트에 그대로 둔다. 호스팅 루트에는 최소한 다음 파일이
같은 층위에 있어야 한다.

```text
.nojekyll
BUNDLE_MANIFEST.txt
BUNDLE_SHA256SUMS.txt
index.html
guide.html
README.md
DEPLOY.md
PUBLISH.md
examples/
templates/
```

archive 안의 `BUNDLE_MANIFEST.txt`와 `BUNDLE_SHA256SUMS.txt`는 업로드 payload를
확인하기 위한 파일이다. 검증 script와 최종 receipt 생성은 source repo에 남아
있으므로, source repo owner가 공개 URL을 받은 뒤 다음 gate를 실행한다.
archive를 넘기기 전 source repo owner는 같은 payload-only 경로를 다음 명령으로
미리 재현한다.

```bash
python3 scripts/smoke_archive_payload_only.py
```

source scripts 없이 payload 내부 checksum만 확인할 때는 payload root에서 다음을
실행한다. POSIX shell에서는 checksum 파일을 표준 `sha256sum -c` 입력으로
바꾸고, size 열도 따로 확인한다.

```bash
test -f BUNDLE_MANIFEST.txt
test -f BUNDLE_SHA256SUMS.txt
test "$(wc -l < BUNDLE_MANIFEST.txt)" = "$(wc -l < BUNDLE_SHA256SUMS.txt)"
awk '{print $1 "  " $3}' BUNDLE_SHA256SUMS.txt | sha256sum -c -
while read -r digest size path; do
  actual=$(wc -c < "$path" | tr -d ' ')
  test "$actual" = "$size" || { echo "size mismatch: $path"; exit 1; }
done < BUNDLE_SHA256SUMS.txt
```

Windows PowerShell에서는 같은 파일을 다음처럼 확인한다.

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

이 확인은 archive에서 풀린 payload 파일의 무결성만 확인한다. 공개 URL 완료
판정은 source repo owner의 URL gate와 browser sign-off에서 닫힌다.

```bash
python3 scripts/final_publication_check.py https://your-host/ai-research-practice/ \
  --write-receipt artifacts/publication/final-publication-receipt.json
```

archive 업로드만으로는 publication claim을 닫지 않는다. 공개 URL에서 checksum,
manifest, private boundary, browser sign-off가 같은 bundle을 가리킬 때 완료로
본다.

## GitHub Pages

GitHub Pages를 쓸 때도 source repo 전체를 Pages source로 잡지 않는다.
`dist/` 산출물만 Pages branch나 Pages artifact에 올린다.

이 repo에는 GitHub Pages용 workflow가 들어 있다.

```text
.github/workflows/pages.yml
```

workflow 권한은 `contents: read`, `actions: read`, `pages: write`,
`id-token: write`를 쓴다. Pages artifact 배포와 배포 후 smoke에 필요한 최소
권한만 둔다.

GitHub repository 설정에서 Pages source를 GitHub Actions로 둔다. `main` branch에
push하거나 workflow를 수동 실행하면 workflow가 다음 순서로 돈다.

```text
checkout
-> python3 scripts/release_check.py --skip-render
-> upload dist/ as Pages artifact
-> deploy to github-pages environment
-> python3 scripts/release_check.py --url page_url --url-retries 6 --url-delay 10 --skip-render
```

CI에서는 renderer 설치 상태가 runner 이미지에 따라 달라질 수 있으므로
`--skip-render`를 쓴다. 로컬 source repo에서는 발행 전에
`python3 scripts/release_check.py`를 실행해 render smoke까지 확인한다. 배포 job은
GitHub Pages가 반환한 `page_url`을 `release_check.py --url ... --skip-render`로
다시 확인한다.

`dist/.nojekyll`도 checksum manifest에 들어간다. Pages artifact 업로드에서는
hidden file이 기본 제외되므로 workflow는 `include-hidden-files: true`를 명시한다.

수동 배포라면 다음 원칙을 지킨다.

```text
source repo
-> python3 scripts/release_check.py
-> dist/ contents or artifacts/publication/ai-research-practice-dist.tar.gz
-> pages branch or static hosting root
-> python3 scripts/final_publication_check.py PUBLIC_URL --write-receipt artifacts/publication/final-publication-receipt.json
```

동기화 폴더 안에서 git metadata 충돌이 나는 환경이라면 먼저 git 저장소 위치를
분리한다. 공개 산출물은 `dist/`의 정적 파일이고, git 운영 방식은 호스팅을
위한 수송 수단일 뿐이다.
발행 검증은 `.git` 디렉토리를 요구하지 않는다. 현재 파일 트리에서
`python3 scripts/release_check.py`를 통과시키고, `dist/`나 archive payload만
공개 호스팅에 올린다.

## 정적 파일 호스트

Netlify, Vercel static output, Cloudflare Pages, object storage, 연구실 웹
서버도 같은 구조를 쓴다. upload directory는 `dist/`이고 publish directory는
호스팅 루트다. archive 업로드를 받는 호스트라면
`artifacts/publication/ai-research-practice-dist.tar.gz`를 풀었을 때 나오는
파일들을 호스팅 루트에 둔다.

배포 뒤에는 source repo에서 URL smoke를 실행한다.

```bash
python3 scripts/final_publication_check.py https://your-host/ai-research-practice/ \
  --write-receipt artifacts/publication/final-publication-receipt.json
```

`your-host`는 실제 공개 host로 바꾼다. 그대로 실행하면 최종 gate가 실패한다.
이 smoke는 `file://`, localhost, private IP, placeholder host를 먼저 거부한
뒤 다음 항목을 확인한다. 기본값은 공개 `guide.html`도
`scripts/render_smoke.py --url`로 렌더한다.

- 공개 URL 루트가 `index.html` redirect 또는 guide 본문을 제공하고,
  `index.html`은 제목, meta refresh, fallback link로 `guide.html`을 가리킨다
- `guide.html`과 주요 Markdown 파일이 열린다
- `BUNDLE_MANIFEST.txt`와 `BUNDLE_SHA256SUMS.txt`가 열리고, manifest에 적힌
  모든 파일의 크기와 sha256이 맞는다
- 공개 URL의 `BUNDLE_SHA256SUMS.txt`가 로컬에서 방금 만든 `dist/` checksum과
  정확히 같다
- guide에 빠른 시작, 용어 경계, 예시 작업장, 운영 경로, 8장, 출처 목록이 들어 있다
- guide와 공개 Markdown에 첫 작업장 preflight,
  `artifacts/first-ai-session-message.txt`, `project-memory.json`,
  `이식 완료 조건`, `dataset·metric·artifact·claim`,
  `publication-browser-signoff.md`가 남아 있다
- render smoke가 PDF를 만든 경우 핵심 텍스트를 렌더 산출물에서도 추출한다
- template과 example 파일이 실제 URL에서 열린다
- `templates/publication-browser-signoff.md`에 `Checksum files`,
  `First workspace preflight`, `Codex porting acceptance` 확인 행이 있다
- 외부 repo와 이론 출처 링크 문자열이 남아 있다
- 본문에 쓰인 실질 외부 URL을 `SOURCES.md`에 등록했고, 생성 HTML의 외부 링크는
  새 탭 격리 속성을 가진다
- manifest에 실린 공개 텍스트 파일 전체에서 개인 경로, 원 대화 원문, 내부
  작업 디렉토리명이 보이지 않는다
- source-only 상태 파일, 내부 작업 메모, 검증 script, 렌더 artifact가 공개
  URL에서 열리지 않는다

## 연구실 서버

연구실 서버나 개인 서버에 올릴 때도 `dist/` 안쪽 파일만 복사한다.

```bash
rsync -av --delete dist/ user@host:/path/to/public/ai-research-practice/
```

`--delete`를 쓰면 서버에 남은 오래된 파일을 지운다. 처음 배포하기 전에는
대상 경로가 맞는지 반드시 빈 테스트 디렉토리에서 확인한다.

서버가 subpath에서 문서를 제공하면 공개 URL은 trailing slash로 확인한다.

```bash
python3 scripts/final_publication_check.py https://your-host/ai-research-practice/ \
  --write-receipt artifacts/publication/final-publication-receipt.json
```

`your-host`는 실제 공개 host로 바꾼다. 그대로 실행하면 최종 gate가 실패한다.

## 완료 기준

publication 완료는 다음 조건이 모두 참일 때만 말한다.

- source repo에서 `python3 scripts/release_check.py`가 통과했다
- 공개 URL에서 `python3 scripts/final_publication_check.py PUBLIC_URL --write-receipt ...`가 통과했다
- 자동 URL render smoke와 브라우저 직접 확인에서 첫 화면, sidebar, mobile 폭을 확인했다
- 브라우저 직접 확인에서 공개 checksum 파일, 첫 작업장 preflight, Codex porting
  acceptance가 보이는지 확인했다
- `templates/publication-browser-signoff.md` 형식으로 직접 확인 결과를 남겼다
- `python3 scripts/verify_publication_signoff.py ...`가 자동 receipt와 브라우저
  sign-off를 같은 공개 URL에 대해 검증했다
- 공개 문서에 개인 작업 흔적이 보이지 않는다

URL smoke가 통과하기 전의 상태는 "발행 가능한 번들"이다. "발행 완료"가
아니다.
