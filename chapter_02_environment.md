# Ch.2 — 현재 상태부터 복원한다

“어디까지 했지?”라는 요청 뒤에는 회고보다 큰 일이 붙어 있었다. 대화 기록에서 이 요청은
repo 상태, 이전 실험, 원고 범위, pending task를 다시 이어 붙이라는 뜻으로 자주 나왔다.
사용자가 원한 것은 채팅 요약보다 현재 연구 상태에 가까웠다. 어느 파일이 source of truth인지,
어느 결과가 최신인지, 어느 claim이 아직 닫히지 않았는지.

연구 상태는 한 파일에 들어 있지 않다. 코드 저장소, launch file, Dockerfile, bag, calibration
note, result table, figure source, TeX 문장, reviewer memo가 따로 움직인다. 어느 날에는
`fixed_launch.py`가 실제 예제에서 불리지 않는다. `final_results.csv` 옆에
`final_results_old.csv`와 `final_results_recheck.csv`가 함께 남는다. 같은 명령이 옵션만
바뀐 채 shell history에 세 번 남아 있기도 하다.

AI는 이런 상태에서 요약을 잘 만든다. 그 요약은 다음에 열 파일을 가리키는 데까지 간다.
`runs/` 아래의 어느 폴더를 볼지, 어떤 table을 다시 열지, 어떤 issue thread가 관련 있는지
찾는 데는 충분하다. 거기서 멈추면 위험하다. “성능이 개선되었습니다”라는 문장만으로는 split,
sequence count, metric script, excluded failure를 알 수 없다.

좋게 끝난 재개 세션은 먼저 읽을 표면을 정했다. repo status, README, 최근 commit, 결과
폴더, 실행 로그, 원고 diff, reviewer comment를 한꺼번에 현재 상태로 올리지 않았다. 각각을
증거 등급으로 놓았다. raw file, command output, generated summary, memory note, assistant
inference는 서로 다른 무게를 가진다.

공개 문서와 비공개 기록도 이 자리에서 갈린다. 원 대화 로그, 개인 경로, 심사위원 원문,
미공개 실험 결과, 인증 정보는 밖으로 나가지 않는다. 공개할 수 있는 것은 반복된 구조다.
파일 이름만 보고 상태를 추정하면 틀린다. 요약만 보고 metric을 믿으면 숫자가 부풀어 오른다.
reviewer 문장을 문체 문제로만 보면 claim은 그대로 열린다.

도구를 옮길 때도 같은 원리가 남는다. 예전 Claude용 규칙 파일, slash command, skill,
permission 설정을 Codex에서 다시 쓰려면 이름보다 행동을 읽는다. “작게 고쳐라”는 여전히
통한다. “가정을 말하라”도 남는다. 특정 호출법, 특정 권한 설정, 특정 extension의 관습은
새 환경에서 그대로 맞지 않을 수 있다. 수행자 이름을 옮기는 대신 처음 읽을 파일의 순서,
손대도 되는 범위, 완료를 말할 수 있는 증거를 옮긴다.

재개는 현재 상태를 다시 만드는 작업이다. 그 작업이 끝나기 전에는 AI가 아무리 그럴듯한
다음 단계를 말해도 아직 시작선에 서 있는 셈이다.
