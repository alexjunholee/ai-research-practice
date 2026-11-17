# 부록 E — 공개 출처와 참고 자료

이 부록은 가이드 본문과 부록에서 인용하거나 참고한 외부 저장소·논문·공식 문서의 공개 링크를 주제별로 모은 목록이다. 각 출처에서는 접근 가능 여부와 제목·저자·저장소의 성격, 그리고 본문에서 실제로 인용한 최소한의 사실만 원문에서 확인했다. 주제별 최종 확인일은 다음과 같다.

- 기존 목록 확인일: 2026-06-18
- 로보틱스 실행 환경 자료 확인일: 2026-07-17
- Ch.2 자료 확인일: 2026-07-26
- 맥락 관리·에이전트 운영 자료 확인일: 2026-07-26

## 외부 에이전트와 스킬 저장소

에이전트 구조와 스킬 구성을 살필 때 참고한 공개 저장소와 공식 SDK다.

- [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)
- [`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents)
- [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph)
- [`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI)
- [`microsoft/autogen`](https://github.com/microsoft/autogen)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [`alexjunholee/robotics-research-agent`](https://github.com/alexjunholee/robotics-research-agent)

## 인간과 AI의 행동 이론

자동화 환경에서 사람이 어떻게 상황 인식을 잃거나 도구를 오용·과신하는지 다룬 고전 연구와 이론 문헌이다.

- [Bainbridge, *Ironies of Automation*](https://doi.org/10.1016/0005-1098(83)90046-8)
- [Parasuraman & Riley, *Humans and Automation: Use, Misuse, Disuse, Abuse*](https://doi.org/10.1518/001872097778543886)
- [Endsley, *Toward a Theory of Situation Awareness in Dynamic Systems*](https://doi.org/10.1518/001872095779049543)
- [Endsley, *Automation and Situation Awareness* (Endsley & Kiris 1995 실험을 저자가 정리한 장)](https://maritimesafetyinnovationlab.org/wp-content/uploads/2019/12/Automation-and-Situation-Awareness-Endsley.pdf)
- [Suchman, *Plans and Situated Actions* / Lancaster profile](https://www.lancaster.ac.uk/humanities-arts-and-social-sciences/people/lucy-suchman)
- [Hutchins, *Cognition in the Wild*](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)

## LLM 에이전트와 검색·근거 검증

추론과 도구 사용을 결합하는 에이전트 구조, 환각(hallucination), 그리고 검색 증강 생성(RAG)의 기초 논문과 보고서다.

- [Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629)
- [Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*](https://arxiv.org/abs/2302.04761)
- [Anthropic, *Agentic coding and persistent returns to expertise*](https://www.anthropic.com/research/claude-code-expertise)
- [Anthropic, *Appendix to Agentic Coding and Persistent Returns to Expertise*](https://cdn.sanity.io/files/4zrzovbb/website/ef87578c3828dc79d711f6d9c52eff39ac4e3be0.pdf)
- [Anthropic, *Scaling Managed Agents: Decoupling the brain from the hands*](https://www.anthropic.com/engineering/managed-agents)
- [Ji et al., *Survey of Hallucination in Natural Language Generation*](https://arxiv.org/abs/2202.03629)
- [Maynez et al., *On Faithfulness and Factuality in Abstractive Summarization*](https://aclanthology.org/2020.acl-main.173/)
- [Guu et al., *REALM: Retrieval-Augmented Language Model Pre-Training*](https://arxiv.org/abs/2002.08909)
- [Karpukhin et al., *Dense Passage Retrieval for Open-Domain Question Answering*](https://arxiv.org/abs/2004.04906)
- [Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://arxiv.org/abs/2005.11401)
- [Izacard & Grave, *Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering*](https://arxiv.org/abs/2007.01282)
- [Borgeaud et al., *Improving language models by retrieving from trillions of tokens*](https://arxiv.org/abs/2112.04426)
- [Izacard et al., *Atlas: Few-shot Learning with Retrieval Augmented Language Models*](https://arxiv.org/abs/2208.03299)

## 모델 버전·품질과 서비스 조건

상용 모델의 추론량 설정, 품질 변동 보고, 서비스 조건 변화를 다룬 공식 문서와 공개 기록이다.

- [Anthropic, *Effort*](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Anthropic, *An update on recent Claude Code quality reports*](https://www.anthropic.com/engineering/april-23-postmortem)
- [GitHub issue, `anthropics/claude-code` #42796](https://github.com/anthropics/claude-code/issues/42796)
- [Business Insider, *Anthropic says Claude Code did get worse*](https://www.businessinsider.com/anthropic-admits-claude-code-issues-user-complaints-denies-nerfing-degrading-2026-4)

## 평가와 재현성

기계학습 연구의 재현성, LLM 추론의 비결정성, 에이전트 벤치마크의 타당성을 점검한 논문과 기술 글이다.

- [Pineau et al., *Improving Reproducibility in Machine Learning Research*](https://arxiv.org/abs/2003.12206)
- [Thinking Machines Lab, *Defeating Nondeterminism in LLM Inference*](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- [*Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation*](https://arxiv.org/abs/2607.02577)
- [*Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents*](https://arxiv.org/abs/2603.29231)

## 연구 하네스와 자동 연구

확인일: 2026-08-09

실행 하네스 설계와 연구 자동화 벤치마크, 그리고 자동 연구 시스템의 실제 성과를 검증한 논문·보고서다.

- [*From Question Answering to Task Completion: A Survey on Agent System and Harness Design*](https://arxiv.org/abs/2606.20683) — 실행 하네스의 여섯 요소
- [Si et al., *Can LLMs Generate Novel Research Ideas?*](https://arxiv.org/abs/2409.04109)
- [Si et al., *The Ideation-Execution Gap* (ICLR 2026)](https://arxiv.org/abs/2506.20803)
- [*PaperBench*](https://arxiv.org/abs/2504.01848)
- [*CORE-Bench*](https://arxiv.org/abs/2409.11363)
- [*ResearchCodeBench*](https://arxiv.org/abs/2506.02314)
- [*ResearchGym*](https://arxiv.org/abs/2602.15112)
- [*Kosmos: An AI Scientist for Autonomous Discovery*](https://arxiv.org/abs/2511.02824)
- [Lu et al., *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*](https://arxiv.org/abs/2408.06292) — 편당 약 15달러, 본문 계산 10~15달러 (확인일 2026-10-23)
- [Yamada et al., *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*](https://arxiv.org/abs/2504.08066) — ICLR 2025 워크숍 제출 세 편, 평균 6.33점, 한계 절 (확인일 2026-10-23)
- [Sakana AI, *The AI Scientist Generates its First Peer-Reviewed Scientific Publication*](https://sakana.ai/ai-scientist-first-publication/) — 내부 검토의 본 트랙 미달 판단, 메타 리뷰 전 철회, 인용 오류 사례 (확인일 2026-10-23)
- [Beel et al., *Evaluating Sakana's AI Scientist*](https://arxiv.org/abs/2502.14297) — 새로움 오분류, 실험 42% 코드 오류 실패 (확인일 2026-10-23)
- [Intology, *Zochi Publishes A* Paper*](https://intology.ai/blog/zochi-acl) — ACL 2025 본 학술대회 채택, 사람이 맡은 부분 (확인일 2026-10-23)
- [METR, *Time Horizon 1.1*](https://metr.org/blog/2026-1-29-time-horizon-1-1/)
- [Ord, *Is there a half-life for the success rates of AI agents?*](https://arxiv.org/abs/2505.05115)
- [Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet* (ICLR 2024)](https://arxiv.org/abs/2310.01798) — 오라클 신호가 있을 때와 없을 때
- [Kim et al., *From Reproduction to Replication: Evaluating Research Agents with Progressive Code Masking*](https://arxiv.org/abs/2506.19724) — pass@1 대 pass@5, 고정 하네스 대 동적 하네스
- [Bean et al., *Measuring what Matters: Construct Validity in Large Language Model Benchmarks*](https://arxiv.org/abs/2511.04703)
- [*When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation*](https://arxiv.org/abs/2602.16763)

## 심사와 출판

확인일: 2026-08-09

학술 심사에서 AI 생성 리뷰 비중과 코드 중심 동료 심사를 다룬 분석과 제안이다.

- [Pangram Labs, *Pangram Predicts 21% of ICLR Reviews are AI-Generated*](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) — 심사평 약 7만 건 중 15,899건(21%), 2025-11-18 (확인일 2026-10-23)
- [*Review the Code, Not the Story: A Vision and Protocol for Code-First Peer Review*](https://arxiv.org/abs/2606.07683)

## 로봇 정책 평가

확인일: 2026-08-09

실세계 분산 평가, 불완전한 시뮬레이터 활용, 통계적 A/B 검정을 다룬 로봇 정책 평가 자료다.

- [*RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies*](https://arxiv.org/abs/2506.18123)
- [*Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators*](https://arxiv.org/abs/2510.04354)
- [Toyota Research Institute, *Statistical Thinking for Robot Policy Evaluation*](https://medium.com/toyotaresearch/statistical-thinking-for-robot-policy-evaluation-from-rigorous-a-b-testing-to-effective-0ae886fbd68d)

## 자율 실험실

확인일: 2026-08-09

무기 재료 합성 자율 실험실의 원논문과 정정 공고, 그리고 후속 검증 논란을 다룬 기사다.

- [Szymanski et al., *An autonomous laboratory for the accelerated synthesis of inorganic materials*, Nature 2023](https://www.nature.com/articles/s41586-023-06734-w)
- [Szymanski et al., *Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials*, Nature 2026](https://www.nature.com/articles/s41586-025-09992-y)
- [Chemistry World, *New analysis raises doubts over autonomous lab's materials discoveries*](https://www.chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article)

위 네 절(`연구 하네스와 자동 연구`, `심사와 출판`, `로봇 정책 평가`, `자율 실험실`)에 인용된 수치는 2026-08-09에 각 원문에서 직접 대조해 확인한 값이다. 본문에 실린 수치는 모두 해당 원문이 보고한 그대로이며, 원문에서 교차 확인할 수 없었던 수치는 본문에서 제외했다.

## 로보틱스 실행 환경

부록 F의 ROS 2, Docker, Jetson 환경 점검에서 기준 삼은 공식 문서다.

- [ROS 2 Humble, *Quality of Service settings*](https://docs.ros.org/en/humble/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
- [Docker, *Running containers*](https://docs.docker.com/engine/containers/run/)
- [Docker, *Host network driver*](https://docs.docker.com/engine/network/drivers/host/)
- [NVIDIA, *JetPack release notes*](https://docs.nvidia.com/jetson/jetpack/release-notes/index.html)

## 맥락 관리와 에이전트 운영

긴 문맥에서의 성능 저하, 스킬·도구 설계, thinking block 보존, prompt caching 규칙을 다룬 기술 문서다.

- [Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Chroma, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*](https://research.trychroma.com/context-rot) — 모델 18종, 입력 길이에 따른 성능 (확인일 2026-10-23)
- [Anthropic, *Context engineering: memory, compaction, and tool clearing*](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)
- [Anthropic, *Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic, *How we built our multi-agent research system*](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Anthropic, *Writing tools for agents*](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Anthropic, *Code execution tool*](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
- [Anthropic, *Extended thinking*](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [Anthropic, *Thinking*](https://platform.claude.com/docs/en/build-with-claude/thinking) — 턴 사이 thinking block 보존 규칙 (확인일 2026-10-23)
- [Anthropic, *Compaction at a token threshold*](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) — 기본 150,000 토큰, 최소 50,000 토큰 (확인일 2026-10-23)
- [Anthropic, *Prompt caching*](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Anthropic, *Structured outputs*](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Claude Code, *Hooks*](https://code.claude.com/docs/en/hooks)
- [Model Context Protocol, *Architecture*](https://modelcontextprotocol.io/docs/learn/architecture)

이 묶음 역시 본문과 부록에서 인용한 정의와 수치를 모두 원문과 대조해 확인했다. 특히 cookbook 문서에 나오는 측정값(최대 맥락 335,279 토큰, 파일 읽기 결과 96.3%, memory를 쓴 둘째 세션 172,623 토큰, 쓰지 않은 둘째 세션 333,977 토큰)은 해당 문서에 기록된 실제 실행 결과에서 가져온 것이다.

## 주장과 근거의 논증 구조

주장과 근거를 단계별로 잇는 논증 구조를 참고할 때 바탕이 되는 문헌이다.

- [Toulmin, *The Uses of Argument*](https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C)

공개 링크 외에 로컬 근거 자료, 대화 로그, 내부 작업 경로는 이 목록에 올리지 않고 로컬 기록에만 보관한다.
