# Ch.6 — 디버깅은 멈춘 지점부터 본다

`ros2 topic list`에는 `/camera/image_raw`가 보인다. publisher도 있다. subscriber callback은
조용하다. 이때 "왜 안 되지?"라고 묻는 순간 답이 많이 나온다. QoS, namespace, remap, executor,
simulated time, Docker network, device permission. 전부 실제 원인일 수 있다.

후보가 익숙할수록 손이 빨리 간다. launch file을 고치고, container를 다시 띄우고, bag replay를
멈추고, clock을 본다. 운이 좋으면 바로 맞는다. 운이 나쁘면 상태가 바뀐 뒤 처음 질문으로
돌아온다. 방금 고친 것이 원인을 없앤 것인지, 원래 다른 상태였는지 알기 어려워진다.

먼저 볼 것은 멈춘 지점이다. camera image가 들어오지 않는가. preprocessing에서 깨지는가. feature
representation이 바뀌었는가. matching이나 retrieval에서 사라지는가. geometry, PnP, optimization
단계에서 흔들리는가. evaluation script가 다른 파일을 읽는가. 지점이 잡히면 확인의 크기가 줄어든다.

잘 풀린 디버깅 세션은 상태를 읽는 명령부터 실행했다. 명령 출력이 나오기 전에는 원인을 확정하지
않았다. 바꾼 파일과 바꾸지 않은 파일을 분리했다. 같은 failure signature가 사라졌는지 다시 봤다.
build pass만으로 runtime success를 말하지 않았다.

명령 실패와 방법 실패도 따로 둔다. `pip install` 실패, CUDA driver mismatch, 빠진 Docker volume,
다른 dataset path는 방법 앞의 실행 환경 문제다. 반대로 명령이 성공해도 metric script가 다른
ground-truth frame을 읽었을 수 있다. 실행이 통과했다는 문장과 평가가 맞았다는 문장은 서로 다른
증거를 요구한다.

VPR 성능이 갑자기 떨어졌을 때 model architecture부터 바꾸면 비용이 커진다. query/database split,
cached feature version, normalization, index order, positive radius, metric script를 먼저 본다.
각 확인은 흔적을 남긴다. command, workdir, output path, observed signal, next stage. 이 흔적이
없으면 다음 대화는 같은 추측을 새 문장으로 다시 만든다.

같은 단계에서 두 번 연속 아무것도 나오지 않으면 단계를 바꾼다. runtime 실패가 이어지면 환경
문제로 떼어 둔다. 결과가 좋아졌더라도 실험 조건이 바뀌었으면 성능 문장은 기다린다. 우회책으로
지나간 자리는 남은 빚으로 적는다.

디버깅의 목표는 원인 이름을 멋지게 맞히는 데 있지 않다. 다음 질문의 범위를 줄이는 데 있다.
