# 로보틱스 연구자를 위한 AI 활용법

> 대화 로그 분석에서 뽑은 로보틱스/CV 연구용 AI 하네스.
> 새 환경에서 AI 셋업을 만들고, 바로 논문 읽기·코드 실행·실험 해석·원고 수정을 시작하기 위한 문서다.

[가이드 열기](guide.html)

[빠른 시작](QUICKSTART.md)

[용어 경계](TERMS.md)

[예시 작업장](EXAMPLE_WORKSPACE.md)

[운영 경로](PATH.md)

[배포](DEPLOY.md)

[발행 전 점검](PUBLISH.md)

[작업 로드맵](ROADMAP.md)

---

## 목표

로보틱스 연구 대화 로그에서 반복적으로 보인 성공 조건과 실패 조건을
정리한다. AI가 잘하는 일, 자주 무너지는 일, 그 이유를 따로 본다.

- ROS2, Docker, CUDA, dataset, bag replay처럼 환경과 물체가 있는 문제에서
  AI가 왜 자주 오진하는지 본다.
- SLAM/VIO/VPR/CV 논문을 paper-code-experiment 단위로 읽는 법을 정한다.
- 실험 숫자를 dataset, split, direction, metric, baseline, artifact가 묶인
  protocol 안에서 해석한다.
- reviewer pressure와 원고 문장을 claim/evidence 문제로 바꾼다.
- 반복 실패를 AGENTS, ledger, replay, template으로 남긴다.

## 핵심 생각

로보틱스 연구에서 AI 셋업의 단위는 연구 상태 전이다.

```text
world / robot / sensor
-> observation / log / dataset / code
-> representation / method assumption
-> experiment protocol / metric
-> paper claim / reviewer defense
```

도구는 이 체인의 한 구간을 돕는다. 하네스는 어느 구간을 보고 있는지,
무엇을 증거로 삼을 수 있는지, 어디까지 주장해도 되는지 정한다.

## source repo 구성

```
ai-research-practice/
├── .github/workflows/pages.yml
├── guide.html
├── QUICKSTART.md
├── TERMS.md
├── EXAMPLE_WORKSPACE.md
├── PATH.md
├── DEPLOY.md
├── PUBLISH.md
├── ROADMAP.md
├── scripts/
│   ├── build_guide.py
│   ├── smoke_runbook_toolchain_sync.py
│   ├── smoke_pages_workflow.py
│   ├── smoke_no_git_dependency.py
│   ├── verify_public.py
│   ├── smoke_quickstart.py
│   ├── smoke_first_workspace_rehearsal.py
│   ├── smoke_example_research_loop.py
│   ├── smoke_templates.py
│   ├── smoke_sources.py
│   ├── smoke_log_analysis_coverage.py
│   ├── smoke_html_usability.py
│   ├── render_smoke.py
│   ├── style_smoke.py
│   ├── build_publish_bundle.py
│   ├── verify_publish_bundle.py
│   ├── build_release_archive.py
│   ├── verify_release_archive.py
│   ├── smoke_archive_payload_only.py
│   ├── smoke_release_archive_extract.py
│   ├── build_publication_handoff.py
│   ├── verify_publication_handoff.py
│   ├── prepare_publication_signoff.py
│   ├── verify_publication_signoff.py
│   ├── smoke_publication_signoff.py
│   ├── smoke_final_publication_check.py
│   ├── smoke_local_http_bundle.py
│   ├── smoke_published_url.py
│   ├── smoke_published_url_contract.py
│   ├── smoke_goal_readiness.py
│   ├── verify_goal_readiness.py
│   ├── build_local_readiness_report.py
│   ├── verify_local_readiness_report.py
│   ├── build_publication_operator_packet.py
│   ├── verify_publication_operator_packet.py
│   ├── final_publication_check.py
│   └── release_check.py
├── chapter_01_start_here.md
├── chapter_02_environment.md
├── chapter_03_harness.md
├── chapter_04_research_workflows.md
├── chapter_05_experiment_protocol.md
├── chapter_06_stage_local_debugging.md
├── chapter_07_manuscript_rebuttal.md
├── chapter_08_external_templates.md
├── examples/
└── templates/
```

## 현재 단계

로컬 source repo는 발행 후보 상태다. 8장 원고, 빠른 시작, 용어 경계,
예시 작업장, 운영 경로, 배포 문서, 발행 점검, 템플릿, 정적 발행 번들이
갖춰졌다. 공개 URL에서 같은 검증을 통과해야 발행 완료로 본다.

공개 HTML은 챕터 원고에서 다시 만든다. 아래 명령은 source repo에서
실행한다. `dist/` 발행 번들에는 검증 script를 포함하지 않는다.
이 검증 명령은 `.git` 디렉토리를 요구하지 않는다. 현재 파일 트리와
`dist/`/archive 산출물을 기준으로 동작한다.

```bash
python3 scripts/build_guide.py
python3 scripts/smoke_runbook_toolchain_sync.py
python3 scripts/smoke_pages_workflow.py
python3 scripts/smoke_no_git_dependency.py
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
python3 scripts/build_publish_bundle.py
python3 scripts/verify_publish_bundle.py
python3 scripts/build_release_archive.py
python3 scripts/verify_release_archive.py
python3 scripts/smoke_archive_payload_only.py
python3 scripts/smoke_release_archive_extract.py
python3 scripts/build_publication_handoff.py
python3 scripts/verify_publication_handoff.py
python3 scripts/prepare_publication_signoff.py
python3 scripts/verify_publication_signoff.py
python3 scripts/smoke_publication_signoff.py
python3 scripts/smoke_final_publication_check.py
python3 scripts/smoke_local_http_bundle.py
python3 scripts/smoke_published_url.py
python3 scripts/smoke_published_url_contract.py
python3 scripts/smoke_goal_readiness.py
python3 scripts/verify_goal_readiness.py
python3 scripts/build_local_readiness_report.py
python3 scripts/verify_local_readiness_report.py
python3 scripts/build_publication_operator_packet.py
python3 scripts/verify_publication_operator_packet.py
```

발행 직전에는 같은 과정을 한 번에 실행할 수 있다.

```bash
python3 scripts/release_check.py
```

발행 후에는 공개 URL을 같은 기준으로 확인한다.

```bash
python3 scripts/final_publication_check.py https://your-host/ai-research-practice/ \
  --write-receipt artifacts/publication/final-publication-receipt.json
python3 scripts/prepare_publication_signoff.py \
  --receipt artifacts/publication/final-publication-receipt.json \
  --output artifacts/publication/publication-browser-signoff.md
```

`your-host`는 실제 공개 host로 바꾼다. 그대로 실행하면 최종 gate가 실패한다.
이 명령은 `file://`, localhost, placeholder host를 거부한 뒤 공개 URL의
checksum이 로컬 `dist/` checksum과 같은지, source-only 경계가 지켜지는지,
공개 `guide.html`이 렌더되는지 확인한다. GitHub Pages workflow는 배포 뒤
`page_url`에 `release_check.py --url ... --skip-render`를 실행하고, 최종 수동
완료 판단은 위 명령과 `templates/publication-browser-signoff.md`에 남긴 브라우저
직접 확인으로 한다. 작성한 sign-off는
`python3 scripts/verify_publication_signoff.py ...`로 자동 receipt와 같은 공개
URL을 가리키는지 확인한다.

## 참고한 축

- 실제 로보틱스/CV 연구 대화 분석에서 추출한 반복 요청, 성공 패턴, 실패 패턴
- 로컬 research harness의 state transition, evidence gate, replay 개념
- 공개 agent/skills repo의 구조와 설치 방식
- `robotics-practice`, `research-notes`, `grad-notes`의 톤과 pipeline 운영 방식

원 대화 로그와 개인 프로젝트 경로는 공개 문서에 포함하지 않는다.
