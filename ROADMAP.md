# Roadmap

## 목표

이 repository는 로보틱스/CV 연구자가 AI를 연구 운영에 붙이는 법을 다루는
공개 한국어 가이드다. 새 사용자는 이 문서를 읽고 자기 작업 공간을
만들고, agent 규칙과 템플릿을 붙이고, 논문 읽기·코드 실행·실험 해석·원고
수정을 바로 시작할 수 있어야 한다.

핵심 근거는 로컬 연구 대화 로그 분석이다. 공개 본문은 원 대화 원문을
싣지 않고, 반복적으로 보인 성공 조건, 실패 조건, 실패 이유, 하네스 규칙만
일반화해 쓴다.

## 완성 조건

- 제목과 본문이 로보틱스/CV 연구용 AI 활용법으로 읽힌다.
- 각 장이 로그 분석 기반의 `잘되는 조건`, `잘 안되는 조건`, `이유`,
  `하네스 규칙`을 포함한다.
- ROS2, Docker, CUDA, dataset, SLAM/VIO/VPR, metric, reviewer response처럼
  분야 물체가 본문 앞쪽에 나온다.
- 독자가 `AGENTS.md`, project memory, experiment contract, dataset audit,
  paper-code map, result provenance, replay case를 자기 workspace에 붙일 수
  있다.
- 외부 agent/skills repo는 그대로 복사하지 않고, 로보틱스 연구 하네스
  관점에서 가져올 패턴과 부족한 점을 나누어 읽는다.
- `guide.html`은 `chapter_*.md`에서 생성되고 브라우저에서 바로 열린다.
- 공개 파일에는 원 대화 원문, 개인 경로, 비밀값, 내부 하네스 로그가
  들어가지 않는다.

## 작업 계획

### Stage 1: Scaffold

상태: 완료.

- 기존 범용 AI 연구 가이드 구조를 로보틱스/CV 연구 구조로 재정의한다.
- 로컬 로그 분석에서 나온 안정 패턴을 공개 가능한 원칙으로 정리한다.
- 공개 agent/skills repo에서 가져올 패턴을 보조 자료로 둔다.
- 초기 템플릿을 로보틱스 연구 단위로 보강한다.
- 정적 `guide.html` 생성 경로를 유지한다.

### Stage 2: Draft

상태: 8장 초고 작성됨. 이후에는 절차 검증과 문체 정리가 필요하다.

- 각 장을 `로그 경향 -> 잘되는 조건 -> 잘 안되는 조건 -> 이유 -> 하네스 규칙`
  흐름으로 확장한다.
- 첫날에는 workspace와 truth source를 복원하게 한다.
- 첫 주에는 paper-code-experiment 루프와 stage-local debugging을 돌리게 한다.
- 첫 달에는 replay, project memory, reviewer/claim gate를 쌓게 한다.
- 원 대화 로그는 공개 본문에 넣지 않고 일반화된 교훈만 반영한다.

### Stage 3: Revise

상태: 로컬 검증 게이트 작성됨. Quickstart, 용어 경계, 예시 작업장, 발행 전
점검, public verification gate, quickstart smoke gate, render smoke
fallback, style smoke gate를 추가했다.

- 빈 환경에서 절차를 따라 할 수 있는지 확인한다.
- tool, agent, harness, skill, memory, ledger 용어가 섞이지 않는지 점검한다.
- 모든 claim을 evidence boundary에 맞춰 재확인한다.
- 로보틱스/CV 물체 없이 떠 있는 일반론을 제거한다.

### Stage 3b: Coherence

상태: 로컬 arc 작성됨. `PATH.md`로 첫날, 첫 주, 첫 달 운영 경로를 추가했고,
예시 작업장이 그 경로를 따라가도록 맞췄다.

- 전체 흐름을 `로보틱스 AI 실패 장면 -> 로그 분석 -> 하네스 규칙 -> 연구 루프
  -> 템플릿` arc로 맞춘다.
- 장 사이의 반복 정의를 줄인다.
- 모든 템플릿이 본문에서 먼저 소개된 뒤 사용되게 한다.

### Stage 4: Edit And Publish

상태: 로컬 발행 후보. 정적 발행 번들과 배포 절차는 준비되었고, 남은 완료
조건은 실제 공개 URL smoke다.

- 공개/비공개 경계 검사를 실행한다.
- `guide.html`을 재생성한다.
- `index.html`과 `guide.html`을 로컬에서 확인한다.
- `dist/` 안쪽 파일만 GitHub Pages나 다른 정적 호스팅 대상으로 발행한다.
- 공개 URL에서 URL smoke를 실행한다.

## 지금 다음 할 일

- source repo에서 `python3 scripts/release_check.py`를 실행한다.
- `dist/` 안쪽 파일만 호스팅에 올린다.
- 공개 URL에서 `python3 scripts/final_publication_check.py PUBLIC_URL --write-receipt artifacts/publication/final-publication-receipt.json`을 실행한다.
- desktop과 mobile 폭에서 첫 화면, navigation, 템플릿 링크를 확인하고 `artifacts/publication/publication-browser-signoff.md`에 남긴다.
- `python3 scripts/verify_publication_signoff.py artifacts/publication/publication-browser-signoff.md --public-url PUBLIC_URL --receipt artifacts/publication/final-publication-receipt.json`을 실행한다.
