# Ch.6 — 어느 단계에서 끊겼는지 가른다

AI에 오류를 물으면 QoS, calibration, cache, normalization 같은 원인 후보를 빠르게 얻을 수 있다. 이 답을 받아 바로 고치기 시작하면 지금 무엇이 돌고 있는지 보기 전에 원인이 정해진다. 답은 Ch.1의 다섯 줄 가운데 `AI가 만든 설명:` 칸에 적어 두고, 어느 단계에서 신호가 끊겼는지 눈으로 본 뒤에 꺼낸다.

[Endsley](https://doi.org/10.1518/001872095779049543)는 situation awareness를 시간과 공간의 한 범위 안에서 환경의 요소를 지각하는 것, 그 의미를 이해하는 것, 가까운 미래의 상태를 예측하는 것으로 정의했다. 확인된 것은 이 정의 한 문장까지다. 세 항목 각각을 원문이 어떻게 풀었는지는 못 봤다. 여기서 가져다 쓰는 것은 셋을 갈라 세웠다는 짜임 하나다. 정의가 셋을 따로 세운 것처럼 이 책의 기록도 셋을 각각 다른 칸에 적는다. 눈으로 본 신호가 한 칸, 그 신호가 나온 단계가 한 칸, 아직 남은 원인 후보가 또 한 칸이다.

## 단계에 먼저 이름을 붙인다

복잡한 로보틱스 pipeline은 단계마다 다른 증상을 보인다. 어느 단계가 끊겼는지에 따라 볼 대상이 달라지므로 단계에 먼저 이름을 붙인다.

```text
input
preprocessing
representation
matching
geometry
optimization
evaluation
```

아래 두 목록은 이 일곱 이름을 그대로 쓴다. 어느 목록을 여는지는 손에 든 증상이 정한다. 앞의 목록은 한 단계 안에서 멈춘다. 뒤의 목록은 일곱을 처음부터 훑는다.

## 신호가 아예 안 올 때

받는 쪽 callback이 빈 채로 있으면 신호는 `input`에서 멈춘 상태다. 이어지는 여섯 단계는 아직 입력을 받기 전이라 여기서 읽을 것은 `input` 하나다. 수정 전에 다음을 본다.

1. `ros2 topic list`로 topic 존재 확인
2. `ros2 topic info --verbose`로 QoS 확인
3. publisher/subscriber namespace 확인
4. `use_sim_time`과 `/clock` 확인
5. container device, network, volume 확인
6. 이어서 코드 또는 launch 수정

1부터 5까지 다섯 줄의 `stage:`는 모두 `input`이다. 1에서 topic 이름이 목록에 보이는데도 callback이 빈 채로 있으면 다음에 볼 것은 profile이다. ROS2 기본 profile은 RELIABLE이고 sensor data profile은 BEST_EFFORT라 driver와 받는 쪽이 어긋나면 메시지가 안 온다. 2가 보는 것이 이 어긋남이다. topic이 오는 것을 눈으로 본 뒤에야 `next stage:`에 `preprocessing`을 적는다. 5가 보는 container device와 network와 volume은 실행 환경 쪽에 속한다. 실행 환경 쪽 증상 하나하나를 어디서 볼지는 Ch.9에서 참조표로 세운다.

1의 `ros2 topic list`를 AI가 대신 찍고 결과를 옮겨 줄 때는 자리가 하나 더 생긴다. 도구 응답에는 길이 제한이 걸린다. Anthropic의 [도구 작성 지침](https://www.anthropic.com/engineering/writing-tools-for-agents)은 도구가 high signal information만 에이전트에 돌려주게 하라고 적었고, 응답에 pagination과 범위 선택과 필터와 잘라내기를 두라고 적었다. Claude Code는 도구 응답을 기본 25,000 토큰으로 제한한다. 이 제한이 걸린 응답은 뒤가 잘린 채로 온다. 짧게 온 목록을 그대로 적어 두기 전에 그것이 빈 목록인지 잘린 목록인지를 먼저 가른다. 잘린 것이면 topic 이름을 좁혀 다시 찍은 결과를 받는다.

## 떨어진 숫자는 맨 위부터

성능 숫자 하나가 떨어졌을 때 그 값은 일곱 단계를 다 지나온 뒤에 나온 것이다. 앞 절에서는 빈 callback 하나가 끊긴 자리를 `input`으로 좁혀 주었다. 다 지나온 값에는 일곱이 그대로 후보로 남는다. 뒤 단계는 앞 단계의 출력을 받아 돌기 때문에 앞이 어긋나면 뒤도 같이 어긋나 보인다. 어느 단계에서 떨어졌는지는 위에서부터 하나씩 짚어 본다. 수정 전에 다음을 본다.

1. dataset, split, sensor input 범위 확인
2. timestamp, frame, calibration 확인
3. preprocessing과 normalization 확인
4. cache, checkpoint, intermediate output 확인
5. matching, geometry, optimization의 입력과 출력 확인
6. metric script와 failure policy 확인
7. 그다음 model architecture, training 설정, control parameter 수정

일곱 이름은 데이터가 지나가는 차례다. `input`으로 들어온 것을 `preprocessing`이 손질하고, `representation`이 그것을 다루기 좋은 꼴로 바꿔 두면 `matching`이 짝을 찾고 `geometry`가 위치를 세우고 `optimization`이 전체를 맞춘다. 마지막 `evaluation`이 그 결과를 숫자로 잰다. 1과 2는 `input`에 들어온 것과 거기 붙은 조건을 본다. 3은 `preprocessing`, 4는 `representation`, 5는 `matching`·`geometry`·`optimization`, 6은 `evaluation`이다. 앞 장에서 숫자마다 dataset과 split과 metric script를 적어 두었다면 1과 6은 그 기록을 다시 읽는 일이 된다. 7은 일곱 이름을 다 지나온 뒤에 남는다.

## 본 것을 적어 두는 형식

앞의 두 목록은 항목마다 확인 하나를 만든다. 다음 세션에서 같은 자리를 다시 열려면 그 확인들이 한 파일에 같은 모양으로 쌓여 있어야 한다. 각 확인은 같은 형식으로 남긴다.

```text
stage:
command:
workdir:
observed signal:
changed file:
output path:
next stage:
```

`stage:`에는 위 일곱 이름 가운데 하나가 들어간다. `ros2 topic list`를 찍어 본 줄이면 `input`이고, metric script를 연 줄이면 `evaluation`이다. `observed signal:`에는 눈으로 본 것을, `next stage:`에는 이 확인 뒤에 옮겨 갈 이름을 적는다. 남은 네 칸은 그 줄을 다시 세울 조건을 받는다. `command:`와 `workdir:`는 같은 신호를 다시 내는 데 필요한 것이다. 그 신호를 다시 내는 사이에 무엇을 건드렸고 결과가 어디로 갔는지는 `changed file:`과 `output path:`가 받는다.

눈으로 본 신호와 그 신호가 나온 단계와 아직 남은 원인 후보 가운데 앞의 둘이 이 일곱 칸 안에 있다. 신호는 `observed signal:`이 받고, 단계는 `stage:`가 받는다. 셋째인 원인 후보는 Ch.1의 `AI가 만든 설명:` 칸에 남는다. 이 형식의 어느 줄을 열어도 눈으로 본 것과 AI가 댄 QoS나 calibration은 서로 다른 칸에서 나온다.

`observed signal:`이 받는 것도 눈으로 본 것 하나다. 앞 절에 든 도구 작성 지침은 오류 메시지를 코드나 traceback이 아니라 다음에 무엇을 하라는 말로 쓰라고 적었다. 이 칸도 같은 자리에 선다. traceback을 통째로 옮겨 붙인 줄과 `input`에서 어느 topic이 빈 채로 있었는지를 적은 줄이 여기서 갈린다. 뒤쪽이면 다음에 열 것이 `next stage:`로 그대로 이어진다.

이 일곱 칸을 어느 파일에 쌓는지도 정해져 있다. 부록 D는 실행 중 문제의 시작점으로 `stage-local-debugging.md`를 둔다. 같은 부록이 적은 멈춤 조건 하나가 이 형식에서 바로 보인다. `next stage:`에 같은 이름이 두 번 이어서 들어가면 같은 단계에서 근거가 그대로인 상태다.

## 도구 탓인지 방법 탓인지

같은 이름이 두 번 들어간 줄에서는 그 단계 안을 한 번 더 가른다. 같은 `stage:`에 적힌 실패라도 종류가 갈리면 다음에 할 일이 갈린다. 앞의 세 종류는 그 줄의 `observed signal:`에 적힌 것으로 갈린다.

| 실패 종류 | 예 |
|---|---|
| 실행 환경 실패 | `pip install`, CUDA driver, Docker volume, dataset path |
| runtime 실패 | callback 없음, tf lookup 실패, node crash |
| 평가 실패 | wrong frame, wrong split, wrong metric script |
| 방법 실패 | 조건을 맞춰 확인한 뒤에도 성능이 낮음 |

첫 줄은 여러 자리를 한꺼번에 받는다. 빌드 성공은 첫 줄에서 한 자리를 지운다. 소스가 컴파일됐다는 사실이 그 한 자리고, `pip install`과 CUDA driver와 Docker volume과 dataset path는 그대로 남는다.

같은 확인을 AI가 code execution tool 안에서 돌렸다면 첫 줄이 받는 자리가 달라진다. Anthropic의 [code execution tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)는 그 컨테이너의 인터넷이 완전히 막혀 있어 런타임에 패키지를 받지 못한다고 적었다. 미리 깔린 것만 도는 자리라 `pip install`은 후보에서 빠지고, 대신 필요한 패키지가 그 목록에 있는지가 첫 줄의 자리로 들어온다. 같은 문서가 적은 두 가지는 첫 줄에 자리를 하나 더 붙인다. 컨테이너는 약 5분 놀면 체크포인트로 저장됐다가 같은 컨테이너 ID로 되살아난다. 도구 판을 `code_execution_20260120` 이후로 올리면 변수 바인딩까지 요청 사이에 남는다. 앞 실행의 상태가 남아 있는 것이 그 자리다.

첫 줄의 자리들을 지우고 나면 둘째 줄이 선다. callback 없음과 tf lookup 실패는 둘째 줄에서 따로 본다. wrong metric script는 셋째 줄에서 따로 본다. output이 쓸 데에 맞는지는 `output path:`에 적은 파일을 열어 본다. 넷째 줄은 앞의 세 줄을 지운 뒤에 남는 자리다. 도구 실패를 넷째 줄에 적으면 아직 남아 있는 자리가 지워진 것으로 기록되고, 다음 확인이 같은 `stage:`로 돌아온다. 도구 실패와 방법 실패가 한 기록에 섞이면 부록 D가 적은 대로 멈춘다.

`evaluation`까지 지나온 줄은 성능 숫자를 두고 쓴 문장을 받쳐 준다. `input`에서 멈춘 줄이 받쳐 주는 것은 그 단계에서 눈으로 본 것까지다. 기록에 적힌 `stage:`와 실패 종류가 원고에 쓸 수 있는 문장의 어디까지를 정한다. 다음 장에서는 그 문장을 주장과 근거로 갈라 `claim-evidence-map.md`에 적는다.
