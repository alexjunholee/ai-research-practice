# Ch.2 — 증거 흐름과 상태 복원

## 목적

연구 상태를 복원할 때 어떤 증거를 어느 무게로 사용할지 정한다. 요약, memory, 파일명, 검색 결과는
방향을 잡는 데 도움이 되지만 source truth를 대신하지 않는다.

## 근거

Endsley의 situation awareness는 현재 요소를 보고, 그 의미를 이해하고, 다음 상태를 예측하는 과정을
나눈다. 연구 상태 복원도 같은 순서를 따른다. 파일이 있는지 보는 것, 그 파일이 어떤 실행에서
나왔는지 이해하는 것, 그 결과로 어떤 claim이 가능한지 판단하는 것은 서로 다른 단계다.

LLM hallucination 연구가 반복해서 보인 문제도 여기 붙는다. 말이 자연스럽고 구조가 맞아 보여도
source와 맞지 않을 수 있다. 그래서 summary와 memory는 orientation이고, source file과 command output은
다른 증거 등급으로 둔다.

## 증거 등급

| 등급 | 예 | 허용되는 말 |
|---|---|---|
| raw artifact | source code, config, TeX, CSV, log | 파일 안에서 직접 확인한 내용 |
| execution output | command output, generated artifact, metric result | 해당 실행의 결과 |
| protocol-bound result | dataset, split, metric, baseline이 닫힌 결과 | 같은 protocol 안의 비교 |
| generated summary | handoff, compact summary, memory note | 다음에 확인할 위치 |
| assistant inference | 원인 추정, 구조 해석, 요약 판단 | 확인해야 할 후보 |

증거 등급은 claim의 상한을 정한다. summary는 source 위치를 알려 줄 수 있다. summary만으로
paper claim을 닫을 수는 없다. execution output은 해당 실행의 결과를 말할 수 있다. 그러나
dataset, split, metric이 닫히기 전에는 방법 개선 claim으로 올라가지 않는다.

## 상태 복원 대상

로보틱스/CV 연구 상태는 여러 artifact에 분산된다.

| 상태 | 확인할 항목 |
|---|---|
| repo state | branch, commit, modified file, build artifact |
| runtime state | process, container, device, environment, output path |
| data state | dataset version, split, sequence, calibration |
| result state | metric output, plot, table, failed run |
| manuscript state | TeX diff, figure source, claim/evidence map |
| memory state | project memory, handoff, durable correction |

## 복원 절차

1. 현재 repo와 공개/비공개 경계를 확인한다.
2. project memory나 handoff가 있으면 orientation으로 읽는다.
3. source of truth 파일을 찾는다.
4. 실행 결과가 필요한 경우 command와 output path를 확인한다.
5. 원고 작업이면 claim이 걸린 table, figure, paragraph를 찾는다.
6. summary와 source가 충돌하면 source를 우선한다.
7. 다음 action 하나만 정한다.

## Evidence gate

작업 전에는 다음 네 줄을 둔다.

```text
current evidence permits:
current evidence forbids:
promotion requires:
quarantine if:
```

예를 들어 `final_results.csv`가 있어도 command와 config가 없으면 현재 evidence는 숫자의 존재만
허용한다. 방법 개선 claim은 금지한다. promotion에는 dataset, split, metric script, baseline 확인이
필요하다. 파일명이 최신처럼 보이지만 생성 시각이나 command가 맞지 않으면 quarantine한다.

## 공개/비공개 경계

공개 문서에는 개인 대화 원문, 개인 경로, reviewer 원문, 미공개 숫자, 인증 정보가 들어가면 안 된다.
공개할 수 있는 것은 일반화된 실패 구조, 운영 규칙, 공개용 template이다.
