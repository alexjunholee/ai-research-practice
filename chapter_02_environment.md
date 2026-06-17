# Ch.2 — 현재 상태는 파일 하나에 없다

"어디까지 했지?"라는 질문은 단순한 요약 요청처럼 보인다. 실제 대화에서는 거의 그렇지 않았다.
사용자는 repo 상태, 실험 결과, 원고 범위, 남은 결정을 한 번에 되살리고 싶어 했다. 어느 파일이
source of truth인지, 어느 결과가 최신인지, 어느 claim이 아직 위험한지 알아야 다음 손을 댈 수
있었다.

로보틱스 연구의 현재 상태는 한 파일에 담기지 않는다. launch file, Dockerfile, bag,
calibration note, result table, figure source, TeX 문장, reviewer memo가 각자 다른 속도로
바뀐다. `fixed_launch.py`가 있어도 실제 예제가 그 파일을 부르지 않을 수 있다.
`final_results.csv` 옆에 `final_results_old.csv`와 `final_results_recheck.csv`가 같이 남아
있을 수 있다. shell history에는 같은 명령이 옵션만 바뀐 채 세 번 남는다.

AI는 이런 상황에서 방향을 빨리 잡는다. 어떤 폴더를 열지, 어떤 table을 다시 볼지, 어떤 issue
thread가 관련 있는지 찾는 데 강하다. 그 덕분에 다음 파일까지 빨리 간다. 다만 요약은 길 안내까지다. 요약문
하나로 split, sequence count, metric script, excluded failure를 닫을 수는 없다.

좋게 이어진 재개 세션은 표면을 섞지 않았다. repo status, README, 최근 commit, 결과 폴더,
실행 로그, 원고 diff, reviewer comment를 모두 같은 무게로 올리지 않았다. raw file은 raw
file이고, command output은 command output이며, memory note는 다음에 볼 곳을 알려 주는 표식이다.
AI가 만든 inference는 다시 확인할 후보로 둔다.

망가진 재개 세션은 대개 현재 상태를 너무 빨리 선언했다. "이 결과가 최신입니다"라고 말한 뒤에
그 결과를 만든 command가 없었다. "수정 완료"라고 썼는데 diff는 문장만 바뀌어 있었다. "baseline
대비 개선"이라고 적었지만 baseline의 split이 달랐다. 현재 상태를 잘못 잡으면 다음 행동이
전부 그 위에 쌓인다.

공개 문서와 비공개 기록도 이때 분리된다. 원 대화 로그, 개인 경로, reviewer 원문, 미공개 실험
숫자, 인증 정보는 밖으로 나가지 않는다. 밖으로 나갈 수 있는 것은 사건의 구조다. 파일 이름만
보고 상태를 믿으면 틀린다. 요약만 보고 metric을 믿으면 숫자가 부푼다. reviewer 문장을 문체
문제로만 보면 공격받은 claim은 그대로 남는다.

Claude용 규칙을 Codex로 옮길 때도 같은 원리가 작동한다. 수행자 이름보다 행동 규칙을 옮긴다.
처음 읽을 파일의 순서, 손대도 되는 범위, 실행 전에 말해야 할 가정, 완료를 말할 수
있는 증거. 특정 slash command와 permission 설정은 새 도구에서 모양이 달라진다. 그러나 현재
상태를 먼저 세우는 습관은 그대로 살아남는다.

재개는 과거를 예쁘게 요약하는 자리가 아니다. 다음 행동이 올라설 현재를 다시 세우는 자리다. 그
일이 끝나기 전에는 AI가 아무리 그럴듯한 다음 단계를 말해도 아직 연구는 움직이지 않았다.
