# Baseline adversary

CIR deliberately strengthens the Transformer it competes against. A dedicated lane tries to make the Transformer win, using any fair, generic improvement. Each upgrade below changed or removed a CIR claim. This history is the main reason to trust the claims that remain, and the main reason so few remain. Rows from 13 October onward are summarized; exact outcomes of R161–R219 are withheld ([publication-policy.md](publication-policy.md#withheld-results)).

| Date (2026) | Baseline upgrade | Effect on the CIR claim | Evidence |
|---|---|---|---|
| 26–27 Sep | **Optimizer: Muon for both arms** (previously AdamW) | Pure delta-rule recurrence had reached 0.587–0.594 against an AdamW Transformer. Under Muon the Transformer overtook it after about 500 updates and finished 0.051 BPB better. **Claim withdrawn.** | I158, I177 |
| 27 Sep | Mechanism probe of the stronger Transformer | Muon makes induction heads form early (enrichment 14× at 625 updates vs 2.3× under AdamW). The earlier recurrent advantage was slow Transformer learning, not a structural edge. Led to the hybrid A010. | I179, I182 |
| 27–30 Sep | **Gated blocks for the Transformer** (same block design as CIR arms) | Strongest Transformer in quality. A010's lead narrowed from 0.065 to 0.034 BPB; cost ratio 0.587–0.625 in two seeds. **Claim narrowed.** | I188, I203 |
| 1 Oct | **Local-global attention** (window 512 in layers 0–1) | Nearly equal quality at 0.907× cost per update. A010 vs this baseline: 0.633–0.643 at final Q, but 0.78–0.82 at early Q. **Claim narrowed.** | I209, I211 |
| 3 Oct | **Learning-rate screening for baselines** (red-team) | The local-global baseline's learning rate had been inherited. Dependent claims marked CONTESTED; screening made mandatory for every comparator. | red-team, 3 Oct |
| 3 Oct | **Engram memory** on both sides | Helps the Transformer more (0.118 vs 0.093 BPB at 750 updates). Transformer + Engram at 750 updates beat the plain Transformer at 1,500. Closes about 63% of A010's margin. **Claim weakened.** | I224 |
| 3 Oct | **Static n-gram heads** on both sides | With the same heads, A019's lead over the Transformer fell to 0.004 BPB at 750 updates; A010 became 1.06× the cost of the Transformer with n-gram heads. **Recurrent-specific advantage ≈ 0 under D2.** | I228, I240 |
| 3 Oct | **One global attention layer (B1A):** remove mixers from layers 0–1 | Matches the local-global Transformer in BPB at 0.502× cost per update. A010 becomes 1.23–1.27× in BPB cost. **BPB claim lost.** | I242, I248 |
| 4 Oct | **Equal-compute attack:** B1A widened to A010's cost per update | BPB tie (0.0023). Recall slightly better for A010. | I244 |
| 4 Oct | **Estimator audit** (recall cost) | Comparator was charged its full budget although its recall had plateaued. Corrected recall advantage vs cheapest Transformers: 0.74–1.0. **Capability claim weakened to marginal.** | I245 |
| 4 Oct | **Windowed B1A** (probe, then canonical timing) | Windowing B1A's attention to 512 costs up to 0.010 BPB and saves only 8.6% per update on this CPU (estimated beforehand at 10–30%). Not cheaper to matched quality, so **B1A stays the frontier**. | I247, I252 |
| 6 Oct | **Transformer with chain-of-thought** on synthetic state tracking | A one-layer Transformer with written intermediate steps reached the A5 target more cheaply than CIR recurrence. **State-tracking cost claim withdrawn.** | I267, I268 |
| 7–8 Oct | **Counted claim vs TF-LGN with n-gram heads, larger Transformers (TF-LG, A010 at width 448), and B1A trained twice as long** | All cost more to reach `Q_N` (0.080–0.111 for the under-trained larger opponents). **Claim held.** | I291, I293 |
| 8 Oct | **Same short-context trick for the Transformer** | TF-LGN trained on 1,024-token chunks lost 0.042 bits and never reached `Q_N`. **Claim held.** | I312 |
| 8 Oct | **Direct cost measurement of TF-LGN** | The bridged estimate was about 5% low; every ratio became 4–5.5% less favourable. **Claim corrected.** | I313 |
| 10 Oct | **Frontier envelope check** | Within the tested compute range, every Transformer configuration measured is worse than B1A width 320. Above 4× budget and for larger B1A: UNATTACKED. | I335 |
| 10 Oct | **Per-language scoring and longer budgets** | English advantage absent at 2× and 4× budget. **Claim narrowed** to Indonesian and the average. | I338, I340 |
| 4 Oct | **Cheapest hybrid against B1A** (R81, R82) | A025, B1A plus thin recurrent mixers, breaks even (0.985×; 0.949× with an optimized implementation). **Delta-hybrid family closed** at context ≤ 4,096. | I251, I252 |
| 13 Oct | **Partial optimized opponents (partial FAIR-OPT):** the same networks plus published n-gram interpolation, with or without a published input memory | The best laptop-scale system (A051) is at 0.26–0.54 at ≤ 4M. A prior-art check finds every A051 component, and the combination, in published work. **Claim narrowed; a complete FAIR-OPT is expected near 1 (hypothesis).** | I399 |
| 14 Oct | **Scale:** 4.7–18.9M on one A100, against published n-gram interpolation | The counted organization is at 0.51–0.57 on Wikipedia text and about 1.0 on web text like the training data; in-window copying carries all of the rest. **Claim lost on in-distribution text at this scale.** | I404 |
| 14 Oct | **A dated strong recipe (FO-L1)** at 20M | Needs about 0.58× the time and 0.43× the FLOPs of plain Transformers at matched quality. Five candidates screened against it; none reached 0.75. **Every candidate lost.** | I406 |
| 15 Oct | **The same recipe at 85M (dense85)** | Reference for a gated delta hybrid and a mixture of experts at 85M; both stayed far from 0.75 (outcomes withheld). **Candidates lost.** | I413, I414 |

![CIR cost ratio to the baseline's final BPB as the baseline was strengthened; the last row is the cheapest hybrid A025 against B1A](../figures/baseline-history.svg)

Values come from different cost sessions and are ESTIMATED; each is comparable only to its own baseline.

## Rules that came out of this

- The cheapest fair Transformer known is a mandatory comparator for every new claim.
- Every comparator family gets its own learning-rate screen.
- Every cost claim must survive a "remove the mixing layers" attack and an equal-compute attack.
- Claims are reported under D1 and D2 side by side.
- Literature is checked before running expensive attacks that ask whether a baseline is a small-scale artifact (B1A's legitimacy was checked against published work on attention-sparse Transformers).
- Since 12 October every claim names the strongest optimized Transformer system (FAIR-OPT) as its primary denominator; D1 and D2 are diagnostic.
- Before a result is promoted, an opponent is built from the published parts it uses (a partial FAIR-OPT).
- Screening decisions use points at or beyond half an epoch, because early advantages of count, copy and recurrent channels faded before a fifth of an epoch.
