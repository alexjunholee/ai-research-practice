# 로보틱스 연구자를 위한 AI 활용법

> AI가 만든 말은 싸다. 연구자의 행동은 비싸다.

[가이드 열기](guide.html)

새벽에 `eval.csv`를 다시 열면 숫자는 이미 칸 안에 있다. 대화창은 그 숫자를 보고
"좋아진 것 같습니다"라고 말할 수 있다. 아직 남은 일이 있다. 어느 명령으로 나온 값인지,
같은 split인지, 실패한 sequence를 뺐는지, 원고에 올려도 되는 말인지 다시 봐야 한다.

ROS2 노드를 다시 띄우고, bag을 돌리고, metric script를 확인하고, 원고의 주장을 줄이는
일은 사람이 한다. 그 행동에는 시간, compute, 파이프라인 안정성, 심사 신뢰가 붙는다.
이 가이드는 그 무거운 행동 앞에서 AI 도구를 어떻게 세워 둘지 본다.

설치 순서나 템플릿은 앞에 두지 않았다. 먼저 볼 것은 대화창의 문장이 연구자의 손으로
내려오는 순간이다.

## 읽을 거리

- [Ch.1: 말은 빨리 오고 손은 늦게 간다](chapter_01_start_here.md)
- [Ch.2: 기억은 파일을 대신하지 못한다](chapter_02_environment.md)
- [Ch.3: 후보를 손에 잡히는 일로 낮추기](chapter_03_harness.md)
- [Ch.4: 초록 다음에는 YAML이 있다](chapter_04_research_workflows.md)
- [Ch.5: 0.42에는 주소가 없다](chapter_05_experiment_protocol.md)
- [Ch.6: callback이 조용할 때](chapter_06_stage_local_debugging.md)
- [Ch.7: 답변서는 표를 먼저 본다](chapter_07_manuscript_rebuttal.md)
- [Ch.8: 별 많은 저장소에서 절반을 버린다](chapter_08_external_templates.md)

부록과 템플릿은 본문을 읽은 뒤 필요한 것만 가져가면 된다.

- [작업장 파일](QUICKSTART.md)
- [용어 경계](TERMS.md)
- [예시 작업장](EXAMPLE_WORKSPACE.md)
- [작업 리듬](PATH.md)
