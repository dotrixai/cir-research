# Current state

**Snapshot:** 2026-10-10 07:47 UTC (previous snapshots: 2026-10-05 15:00 UTC, 2026-10-04 07:15 UTC; see [research-log.md](research-log.md))

> **This document reflects an evolving research program and may change as new experiments strengthen or falsify current hypotheses.**

## Summary

- **CIR-specific architectures (D2): objective not reached.** The delta-rule recurrent mixers and their hybrids have no cost advantage over the cheapest fair Transformer (B1A). The cheapest hybrid breaks even (0.949–0.985×). An analytic bound rules out mixer substitution as a route to the 0.50 gate at context ≤ 4,096. This family is closed for general language modeling at this scale.
- **A generic organization (D1) is now the main line.** A small one-attention Transformer combined with counted n-gram statistics, an in-context cache, a longest-match pointer and a tiny trained gate reaches the final quality of a strong Transformer (TF-LGN) at **0.0625–0.0634× its training cost**, averaged over English and Indonesian, on two seeds (ESTIMATED).
- **The average hides a large language gap.** Indonesian: **0.032×**. English: the cheapest configuration does not reach TF-LGN quality in its budget; the best English configuration reaches **0.149×** (one evaluation run). Against B1A at equal budget, the English advantage fades as the small English corpus repeats.
- **This is not a new method.** The organization matches published prior art, including modded-nanogpt PR #380. What CIR contributes is matched-quality cost accounting that was attacked, reproduced and corrected on small hardware.
- **Active:** R161 tests whether data repetition, rather than language, explains the gap.

## Experimental regime

| Item | Value |
|---|---|
| Networks (counted organization) | one-attention Transformer (B1A family), width 128 (0.82M parameters) or 192 (1.43M) |
| Networks (CIR mixers, earlier phase) | about 3.94M effective parameters (width 320); up to about 7M (width 448) |
| Context | 4,096 tokens; the cheapest configuration trains on 1,024-token chunks |
| Data | English 3.86M tokens, Indonesian 31.2M tokens, short stories; BPE vocabulary of 2,048 |
| Budget | 1,500 updates (batch 8, 32,768 tokens per update) at 1×; ladder from 0.5× to 4× |
| Quality metric (counted phase) | bits per token on positions whose 12-token context does not appear in training (the training data contains duplicates) |
| Hardware | one commodity laptop CPU (Intel Core i5-13420H), two pinned performance cores; no GPU |
| Seeds | two for the main counted results; one for per-language and ladder results |

## Baselines

| Name | Role |
|---|---|
| **TF-LGN** | gated local-global Transformer with n-gram heads; its final quality defines the target `Q_N`. Its cost per token is now measured directly (I313) |
| **B1A** (width 320) | the cheapest fair Transformer found; used for equal-budget comparisons and as the frontier for CIR mixers |

Baseline frontier status for the counted claim: STRONG for `Q_N` (four opponent routes attacked: n-gram heads, larger Transformers up to width 448, twice the training, and the same short-context training). UNATTACKED above 4× budget and for B1A larger than width 320.

## Counted organization: results

| Measure | Value | Label | Seeds | Status |
|---|---|---|---|---|
| Training cost to `Q_N`, average EN+ID, A039 (width 128) | 0.0625 / 0.0634× TF-LGN | ESTIMATED | 2 | REPRODUCED |
| Same, width 192 | 0.083 / 0.077× | ESTIMATED | 2 | REPRODUCED |
| Indonesian, best configuration | 0.032× | ESTIMATED | 1 | SUPPORTED |
| English, best configuration (width 192, short context) | 0.149× | ESTIMATED | 1 | SUPPORTED |
| English, A039 | does not reach `Q_N` in 1,500 updates | MEASURED | 1 | SUPPORTED |
| Cheaper-inference variant: training / prefill inference | 0.065–0.066× / 0.48× TF-LGN | ESTIMATED / MEASURED | 2 | REPRODUCED |
| Phase-robust variant (overlapping chunks) | training 0.062×, inference 0.49× | ESTIMATED / MEASURED | 1 | PROVISIONAL |
| Budget ladder vs B1A, same budget, average | 0.048 / 0.063 / 0.067 / 0.066 at 0.5× / 1× / 2× / 4× | ESTIMATED | 1 | SUPPORTED |
| Same, per language | ID 0.044 / 0.040 / 0.038 / ≤ 0.034; EN 0.053 / 0.121 / not reached / not reached | ESTIMATED | 1 | CONTESTED for EN |
| Unseen text (Indonesian Wikipedia) | 0.053 / 0.055× TF-LGN | ESTIMATED | 2 | REPRODUCED |
| Long copy gain | 3.1–3.3 bits (TF-LGN 2.89) | MEASURED | 1–2 | SUPPORTED |
| Exact single-token recall | 0.99+, only with the trained gate | MEASURED | 1–2 | SUPPORTED |
| Count table memory | about 434 MB (about 76× the network weights) | MEASURED | 1 | — |
| Token-by-token decode cost | not measured | — | — | OPEN |

## CIR-specific organizations against B1A

| Organization | Cost to B1A's BPB | Status |
|---|---|---|
| A010 (two delta-rule layers + one softmax layer) | 1.23–1.27× | PROVISIONAL |
| A025 (B1A + thin delta mixers) | 0.985× (0.949× optimized) | FALSIFIED against frozen criteria; family closed |
| A025n (negative-eigenvalue variant) on text mixed with parity data | 0.939× | PROVISIONAL; below the frozen 0.90 criterion |

State tracking: negative-eigenvalue recurrence learns parity inside the language model with a strong enough signal (15% of data); B1A never does. A one-layer Transformer with chain-of-thought reaches a harder permutation target more cheaply than CIR recurrence, so the state-tracking **cost** claim is falsified (I267–I268).

## Gate status

| Gate | CIR-specific organizations (D2) | Generic counted organization (D1) |
|---|---|---|
| ≤ 0.75 signal | Not reached (best 0.949–0.985×) | Passed, both languages |
| ≤ 0.50 interesting | Not reached; analytically out of reach for mixer substitution here | Passed, both languages; inference about 0.49× |
| ≤ 0.20 industry-level | Not reached | Passed: English 0.149× (one run), Indonesian 0.032× |
| ≤ 0.10 breakthrough-level | Not reached | **Partly passed:** on average and in Indonesian, two seeds; **not in English** |

All D1 passes are PROVISIONAL, generic, prior art, and limited to networks ≤ 1.4M parameters on one CPU.

## Active threats

1. **Language and data repetition.** The English gain is small and disappears at 2× and 4× budget, where the 3.86M-token English corpus is seen 6–13 times. Under test in R161.
2. **Scale.** Networks ≤ 1.4M parameters, data ≤ about 200M tokens, opponents ≤ width 448. Larger Transformers may catch up above 4× budget; a fitted equivalent-compute multiplier of about 15× partly reflects the fixed-size opponent's capacity limit.
3. **Prior art.** The organization is known (modded-nanogpt PR #380; infini-gram; cache language models).
4. **Deployment.** Decode cost unmeasured; count tables about 434 MB.
5. **Gate dependence.** The gate needs about 4,000 tokens of in-domain text; it does not transfer across languages.
6. **D2.** No CIR-specific primitive that reduces dense computation for language quality has been found.

## Active and queued work

| ID | Question | Status |
|---|---|---|
| R161 | With the Indonesian corpus cut to the English size (so it repeats as often), does the Indonesian advantage collapse? | UNDER EVALUATION (training) |
| Decode | Token-by-token generation cost of the counted organization | Queued |
| Tables | Smaller count tables without quality loss | Queued |
| English | Larger English corpus or a larger English network | Conditional on R161 |
| Ladder | Opponents larger than B1A width 320 above 4× budget | Conditional; heavy for current hardware |

## What would falsify the current direction

- R161 shows the Indonesian gain survives heavy repetition, so the English gap is about language.
- A larger English corpus still leaves English above 0.10×.
- A larger Transformer above 4× budget matches the counted organization.
- Decode cost or table memory erases the inference advantage.
