# Ch.6 — callback이 조용할 때

`ros2 topic list`에는 `/camera/image_raw`가 보인다. publisher도 있다. 그런데 subscriber
callback은 조용하다. 이 상태에서 "왜 안 되지?"라고 묻는 순간 답은 너무 많이 온다.
QoS, namespace, remap, executor, simulated time, Docker network, device permission.
다 들어본 말이고, 한 번쯤 맞았던 말이다.

익숙한 원인은 손을 빨리 움직이게 만든다. launch 파일을 고치고, 컨테이너를 다시 띄우고,
bag replay를 멈추고, clock을 확인한다. 운이 좋으면 그중 하나가 맞는다. 운이 나쁘면
상태를 더 흐린 뒤 처음 질문으로 돌아온다. 방금 바꾼 것이 원인을 고친 것인지, 원래
다른 상태였는지 알기 어려워진다.

처음에 필요한 것은 원인 이름보다 신호가 사라진 자리다. 카메라가 들어오지 않는지,
전처리에서 깨지는지, 표현이 바뀌었는지, 매칭이나 검색에서 사라졌는지, 기하와 최적화가
흔들렸는지, 평가 스크립트가 다른 파일을 읽고 있는지. 멈출 곳을 정하면 확인의 크기가
달라진다.

좋은 요청은 길지 않아도 좁다. "지금 보는 것은 camera image subscriber다. topic은 보이지만
callback은 호출되지 않는다. 원인을 확정하지 말고, 상태만 읽는 확인부터 순서대로 달라.
명령 출력이 나오기 전에는 원인명을 쓰지 말라." 이 정도만 붙어도 대화는 달라진다. 원인
후보가 확인 순서로 내려온다.

명령 실패와 방법 실패는 따로 놓아야 한다. `pip install` 실패, CUDA driver mismatch,
빠진 Docker volume, 다른 dataset path는 방법 앞에 놓인 실행 환경 문제다. 반대로 명령이
성공해도 metric script가 다른 ground-truth frame을 읽었을 수 있다. 실행이 통과했다는
말과 평가가 맞았다는 말은 서로 다른 문장이다.

디버깅은 흔적을 남기지 않으면 다시 원점으로 돌아간다. 어느 단계에서 멈췄는지, 기대한
신호와 관찰한 신호가 무엇인지, 어떤 명령을 실행했는지, 그 결과 다음에 어디를 볼 수
있게 됐는지를 적어 둔다. 이 흔적이 없으면 다음 대화창은 같은 추측을 새 문장으로 반복한다.

VPR 성능이 갑자기 떨어졌을 때 model architecture부터 바꾸면 비용이 커진다. query와
database split, cached feature version, normalization, index order, positive radius,
metric script를 먼저 본다. 각 확인은 하나의 산출물을 남긴다. 산출물이 없으면 그 행동은
기억 속에서만 일어난다.

같은 단계에서 두 번 연속 아무것도 나오지 않으면 단계를 바꾼다. 명령 실패가 반복되면
환경 문제로 떼어 둔다. 결과가 좋아졌더라도 실험 조건이 바뀌었으면 성능 문장은 기다린다.
우회책으로 지나간 자리는 장부에 빚으로 남긴다. 디버깅은 원인을 맞히는 재주보다, 행동
하나가 다음 질문을 좁히게 만드는 습관에 가깝다.
