# Ch.5 — 0.42에는 주소가 없다

결과 폴더에 `0.42`가 남아 있다. 처음 보면 좋은 숫자다. 대화창도 그렇게 읽기 쉽다.
"개선된 것 같습니다." 그런데 `0.42`는 아직 말이 짧다. ATE인지 RPE인지, meter인지
degree인지, monocular scale을 맞춘 뒤의 값인지, 실패 sequence를 뺐는지 알 수 없다.
숫자는 칸 안에 있지만, 결과는 아직 도착하지 않았다.

VPR의 `R@1`도 같은 방식으로 사람을 속인다. exact-frame retrieval에서 나온 값인지,
25m radius 안의 retrieval인지, query가 camera이고 database가 LiDAR인지 그 반대인지에
따라 같은 이름의 숫자가 다른 말을 한다. 숫자와 문장은 서로 가깝게 붙고 싶어 한다.
그 사이에 실험 조건을 끼워 넣는 일은 사람 몫이다.

숫자 옆에는 주소가 붙어야 한다. 데이터셋, split이나 sequence, sensor와 modality, query와
database의 방향, ground truth, metric, threshold나 alignment, baseline, command, config,
산출물 경로, 실패 조건. 길어 보이는 이 항목들이 숫자의 주소다. 주소가 없으면 숫자는
기억 속의 인상으로 남는다.

SLAM과 VIO에서는 trajectory를 무엇과 맞췄는지가 앞에 온다. KITTI, EuRoC, TUM,
Newer College는 sequence convention부터 다르다. monocular, stereo, RGB-D, LiDAR, IMU
조합마다 scale과 frame 문제가 달라진다. timestamp sync, dropped frame, bag clock도
숫자의 뜻을 바꾼다. plot에서 drift가 줄어 보인다는 말만으로는 방법의 성능을 아직
말하지 못한다.

VPR과 cross-modal retrieval에서는 방향과 표현이 자주 미끄러진다. query modality,
database modality, positive definition, radius rule, feature extractor, projection head,
normalization, R@K나 mAP가 함께 움직인다. backbone feature인지 projection head 출력인지,
teacher feature인지 student feature인지, fine-tuning 뒤 feature인지 pre-trained
feature인지에 따라 숫자는 다른 얼굴을 한다.

좋아졌다는 말은 늦게 온다. 먼저 쓸 수 있는 문장은 작다. "EuRoC MH_01-05에서 같은
alignment와 같은 metric script를 쓴 baseline 대비 ATE median이 줄었다." 이 문장은
덜 멋있지만 버틴다. 멋진 문장은 표가 움직이기 전에 달려 나가고, 작게 쓴 문장은 다시
열어도 덜 흔들린다.

실패도 결과에 들어간다. timeout, OOM, sensor dropout, tracking lost, missing sequence,
metric script failure, invalid ground truth를 빼고 성공한 숫자만 보면 안정성은 쉽게
부풀어 오른다. 로보틱스 연구에서 실패 분포는 부록 잡음으로 빠지지 않는다. 어느 조건에서
약해지는지, 어떤 sequence를 제외했는지, 어떤 sensor 조합에서 무너졌는지가 주장 안으로
들어온다.

숫자는 혼자 논문으로 올라가지 못한다. 주소가 붙고, 같은 조건의 비교가 붙고, 실패한 줄이
같이 붙은 뒤에야 문장이 된다.
