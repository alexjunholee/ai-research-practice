# Ch.7 — 답변서는 claim부터 다시 본다

심사위원이 “comparison is unfair”라고 썼다. AI에 붙이면 공손한 답변 초안이 곧 나온다.
지적에 감사하고, 설명이 부족했음을 인정하고, 수정하겠다고 말한다. 문장만 보면 나쁘지 않다.
그러나 이 comment는 표를 보고 있다.

먼저 열 것은 Table 2다. baseline이 같은 split을 썼는지, metric script가 같았는지, runtime
조건이 바뀌었는지, 공개 코드와 논문 코드가 같은 경로를 탔는지 본다. 이 중 하나라도 열려
있으면 답변서 문장은 아직 앞서 있다. 공손한 문장은 표의 빈칸을 채우지 못한다.

원고 작업에서 AI는 표면을 빠르게 부드럽게 만든다. robust, general, significant 같은 단어가
붙고, 관련 논문 몇 편이 novelty 문장 옆에 온다. 이 작업은 위험하다. claim과 evidence가
그대로인데 문장만 강해지면 reviewer가 본 구멍은 더 잘 보인다.

대화 기록에서 잘 된 답변서는 공격받은 claim부터 적었다. 그 claim이 기대는 figure, table,
experiment, citation을 옆에 두었다. 빠진 실험이 있으면 실험으로 보냈다. 설명 부족이면
method 문단과 caption을 고쳤다. 실제 한계이면 claim을 줄였다. 그 뒤에야 답변 문장이 왔다.

반대로 빨리 망가진 원고 작업은 comment를 붙이고, 공손한 답변을 만들고, paragraph polish로
넘어갔다. reviewer가 비교 조건을 물었는데 답변은 tone만 좋아졌다. evaluation boundary가
열려 있는데 “more comprehensive” 같은 문장이 들어갔다. 이런 문장은 잠깐 그럴듯하지만 다음
round에서 다시 공격받는다.

답변서의 기본 단위는 claim과 evidence다. 어떤 claim이 공격받았는가. 현재 evidence가 그 claim을
어디까지 받치는가. 새 실험이 필요한가. 이미 있는 표를 다시 계산하면 되는가. 한계를 인정하고
scope를 줄일 자리인가. 이 질문을 통과한 뒤의 문장은 대체로 짧아진다.

예의도 답변서의 일부다. 다만 예의가 실험 조건을 대신하지 않는다. 같은 sequence split과 같은 metric
script로 baseline을 다시 맞췄다면 그렇게 쓴다. Section 4.3과 Table 2를 고쳤다면 그곳을
가리킨다. cross-dataset generalization을 보이지 않았다면 그 claim을 접는다. 심사 위험은
문장이 부드러워질 때보다 표, 코드, claim이 같은 곳을 가리킬 때 줄어든다.
