# Ch.1 — 싼 답과 비싼 실행

밤 늦게 ROS2 노드가 조용하다. `topic list`에는 카메라가 보이고, publisher도 떠 있다.
subscriber callback만 오지 않는다. AI에게 로그를 붙이면 답은 금방 나온다. QoS, namespace,
remap, executor, `use_sim_time`, Docker network. 그중 몇 개는 정말 맞을 수 있다.

답은 빠르다. 비용은 실행에서 생긴다. launch file을
고치면 다른 노드가 같이 움직인다. container를 다시 띄우면 겨우 맞춰 둔 volume과 device
권한이 흔들린다. bag을 다시 돌리면 한 시간이 간다. metric을 다시 계산하면 방금 좋아 보였던
표 한 줄이 사라질 수 있다. reviewer 답변서에서 claim을 낮추면 문단 하나만 바뀌지 않는다.
논문의 자세가 바뀐다.

AI는 이 비용을 거의 느끼지 않는다. 후보를 열 개 더 만드는 데 드는 비용이 작다. 연구자는
그중 하나를 고르는 순간 장비, 시간, 원고, 신뢰를 건다. AI를 잘 쓰려면 답 뒤의 실행을 같이
봐야 한다. 답이 많이 나오는 상황에서 어느 답을 아직 실행하지 않을지 정하는 일이 따라온다.

대화 기록에서 좋은 방향으로 간 경우는 대체로 이 지점에서 멈췄다. `final_results.csv`를
읽은 뒤 바로 "성능 향상"이라고 쓰지 않았다. command, config, split, metric script를 다시
봤다. callback이 비어 있을 때 QoS부터 바꾸지 않았다. topic, clock, namespace, container
권한을 차례로 읽고, 어느 단계에서 신호가 끊기는지 먼저 확인했다. reviewer comment를 받았을
때도 공손한 문장을 먼저 만들지 않았다. 공격받은 claim과 그 claim을 받치는 표를 나란히 놓았다.

반대로 일이 빨리 망가진 경우도 있었다. 파일 이름을 현재 상태로 믿었다. compact summary를
원문처럼 썼다. trajectory 일부가 그려졌다는 사실을 run 전체의 성공으로 올렸다. build가
통과했다는 말로 runtime까지 지나갔다고 썼다. 코드에 factor가 있다는 사실을 optimizer가 그
factor를 쓴 증거로 삼았다. 숫자가 좋아 보인다는 감각이 dataset split, frame convention,
metric threshold 확인보다 먼저 문장으로 나갔다.

여기에는 오래된 행동 문제가 들어 있다. James March가 말한 exploration과 exploitation의
긴장은 연구실에서도 그대로 보인다. AI는 exploration을 쉽게 늘린다. 더 많은 원인, 더 많은
paper, 더 많은 문장, 더 많은 우회로를 만든다. 연구자는 어느 순간 exploitation으로 들어가야
한다. 하나를 골라 실행하고, 실패를 받고, 그 결과를 원고와 실험 기록에 남겨야 한다.

Loewenstein이 말한 risk-as-feelings도 멀리 있지 않다. 좋아 보이는 숫자를 의심할 때의 아까움,
간신히 돌아가는 pipeline을 건드릴 때의 불안, reviewer가 지적한 빈 표를 보는 압박이 판단에
섞인다. AI는 이 감정을 겪지 않는다. 그래서 AI가 담담하게 내놓은 다음 행동이 연구자에게는
오늘 밤을 다시 쓰는 결정이 된다.

여기서 말하는 하네스는 짧은 제동 장치다. 답이 나온 뒤 바로 실행하지 않기 위해 둔다. 지금 본
것이 raw log인지, 요약인지, 실행 결과인지, 원고 claim인지 먼저 적는다. 손댈 대상이 code인지,
config인지, dataset인지, 문장인지 적는다. 실행 뒤 남길 command, output path, 실패 조건,
claim 범위를 정한다.

AI를 잘 쓰는 사람은 답의 개수를 세지 않는다. 싸게 나온 답과 비싸게 치를 실행을 같은 무게로
다루지 않는다. 연구는 그 차이를 아는 쪽에서 앞으로 간다.
