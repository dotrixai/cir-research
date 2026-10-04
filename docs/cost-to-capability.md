# Cost to capability

## Decomposition

```
TotalCostRatio(Q) ≈ ρ_u × ρ_c
```

- `ρ_u`: updates (equivalently tokens, at fixed batch) the candidate needs to reach `Q`, divided by the updates the baseline needs. Read from validation curves; between checkpoints, interpolated. Capability curves are first made monotone (isotonic) and the first crossing is used for every arm.
- `ρ_c`: candidate cost per update divided by baseline cost per update, from one canonical timing session.

`Q` is defined as "the baseline's quality after N updates", for N = 375, 500, 750, 1,000, 1,250, 1,500. A ratio below 1 favors CIR.

All ratios below are ESTIMATED (computed from MEASURED BPB curves and MEASURED per-update timings). They hold only for the regime in [current-state.md](current-state.md#experimental-regime).

## Cost per update (ρ_c), MEASURED

The same pair varies by about ±3% between sessions, so ratios are compared only within one session.

| Session | Arm | Cost per update relative to gated local-global Transformer |
|---|---|---|
| R78 (5 arms) | A010 | 0.867 |
| | A019 | 0.678 |
| | TF-LG + n-gram heads | 0.798 |
| | gated full attention | 1.090 |
| R79 | B1A | 0.502 |
| | A010 | 0.902 |
| R80 | B1A (width 320) | 0.506 |
| | B1A (width 448) | 0.794 |
| | A010 | 0.887 |

A010 costs about 1.75–1.80× B1A per update. In profiling, B1A's single attention layer is about 45% of its forward time at 4,096 tokens (indicative, not canonical).

## A010 against earlier baselines: two seeds

Source: R62, R67 (I203, I211). Seeds 11 and 22, per-update ratios from canonical sessions.

| Q = baseline after N updates | 375 | 500 | 750 | 1,000 | 1,250 | 1,500 |
|---|---|---|---|---|---|---|
| vs gated local-global, seed 11 | 0.818 | 0.814 | 0.762 | 0.731 | 0.700 | 0.643 |
| vs gated local-global, seed 22 | 0.784 | 0.799 | 0.749 | 0.730 | 0.716 | 0.633 |
| vs gated full attention, seed 11 | 0.695 | 0.733 | 0.720 | 0.698 | 0.677 | 0.625 |
| vs gated full attention, seed 22 | 0.662 | 0.685 | 0.673 | 0.664 | 0.654 | 0.587 |

Against the local-global Transformer, the 0.75 gate is crossed only from Q ≈ its quality after 750–1,000 updates. The BPB gap stays roughly constant through training, and the baseline's curve is steep early, so the cost ratio improves with the target quality. Nothing is claimed beyond 1,500 updates.

## D1 vs D2: one session, seed 11

Source: R72 formal verdict, R78 cost session (I240). D1 = gated local-global Transformer. D2 = the same Transformer with the same n-gram heads as A019 (TF-LGN).

| Q = baseline after N updates | 375 | 500 | 750 | 1,000 | 1,250 | 1,500 |
|---|---|---|---|---|---|---|
| A010 vs D1 | 0.80 | 0.80 | 0.74 | 0.71 | 0.68 | 0.63 |
| A019 vs D1 | 0.38 | 0.46 | 0.51 | 0.54 | 0.54 | 0.50 |
| A010 vs D2 | n/m | n/m | 1.14 | 1.10 | 1.07 | 1.06 |
| A019 vs D2 | n/m | n/m | 0.79 | 0.83 | 0.85 | 0.84 |

n/m = not measured (D2 evaluated from 750 updates). Machine-readable: [../results/cost-to-q.csv](../results/cost-to-q.csv). Chart: [../figures/cost-to-q.svg](../figures/cost-to-q.svg).

Reading: A019's low D1 ratio is mostly the n-gram heads, which help a Transformer nearly as much. Under D2, A010 is more expensive than the Transformer with n-gram heads.

## Against the cheapest Transformer (B1A), final quality

| Comparison | ρ_u | ρ_c | Cost ratio | Seeds |
|---|---|---|---|---|
| A010 vs B1A, width 320, BPB | 0.70 | 1.75–1.80 | **1.23–1.27** | 1 |
| A010 width 448 vs B1A width 448, BPB (fixed tokens) | 0.71 | about 1.77 | about 1.25 | 1 |
| A010 vs B1A widened to equal cost per update, BPB | | | about 1.10 (BPB difference 0.0023, a tie) | 1 |
| A010 vs B1A, associative recall (N=8 / N=32, at B1A's plateau) | | | 0.81 / 0.78 | 1 |
| A010 vs wide B1A, associative recall (N=8 / N=32) | | | 1.01 / 0.74 | 1 |

## Associative recall, corrected estimator

Source: I245. An earlier estimator charged the baseline its full 1,500 updates even when its recall had already plateaued, which favored CIR (reported 0.36–0.69, now SUPERSEDED). Corrected values, A010 cost to reach each baseline's recall plateau (seed 11 / seed 22):

| Baseline | N = 8 | N = 32 |
|---|---|---|
| gated full attention | 0.44 / 0.50 | 0.48 / 0.36 |
| gated local-global | 0.36 / 0.45 | 0.40 / 0.37 |
| local-global + n-gram heads | 0.69 / 0.97 | 0.58 / 0.49 |
| B1A (width 320) | 0.81 | 0.78 |
| B1A (width 448) | 1.01 | 0.74 |

Large recall advantages exist only against expensive Transformers. Against the cheapest ones the advantage is 0.74–1.0, i.e. marginal.

## Bounds

- **Longer context does not help A010.** Per-update cost ratio A010/TF-LG rises from 0.887 at 4,096 tokens to 0.942 at 8,192 (MEASURED, I209).
- **Amdahl bound (ESTIMATED).** B1A's training cost splits roughly into shared parts (channel mixing, embeddings, output head), mixer projections, and the attention kernel. A recurrent core that replaced the attention kernel at zero cost would still leave a per-update ratio of 0.55–0.72 against B1A at 4,096 tokens. Reaching the 0.50 gate by mixer substitution would therefore also need a large update-efficiency advantage, for which there is no evidence against B1A.
