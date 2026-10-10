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
| R81 | A025 | 0.592 |
| | B1A (width 320) | 0.501 |
| | A010 | 0.890 |
| R82 | A025 | 0.587 |
| | A025, optimized implementation | 0.569 |
| | B1A (width 320) | 0.500 |
| | B1A, attention window 512 | 0.457 |

A010 costs about 1.75–1.80× B1A per update; A025 about 1.18×. A 512-token attention window saves only 8.6% of B1A's cost per update on this CPU. In profiling, B1A's single attention layer is about 45% of its forward time at 4,096 tokens (indicative, not canonical).

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
| A025 vs B1A, width 320, BPB | about 0.83 | 1.18 | **0.985** (0.980 re-measured; 0.949 optimized) | 1 |
| A025n vs B1A, BPB on text with 6% synthetic parity examples | about 0.80 | 1.18 | 0.939 | 1 |
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
- **Amdahl bound (ESTIMATED).** B1A's training cost splits roughly into shared parts (channel mixing, embeddings, output head), mixer projections, and the attention kernel. A recurrent core that replaced the attention kernel at zero cost would still leave a per-update ratio of 0.55–0.72 against B1A at 4,096 tokens by profiling, and about 0.77–0.87 using the attention share implied by the canonical windowing measurement (I252). Reaching the 0.50 gate by mixer substitution would therefore also need a large update-efficiency advantage. Against B1A, the best measured is about 0.70 (A010), paid for by 1.75× cost per update.
- **The hybrid family is closed in this regime.** The cheapest hybrid, A025, trades about 35–40% of A010's update advantage for about a quarter of its extra per-update cost, and lands at break-even (0.985). An optimized implementation gave only 3% more.
- **Mixed-data regime.** With 6% synthetic parity data, A025n is 0.939× B1A. That is below parity but above the frozen 0.90 criterion, and the BPB gap appeared whether or not A025n learned parity (I256). It most likely reflects B1A being disrupted by tokens it cannot model.

## Counted organization (D1)

Target quality `Q_N` = TF-LGN's final quality at 1,500 updates. Metric: bits per token on positions whose 12-token context does not appear in training (the corpus has duplicates; I269, I270). Cost = canonical cost per token × updates to `Q_N`, plus measured counting time. TF-LGN's cost per token is now measured directly in the same session; the bridged estimate used before 2026-10-08 was about 5% low, so earlier ratios were 4–5.5% too favourable (I313). All values below are corrected and ESTIMATED.

### Step by step (average of English and Indonesian)

| Step | Training cost to `Q_N` (× TF-LGN) | Seeds | Evidence |
|---|---|---|---|
| Width 192 + counted prior + cache | 0.172 / 0.189 | 2 | I283, I284 |
| + windowed attention + pointer | 0.128 | 1 | I294 |
| + trained gate | 0.0995 / 0.101 | 2 | I298, I314 |
| + training on 1,024-token chunks | 0.083 / 0.077 | 2 | I308, I315 |
| Width 128 (A039) | **0.0625 / 0.0634** | 2 | I316, I318 |
| A039, cheaper-inference variant | 0.065 / 0.066 | 2 | I321, I323 |
| A039, overlapping chunks (phase-robust) | 0.062 | 1 | I331 |

Against B1A trained twice as long, A039 is 0.062× (I318). Width 96 gives 0.063 (no better; I320).

### Per language (I337–I339)

| Measure | Indonesian | English |
|---|---|---|
| Best organization vs TF-LGN | 0.032× (A039) | 0.149× (width 192, short context) |
| A039 vs TF-LGN | 0.032× | target not reached in 1,500 updates |
| Width 192 windowed (A036) vs TF-LGN | 0.067× | 0.188× |

### Budget ladder against B1A at the same budget (I326, I332, I340)

Independent annealed runs at each budget, B1A width 320.

| Budget | 0.5× | 1× | 2× | 4× |
|---|---|---|---|---|
| Average EN+ID | 0.048 | 0.063 | 0.067 | 0.066 |
| Indonesian | 0.044 | 0.040 | 0.038 | ≤ 0.034 |
| English | 0.053 | 0.121 | not reached | not reached |
| English corpus passes | 1.6 | 3.2 | 6.4 | 12.7 |

A fit `L(C) = E + A·C^−γ` with a separate asymptote per arm gives an equivalent-compute multiplier of 14.8–17.9× at B1A's final quality (I334). This is ESTIMATED from a fit, and part of it reflects the capacity limit of a fixed-size opponent: A039 at 4× already passes B1A's fitted asymptote. Within the tested compute range, every other Transformer configuration measured was worse than the B1A width-320 curve (I335). Above 4×, with larger opponents, no claim is made.

### Inference (prefill)

| Configuration | Cost per token × TF-LGN | Evidence |
|---|---|---|
| Claim view (more expensive features) | 1.15 | I317 |
| Cheaper-inference variant, vectorized lookup | 0.48 (0.41× TF-LG, 0.81× B1A) | I328 |
| Overlapping chunks | 0.49 | I333 |

Measured in interleaved sessions (8 rounds, calibrated each round). Token-by-token decode is not measured. Count tables at 1,500 updates need about 434 MB, about 76× the network weights; pruning singletons saves only 36% of memory at +0.024 bits (I296).

