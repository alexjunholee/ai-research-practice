# 로보틱스 연구자를 위한 AI 활용법

> 대화 로그 분석에서 뽑은 로보틱스/CV 연구용 AI 활용 가이드.
> AI가 잘하는 일과 못하는 일, 그 차이가 생기는 이유, 용도별 도구 역할,
> 하네스라는 판단 구조를 설명하는 문서다.

[가이드 열기](guide.html)

[부록 A — 작업장 파일](QUICKSTART.md)

[용어 경계](TERMS.md)

[예시 작업장](EXAMPLE_WORKSPACE.md)

[부록 C — 작업 리듬](PATH.md)

[작업 로드맵](ROADMAP.md)

발행 절차와 자동 점검 문서는 repo 안에 남겨 두지만, 현재 독자용 본문에서는
앞세우지 않는다.

---

## 목표

로보틱스 연구 대화 로그에서 반복적으로 보인 성공 조건과 실패 조건을
정리한다. 설치 순서보다 먼저 AI가 잘하는 일, 자주 무너지는 일, 그 이유를
따로 본다.

- AI가 후보를 싸게 늘리는 능력과 사람이 비용 있는 연구 행동을 선택해야
  하는 상황을 먼저 설명한다.
- ROS2, Docker, CUDA, dataset, bag replay처럼 환경과 물체가 있는 문제에서
  AI가 왜 자주 오진하는지 본다.
- SLAM/VIO/VPR/CV 논문을 paper-code-experiment 단위로 읽는 법을 정한다.
- 실험 숫자를 dataset, split, direction, metric, baseline, artifact가 묶인
  protocol 안에서 해석한다.
- reviewer pressure와 원고 문장을 claim/evidence 문제로 바꾼다.

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
│   ├── verify_*.py
│   ├── build_*.py
│   └── release/publication helpers
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

공개 홈페이지 링크를 내리고 구조를 다시 쓰는 중이다. 이전 초고는 새 환경
셋업과 발행 절차 설명으로 중심이 기울었다. 다음 원고는 AI 사용의 기본
그림에서 시작한다.

```text
AI가 잘하는 일
AI가 못하는 일
그 차이가 생기는 이유
사람이 감당하는 연구 위험
하네스가 고정하는 판단 구조
```

공개 HTML은 챕터 원고에서 다시 만든다. `guide.html`을 손으로 고치지 않는다.

## 참고한 축

- 실제 로보틱스/CV 연구 대화 분석에서 추출한 반복 요청, 성공 패턴, 실패 패턴
- 로컬 research harness의 state transition, evidence gate, replay 개념
- 공개 agent/skills repo의 구조와 설치 방식
- `robotics-practice`, `research-notes`, `grad-notes`의 톤과 pipeline 운영 방식

원 대화 로그와 개인 프로젝트 경로는 공개 문서에 포함하지 않는다.
