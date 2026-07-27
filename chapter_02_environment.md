# Ch.2 — 적어 둔 것 다시 돌려 보기

우리는 AI와 주고받은 대화에서 사람 쪽 입력 27,759개를 분류해 봤다. 눈에 띄게 많이 나온 실패는 지금 무엇이 돌고 있는지 보지 않고 원인을 정해 버린 것이었다. 분류 기준표와 집계 파일이 남아 있지 않아 앞 장은 이 수를 우리 로그의 경향까지로만 쓴다. 답을 받을 때마다 다섯 줄을 적어 두라고 앞 장에서 한 것이 그래서다. 모델이 만든 설명, 실제로 본 파일, 실행한 명령, 나온 결과, 그 결과로 말할 수 있는 범위. 앞의 하나는 모델이 한 말이고 나머지 넷은 내가 눈으로 본 것이라, 적어 두면 둘이 나중에도 갈린다.

다만 그 다섯 줄이 붙잡아 두는 것은 적을 당시의 상태다. 며칠 지나 열어 보면 경로도 명령도 그때 나온 숫자도 적어 둔 그대로인데, 그사이 기계 쪽은 계속 움직였다.

ROS2를 예로 들면 이렇다. 토픽마다 QoS profile이 붙는데, 보내는 쪽과 받는 쪽이 맞아야 메시지가 건너간다. 기본 profile은 RELIABLE이고 카메라나 LiDAR driver 쪽은 BEST_EFFORT로 두는 sensor data profile을 쓴다. 보내는 쪽이 BEST_EFFORT인데 받는 쪽이 RELIABLE이면 메시지가 안 온다. 지난주에 토픽이 들어오는 것을 보고 잘 맞아 있다고 적어 두었어도, 그동안 누가 받는 쪽을 기본값으로 돌려놓았으면 그 줄은 이제 틀렸다. 읽어서는 틀린 티가 안 난다. 그래서 적어 둔 파일을 열고 적어 둔 명령을 그대로 다시 돌린다.

## 적어 둔 것과 지금 도는 것

다섯 줄이 답 하나마다 붙는 기록이라면, 작업 공간 전체를 놓고 같은 일을 하는 자리가 부록 B의 첫날 체크리스트다. 칸이 일곱이다.

```text
project goal:
code truth:
dataset truth:
experiment truth:
manuscript truth:
reviewer risk:
durable corrections:
```

`code truth` 칸에는 지금 참으로 치는 코드 경로를, `dataset truth` 칸에는 어느 split을 쓰고 있는지를 적는다. `reviewer risk`에는 심사에서 걸릴 만한 자리를 적어 둔다. 마지막 칸에는 계속 물고 갈 교정 사항을 올린다. 같은 것을 두 번 바로잡았으면 여기 올려 두고, 다음에 이 파일을 여는 사람이 그걸 아는 채로 시작한다.

이 칸들이 어디에 놓이느냐도 함께 정해진다. 칸을 채우다 보면 심사 의견 원문과 미공개 숫자가 같이 들어오는데, 이런 줄이 갈 자리는 공개 저장소와 다르다. 반복되는 실패 유형과 운영 규칙과 공개용 template은 공개 저장소에 둔다. 개인 대화 원문과 개인 경로와 reviewer 원문과 미공개 숫자와 인증 정보는 로컬 기록에 남긴다. 부록 D도 다시 시작할 때 확인할 것으로 이 경계를 꼽아 두었다.

읽어서 돌아오는 데까지가 여기다. 일곱 칸은 지난번에 눈으로 보고 적은 값이라 지금도 그런지는 돌려 봐야 안다. 그리고 돌려 봐야 아는 자리는 여섯 군데로 흩어져 있다.

| 상태 | 확인할 항목 |
|---|---|
| repo | branch, commit, modified file, build output |
| 실행 | process, container, device, environment, output path |
| 데이터 | dataset version, split, sequence, calibration |
| 결과 | metric output, plot, table, failed run |
| 원고 | TeX diff, figure 원본, table, paragraph |
| 기억 | project memory, handoff, durable correction |

맨 아래 기억 줄만 지난번의 내가 남긴 것이고, 위의 다섯은 기계가 지금 들고 있는 상태다. 다섯은 각자 따로 봐야 한다. repo가 깨끗해도 container는 그때 그대로일 수 있고 아닐 수 있다. metric output이 남아 있어도 지금 코드에서 나온 값인지는 데이터 줄을 따로 봐야 안다.

실행 줄을 여는 방법은 Ch.9에 모아 두었다. 환경을 갈아엎기 전에 `pip show`와 `dpkg -l | grep`과 `apt policy`로 지금 무엇이 깔려 있는지 적고, 새 terminal에서 package를 못 찾으면 `echo $AMENT_PREFIX_PATH`로 지금 걸린 workspace를 읽는다. 토픽이 안 들어올 때 `ros2 topic list`와 `ros2 node list`를 함께 찍으면 노드가 안 뜬 것인지 이름이 다른 데 붙은 것인지가 갈린다. 적어 둔 줄에는 그 갈래가 안 남는다.

우리가 파일을 열고 명령을 돌리는 동안 그 결과는 모델이 든 창에도 그대로 쌓인다. Anthropic의 [context engineering cookbook](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)은 아무것도 걸지 않고 돌린 실행의 최대 맥락을 335,279 토큰으로 쟀고, 그중 96.3%가 파일 읽기 결과였다. 도구 호출 기록이 1.9%, 추론이 1.7%다. 창에 든 것의 거의 전부가 어느 시점에 읽힌 파일의 내용이고, 그 파일이 그 뒤에 바뀌었으면 창은 옛것을 들고 있다.

같은 cookbook이 세션을 두 번 이어 돌려 앞 세션이 남긴 것을 뒤 세션이 어떻게 받는지도 쟀다. 첫 세션에서 찾은 것을 창 밖 저장소에 적어 둔 쪽은 둘째 세션을 5K 토큰에서 시작했고, 적어 두지 않은 쪽은 둘째 세션에서 문서 여덟 개를 다시 읽어 332K까지 갔다. 그 저장소는 우리 디스크다. memory 도구는 client-side로 돌아서, 모델이 호출을 내면 우리 쪽 애플리케이션이 그 조작을 로컬에서 실행한다. 모델이 내는 명령은 `view`·`create`·`str_replace`·`insert`·`delete`·`rename` 여섯이다. 모델이 쓴 것도 이렇게 우리 디스크에 남고, 표의 기억 줄에 적힌 `project memory`와 handoff가 다섯 줄과 같은 파일 시스템에 놓인다.

## 모델이 대신 써 둔 요약

다섯 줄 대신 요약만 남은 자리가 있다. 대화 끝에 붙는 압축본, 다음 세션에 넘기려고 써 둔 handoff 메모, `project memory`에 적힌 몇 줄. 모델이 쓴 글이다.

대화 끝에 붙는 압축본은 compaction이 만든다. 앞 절의 cookbook은 이 연산이 창 전체에 걸린다고 적었다. 사용자가 한 말, 모델이 한 말, 도구 호출, 도구 결과, 앞서 한 압축의 결과까지 전부가 요약 하나로 납작해진다. 기본 트리거는 150K 토큰이다. cookbook이 트리거를 180K로 두고 돌린 실행에서는 압축 한 번이 앞 대화를 약 2,783 토큰으로 줄였다.

같은 cookbook이 clearing을 그 옆에 두었다. 이쪽은 다시 불러올 수 있는 낡은 결과를 창 안에서 떨어내면서 호출이 있었다는 기록은 남긴다. 이 가름은 앞 장의 다섯 줄이 "실행한 명령"과 "나온 결과"를 따로 적어 두는 짜임과 같다. 명령 줄이 남아 있으면 결과는 다시 돌려서 얻는다. 기본 트리거는 100K 토큰이고, 가장 최근 도구 결과 셋은 그대로 둔다. `exclude_tools`에 도구 이름을 적어 두면 그 도구의 결과는 그대로 남는데, memory를 여기 적어 둔다. 떨어낸 자리 앞으로 잡아 둔 prompt cache는 이 처리로 무효가 된다.

clearing이 갈라 둔 그 둘을 compaction 쪽은 한 덩이로 묶어 요약 문장에 담는다. 그렇게 묶인 글에서 어느 대목이 어디서 왔는지는 원문을 옆에 놓고 맞춰 봐야 갈린다.

Maynez 등은 [뉴스 기사와 요약문을 나란히 놓고](https://aclanthology.org/2020.acl-main.173/) 판정자들에게 기사에 없는 구간을 표시하게 했다. 판정자들에게 기사를 함께 준 것이 그 과제의 조건이었다. 그렇게 표시된 구간이 한 문장짜리 요약의 70%를 넘었다. 2020년 요약 모델을 뉴스 한 문장 요약 과제에서 잰 수다.

우리가 인계 메모를 읽을 때 하는 일도 그 조건을 갖춰야 한다. 옆에 파일을 놓고 줄마다 맞춰 본다. 메모만 읽어서 걸러 낼 수 있는 문장은 앞뒤가 안 맞는 문장뿐인데, 걸리는 문장은 앞뒤가 맞는 채로 걸린다. "calibration을 다시 맞춘 뒤 성능이 올랐다"는 줄에는 틀린 데가 없다. 언제 만졌는지가 안 적혀 있어서, 그 줄만 놓고는 참인지 거짓인지 가릴 자리가 없다. 출처만으로 가릴 수 없는 이런 출력을 Ji 등의 [hallucination 조사](https://arxiv.org/abs/2202.03629)가 extrinsic hallucination이라 부른다. 같은 조사가 읽는 쪽에서 왜 안 걸리는지도 적었다.

> Hallucinated text gives the impression of being fluent and natural despite being unfaithful and nonsensical.

글의 결로는 참과 거짓이 갈리지 않으니, 가르는 자리를 세션 첫머리에 미리 박아 둔다. 부록 B는 첫날 체크리스트 옆에 첫 세션에 넣을 프롬프트도 두었는데, 거기 이 한 줄이 들어 있다.

```text
Do not infer project truth from summaries when source files or artifacts are
available.
```

## 며칠 지켜보기만 하면

파일을 옆에 놓기만 하면 되는 일인데, 며칠 만에 앉으면 요약을 읽는 것으로 그 자리가 채워진다. 며칠 자리를 비운 사람에게 그사이 기계가 한 일은 돌아와서 읽는 것으로만 남는다. 손을 대지 않고 지켜보기만 한 자리와 겹치는 데가 여기다. 그 자리에 놓인 사람이 어떻게 되는지는 자동화를 오래 조사한 쪽에서 이미 살펴 두었다.

Endsley는 [상황을 안다는 것](https://doi.org/10.1518/001872095779049543)을 지금 무엇이 있는지 알아채는 일, 그게 무슨 뜻인지 잡는 일, 곧 어떻게 될지 내다보는 일로 갈라 놓았다. Endsley와 Kiris는 1995년에 길 찾기 과제를 놓고 사람이 직접 몰 때와 기계가 대신 몰 때를 견줬다. 기계가 맡은 쪽에서 낮게 나온 것은 두 번째였다. 첫 번째는 그대로였다. 확인된 것은 앞의 둘까지고, 세 번째를 쟀다는 말은 자료에 없다.

Endsley가 [그 실험을 자기 글에서 다시 정리하며](https://maritimesafetyinnovationlab.org/wp-content/uploads/2019/12/Automation-and-Situation-Awareness-Endsley.pdf) 지켜보는 사람의 처지를 적었다.

> When acting as monitor of an automated system, people are frequently slow in detecting that a problem has occurred necessitating their intervention.

알아챈 다음에도 일이 남는다.

> Once detected, additional time is also needed to determine the state of the system and sufficiently understand what is happening in order to be able to act.

연구실을 잰 자료는 여기 없다. 가져올 수 있는 것은 지켜보기만 했다는 조건까지다. 요약을 읽고 "여기까지 했지" 할 때 돌아오는 것은 첫 번째다. 어디에 무엇이 있었는지는 안다. 그게 지금 무슨 상황인지는 명령을 돌려 봐야 나온다.

## 어디까지 말해도 되나

명령을 돌리고 나면 손에 결과가 남는다. 그걸로 어디까지 말해도 되는지는 무엇을 함께 봤느냐로 갈린다.

| 자료 | 예 | 말할 수 있는 범위 |
|---|---|---|
| 원 파일 | 소스 코드, config, TeX, CSV, log | 파일 안에서 직접 확인한 내용 |
| 실행 결과 | command output, generated figure, metric result | 해당 실행에서 나온 결과 |
| 조건을 확인한 결과 | dataset, split, metric, baseline을 확인한 숫자 | 같은 조건 안의 비교 |
| 요약 | handoff, compact summary, memory note | 다음에 확인할 위치 |
| AI 추정 | 원인 추정, 구조 해석, 요약 판단 | 확인해야 할 설명 |

어느 줄이 맞고 어느 줄이 틀렸다는 표가 아니다. 줄마다 어디까지 말해도 되는지가 다르다. 요약 줄에 적힌 "다음에 확인할 위치", 그게 요약을 쓸 데다.

앞 장의 다섯 줄이 이 표에 그대로 얹힌다. "모델이 만든 설명"은 맨 아래 AI 추정이고, "실제로 본 파일"은 맨 위 원 파일이며, "실행한 명령"과 "나온 결과"는 그 아래 실행 결과다. 마지막 "말할 수 있는 범위"에는 앞의 넷이 닿은 줄의 오른쪽 칸을 옮겨 적는다.

이를테면 `final_results.csv`를 열어 숫자를 봤다면 거기까지가 맨 윗줄이다. 그 숫자를 뽑은 command와 config를 찾으면 실행 결과가 된다. 셋째 줄로 가려면 조건을 확인해야 하고, 무엇을 짚을지는 부록 D가 여섯 줄로 적어 두었다. 같은 실험 숫자를 다시 볼 때 먼저 물으라는 것들이다.

```text
Which dataset?
Which split?
Which direction?
Which metric script?
Which baseline?
Which output?
```

여섯 줄을 채우고 나면 그 숫자가 어느 조건 안의 값인지가 정해지고, 같은 조건의 baseline과 견줄 수 있다. `final_results`라는 이름은 여기에 아무것도 보태지 않는다.

## 여는 순서

여기까지를 하나로 묶으면 일곱 줄이 된다.

1. 현재 repo와 공개/비공개 경계를 확인한다.
2. project memory나 handoff가 있으면 방향을 잡는 자료로 읽는다.
3. 원 파일을 찾는다.
4. 실행 결과가 필요한 경우 command와 output path를 확인한다.
5. 원고 작업이면 table, figure, paragraph를 함께 본다.
6. summary와 원 파일이 충돌하면 원 파일을 우선한다.
7. 다음 행동 하나만 정한다.

첫 줄이 앞에서 본 공개/비공개 경계다. 지금 열어 놓은 저장소가 어느 쪽인지 먼저 보고 나면 뒤에서 기록을 남길 자리가 정해진다.

둘째 줄까지가 읽는 일이고 셋째부터 돌려 보는 일이다. 요약은 어느 파일을 열지 정하는 데까지 쓴다. 자료를 미리 임베딩해 두고 꺼내는 방식과, 경로와 질의와 링크 같은 가벼운 식별자만 들고 있다가 실행 때 불러오는 `just in time` 방식을 Anthropic의 [effective context engineering 글](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)이 갈라 놓았다. 요약을 이렇게 쓰는 것이 뒤쪽이다. 앞쪽으로 갈수록 창에 미리 들어가는 토큰이 늘어난다. 같은 글이 context rot을 따로 적었다. 창에 든 토큰이 늘수록 모델이 그 안의 정보를 정확히 되짚어 내는 힘이 떨어진다. 열어 보니 요약이 말한 것과 다른 것이 들어 있으면 여섯째 줄로 간다. 그때 어긋난 자리를 새로 적는 다섯 줄 옆에 남기고 요약은 그대로 둔다. 요약을 고쳐 두면 다음번에 무엇이 어긋났는지 대조할 원본이 없어진다. 같은 자리에서 또 어긋나면 첫날 체크리스트의 `durable corrections`로 올린다.

셋째와 넷째 줄에서 지난번과 어긋난 것을 찾는다. 원 파일을 찾을 때 config와 split과 calibration file을 함께 열고, 명령과 output path를 볼 때 그 명령이 어느 container에서 어떤 environment로 돌았는지 본다. 코드가 그대로여도 split이 바뀌었으면 같은 조건이 아니다. 원고 작업이면 다섯째 줄에서 TeX diff와 figure 원본과 table을 함께 열고, 문단이 인용한 숫자가 방금 확인한 실행에서 나온 값인지 맞춰 본다.

어긋난 자리를 다 찾고 나면 마지막 줄에서 하나만 고른다. 여기서 branch와 config와 script와 원고 문단을 한꺼번에 손대면, 다음번에 수치가 달라졌을 때 넷을 하나씩 되돌려 가며 원인을 찾아야 한다. 다음 장이 그 이야기다.

다만 고르는 하나가 멈추는 것일 때도 있다. 부록 D가 그 자리를 적어 두었다. 같은 단계에서 근거가 그대로일 때, 도구 실패와 방법 실패가 섞여 있을 때, 실험 조건이 바뀌었는데 숫자를 비교하려 할 때, 심사 위험이 남았는데 문장 다듬기만 반복할 때, 비공개 자료가 공개 문서에 섞일 위험이 있을 때다. 이 자리에서도 물으면 답은 나온다. 멈추는 쪽은 사람이 정한다.

멈추든 이어 가든 그날 돌려 본 것을 다섯 줄에 적어 둔다. 다음에 다시 앉는 사람이 어디부터 열지가 거기서 나온다.
