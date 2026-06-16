# Ch.5 — 실험 숫자는 protocol에서 나온다

로보틱스 실험에서 숫자는 늦게 온다. protocol이 먼저다. AI가
결과 표를 보고 "개선됐다"고 말하려면 그 숫자가 어떤 dataset, split, sensor,
metric, baseline, artifact에서 나왔는지 알아야 한다.

같은 `0.42`도 ATE인지 RPE인지, meter인지 degree인지, monocular scale을
맞췄는지, failure sequence를 제외했는지에 따라 전혀 다른 말로 이어진다. 같은
`R@1`도 exact-frame retrieval인지 radius 25m 안의 retrieval인지, query가
camera이고 database가 LiDAR인지 그 반대인지에 따라 claim이 바뀐다.

## Result provenance tuple

모든 결과 숫자는 tuple로 보관한다.

```text
number:
dataset:
split / sequence:
sensor / modality:
direction:
ground truth:
metric:
threshold / alignment:
baseline:
command / config:
artifact path:
failure condition:
claim allowed:
```

이 tuple이 비면 숫자는 관찰이다. tuple이 닫히면 숫자를 비교할 수 있다.
comparison target과 reviewer risk까지 닫히면 원고 문장으로 올라간다.

## SLAM/VIO contract

SLAM과 VIO에서는 trajectory가 무엇과 어떻게 맞춰졌는지가 먼저다.

| Field | 확인할 것 |
|---|---|
| Dataset | KITTI, EuRoC, TUM, Newer College처럼 sequence convention이 있는가 |
| Sensor | monocular, stereo, RGB-D, LiDAR, IMU 조합 |
| Time | timestamp sync, dropped frame, bag clock |
| Frame | camera, IMU, LiDAR, world frame convention |
| Alignment | SE(3), Sim(3), scale correction 여부 |
| Metric | ATE, RPE, drift, success rate |
| Baseline | 같은 sensor와 같은 split인지 |
| Artifact | trajectory file, log, config, plot |

AI는 trajectory plot을 보고 drift가 줄었다고 말하기 쉽다. 하네스는 먼저
alignment와 failure sequence를 묻는다. Sim(3) alignment가 들어간 monocular
결과와 metric-scale LiDAR 결과를 같은 문장에 올리면 reviewer가 바로 잡는다.

## VPR/cross-modal contract

VPR과 cross-modal retrieval에서는 방향과 feature space가 claim을 결정한다.

```text
query modality:
database modality:
positive definition:
negative definition:
radius or exact-frame rule:
feature extractor:
projection head:
normalization:
R@K / mAP / precision:
```

cross-modal 실험에서 특히 많이 깨지는 부분은 representation이다. backbone
feature를 썼는지 projection head 출력을 썼는지, teacher feature인지 student
feature인지, fine-tuning 후 feature인지 pre-trained feature인지가 결과를
바꾼다. gradient accumulation은 batch size처럼 보일 수 있지만 real negative
수와 다른 의미다. AI가 이 구분을 놓치면 좋은 숫자에 잘못된 설명을 붙인다.

## 숫자를 해석하는 순서

1. 숫자의 파일과 생성 명령을 찾는다.
2. config가 실제 run에 쓰였는지 확인한다.
3. sample count와 sequence count를 확인한다.
4. metric script의 positive/negative 정의를 읽는다.
5. baseline과 같은 protocol인지 확인한다.
6. claim을 한 문장으로 줄인다.

이 순서를 지키면 AI는 "좋아 보인다"에서 멈추지 않는다. "EuRoC MH_01-05에서
same alignment와 same metric script를 쓴 baseline 대비 ATE median이 줄었다"처럼
작지만 검증 가능한 말을 할 수 있다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| 결과 숫자 | tuple이 닫힌 뒤 comparison을 말했다 | 숫자 하나로 method 개선을 말했다 | 같은 값도 metric, alignment, split에 따라 다른 claim을 만든다 |
| SLAM/VIO 평가 | frame, scale, alignment, sequence filter를 먼저 봤다 | trajectory plot의 모양으로 drift를 판단했다 | plot은 신호지만 reviewer가 보는 것은 protocol이다 |
| VPR 평가 | query/database 방향과 positive rule을 잠갔다 | `R@1` 이름만 보고 성능을 비교했다 | exact-frame과 radius-based retrieval은 같은 숫자라도 의미가 다르다 |
| 실패 run | timeout, OOM, tracking lost를 result provenance에 넣었다 | 성공한 sequence만 보고 안정성을 말했다 | failure distribution은 로보틱스 claim의 일부다 |

## 실패도 protocol에 들어간다

실패 run의 조건까지 protocol에 넣으면 다음 실험의 boundary로 남는다.

```text
timeout:
OOM:
sensor dropout:
tracking lost:
missing sequence:
metric script failure:
invalid ground truth:
```

실패를 적지 않으면 AI는 성공한 숫자만 보고 방법이 안정적이라고 말한다.
로보틱스 연구에서는 실패 분포도 claim에 들어간다.
