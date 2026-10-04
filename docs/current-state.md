# Current state

**Snapshot:** 2026-10-04 07:15 UTC

> **This document reflects an evolving research program and may change as new experiments strengthen or falsify current hypotheses.**

## Experimental regime

| Item | Value |
|---|---|
| Model size | about 3.94M effective parameters (width 320, 3 layers); one additional width at about 7M (448) and one at about 2.8M (256) |
| Context | 4,096 tokens |
| Batch | 8 sequences = 32,768 tokens per update |
| Budget | up to 1,500 updates, about 49M tokens, cosine schedule |
| Data | English and Indonesian text (including Indonesian Wikipedia and short stories); BPE vocabulary of 2,048 |
| Quality metric | macro-averaged BPB on held-out English and Indonesian sets |
| Hardware | one commodity laptop CPU (Intel Core i5-13420H), two pinned performance cores, PyTorch eager; no GPU |
| Seeds | two for the main A010 comparisons; one for most other results |

## Strongest CIR candidate

**A010**: two delta-rule recurrent mixing layers followed by one full causal softmax attention layer with rotary position encoding, trained with Muon ([architecture.md](architecture.md)). Status: REPRODUCED against two Transformer baselines; CONTESTED as a cost claim because a cheaper Transformer was found afterwards.

## Strongest baseline

**B1A**: a Transformer whose first two layers have no token mixer and whose last layer is a single global attention layer. It matches the gated local-global Transformer's BPB within 0.005 at 0.502× its cost per token (MEASURED, one seed, I242). It is the mandatory comparator for all new claims.

## Reproduced evidence

| Comparison | Quality at 1,500 updates | Cost to final Q | Seeds |
|---|---|---|---|
| A010 vs gated local-global Transformer | 0.041 lower BPB | 0.633, 0.643 (ESTIMATED) | 2 |
| A010 vs gated full-attention Transformer | 0.034 lower BPB | 0.587–0.625 (ESTIMATED) | 2 |

Against the local-global Transformer, the cost ratio at early quality (its quality after 375–500 updates) is 0.78–0.82, falling to 0.63–0.64 at final quality. Both baselines are now known to be more expensive than B1A, so these results show an advantage over those baselines only.

## Against the cheapest Transformer

| Measure | Value | Label | Seeds |
|---|---|---|---|
| A010 cost to reach B1A's final BPB | 1.23–1.27× | ESTIMATED | 1 |
| BPB at equal compute (B1A widened to A010's cost per update) | 0.0023 lower for A010, i.e. a tie | MEASURED | 1 |
| A010 cost to B1A-level associative recall (corrected estimator) | 0.74–1.0× | ESTIMATED | 1 |

**No robust cost advantage over the cheapest fair Transformer is established.**

## Gate status

| Gate | Against earlier strong Transformers | Against B1A |
|---|---|---|
| ≤ 0.75 signal | Passed in the tested regime (BPB, two seeds) | Not reached (BPB); recall marginal, under challenge |
| ≤ 0.50 interesting | CONTESTED: 0.50 once (A019, one seed, D1); 0.84 under D2 | Not reached |
| ≤ 0.20 industry-level | Not reached | Not reached |
| ≤ 0.10 breakthrough-level | Not reached | Not reached |

## Active threats

1. **Cheaper Transformers.** B1A already removed the BPB advantage; a windowed B1A may be another 10–30% cheaper per token (ESTIMATED; being measured in R82).
2. **Generic modules.** Engram and static n-gram heads help Transformers as much or more than they help CIR candidates.
3. **Analytic bound.** At 4,096 tokens of context, even a free recurrent core replacing B1A's attention leaves a per-update cost ratio of 0.55–0.72 (ESTIMATED), so the 0.50 gate cannot be reached by mixer substitution alone in this regime.
4. **Scale.** Attention's share of cost shrinks roughly in proportion to 1/width (PROJECTED), which shrinks any saving from replacing it.
5. **Small capability edge.** The recall advantage against B1A is marginal and rests on one seed.
6. **Hardware specificity.** One laptop CPU; thin recurrent mixers there are limited by per-call overhead.
7. **Prior art.** The remaining state-tracking hypothesis is a rediscovery of published work (DeltaNet with negative eigenvalues, RWKV-7).

## Scaling status

Three widths at small scale; nothing above about 7M parameters. Against B1A, A010's update-efficiency ratio is 0.70 at 4M and 0.71 at 7M, so the cost ratio stays around 1.23 at both. See [scaling.md](scaling.md).

## Capability status

Probed: BPB, short-range copying, long verbatim copying, associative recall, bracket closing, context use by position. Not measurable at this scale: grammar, binding, reasoning, coherent generation. See [capabilities.md](capabilities.md).

## Active experiments

| ID | Question | Status |
|---|---|---|
| R81 | Can thin recurrent mixers added to B1A (A025) beat B1A on BPB cost (criterion ≤ 0.90) or recall cost (≤ 0.75)? | UNDER EVALUATION. Interim curves (one seed): A025 keeps about 15–20% of A010's BPB margin over B1A; projected update ratio about 0.9–0.95, so the BPB criterion is likely to fail. No verdict yet. |
| R82 | Systems session: can an optimized implementation lower A025's cost per update, and how much does a windowed B1A save? | Frozen, queued after R81 |
| H032 | Can recurrence with negative transition eigenvalues track state (parity, modular counting, permutations) where a single attention layer cannot, at test lengths beyond training length? | Frozen, queued. Synthetic, tiny models. A narrow capability question; the idea is prior art |
| R74 | Can the dense projections of a mixing layer be removed without quality loss? | Frozen, queued; B1A included |
| A026 | Does a negative-eigenvalue variant of A010 keep language quality? | Conditional on H032 |

## What would falsify the current direction

- R81 fails both frozen criteria: the delta-hybrid family is closed at contexts up to 4,096 under D2, and a first-principles reset follows with B1A as mandatory comparator.
- H032 shows no state-tracking gain, or the gain costs language quality.
- Any surviving edge vanishes with a second seed or a larger width.
- Windowed Transformers with an exact n-gram index match long-context capability more cheaply.

## Open research questions

1. Is there any structural cost asymmetry between recurrence and attention at practical context lengths once generic modules are shared?
2. Does an expressivity advantage (state tracking) translate into anything measurable on language?
3. Does any advantage appear only at contexts far beyond 4,096 tokens, and do real tasks need it? Current evidence: softmax models at this scale use little context beyond about 2,000 tokens, and the recurrent state does not substitute for distant attention.
4. How do the results change on GPUs and at 100M+ parameters?
