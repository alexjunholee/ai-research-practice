# Ch.4 — 논문은 초록에서 끝나지 않는다

ORB-SLAM3 논문을 읽고 나면 좋은 요약은 금방 나온다. feature, map, loop closing,
inertial initialization 같은 단어가 줄을 선다. 다음날 실제 저장소를 열면 문제가
달라진다. 어느 파일을 봐야 하는지, 어떤 설정이 켜져 있는지, 논문에 있던 ablation이
공개 코드에도 남아 있는지 확인해야 한다.

FAST-LIO2도 마찬가지다. ikd-tree, deskew, IMU propagation, residual update를 안다고
해서 실험을 다시 돌릴 수 있는 것은 아니다. DINO나 SAM을 localization에 붙인 논문은
feature space, projection head, teacher/student 차이가 평가 숫자에 어디서 들어가는지
봐야 한다. AI는 이 이름들을 빨리 모은다. 연구자는 이름이 실제 코드와 실험으로 내려가는
길을 본다.

초록은 논문이 독자에게 하는 약속이다. 그 약속을 믿어도 되는지는 방법과 실험 조건이
결정한다. AI에게 처음 맡길 일도 여기까지다. 이 논문이 어떤 압박을 풀려 하는지, 어떤
표현 방식이나 최적화를 바꿨는지, 어떤 센서와 calibration을 전제로 삼는지 뽑아내게
한다.

그다음부터는 말이 느려져야 한다. 초록만 보고 새로움을 확정하지 않는다. 학회명, 인용
수, GitHub 별 수로 중요도를 대신하지도 않는다. 최고 성능이라는 말은 같은 평가 조건이
보이기 전까지 기다린다.

공개 저장소에는 여러 층이 섞여 있다. 논문에는 있지만 공개판에서 빠진 모듈이 있고,
설정에는 남았지만 실제 실행 경로에는 닿지 않는 옵션도 있다. 죽은 코드가 살아 있는
구현처럼 보이는 일도 흔하다.

AI는 함수 후보를 찾는 데 강하다. 어느 파일에 descriptor extractor가 있는지, 어느
class가 optimizer를 감싸는지, 어느 script가 평가를 호출하는지 빨리 찾는다. 그 다음
질문은 사람이 붙여야 한다. 지금 이 함수가 실제 설정에서 호출되는가. 논문 결과를 만들
때 이 경로를 썼는가. 실패 산출물이 남아 있는가.

논문 읽기의 끝은 한 문장짜리 평이 아니다. 다음에 확인할 산출물이 있어야 한다.
데이터셋, split, 센서 조합, 질의와 데이터베이스 방향, ground-truth frame, metric,
threshold, baseline, 산출물 경로. 이 항목들이 닫히면 요약은 비교 가능한 재료가 된다.

SLAM/VIO에서는 ATE와 RPE, trajectory alignment, scale, frame convention이 주장을
바꾼다. VPR과 cross-modal retrieval에서는 exact-frame retrieval인지, radius-based
retrieval인지, feature가 backbone인지 projection head인지가 숫자의 뜻을 바꾼다.
AI는 표를 잘 만든다. 자주 틀리는 곳은 표의 빈칸을 관습으로 채우는 순간이다.

이슈 글타래도 읽을 가치가 있다. ORB-SLAM3, LIO-SAM, FAST-LIO2, COLMAP 같은 저장소의
issue에는 논문 본문에 없는 말이 남는다. 빌드 실패, 데이터셋 관례, 의존성 버전,
센서별 버그가 그 안에 있다. 논문만 읽으면 방법의 윤곽을 안다. issue까지 읽으면 실제
사용자가 어디서 멈추는지 보인다.

모든 issue를 요약할 필요는 없다. 연구 행동을 바꾸는 issue만 남긴다. 실행 방법을
바꾸는가. 평가 조건을 바꾸는가. 인용이나 한계를 바꾸는가. 이 셋 중 하나에 닿지 않는
discussion은 읽고 지나간다.

한 편을 제대로 읽으면 다음 세션의 출발점이 달라진다. AI는 같은 논문을 다시 요약하지
않아도 된다. 바로 코드 경로나 실험 조건에서 이어서 움직일 수 있다.
