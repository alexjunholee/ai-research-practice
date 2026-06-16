# Roadmap

## 현재 상태

홈페이지 링크를 내리고 원고를 다시 쓴다. 이전 초고는 새 환경 셋업과 발행
절차 설명이 앞에 서 있었다. 새 원고는 AI 사용의 기본 그림에서 시작한다.

기준 문서는 `harness/style-benchmark-audit.md`다. `research-notes`,
`grad-notes`, `slam-history-book`, `robotics-practice`, `sensor-fusion-guide`의
초반 장을 읽어 장르 기준을 잡았다.

## 새 목표

로보틱스/CV 연구자가 AI를 연구 도구로 제대로 쓰기 위한 한국어 가이드.
독자는 도구 이름보다 먼저 다음 그림을 이해해야 한다.

```text
AI가 잘하는 일
AI가 못하는 일
그 차이가 생기는 이유
사람이 감당하는 연구 위험
하네스가 고정하는 판단 구조
```

## Stage 1: 구조 재정의

상태: 진행 중.

- opener를 인간-AI 행동 구조에서 시작하게 한다.
- 시계열 구성과 입문 순서 문구를 중심 목차에서 제거한다.
- 셋업, 템플릿, 발행 절차는 부록으로 낮춘다.
- `outlines/repo-plan.md`를 새 구조로 유지한다.
- 각 장의 계약을 `opening pressure -> human-AI conflict -> robotics/CV object
  -> source/log evidence -> what AI does well -> where AI fails -> human
  decision -> harness fix -> closing return`으로 잡는다.

## Stage 2: 본문 재작성

상태: Ch.1 opener를 먼저 교체함.

- Ch.1은 AI의 후보 생성과 인간의 risk-bearing action 충돌을 한 장면에서
  시작한다. 이론 이름은 장면 뒤에 필요한 만큼만 붙인다.
- Ch.2는 연구 상태가 사람과 artifact 사이에 흩어져 있다는 문제로 다시
  시작한다.
- Ch.3은 로그 분석을 표 설명이 아니라 하네스가 왜 발산을 수렴시키는지
  보여주는 판단 구조로 다시 쓴다.
- Ch.4-7은 용도별 사용법으로 재배치한다: 논문 읽기, 코드/실험, 디버깅,
  원고와 rebuttal.
- Ch.8은 외부 agent repo를 유명 repo 소개가 아니라 구조 해부로 읽는다.

Stage 2 중에는 발행 점검 설명을 늘리지 않는다. 글이 먼저다.

## Stage 3: 산문 교정

상태: 예정.

- `STYLE_PROSE.md`와 `EDITOR_PERSONA.md`를 기준으로 문단 단위 음독 교정을 한다.
- 챕터 메타 선언, 번역체, 부정 대조, 자기 작법 설명체를 줄인다.
- 표와 bullet이 본문을 대신하지 않게 한다.
- 논문과 이론 출처는 문장 안에서 필요한 만큼만 쓴다.
- "AI가 만든 후보는 싸다. 사람의 행동은 비싸다." 같은 중심 문장은 살리되,
  그 주변의 영문식 추상어를 한국어 문장으로 낮춘다.

## Stage 4: 다시 공개할지 판단

상태: 보류.

홈페이지에 다시 올릴지는 원고가 산문과 구조를 회복한 뒤 판단한다. 지금은
발행 검증보다 글의 첫 인상, 중심 논지, 국문 문체가 우선이다.
