# Ch.5 — 숫자는 혼자 말하지 못한다

결과 폴더에 `0.42`가 남아 있다. AI에게 보여 주면 "개선된 것 같습니다"라는 문장이
금방 나온다. 하지만 그 값이 ATE인지 RPE인지, meter인지 degree인지, monocular scale을
맞춘 뒤의 값인지 아직 모른다. 실패 sequence를 뺐는지도 보지 않았다. 숫자는 있다.
아직 결과는 아니다.

VPR의 `R@1`도 같은 함정에 걸린다. exact-frame retrieval에서 나온 값인지, 25m radius
안의 retrieval인지, query가 camera이고 database가 LiDAR인지 그 반대인지에 따라 같은
이름의 숫자가 다른 주장을 만든다. AI는 숫자와 문장을 가깝게 붙인다. 연구자는 그
사이에 실험 조건을 넣어야 한다.

모든 결과 숫자에는 출처가 붙어야 한다. 데이터셋, split이나 sequence, sensor와
modality, 방향, ground truth, metric, threshold나 alignment, baseline, command,
config, 산출물 경로, 실패 조건. 길어 보이지만 이 항목들이 없으면 숫자는 관찰에
머문다.

출처가 닫히면 비교를 말할 수 있다. 비교 대상과 심사 위험까지 닫힌 뒤에야 원고 문장이
된다. 이 순서를 바꾸면 AI는 좋은 숫자에 좋은 형용사를 붙인다. 그 문장은 대체로
원고에서 오래 버티지 못한다.

SLAM과 VIO에서는 trajectory가 무엇과 어떻게 맞춰졌는지가 먼저다. KITTI, EuRoC, TUM,
Newer College처럼 dataset마다 sequence convention이 다르고, monocular, stereo,
RGB-D, LiDAR, IMU 조합마다 scale과 frame 문제가 달라진다. timestamp sync, dropped
frame, bag clock도 숫자의 의미를 바꾼다.

AI는 trajectory plot을 보고 drift가 줄었다고 말하기 쉽다. 하네스는 먼저 alignment와
failure sequence를 묻는다. Sim(3) alignment가 들어간 monocular 결과와 metric-scale
LiDAR 결과를 같은 문장에 올리면 reviewer가 바로 잡는다. plot은 신호다. 실험 조건이
주장을 허락한다.

VPR과 cross-modal retrieval에서는 방향과 feature space가 주장을 결정한다. query
modality, database modality, positive definition, radius rule, feature extractor,
projection head, normalization, R@K나 mAP가 함께 움직인다.

특히 많이 깨지는 부분은 표현이다. backbone feature를 썼는지 projection head 출력을
썼는지, teacher feature인지 student feature인지, fine-tuning 뒤 feature인지
pre-trained feature인지가 결과를 바꾼다. gradient accumulation은 batch size처럼 보일
수 있지만 real negative 수와 같은 말이 아니다. AI가 이 구분을 놓치면 좋은 숫자에
잘못된 설명을 붙인다.

해석은 작은 문장으로 내려가야 한다. "좋아졌다" 대신 "EuRoC MH_01-05에서 같은
alignment와 같은 metric script를 쓴 baseline 대비 ATE median이 줄었다"처럼 말해야
한다. 작지만 버틸 수 있는 문장이다.

실패도 결과에 들어간다. timeout, OOM, sensor dropout, tracking lost, missing
sequence, metric script failure, invalid ground truth를 적어 두지 않으면 AI는 성공한
숫자만 보고 안정성을 쉽게 말한다. 로보틱스 연구에서 실패 분포는 부록의 잡음이 아니다.
방법이 어디서 무너졌는지, 어느 sensor 조건에서 약한지, 어떤 sequence를 제외했는지가
주장의 일부가 된다.
