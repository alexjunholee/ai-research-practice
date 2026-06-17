# Ch.4 — 논문은 코드 경로까지 읽힌다

ORB-SLAM3 논문을 읽으면 줄거리는 빠르게 잡힌다. feature, map, loop closing, inertial
initialization이 한 흐름으로 보인다. AI도 이 요약을 잘한다. 기존 방법의 어느 압박을 풀었는지,
어떤 모듈이 새로 들어갔는지, 저장소에서 어느 파일부터 열 만한지 빠르게 정리한다.

논문 요약에서 실행 경로로 내려가면 일이 달라진다. 어떤 YAML이 실제 예제에서 불리는지,
논문에 나온 ablation이 공개 코드에도 남아 있는지, 설정 파일의 옵션이 optimizer까지
도달하는지 확인할 차례가 온다. 공개 저장소에는 논문 당시 코드, camera-ready 뒤 수정,
issue 답변용 임시 패치, 이제 불리지 않는 예제 스크립트가 함께 남는다.

FAST-LIO2도 같은 식으로 읽힌다. ikd-tree, deskew, IMU propagation, residual update라는
이름만 알면 설명은 가능하다. 재현은 다른 문제다. EuRoC나 KITTI 예제를 다시 돌릴 때는
sensor time, trajectory frame, sequence exclusion, evaluation script가 앞에 나온다. method
이름을 아는 것과 같은 조건에서 숫자를 얻는 일은 이어져 있지만 붙어 있지 않다.

대화 기록에서 자주 드러난 구분이 있다. 코드에 존재하는 것과 실제로 쓰이는 것은 다르다.
factor가 source에 있을 수 있다. config key도 있을 수 있다. documentation에는 planned
feature로 적혀 있을 수 있다. 그래도 optimizer가 그 factor를 소비하지 않으면 paper method의
근거가 되지 않는다. 그래서 implementation audit에는 active, disabled, configured-unused,
planned-only, tested-failed, dead 같은 이름이 필요했다.

AI는 이 작업의 앞부분에서 강하다. repo를 훑고, function 이름을 찾고, issue thread를 모으고,
paper와 code의 후보 연결을 만든다. 그다음 질문은 더 엄격해진다. 이 함수가 실제로 호출되는가.
이 config가 runtime에 읽히는가. 이 script가 논문 표의 숫자를 만든 script인가. issue에서
바뀐 convention이 현재 branch에도 들어왔는가.

논문 한 편을 내 연구에 붙일 때는 code path, experiment path, claim path가 함께 간다.
paper-code-experiment map은 이 세 줄을 한 장에 놓는다. 논문이 무엇을 주장했고, 공개 코드가
무엇을 실제로 돌리며, 내가 어느 조건에서 비교할 수 있는지.

다음 질문은 초록에서 나오지 않는다. 대개 YAML, 실행 명령, issue, 실패한 sequence, table
caption에서 나온다.
