# Ch.5 — 숫자는 조건을 달고 나온다

결과 폴더에 `0.42`가 남아 있다. ATE일 수도 있고 RPE일 수도 있다. meter일 수도 있고 degree일
수도 있다. monocular scale을 맞춘 뒤의 값인지, 실패 sequence를 뺀 평균인지, alignment policy가
지난번과 같은지도 아직 모른다. 그 값만으로는 논문 문장을 만들 수 없다.

VPR의 `R@1`도 같은 함정을 가진다. exact-frame retrieval에서 나온 값인지, 25m radius 안의
retrieval인지, query가 camera이고 database가 LiDAR인지 그 반대인지에 따라 의미가 바뀐다.
backbone feature, projection head output, teacher feature, student feature, fine-tuned feature가
같은 표 안에 들어가면 비교가 쉬워 보인다. 실제로는 서로 다른 실험일 수 있다.

대화 기록에서 사용자는 좋은 숫자보다 먼저 조건을 물었다. sequence 방향, yaw formula,
ground-truth frame, accepted-only metric, all-query metric, threshold definition, full-bag
coverage. 숫자가 좋아 보여도 이 항목들이 비어 있으면 문장은 기다렸다. AI가 가장 자주 서두른
자리도 여기였다. 값이 높거나 낮다는 사실을 곧바로 방법의 평가로 옮겼다.

숫자 옆에는 긴 꼬리가 붙는다. dataset, split, sequence, sensor, modality, query/database 방향,
ground truth, frame, alignment, metric, threshold, baseline, command, config, output path,
timeout, failure policy. 행정용 목록처럼 보이지만 그렇지 않다. 하나만 바뀌어도 같은 숫자가
다른 주장을 만든다.

SLAM과 VIO에서는 coverage가 먼저 걸린다. trajectory가 어디서 끊겼는지, pose count가 몇 개인지,
timestamp span이 전체 bag을 덮는지, tracking lost를 어떻게 처리했는지 봐야 한다. censored
trajectory에서 낮은 error가 나와도 full-run success와 같이 둘 수 없다. Sim(3) alignment로
metric이 계산됐다고 해서 trajectory가 물리적으로 말이 된다는 뜻도 아니다.

VPR과 cross-modal retrieval에서는 방향과 positive definition이 먼저 온다. camera-to-LiDAR인지,
LiDAR-to-camera인지, radius rule이 무엇인지, query count가 몇 개인지, invalid query를 어떻게
처리했는지 확인한다. model이 좋아졌다는 말은 이 조건들이 고정된 뒤에야 나온다.

그래서 좋은 문장은 대체로 좁다. "EuRoC MH_01-05에서 같은 alignment와 같은 metric script를 쓴
baseline 대비 ATE median이 줄었다." 화려하지 않다. 그래도 다음날 다시 열었을 때 덜 흔들린다.
"성능이 향상되었다"는 문장은 조건이 붙기 전까지 너무 넓다.

실패한 줄도 결과다. timeout, OOM, sensor dropout, tracking lost, missing sequence, metric script
failure, invalid ground truth를 빼고 성공 숫자만 남기면 안정성이 부풀어 오른다. 로보틱스
연구에서 실패 분포는 부록의 잡음이 아니다. 어느 조건에서 약해지는지가 방법의 일부다.
