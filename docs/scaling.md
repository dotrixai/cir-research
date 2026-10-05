# Scaling

Small-scale results do not establish large-scale behavior. This document separates what was MEASURED, what was ESTIMATED from measurements, and what is PROJECTED or hypothesized.

## Scale points tested

| Width | Effective parameters | Tokens | Tokens per parameter | Comparisons |
|---|---|---|---|---|
| 256 | about 2.8M | scaled to match the 320 ratio | about 12.3 | A010 vs gated local-global Transformer |
| 320 | about 3.94M | about 49M | about 12.3 | all main results |
| 448 | about 7M | about 49M (fixed) | about 6.4 | A010 vs gated local-global Transformer; A010 vs B1A; B1A wide (equal-compute attack) |

All at 3 layers, 4,096-token context, batch 8, one CPU. Depth, context length, batch size and hardware have not been scaled for the current candidates.

## Observations

| Observation | Values | Label | Status |
|---|---|---|---|
| A010 vs local-global Transformer, cost to final Q | width 320: 0.633–0.643 (two seeds); width 448: 0.719 (ρ_u 0.794, ρ_c 0.906) | ESTIMATED | width 448: PROVISIONAL (one seed) |
| BPB margin vs local-global Transformer | width 448 at fixed tokens: 0.025, shrinking from 0.041 at width 320 in every domain | MEASURED | PROVISIONAL |
| BPB margin at a fixed tokens-per-parameter ratio | width 256: 0.025; width 320: 0.041 (margin grew with size) | MEASURED | PROVISIONAL; learning rates differed between widths |
| A010 update efficiency vs B1A | ρ_u 0.70 at width 320, 0.71 at width 448 | ESTIMATED | PROVISIONAL |
| A010 cost to B1A's BPB | about 1.23–1.27 at both widths | ESTIMATED | PROVISIONAL |
| Per-update ratio A010 vs local-global | 0.875 (width 320) vs 0.906 (width 448) in one session | MEASURED | |
| Recall advantage vs local-global Transformer | persisted at width 448 | ESTIMATED | CONTESTED: measured with the estimator later found biased; not re-audited |

## Confounds

- **Tokens per parameter.** The width-448 run kept tokens fixed, so tokens per parameter fell from about 12.3 to 6.4. That alone could explain the weaker ratio against the local-global Transformer. At a fixed ratio, the margin grew from 2.8M to 4M, the opposite direction.
- **Learning rate.** Selected learning rates differed between widths, and the local-global baseline's learning rate was inherited rather than screened.
- **Sub-optimal training budget.** All runs are below compute-optimal token budgets.
- **Depth.** Only 3 layers. Literature suggests lookup modules are most valuable in shallow models, so the value of generic modules relative to recurrence may be overstated here.

## Projections and hypotheses

These are not evidence.

- **Attention share shrinks with width (PROJECTED).** Per token, attention cost grows with context length T while projection and channel-mixing cost grow with width d. Attention's share of cost therefore falls roughly in proportion to 1/d at fixed T; at d = 4,096 and T = 4,096 it would be about 8%. Any saving from replacing attention with a cheaper mixer shrinks accordingly, so a mixer-substitution advantage at 4M would not be expected to persist at large width with the same context.
- **Where a structural asymmetry could remain (hypothesis).** Recurrent state and exact n-gram indices cost O(1) per token regardless of context, while global attention costs O(T). This matters only when T is large relative to width and the task genuinely needs distant information. At this scale and on this data, softmax models use little context beyond about 2,000 tokens, and the recurrent state did not substitute for distant attention. Credence in this route is currently low.
- **State tracking (hypothesis H032).** Recurrence with negative transition eigenvalues can represent state-tracking tasks that constant-depth Transformers provably cannot. Whether this is worth anything for language at any scale is open.

## What would count as positive scaling evidence

1. A cost ratio against the cheapest fair Transformer of ≤ 0.75 that holds or improves across at least three widths spanning 10× in parameters, at a fixed tokens-per-parameter ratio, with screened learning rates on both sides.
2. The same under D2 (generic modules on both sides).
3. Reproduction with a second seed at the largest width.
4. Confirmation on at least one additional hardware type, preferably GPU.

None of these conditions is currently met. Runs at 30M+ parameters or 16K+ context would take days to weeks each on the current hardware and are not scheduled.
