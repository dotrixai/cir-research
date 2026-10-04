# Current evidence

Snapshot: 2026-10-04 07:15 UTC. Regime unless stated: about 4M effective parameters, 3 layers, 4,096-token context, batch 8, up to 1,500 updates (about 49M tokens), English and Indonesian text, one laptop CPU. Status vocabulary: [docs/methodology.md](../docs/methodology.md#12-epistemic-status). Machine-readable: [evidence-table.csv](evidence-table.csv).

## Standing results

| ID | Finding | Value | Label | Seeds | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|---|
| I203 | A010 vs gated full-attention Transformer | 0.034 lower BPB; cost to final Q 0.587–0.625 | MEASURED / ESTIMATED | 2 | REPRODUCED | Holds against the strongest Transformer in quality tested | Expensive baseline |
| I211 | A010 vs gated local-global Transformer | 0.041 lower BPB; cost to final Q 0.633–0.643; at early Q 0.78–0.82 | MEASURED / ESTIMATED | 2 | REPRODUCED, CONTESTED | Real advantage over that baseline | Not the cheapest baseline; inherited learning rate |
| I242 | B1A (one attention layer) vs gated local-global Transformer | BPB within 0.005 at 0.502× cost per update | MEASURED | 1 | SUPPORTED | Earlier D1 ratios used an inefficient baseline | One seed |
| I242, I248 | A010 vs B1A, BPB | cost to final Q 1.23–1.27 (ρ_u 0.70, ρ_c 1.75–1.80) | ESTIMATED | 1 | PROVISIONAL | No BPB advantage against the cheapest Transformer | One seed |
| I244 | A010 vs B1A at equal compute | BPB difference 0.0023 | MEASURED | 1 | PROVISIONAL | Tie | Within seed noise |
| I245 | Recall cost vs cheapest Transformers | 0.74–1.0 | ESTIMATED | 1–2 | CONTESTED | Marginal | Depends on Q and seed |
| I240 | A019 vs D1 / D2 at final Q | 0.50 / 0.84 | ESTIMATED | 1 | CONTESTED | Gain is the generic n-gram module | Prior art; one seed |
| I240 | A010 vs D2 at final Q | 1.06 | ESTIMATED | 1 | PROVISIONAL | No recurrent-specific BPB advantage under D2 | One seed |
| I224 | Engram gain, Transformer vs A010 | 0.118 vs 0.093 BPB at 750 updates | MEASURED | 1 | SUPPORTED | Generic module helps the Transformer more | 750 updates only |
| I221 | A010 vs local-global at width 448 | cost to final Q 0.719 | ESTIMATED | 1 | PROVISIONAL | Signal gate passed; advantage shrinking with width | Tokens per parameter fell |
| I248 | A010 vs B1A across widths | ρ_u 0.70 (width 320), 0.71 (width 448) | ESTIMATED | 1 | PROVISIONAL | No trend toward an advantage with width | Fixed tokens |
| I246, I250 | Context use at this scale | no softmax model copies verbatim beyond about 2,000 tokens; exact n-gram heads copy at any gap | MEASURED | 1 | SUPPORTED | Long-context route weak at this scale | This data only |
| I209 | A010 per-update ratio, 4,096 → 8,192 context | 0.887 → 0.942 | MEASURED | 1 | SUPPORTED | Longer context does not help A010 | One session |

## Superseded or quarantined

| ID | Former claim | Why | Status |
|---|---|---|---|
| I158 | Pure delta at 0.587–0.594 | AdamW only; reversed under Muon (I177) | SUPERSEDED |
| I188 | A010 at 0.570 | Baseline strengthened | SUPERSEDED |
| I222 | A019 at 0.530 at intermediate Q | Final-Q and D2 comparisons (I240) | SUPERSEDED |
| I241 | Recall cost 0.36–0.69 against all tested Transformers | Biased estimator (I245) | SUPERSEDED |
| I183, I186 | Early per-update ratios | Uncontrolled core placement | QUARANTINED |

## Under evaluation

| ID | Question | State |
|---|---|---|
| R81 | A025 (thin recurrent mixers on B1A) vs B1A: BPB cost ≤ 0.90, recall cost ≤ 0.75 | Training. Interim (one seed): A025 keeps about 15–20% of A010's BPB margin over B1A; no verdict |
| R82 | Optimized A025 implementation; windowed B1A cost | Frozen, queued |
| H032 | Synthetic state tracking with negative-eigenvalue recurrence | Frozen, queued |
| R74 | Removing dense projections from a mixing layer | Frozen, queued |

## Figures

- [../figures/cost-to-q.svg](../figures/cost-to-q.svg): cost to matched Q, D1 and D2, one session.
- [../figures/baseline-history.svg](../figures/baseline-history.svg): A010's cost ratio as the baseline was strengthened.
