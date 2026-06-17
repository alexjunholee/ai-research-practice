# Ch.4 — 논문은 실행 경로로 읽는다

ORB-SLAM3 논문을 읽으면 줄거리는 금방 잡힌다. feature, map, loop closing, inertial
initialization이 한 흐름으로 보인다. AI도 이 요약을 잘한다. 어떤 모듈이 새로 들어갔는지,
기존 방법의 압박을 어디서 풀었는지, 저장소에서 어느 파일부터 열 만한지 빠르게 정리한다.

그다음부터 논문 읽기는 코드 읽기로 내려온다. 어떤 YAML이 실제 예제에서 불리는가. 논문에 나온
ablation이 공개 코드에도 남아 있는가. config key가 optimizer까지 도달하는가. 공개 저장소에는
논문 당시 코드, camera-ready 뒤 수정, issue 답변용 임시 패치, 이제는 불리지 않는 예제 스크립트가
한꺼번에 남는다.

FAST-LIO2도 마찬가지다. ikd-tree, deskew, IMU propagation, residual update라는 이름을 알면
설명은 가능하다. 재현은 다른 일이다. EuRoC나 KITTI 예제를 다시 돌릴 때는 sensor time,
trajectory frame, sequence exclusion, evaluation script가 먼저 걸린다. method 이름을 아는
것과 같은 조건에서 숫자를 얻는 일 사이에는 꽤 긴 길이 있다.

대화 기록에서 자주 나온 오류는 코드의 존재를 방법의 증거로 올리는 일이었다. source에 factor가
있을 수 있다. config key도 있을 수 있다. documentation에는 planned feature로 적혀 있을 수
있다. 그래도 runtime에서 그 factor가 optimizer로 들어가지 않으면 논문 method의 증거가 되지
않는다. 이때 필요한 말은 active, disabled, configured-unused, planned-only, tested-failed,
dead 같은 상태 이름이다.

AI는 이 작업의 초입에서 강하다. repo를 훑고, function 이름을 찾고, issue thread를 모으고,
paper와 code의 후보 연결을 만든다. 연구자가 이어서 물어야 할 질문은 더 좁다. 이 함수가
실제로 호출되는가. 이 config가 runtime에 읽히는가. 이 script가 논문 표의 숫자를 만든 script인가.
issue에서 바뀐 convention이 현재 branch에도 들어왔는가.

논문 한 편을 내 연구에 붙일 때는 세 줄이 같이 움직인다. paper path, code path, experiment
path. 논문이 무엇을 주장했는지, 공개 코드가 무엇을 실제로 돌리는지, 내가 어느 조건에서 비교할
수 있는지 한 장에 놓아야 한다. 한 줄이 비면 AI의 요약은 좋아도 내 연구의 근거는 빈다.

논문 읽기의 다음 질문은 대개 초록에서 나오지 않는다. YAML, 실행 명령, issue comment, 실패한
sequence, table caption에서 나온다. AI에게 맡길 일은 그 길을 빨리 찾아내는 것이다. 연구자가
맡을 일은 그 길이 실제로 실행됐는지 확인하는 것이다.
