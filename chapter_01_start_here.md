# Ch.1 — 답을 받은 뒤에 남는 일

로보틱스 연구에서 AI를 붙여 본 기록을 모아 보면 처음부터 같은 장면이 반복된다. 사용자는
코드, 로그, 결과 표, reviewer comment를 던진다. AI는 빠르게 읽고, 후보를 늘리고, 다음
행동을 말한다. 여기까지는 자주 잘 된다. 혼자 보던 터미널에서는 안 보이던 파일이 나오고,
warning 한 줄에서 확인할 목록이 생기고, 심사 의견은 실험·설명·한계로 나뉜다.

그 뒤부터 비용이 붙는다. 후보가 열 개로 늘어나는 동안에는 아무 파일도 바뀌지 않는다.
그중 하나를 실행하는 순간 Docker, bag, 결과 표, 원고가 움직인다. Docker를 다시 띄우면
멀쩡하던 환경이 바뀔 수 있다. bag을 다시 돌리면 밤이 간다. 좋아 보이던 `R@1`을 의심하면
표 한 줄이 사라진다. 답변서에서 claim을 낮추면 방금
쓴 문단을 다시 열어야 한다. AI가 만든 문장은 비용을 거의 내지 않는다. 연구자는 실행,
시간, 장비, reviewer 신뢰를 건다.

대화 기록에서 잘 끝난 세션은 대체로 이 경계를 늦게라도 붙잡았다. `final_results.csv`를
바로 믿지 않고 command와 config를 다시 보았다. “좋아졌다”는 말을 쓰기 전에 같은 split과
같은 metric script인지 확인했다. callback이 조용할 때 QoS부터 고치지 않고 topic, clock,
namespace, container 권한을 순서대로 읽었다. reviewer에게 답하기 전에는 공손한 문장보다
먼저 공격받은 claim과 빈 근거를 갈라 놓았다.

반대로 빨리 무너진 세션도 모양이 일정했다. 파일 이름을 현재 상태처럼 믿었다. compact
summary를 원문처럼 다뤘다. partial trajectory, build pass, plot 생성 같은 좁은 성공을
전체 성공으로 올렸다. 코드에 factor가 있다는 사실을 optimizer가 그 factor를 쓴다는
증거로 삼았다. 숫자가 좋아졌다는 말이 dataset split, frame convention, metric threshold보다
앞섰다.

이 차이는 모델 성능만으로 설명되지 않는다. AI는 후보를 거의 비용 없이 늘린다. 사람은 후보를
행동으로 바꾸며 비용을 낸다. March가 말한 exploration과 exploitation의 긴장은 여기서도
보인다. 새 가능성을 더 보는 일과 그 가능성 하나에 하루를 쓰는 일은 다른 시간표를 가진다.
Loewenstein이 risk as feelings에서 말한 감정도 연구실 안으로 들어온다. 좋아 보이는
숫자를 의심할 때의 아까움, 간신히 돌아가는 pipeline을 건드릴 때의 불안, 빈 답변서 표를
보는 압박이 판단에 섞인다.

prompt는 시작을 빠르게 만든다. harness는 답을 받은 뒤의 일을 느리게 잡는다. 지금 본 것이
raw artifact인지, 생성된 요약인지, 실행 결과인지, 원고 claim인지 구분한다. 이제 바꿀 것이
코드인지, config인지, 실험 조건인지, 문장인지 적는다. 바꾼 뒤 남길 command, output path,
실패 조건, claim 범위를 정한다.

AI를 잘 쓴 세션은 답이 많아서 좋았던 것이 아니었다. 답이 나온 뒤에도 무엇을 아직 실행하지
않을지 알았다. 그 보류가 연구를 살렸다.
