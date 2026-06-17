# Ch.3 — 하네스는 실행 전에 묻는다

실패 로그를 붙이면 원인 이름이 빨리 나온다. ROS2 callback이 조용하면 QoS, namespace, remap,
executor, simulated time, Docker network가 나온다. VPR 숫자가 떨어지면 split, feature cache,
normalization, index order, positive radius가 나온다. 혼자였다면 늦게 떠올렸을 후보가 한 번에
책상 위에 놓인다.

그 목록은 아직 행동이 아니다. `ros2 topic info --verbose`를 보는 일과 launch file을 고치는
일은 다르다. container 권한을 바꾸는 일과 bag replay를 다시 도는 일도 다르다. 원고에서
`robust`를 지우면 reviewer 앞에 내놓는 claim 범위도 같이 줄어든다. 같은 "확인"이라는 말 안에
읽기, 수정, 실행, 주장 변경이 섞이면 AI와 사람이 서로 다른 일을 하고도 같은 일을 했다고 믿는다.

하네스는 이 혼동을 줄이는 짧은 문답이다.

지금 본 것은 무엇인가.  
이제 무엇을 바꿀 것인가.  
바꾼 뒤 무엇이 남아야 하는가.  
그 결과로 어디까지 말할 수 있는가.

대화 기록에서 위험한 순간은 이 네 질문 중 하나가 빠질 때였다. warning 한 줄을 전체 실패의
원인으로 올렸다. `R@1` 하나가 좋아지자 방법이 좋아졌다는 문장이 나왔다. build가 통과하자
runtime까지 통과한 것처럼 말했다. 한 process가 끝났는데 다른 process가 같은 log를 쓰고 있었다.
AI의 설명이 그럴듯해도 행동 단위가 없으면 연구는 미끄러진다.

좋게 풀린 세션은 작았다. topic이 보이는지 읽는다. subscriber가 받는지 본다. clock과 namespace를
확인한다. 그다음 launch file을 고친다. VPR에서는 query/database 방향과 cache version을 먼저
본다. 그다음 feature extractor나 model architecture를 건드린다. 원고에서는 공격받은 claim을
적고, 그 claim을 받치는 표와 그림을 본 뒤 문장을 바꾼다.

하네스는 AI의 발산을 살려 둔다. 낯선 원인을 빨리 띄우고, 볼 파일을
넓히고, reviewer comment가 건드린 부분을 여러 갈래로 보여 준다. 다만 후보가 곧 원인으로
승격되는 순간을 막는다. local success가 system success로 올라가는 순간을 막는다. generated
summary가 source truth 자리를 차지하는 순간을 막는다.

한 번 틀린 자리는 기록으로 남긴다. Docker 에러에서 driver를 자꾸 의심했다면 다음에는 device
권한과 volume을 먼저 보는 규칙이 남는다. exact-frame retrieval과 radius-based retrieval을
섞었다면 metric 이름 옆에 positive definition을 붙인다. reviewer comment를 문체 문제로만
처리했다면 답변서 앞에 claim과 evidence 칸을 둔다.

하네스는 AI가 만든 후보 하나를 연구 행동 하나로 내릴 때 작동한다. 그 행동이 감당할 비용과
남길 증거를 먼저 보게 만든다.
