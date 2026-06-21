# AI와 로봇 연구하기

# Ch.0 — 구조를 남겨라

AI는 연구 작업에서 유용하다. 큰 repo에서 관련 파일을 검색하고, 긴 로그에서 확인할 원인을 빠르게 찾아내고, 논문을 보고 코드를 프로토타입으로 구현하는 등 일반화 작업을 매우 빠르게 수행한다. 그러나 잘 못하는 부분도 분명 있다. 이 글을 읽는 사용자는 AI 모델을 다그쳐도 보고, 꾸짖어도 보고, 달래도 보고 하면서 사람과 똑같이 대해가며 더 나은 결과를 이끌어낸 경험이 있다. 그런데 늘 이렇게 할 수는 없지 않은가. 우리가 AI를 어르고 달래기 위해서 일을 하는 게 아니지 않은가. 이 아티클은 이 상황을 타개하는 원리와 도구를 소개하기 위해 작성하였다.

## 비싼 구독 모델을 쓰면 해결되지 않나?

일단 우리 연구실에서는 200 USD짜리 구독을 6개월째 해오고 있다. 좋은 모델을 쓰면 성능이 더 좋아지는 부분이 있기 때문이다. 그래도 작업 품질은 일정하지 않다. 문제는 상용 구독이 폐쇄형 서비스라는 점이다. 사용자는 통제할 수 없는 모델에 프롬프트만 입력한다. 공급자는 실제 parameter 수, token limit, backend routing, system prompt, cache, thinking 처리의 변화 정보를 제한적으로만 공개한다. Anthropic의 [2026년 4월 Claude Code postmortem](https://www.anthropic.com/engineering/april-23-postmortem)은 reasoning effort 변경, thinking cache bug, 짧은 답변을 유도한 system prompt가 품질 저하 보고로 이어졌다고 적었다. 공급자가 이런 항목을 바꿔도 우리는 알아채기조차 힘들다. 장기 연구에는 안정적인 작업 조건이 필요하다.

## SOTA 모델을 자체 서버에서 돌리면 어떤가?

최신의 무거운 모델을 자체 서버에 올리면 공급자의 routing이나 quota 변화에서 조금 자유로워진다. 그러나 상용 서비스는 LLM 가중치에 모델 선택, routing, system prompt, context 압축, cache, tool 호출, retrieval, 권한, 실행 환경을 묶어 제공한다. 연구실에서 같은 효과를 내려면 논문 PDF, code path, 실험 로그, dataset convention, reviewer comment를 검색 가능한 단위로 정리하고, 질문마다 어떤 근거를 쓸지 정해야 한다.

그러나 이러한 데이터셋을 분야별로 모두 구축하고 가지고 있는 것은 초대형 기업이 아닌 이상 불가능하다. 물론, 비슷한 성능을 더 적은 데이터를 사용해서 구현할 수는 있다. 최신 연구 중 [REALM](https://arxiv.org/abs/2002.08909) 같은 연구들은 지식을 모두 parameter에 밀어 넣는 대신, pre-training 단계부터 retriever를 붙여 필요한 문서를 검색해 모델이 읽게 했다. [DPR](https://arxiv.org/abs/2004.04906)은 질문과 passage를 dense representation으로 맞추는 dual encoder를 학습했다. [RAG](https://arxiv.org/abs/2005.11401)는 generator가 사실을 더 정확히 다루고 provenance와 knowledge update 문제를 줄이기 위해 seq2seq model의 parametric memory와 Wikipedia dense index를 결합했다.

이렇게 해서 데이터를 구축하고 찾는 것은 어떻게 한다고 치자. 그래도 여전히 문제는 있다. 이러한 사전 지식을 가지고 LLM을 생성하는 것은 어떻게 해야 할까? 이는 조금 더 CS 이론에 가까운 부분이지만, 우리가 연구하고자 하는 도메인에 특성화된 지식을 전문가 수준으로 활용하기 위해서는 [FiD](https://arxiv.org/abs/2007.01282), [RETRO](https://arxiv.org/abs/2112.04426), [Atlas](https://arxiv.org/abs/2208.03299) 같은 여러 방법론이 적용되어야 할 것이다. 결국 기업이 제공하는 수준으로 완벽히 로컬 모델을 작동시키는 것은 거의 불가능에 가깝다. 그래서 우리는 기본적인 범용 모델을, 변화시키지 않고, input / output만으로 원하는 결과를 얻어내도록 모델의 작동 방식을 변화시켜야 한다.

이 역할 분리를 실제 사용 통계로 보면, Anthropic의 [2026년 Claude Code 사용 분석](https://www.anthropic.com/research/claude-code-expertise)은 이 분업이 어떻게 일어나는지 통계를 공유했다. 사용자는 목표, 접근 방식, 완료 기준을 정하는 쪽에 더 많이 개입했고, Claude는 파일을 고치고 명령을 실행하는 쪽을 더 많이 맡았다. 사용자의 전문성은 특히 문제를 구체적으로 세팅하고, 검증할 대상을 정확히 짚고, agent의 잘못된 판단을 바로잡는 능력으로 나타났다. 그래서 우리는 어떤 문제를 풀 것인지 좁히고, 무엇을 확인해야 하는지 정하고, 잘못된 실행 방향을 끊어 내는 능력을 키우려 한다.

## 그러면 우리가 해야 할 일은 무엇인가?

AI를 사람처럼 대하면 처음에는 잘 되는 것처럼 보인다. 더 자세히 설명하고, 다시 부탁하고, 틀렸다고 지적하면 답이 좋아질 때가 있다. 이 방식은 작업 방식으로 불안정하다. 매번 사용자가 상황을 기억하고, 모델의 답을 의심하고, 빠진 맥락을 다시 채워 넣어야 하기 때문이다.

연구 작업에서는 이 방식이 금방 한계에 닿는다. 실험은 며칠씩 이어지고, 원고는 여러 번 바뀌고, reviewer comment는 과거 결과와 현재 코드 상태를 동시에 요구한다. 이때는 AI가 틀리지 않게 만드는 작업 구조가 필요하다.

그래서 작업 환경부터 바꿔야 한다. 어떤 파일을 봤는지, 어떤 command를 실행했는지, 어떤 결과를 근거로 삼았는지를 남겨야 한다. 그래야 AI가 바뀌어도 같은 일을 다시 이어갈 수 있다. 이렇게 하면 모델 성능이 낮아져도 작업을 계속 붙잡을 수 있다. 좋은 모델은 더 빨리 찾고 더 잘 정리하겠지만, 성능이 낮은 모델도 같은 파일과 같은 로그를 보고 같은 절차를 따라갈 수 있다. 이 아티클은 그 절차를 만드는 도구들을 소개한다.

이 글을 훑어 볼 분들에게 전하는 조언은, 이를 읽지 말고 에이전트에게 이 페이지를 넘겨서 문서화하게 하고 여기에 나온 법칙대로 자기만의 하네스를 만들라는 것이다. 사람이 이런 작업을 하는 시대는 지났다. 이 페이지를 직접 agent에게 읽히고 하네스를 작성하도록 시키시라.

로보틱스 연구 대화에서 나온 사용자 입력 27,759개를 분류했다. 구현 디버깅, reviewer response, 원고 수정, 실험 결과 해석, build/test 확인이 반복해서 나왔다. 실패도 뚜렷했다. 빈도로 보면 현재 실행 상태를 보지 않은 단정과 코드 존재를 실제 사용으로 보는 착각이 가장 많았고, protocol이 다른 숫자를 같은 성능 비교에 올리는 일이 그다음이었다.

먼저 세 가지를 정한다. 무엇을 실제로 확인했는지, 어떤 상태를 바꾸려는지, 실행 뒤 어디까지 말할 수 있는지다. 연구자는 그 기준을 두고 AI가 만든 설명, 코드 수정, 실험 숫자, 원고 문장을 받아들일지 판단한다.

## AI는 탐색과 분류에서 힘을 낸다

분류 결과에서 AI가 도움을 준 장면도 분명했다. 큰 repo에서 관련 파일을 찾고, 로보틱스 task의 실패를 config, calibration, 실행 상태, 평가 지표로 나누고, 논문 section과 figure가 받치는 주장을 대조했다. 조건이 충분히 주어졌을 때는 구현 계획도 빠르게 만들었다.

이 능력은 연구 초반에 특히 유용하다. 일반적인 로보틱스 task에서 성능이 떨어졌을 때 dataset, split, sensor input, timestamp, frame, calibration, preprocessing, cache, metric script를 같이 확인하게 한다. 그다음에야 model architecture, training 설정, control parameter를 고친다.

[ReAct](https://arxiv.org/abs/2210.03629)는 reasoning trace와 task-specific action을 번갈아 생성하게 해, Wikipedia API나 환경에서 새 정보를 얻으며 plan을 고치게 했다. [Toolformer](https://arxiv.org/abs/2302.04761)는 calculator, QA, search, translation, calendar API를 언제 부를지 모델이 학습하게 했다. 연구 작업으로 옮길 때는 tool 호출과 근거의 무게를 나눠야 한다. `ros2 topic info --verbose`에서 QoS 조건을 확인한 뒤에야 QoS mismatch를 관찰 결과로 말할 수 있다.

## 상태를 복원하라

AI 답변은 현재 상태에서 자주 빗나간다. compact summary, 이전 계획, 파일명, 사람의 기억은 방향을 잡는 데 쓴다. 실험 결과와 논문 주장은 원 파일, 로그, 실행 결과로 확인한다. 현재 branch, 수정된 config, 생성된 CSV, 실패한 run, cache version, TeX diff, reviewer가 문제 삼은 문장은 직접 확인해야 한다.

[Maynez et al. 2020](https://aclanthology.org/2020.acl-main.173/)은 abstractive summarization 출력에서 입력 문서와 어긋나는 문장을 확인했다. [Ji et al. 2022](https://arxiv.org/abs/2202.03629)은 NLG hallucination을 원문이나 세계 지식과 어긋나는 생성으로 정리했다. 요약은 다음에 볼 위치를 알려 준다. 실험 숫자와 원고 문장은 원 파일과 실행 결과로 확정한다.

로보틱스 metric은 조건에 묶여 있다. 같은 이름의 metric이라도 dataset, split, sensor, frame, calibration, metric script, failure policy가 다르면 다른 값이다. 낮은 error, 높은 success rate, 빠른 latency도 조건을 확인한 뒤에야 원고에 올릴 수 있다.

AI 답변을 받기 전에 세 가지를 확인한다.

- 실제로 본 파일
- 실행한 명령
- 그 결과로 말할 수 있는 범위

이 세 가지가 없으면 답변은 다시 일반론으로 돌아간다.

## 후보 설명을 실행하려면 비용이 든다

AI는 후보 설명을 많이 만든다. 사람은 그중 하나를 실행한다. 여기서 비용이 생긴다. GPU 시간, 실험 일정, 공동저자 신뢰, reviewer risk가 함께 걸린다. 로봇 연구에서 잘못 고른 실험은 하루를 잃고, 잘못 올린 주장은 원고의 약점이 된다.

Guilford의 divergent thinking은 가능한 방향을 여는 능력을 말한다. March의 exploration/exploitation 구분에도 같은 긴장이 있다. 새 방법을 찾는 일과 지금의 방법을 밀고 가는 일은 비용 구조가 다르다. Kahneman과 Tversky의 prospect theory 이후 위험 판단 연구에 따르면, 사람은 손실 가능성 앞에서 계산 이외의 요소도 따른다.

Bainbridge가 지적한 [automation 역설](https://doi.org/10.1016/0005-1098(83)90046-8)은 이 상황에도 나타난다. 자동화는 쉬운 일을 줄여 주지만, 사람에게 감시와 드문 개입을 남긴다. AI가 초안을 빨리 만들수록 사람은 그럴듯한 초안 중 무엇을 버릴지 판단해야 한다.

[Suchman의 *Plans and Situated Actions*](https://www.lancaster.ac.uk/humanities-arts-and-social-sciences/people/lucy-suchman)는 Xerox PARC에서 사람들이 복사기를 쓰는 장면에서 출발했다. 시스템이 예상한 절차와 사용자가 실제로 마주한 상황은 자주 어긋났다. 연구에서 행동은 prompt 뒤에 온다. 파일, process, dataset, log, table, reviewer comment를 보고 나서야 실제 행동을 판단할 수 있다. [Hutchins의 *Cognition in the Wild*](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)는 해군 함정의 항법을 따라갔다. 연구 판단은 repo, terminal, 노트, 표, figure에 분산된다. AI와 연구하려면 이 자료들을 한 번의 판단 안에 다시 모아야 한다.

## 작업을 좁혀라

하네스는 AI 작업 하나가 바꿀 대상을 정한다. 한 번의 작업마다 다음을 먼저 확인한다.

```text
현재 확인한 것:
지금 바꿀 대상:
바로 실행할 확인:
결과가 나오면 말할 수 있는 것:
아직 말하면 안 되는 것:
```

"이 코드 고쳐줘"라는 요청도 여러 종류다. 실행 환경 문제일 수 있고, runtime path 문제일 수 있고, metric script 문제일 수 있고, 논문 문장 문제일 수 있다. CUDA driver 문제에서 method를 고치면 시간을 잃는다. metric script 문제에서 원고 문장을 고치면 심사 위험이 커진다.

AI 작업 하나마다 repo 이해, 코드 수정, 실험 해석, 원고 주장 중 하나를 고른다. 바꿀 대상을 작게 정하고, 확인한 결과 안에서만 말한다.

## 논문과 코드를 대조하라

AI에게 논문을 주면 abstract와 method 요약은 빨리 나온다. 그다음에는 논문이 실제로 주장한 것, 공개 repo에 들어 있는 것, 현재 환경에서 실행되는 경로가 같은지 확인해야 한다.

로봇 논문은 세 층으로 읽는다.

- 논문 안의 방법 주장
- 공개 repo의 구현 상태
- 현재 환경에서 실행되는 경로

이 셋은 자주 어긋난다. 논문에는 module이 있고 repo에도 파일이 있지만 config에서 꺼져 있을 수 있다. README command는 돌아가지만 논문 table의 숫자를 만든 script와 다를 수 있다. issue에서 frame convention이 바뀌었는데 오래된 branch를 보고 있을 수도 있다.

논문 한 편을 읽을 때 다음 질문을 남긴다.

- 중심 주장은 어느 section, table, figure에 있는가.
- 그 주장을 받치는 code path는 어디인가.
- 그 code path가 runtime에서 실제로 호출되는가.
- dataset, split, metric, baseline은 논문과 같은가.
- 원고에서 가져올 수 있는 말은 어디까지인가.

AI에게 맡길 일은 method component를 뽑고, repo에서 관련 class와 config를 찾고, issue thread에서 convention 변화를 모으는 일이다. 실제 호출 여부와 주장 범위는 파일과 실행 결과로 확인한다.

## 숫자에 조건을 붙여라

낮은 error나 높은 success rate는 dataset, split, sequence, sensor, ground-truth frame, alignment, metric script, baseline과 함께 읽어야 한다. 로보틱스 benchmark는 숫자만 두지 않고 evaluation script, dataset protocol, failure policy를 함께 둔다.

main metric이 개선되었다는 문장에는 dataset, sensor 입력, timestamp span, frame, calibration, failure policy가 함께 있어야 한다. event count를 말할 때도 무엇을 센 것인지, invalid output을 포함했는지, 같은 metric script를 썼는지 확인해야 한다.

AI는 CSV를 읽고 best row를 고르고, plot caption을 쓰고, baseline 대비 차이를 계산하는 데 빠르다. "성능이 좋아졌다"는 문장은 dataset, split, metric script, baseline을 확인한 뒤에 쓴다.

실험 하나마다 다음 항목을 기록한다.

```text
dataset:
split / sequence:
sensor or modality:
ground truth:
frame or alignment:
metric:
baseline:
command:
config:
output path:
failure policy:
```

timeout, OOM, tracking lost, missing sequence, metric script failure도 결과다. 실패를 남겨야 같은 조건을 다른 이름으로 반복하는 일을 줄일 수 있다.

## 파일 존재와 실제 실행은 다르다

파일 존재와 방법 사용은 따로 확인한다. config key와 optimizer 또는 trainer의 실제 소비도 따로 확인한다. 하네스 분석에서 반복된 실패 중 하나가 이 혼동이었다.

구현 상태는 적어도 다음 중 하나로 나눠야 한다.

- 구현되어 있고 실행 중이다.
- 구현되어 있지만 꺼져 있다.
- config에는 있지만 실행 경로 밖에 있다.
- 계획만 있고 code path가 없다.
- 테스트했지만 실패했다.
- dead code이거나 unreachable이다.
- 아직 모른다.

실행 상태도 따로 본다. 오래 돌린 실험에서는 stale process, 오래된 binary, 부분 log, 이전 cache가 현재 결과처럼 보일 수 있다. long-running training이나 ROS bag 재생은 command, cwd, process, output log, checkpoint dir, config snapshot, 최신 metric을 같이 남긴다.

build pass는 소스 컴파일만 확인한다. callback, tf lookup, metric correctness, output validity는 따로 확인한다.

## 끊긴 단계를 찾아라

AI를 쓰는 디버깅에서는 root cause가 빨리 나온다. QoS, calibration, cache, normalization 같은 말이 바로 나온다. 어느 stage에서 신호가 끊겼는지 확인하기 전까지는 가능한 원인이다.

로봇 pipeline은 data loading, preprocessing, representation, matching, geometry, optimization, evaluation 중 여러 곳에서 끊긴다. 같은 에러 메시지라도 다른 단계의 실패일 수 있다.

ROS2 callback이 비어 있을 때는 topic, QoS, namespace, `use_sim_time`, `/clock`, container device, network를 본다. 일반적인 로보틱스 task에서 성능이 떨어졌을 때도 dataset, split, sensor input, timestamp, frame, calibration, preprocessing, cache, metric script, failure policy를 먼저 본다.

디버깅 기록은 짧아도 된다.

```text
stage:
command:
observed signal:
changed file:
output path:
next check:
```

이 기록은 다음 AI 세션이 같은 stage부터 다시 확인하게 만든다.

## 주장부터 검증하라

AI는 문장을 매끄럽게 만든다. reviewer가 문제 삼은 것이 tone인지, 실험 조건인지, 주장 범위인지 분리하지 않은 채 문장만 다듬으면 답변이 약해진다.

Toulmin의 argument model은 주장, 근거, 보증, 반박을 나눈다. 논문 답변도 대체로 이 구조를 가진다. reviewer comment는 Table 2의 비교 조건, Figure caption의 범위, ablation의 빠진 baseline, generalization이라는 단어의 크기를 문제 삼을 수 있다.

답변서를 쓰기 전에 네 가지를 적는다.

```text
공격받은 주장:
현재 근거:
새로 필요한 확인:
고칠 원고 위치:
```

근거가 충분하면 문장을 쓴다. 근거가 부족하면 새 실험, 재계산, 주장 축소 중 하나를 고른다. 정중한 문장은 실험 조건 위에 얹는다. 같은 split과 같은 metric script로 baseline을 다시 맞췄다면 그렇게 쓴다. cross-dataset generalization 근거가 없으면 해당 표현은 줄인다.

## 습관만 이식하라

`multica-ai/andrej-karpathy-skills` 같은 skill repo에는 작은 수정, 가정 명시, 실패 보고 습관이 잘 남아 있다. `datawhalechina/hello-agents` 같은 입문 repo는 agent, memory, tool use, evaluation의 전체 항목을 정리한다. LangGraph, AutoGen, CrewAI, OpenAI Agents SDK 문서는 workflow와 tool 호출의 형태를 정리한다.

그 자료를 로봇 연구에 그대로 적용하면 빠지는 항목이 많다. 일반 agent repo는 코드 변경과 도구 호출에 강하다. 로봇 연구에서는 dataset, calibration, frame, metric, 실패 처리, reviewer risk가 실험 숫자의 의미를 정한다.

Anthropic의 [Managed Agents](https://www.anthropic.com/engineering/managed-agents)는 agent를 하나의 큰 실행 환경으로 묶지 않고 session, harness, sandbox를 나누는 방식을 제시했다. 연구 workspace에 옮기면 session은 다음 세션이 다시 읽을 기록이고, harness는 agent가 따라야 할 규칙이며, sandbox는 실제 파일·command·dataset이 있는 실행 경계다. 외부 repo를 가져올 때도 prompt 문구보다 이 세 경계를 먼저 옮겨야 한다.

먼저 작업 습관을 본다.

- 작은 단위로 고친다.
- 가정을 먼저 적는다.
- 읽은 파일과 보지 않은 파일을 구분한다.
- 실패 단계를 남긴다.
- 다음 사람이 이어갈 수 있게 한다.

여기에 로봇 연구 항목을 더한다.

- dataset, split, sequence
- frame convention
- task input/output
- metric script
- baseline
- failure policy
- 원고에서 쓸 수 있는 주장 범위

옮길 때는 durable state를 `project-memory.json`, ledger, replay case로 남기고, 행동 규칙은 `AGENTS.md`나 template로 옮긴다. 실제 실행 경계는 repo, dataset, artifact, command로 나눈다.

GitHub star 수는 발견의 단서다. 기준은 내 연구에서 같은 metric 혼동, 같은 cache 실수, 같은 reviewer comment를 줄일 수 있는지다.

## 다음 사람이 같은 질문에서 시작하게 한다

AI 작업은 기록이 있어야 이어진다. 어떤 파일을 봤는지, 어떤 명령을 실행했는지, 어떤 숫자가 어떤 조건에서 나왔는지, 어떤 문장을 어디까지 말할 수 있는지 남긴다.

처음부터 큰 체계를 만들 필요는 없다. 논문 한 편을 읽을 때는 주장, code path, 실험 조건을 적는다. 실험 하나를 돌릴 때는 dataset, split, metric, baseline, command, output path를 적는다. 디버깅 중에는 stage, command, 관찰한 signal을 남긴다. 원고를 고칠 때는 공격받은 주장과 현재 근거를 분리한다.

다음 세션은 이 기록에서 시작한다. 같은 폴더를 다시 열었을 때 먼저 물어야 할 질문이 남아 있으면 된다.

## 참고한 축

- Bainbridge, *Ironies of Automation*
- Endsley, *Toward a Theory of Situation Awareness in Dynamic Systems*
- Suchman, *Plans and Situated Actions*
- Hutchins, *Cognition in the Wild*
- March, *Exploration and Exploitation in Organizational Learning*
- Kahneman & Tversky, *Prospect Theory*
- Yao et al., *ReAct*
- Schick et al., *Toolformer*
- Ji et al., *Survey of Hallucination in Natural Language Generation*
- Toulmin, *The Uses of Argument*
