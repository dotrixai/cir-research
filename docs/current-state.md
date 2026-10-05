# Current state

**Snapshot:** 2026-10-05 15:00 UTC (previous snapshot: 2026-10-04 07:15 UTC)

> **This document reflects an evolving research program and may change as new experiments strengthen or falsify current hypotheses.**

## Summary

- On the cost objective, **no CIR organization reaches the 0.75 signal gate against the cheapest fair Transformer (B1A)** in the regime this hardware can reach (about 4M parameters, context ≤ 4,096).
- The cheapest member of the hybrid family (A025) **breaks even** with B1A: 0.985× the cost to the same BPB, 0.949× with an optimized implementation. The full hybrid A010 costs 1.23–1.27×. **The delta-hybrid mixer family is closed for BPB at context ≤ 4,096.**
- An analytic bound now measured on the canonical instrument shows that replacing B1A's mixer, even with a free one, cannot reach the 0.50 gate in this regime.
- **The one structural asymmetry found is a narrow capability: state tracking (parity).** Recurrent mixers that allow negative transition eigenvalues learn it; B1A never does. Inside a language model, though, the capability emerged in only 1 of 3 runs. The mechanism is prior art.
- Current work tests whether a stronger training signal makes that capability reliable (R88), and whether pre-pretraining on formal languages saves tokens differently for CIR and Transformer organizations (R89).

**The program objective has not been reached.**

## Experimental regime

| Item | Value |
|---|---|
| Model size | about 3.94M effective parameters (width 320, 3 layers); one additional width at about 7M (448) and one at about 2.8M (256) |
| Context | 4,096 tokens |
| Batch | 8 sequences = 32,768 tokens per update |
| Budget | up to 1,500 updates, about 49M tokens, cosine schedule |
| Data | English and Indonesian text (including Indonesian Wikipedia and short stories); BPE vocabulary of 2,048. State-tracking runs add a small share of synthetic parity examples |
| Quality metric | macro-averaged BPB on held-out English and Indonesian sets |
| Hardware | one commodity laptop CPU (Intel Core i5-13420H), two pinned performance cores, PyTorch eager; no GPU |
| Seeds | two for the main A010 comparisons and the state-tracking replication; one for most other results |

## Strongest baseline

**B1A**: a Transformer whose first two layers have no token mixer and whose last layer is a single global attention layer. It matches the gated local-global Transformer's BPB within 0.005 at about 0.50× its cost per update (MEASURED, I242, confirmed in sessions R79–R82). A windowed version (attention window 512) was measured at 0.914× B1A's cost per update with up to 0.010 BPB loss, so it is not cheaper to matched quality; **B1A remains the mandatory comparator** (I252).

## CIR organizations, measured against B1A

| Organization | Description | Cost to B1A's BPB | Status |
|---|---|---|---|
| A010 | two delta-rule recurrent layers + one softmax attention layer | 1.23–1.27× (ρ_u 0.70, ρ_c about 1.75), constant from width 320 to 448 | PROVISIONAL, one seed |
| A025 | B1A + two thin delta-rule mixers in layers 0–1 | **0.985×** (ρ_u about 0.83, ρ_c 1.18); 0.949× with an optimized implementation | Frozen criteria (≤ 0.90 BPB, ≤ 0.75 recall) **both failed**; family closed (I251, I252) |
| A025n | A025 with transitions allowed negative eigenvalues (same cost per update) | 0.939× on text with 6% synthetic parity examples | Below the frozen 0.90 criterion; see below (I255) |
| A019 | A010 with static n-gram heads instead of softmax | about 0.84× against a Transformer with the same heads (D2) | CONTESTED; gain from a generic module (I240) |

Against earlier, more expensive Transformers, A010's two-seed results still stand as measured: 0.633–0.643× the cost of a gated local-global Transformer and 0.587–0.625× of a gated full-attention Transformer (REPRODUCED). They no longer support a claim against the cheapest Transformer.

## State tracking

| Experiment | Result | Status |
|---|---|---|
| H032, synthetic, tiny models (2 seeds) | Parity: negative-eigenvalue delta mixer generalizes from length 64 to 256 at 0.96–0.98 accuracy; the current CIR mixer, a tiny B1A and a tiny full Transformer stay at chance (and fail even in-distribution at this budget). Modular counting: not solved. Permutations (S3): learned by one seed only | SUPPORTED for parity (I253) |
| R83–R84, inside the language model, seed 11 | A025n learns parity in-distribution (1.0) and at 2× length (0.96); 4× length 0.59. B1A and A025 stay at chance through 1,500 updates. BPB on the mixed data: A025n 0.024 lower than B1A | PROVISIONAL (I254, I255) |
| R85–R87, replication | A025n did **not** learn parity on seed 22, even at 1,500 updates, nor with a longer training span on seed 11. Its mixed-data BPB advantage over B1A replicated (0.017–0.026 at 750 updates) regardless | Learning in the LM: **1 of 3 runs** (I256, I257) |

Interpretation: the mechanism is available to the negative-eigenvalue organization and unavailable to B1A, but a sparse synthetic signal (about 6% of data) does not reliably make it emerge at this scale. Parity is in TC⁰, so the Transformer's failure here is empirical, not a complexity separation. The mechanism is prior art (Grazzi et al. 2025; RWKV-7). This is a **narrow capability result, not a cost result**.

## Gate status

| Gate | Against earlier strong Transformers | Against B1A (frontier) |
|---|---|---|
| ≤ 0.75 signal | Passed in the tested regime (BPB, two seeds) | **Not reached.** Best: A025 0.949–0.985 (break-even); recall marginal |
| ≤ 0.50 interesting | CONTESTED: 0.50 once (A019, one seed, D1); 0.84 under D2 | Not reached; analytically out of reach for mixer substitution at context ≤ 4,096 |
| ≤ 0.20 industry-level | Not reached | Not reached |
| ≤ 0.10 breakthrough-level | Not reached | Not reached |

## Active threats and constraints

1. **Analytic bound, now tighter.** Measured on the canonical instrument, B1A's attention kernel is only about 13–23% of its cost per update, so even a free replacement leaves a ratio of about 0.77–0.87 (ESTIMATED).
2. **Generic modules.** Engram and n-gram heads help Transformers as much or more than CIR candidates; under D2 they are neutral.
3. **Scale.** Attention's share of cost falls roughly with 1/width (PROJECTED). Models ≥ 30M parameters or contexts ≥ 16K are beyond a realistic CPU budget (days to weeks per run).
4. **Capability reliability.** State tracking emerged in 1 of 3 language-model runs.
5. **Prior art.** The state-tracking mechanism and formal-language pre-pretraining are both published ideas.
6. **Learning-rule axis.** A first-principles pass found no training-rule lever specific to recurrent organizations under D2 in this regime (selective backward and count-based statistics also apply to Transformers).

## Active experiments

| ID | Question | Status |
|---|---|---|
| R88 | With 2.5× more parity examples (15%), does A025n learn parity on the seed that failed, while B1A still does not? | UNDER EVALUATION (training) |
| R89 | Does 100 updates of formal-language pre-pretraining (k-Shuffle Dyck) reduce total tokens to matched quality, and differently for B1A and A025? Criterion: total cost ≤ 0.90 of the clean control | Frozen, queued after R88 |
| H033 | Draft hypothesis: formal-language pre-pretraining helps organizations whose computational class includes the language, so the savings depend on organization. Credence about 15% | Tested first by R89 |

Cancelled: R74 (thin-mixer projection removal), because the thin-mixer family was closed by R81/R82.

## What would falsify the current direction

- R88 fails: state tracking does not emerge reliably even with a stronger signal. The capability path at this scale then closes.
- R89 shows no saving, or the same saving for both organizations: formal-language pre-pretraining is then a generic lever with no CIR-specific asymmetry.
- Any surviving capability edge vanishes with a second seed.

## Open decisions

After R88, the program will choose between: documenting the cost axis at this scale as falsified; continuing the capability path with stronger signals and harder state-tracking tasks; or reporting against standard Transformers (D1), where cheap organizations already reach about 0.50× but rely mostly on prior art. Larger scale is not within the current hardware budget.
