# Ch.3 — 하네스는 답을 행동으로 내린다

실패 로그를 붙이면 원인 이름이 빨리 나온다. ROS2 callback이 조용하면 QoS, namespace,
remap, executor, simulated time, Docker network가 나열된다. VPR 숫자가 떨어지면 split,
feature cache, normalization, index order, positive radius가 나온다. 이 목록은 유용하다.
혼자라면 늦게 떠올렸을 후보가 한 번에 올라온다.

목록과 행동 사이에는 거리가 있다. `ros2 topic info --verbose`를 보는 일은 상태 읽기다.
container 권한을 고치는 일은 환경 변경이다. bag replay를 다시 돌리면 시간과 산출물이 같이
움직인다. 원고에서 “robust”를 지우는 일은 reviewer에게 내놓을 claim 범위를 바꾼다. 같은
“확인”이라는 말 안에 읽기, 수정, 실행, 주장 변경이 섞인다.

하네스는 이 섞임을 줄이는 이름이다. 거창한 시스템보다 먼저 세 칸을 둔다. 지금 본 것.
이제 바꿀 것. 바꾼 뒤 남길 것. 여기에 한 칸을 더 붙인다. 지금 증거로 말할 수 있는 claim과
아직 말하지 않을 claim.

대화 기록에서 반복된 실패는 이 칸들이 빠질 때 나왔다. 눈에 띄는 warning을 전체 실패의
원인으로 올렸다. `R@1` 하나가 좋아지자 방법이 좋아졌다는 문장이 먼저 나왔다. build가
통과하자 runtime 상태까지 닫힌 것처럼 말했다. 한 process가 끝났는데 같은 log를 다른
process도 쓰고 있었다. 이 경우 AI의 설명이 틀렸다기보다, 행동 단위가 정해지지 않았다.

반대로 잘 풀린 세션은 작은 행동으로 내려갔다. topic이 보이는지 읽는다. subscriber가
받는지 본다. clock과 namespace를 확인한다. 그다음에 launch file을 고친다. VPR에서는 먼저
query/database 방향과 cache version을 확인한다. 그다음에 feature extractor나 model
architecture를 건드린다. 원고에서는 공격받은 claim을 적고, 그 claim을 받치는 표와 그림을
확인한 뒤 문장을 바꾼다.

하네스는 AI의 발산을 지우지 않는다. 발산은 남겨 둔다. 다만 후보가 곧 원인으로 올라가고,
local success가 system success로 올라가고, generated summary가 source truth로 올라가는
순간을 막는다. 좋은 하네스는 답을 줄이기보다 답이 연구 행동으로 내려갈 때 통과할 문턱을
만든다.

한 번 틀린 자리는 기록으로 남긴다. 같은 Docker 에러에서 driver를 반복해서 의심했다면
다음에는 권한과 volume을 먼저 보는 rule이 남는다. exact-frame retrieval과 radius-based
retrieval을 섞었다면 metric 이름 옆에 positive definition을 붙인다. reviewer comment를
문체 문제로만 처리했다면 답변서 앞에 claim/evidence 칸을 둔다. 반복된 실수는 조언보다
gate로 남을 때 오래 간다.
