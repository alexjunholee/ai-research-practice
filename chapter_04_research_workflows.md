# Ch.4 — 논문 읽기는 paper-code-experiment로 이어진다

로보틱스 논문 읽기는 코드와 실험으로 이어진다. ORB-SLAM3를 읽으면 feature,
map, loop closing, inertial
initialization의 code path가 남아야 한다. FAST-LIO2를 읽으면 ikd-tree,
deskew, IMU propagation, residual update가 실제 파일 어디에 있는지 확인해야
한다. DINO나 SAM을 localization에 쓰는 논문을 읽으면 feature space, projection
head, teacher/student 차이가 metric에 어떻게 들어가는지 남아야 한다.

AI는 논문을 빨리 훑는다. 그 속도가 장점이다. paper, code, experiment를
연결하면 빠른 요약도 연구 자산으로 남는다.

```text
paper claim
-> method assumption
-> code path
-> experiment protocol
-> reusable comparison
```

## Paper pass

첫 번째 pass에서 AI에게 맡길 일은 claim 구조 추출이다.

- 이 논문이 해결한다고 말하는 pressure
- method가 바꾸는 representation 또는 optimization
- 필요한 sensor, calibration, dataset assumption
- experiment가 실제로 닫는 claim
- limitation이 줄이는 claim

이 단계에서 금지할 말이 있다. abstract만 보고 novelty를 판단하지 않는다.
venue, citation, GitHub star로 중요도를 대신하지 않는다. "SOTA"라는 단어는
metric protocol이 확인되기 전까지 보류한다.

## Code pass

코드는 상태를 확인한 뒤에 method evidence로 남는다. 많은 repo에는 죽은 코드,
비활성 옵션, 논문에는 있지만 release에는 빠진 module, config로만 남은
ablation이 있다.

각 component에는 상태를 붙인다.

| Status | 뜻 |
|---|---|
| implemented-active | 현재 config와 run path에서 쓰인다 |
| implemented-disabled | 코드가 있지만 꺼져 있다 |
| configured-unused | config에는 있으나 실제 path에 닿지 않는다 |
| planned-only | 문서나 issue에만 있다 |
| tested-failed | 실행했으나 실패 artifact가 있다 |
| dead | 호출 경로가 끊겼다 |
| unknown | 아직 근거가 없다 |

AI는 function 후보를 찾는 데 유용하다. 사람 또는 하네스는 호출 경로와 run
artifact를 확인한다. "이 파일에 함수가 있다"와 "논문의 method를 구현해
결과에 썼다" 사이에는 여러 gate가 있다.

## Experiment pass

논문 읽기의 세 번째 pass는 실험 contract다.

```text
dataset:
split:
sensor / modality:
query -> database direction:
ground truth frame:
metric:
threshold:
baseline:
artifact:
```

SLAM/VIO에서는 ATE, RPE, trajectory alignment, scale, frame convention이
claim을 바꾼다. VPR과 cross-modal retrieval에서는 exact-frame retrieval인지,
radius-based retrieval인지, query/database 방향이 무엇인지, feature가
backbone인지 projection head인지가 숫자의 뜻을 바꾼다.

AI가 잘하는 일은 표를 만드는 것이다. AI가 자주 실패하는 일은 표의 빈칸을
상식으로 채우는 것이다.

## 로그에서 갈린 지점

| 장면 | 좋게 끝난 세션 | 무너진 세션 | 이유 |
|---|---|---|---|
| Abstract 요약 | claim, assumption, experiment가 따로 남았다 | novelty를 한 문장으로 확정했다 | abstract는 논문의 약속이고, 검증은 method와 experiment에서 닫힌다 |
| Code 확인 | function 후보 뒤에 호출 경로와 config를 확인했다 | 파일에 함수가 있다는 사실을 구현 완료로 읽었다 | code presence와 active method는 다른 상태다 |
| Experiment 연결 | dataset, split, metric, artifact가 map에 들어갔다 | 표의 빈칸을 관습으로 채웠다 | 로보틱스 숫자는 protocol 밖에서 같은 뜻을 유지하지 않는다 |
| Issue 읽기 | build, dataset, metric, sensor setup에 영향을 주는 issue만 묶었다 | 열린 issue 전체를 요약했다 | operational knowledge는 연구 행동을 바꾸는 경우에만 evidence로 남는다 |

## Issue와 PR을 읽는다

공개 repo의 issue와 pull request는 논문 본문에 없는 operational knowledge를
준다. ORB-SLAM3, LIO-SAM, FAST-LIO2, COLMAP 같은 저장소에서는 build failure,
dataset convention, dependency version, sensor-specific bug가 issue에
남는다. 논문만 읽으면 method를 안다. issue까지 읽으면 실제 사용자가 어디서
막히는지 안다.

AI에게는 다음 질문을 준다.

```text
Find issues that change how this method should be run, evaluated, or cited.
Do not summarize all issues.
Group only issues that affect dataset, build, metric, sensor setup, or claim.
```

이 질문은 관련 없는 discussion을 줄이고, 연구 행동에 영향을 주는 issue를
끌어낸다.

## 읽기 결과물

한 편을 읽은 뒤에는 다음 연구 행동으로 이어지는 짧은 map을 남긴다.

```text
paper:
main claim:
method assumption:
code path:
experiment protocol:
comparison I can reuse:
claim I cannot make:
next artifact to inspect:
```

이 map이 있으면 다음 AI 세션은 같은 논문을 다시 요약하지 않는다. 바로 code
path나 experiment protocol에서 이어서 움직일 수 있다.
