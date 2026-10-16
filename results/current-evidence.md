# Current evidence

Snapshot: 2026-10-16 13:00 UTC (previous: 2026-10-10 07:47 UTC). The primary lane has been paused since 2026-10-15 ([../docs/direction-change.md](../docs/direction-change.md)). Status vocabulary: [docs/methodology.md](../docs/methodology.md#12-epistemic-status). Machine-readable: [evidence-table.csv](evidence-table.csv).

Exact outcomes of R161–R219 (10–15 Oct) are withheld for now; rows for that period give conclusions and the few public headline values ([publication policy](../docs/publication-policy.md#withheld-results)). Since 12 October (charter v1.1) the primary denominator is the strongest optimized Transformer system (FAIR-OPT); ratios against plain or moderately tuned Transformers are DIAGNOSTIC.

## GPU phase (14–15 Oct): one A100, 4.7–85M parameters, one epoch of 0.38B tokens, one seed

| ID | Finding | Value | Label | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|
| I404 | Counted organization vs published n-gram interpolation (FO-2-lite), 4.7–18.9M | 0.51–0.57 Wikipedia text; about 1.0 web text like the training data | ESTIMATED | PROVISIONAL | Edge disappears on in-distribution text; in-window copying carries the rest | One seed; one epoch |
| I406 | Strong published recipe FO-L1 vs plain dense family, 20M | 0.58× time / 0.43× FLOPs at the recipe's half-epoch quality | MEASURED / ESTIMATED | PROVISIONAL | Published recipes move the bar | One seed |
| I406 | Five candidates vs FO-L1, 20M | none ≤ 0.75 | ESTIMATED | SUPPORTED | Count and copy channels help early, then fade | Outcomes withheld |
| I410 | Cheap published levers on FO-L1, 20M | small FLOP gains, no time gain | ESTIMATED | SUPPORTED | Not a route to the signal gate | Outcomes withheld |
| I412–I414 | Gated delta hybrid (20M, 85M), mixture of experts (85M) on the recipe | small FLOP gains, slower per update, far from 0.75 | ESTIMATED | SUPPORTED | No sign of an advantage growing with scale within 20–85M | One seed; outcomes withheld |

## Laptop phase after 10 Oct 07:47 UTC

| ID | Finding | Value | Label | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|
| I345, I346, I362 | Cause of the English–Indonesian gap (R161, R164, R172) | withheld | — | SUPPORTED | Data repetition and evaluation sets, not language | One seed |
| I341 | Provenance of the Indonesian evaluation sets | UD-GSD is out of distribution; Indonesian Wikipedia dev is held-out in-distribution text | — | CORRECTION | The 9 Oct "unseen text" result was not a domain shift | |
| I350 | Tokenizer composition | about 1.6% Indonesian training text; 2.04 vs 2.82 bytes per token | MEASURED | CAVEAT | Per-token ratios across languages are tokenizer-specific | |
| I359 | Table construction cost | about 0.65% of A039's training time | MEASURED | CORRECTION | Headline 0.0625 → about 0.063 | |
| I370, I371 | Hashed n-gram input memory (A051) | withheld | — | SUPPORTED | Joins the best laptop-scale system; prior art | |
| I370, I396 | A051 vs plain dense Transformer | 0.038 (English) / 0.055 (Indonesian Wikipedia) | ESTIMATED | DIAGNOSTIC | Not a primary claim | Plain opponent |
| I399 | A051 vs partial optimized opponents (FO-2-lite, FO-2+3-lite), ≤ 4M | 0.26–0.54 | ESTIMATED | PROVISIONAL | Survives partial opponents; every part published; complete FAIR-OPT expected near 1 (hypothesis) | One seed |
| I401 | What carries the remaining edge | mostly in-window copying | — | SUPPORTED | Not memorized text | Outcomes withheld |
| I400–I403 | Original training-compute lever at laptop scale | none found | — | NOT FOUND | Stop rule fired 13 Oct | Laptop scale |
| I355, I356, I376, I377, I379, I384, I387, I394 | Decoding, table size, quantization, speculative decoding | withheld | — | MEASURED | Secondary objective | Outcomes withheld |

## Counted organization through 10 Oct 07:47 UTC (generic, now DIAGNOSTIC)

Rows as published on 10 October, with statuses updated on 16 October.

| ID | Finding | Value | Label | Seeds | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|---|
| I316, I318 | A039 vs TF-LGN, average EN+ID | training cost to `Q_N` 0.0625 / 0.0634 (about 0.063 with measured table cost, I359) | ESTIMATED | 2 | REPRODUCED, DIAGNOSTIC | Cheapest organization measured; headline revoked under charter v1.1 | Generic, prior art (modded-nanogpt PR #380) |
| I338, I339 | Per language | Indonesian 0.032; English 0.149 at best; A039 does not reach English `Q_N` | ESTIMATED | 1 | SUPERSEDED (interpretation) | The gap came mainly from repetition and evaluation sets, not language (I345, I346, I362) | Repetition differs by language |
| I340 | English vs B1A across budgets | 0.053 / 0.121 / not reached / not reached (0.5×–4×) | ESTIMATED | 1 | SUPPORTED | English gain fades as data repeats; repetition confirmed as the main cause | Cause tested in R161, R164, R172 |
| I326, I332 | Average vs B1A across budgets | 0.048 / 0.063 / 0.067 / 0.066 | ESTIMATED | 1 | SUPPORTED | Flat across an eightfold budget range | Fixed-size opponent |
| I334 | Ladder fit | equivalent-compute multiplier 14.8–17.9× | ESTIMATED | 1 | PROVISIONAL | Large within the tested range | Partly the opponent's capacity limit |
| I321, I323, I328 | Cheaper-inference variant | training 0.065 / 0.066; prefill 0.48× TF-LGN | ESTIMATED / MEASURED | 2 | REPRODUCED, DIAGNOSTIC | Cheaper to read text too | Decode measured later, outcome withheld; tables about 434 MB |
| I324, I325 | Unseen Indonesian Wikipedia | 0.053 / 0.055 | ESTIMATED | 2 | REPRODUCED, RELABELLED | Held-out text from the training distribution, not a domain shift (I341) | Gate tuned in-domain |
| I299, I309 | Copy and recall | copy 3.1–3.3 bits (TF-LGN 2.89); recall 0.99 with gate | MEASURED | 1–2 | SUPPORTED | Counted pointer copies and looks up well | Single-token lookup |
| I291, I293, I312, I335 | Frontier attacks | four opponent routes all cost more | ESTIMATED | 1 | SUPERSEDED | Opponents with the same published parts give 0.26–0.54 (I399) | Unattacked above 4× budget |

## CIR-specific organizations and earlier results

| ID | Finding | Value | Label | Seeds | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|---|
| I203 | A010 vs gated full-attention Transformer | 0.034 lower BPB; cost to final Q 0.587–0.625 | MEASURED / ESTIMATED | 2 | REPRODUCED | Holds against the strongest Transformer in quality tested | Expensive baseline |
| I211 | A010 vs gated local-global Transformer | 0.041 lower BPB; cost to final Q 0.633–0.643; at early Q 0.78–0.82 | MEASURED / ESTIMATED | 2 | REPRODUCED, CONTESTED | Real advantage over that baseline | Not the cheapest baseline; inherited learning rate |
| I242 | B1A (one attention layer) vs gated local-global Transformer | BPB within 0.005 at 0.502× cost per update | MEASURED | 1 | SUPPORTED | Earlier D1 ratios used an inefficient baseline | One seed |
| I242, I248 | A010 vs B1A, BPB | cost to final Q 1.23–1.27 (ρ_u 0.70, ρ_c 1.75–1.80), constant from width 320 to 448 | ESTIMATED | 1 | PROVISIONAL | No BPB advantage against the cheapest Transformer | One seed |
| I244 | A010 vs B1A at equal compute | BPB difference 0.0023 | MEASURED | 1 | PROVISIONAL | Tie | Within seed noise |
| I245 | Recall cost vs cheapest Transformers | 0.74–1.0 | ESTIMATED | 1–2 | CONTESTED | Marginal | Depends on Q and seed |
| I240 | A019 vs D1 / D2 at final Q | 0.50 / 0.84 | ESTIMATED | 1 | CONTESTED | Gain is the generic n-gram module | Prior art; one seed |
| I240 | A010 vs D2 at final Q | 1.06 | ESTIMATED | 1 | PROVISIONAL | No recurrent-specific BPB advantage under D2 | One seed |
| I224 | Engram gain, Transformer vs A010 | 0.118 vs 0.093 BPB at 750 updates | MEASURED | 1 | SUPPORTED | Generic module helps the Transformer more | 750 updates only |
| I221 | A010 vs local-global at width 448 | cost to final Q 0.719 | ESTIMATED | 1 | PROVISIONAL | Signal gate passed; advantage shrinking with width | Tokens per parameter fell |
| I248 | A010 vs B1A across widths | ρ_u 0.70 (width 320), 0.71 (width 448) | ESTIMATED | 1 | PROVISIONAL | No trend toward an advantage with width | Fixed tokens |
| I251 | A025 (B1A + thin delta mixers) vs B1A | cost to final Q 0.985; recall never reaches B1A's plateau | ESTIMATED | 1 | FALSIFIED (frozen criteria ≤ 0.90, ≤ 0.75) | The hybrid family breaks even with the cheapest Transformer | One seed; this regime |
| I252 | Optimized A025; windowed B1A | A025 0.949; window 512 saves 8.6% per update | ESTIMATED / MEASURED | 1 | SUPPORTED | Family closed; B1A stays the frontier | One session |
| I253 | Synthetic parity, tiny models | negative-eigenvalue recurrence 0.96–0.98 at 4× length; Transformers at chance | MEASURED | 2 | SUPPORTED | Narrow expressivity asymmetry | Prior art; not a complexity separation |
| I254–I257 | Parity inside the language model | A025n learns it in 1 of 3 runs (1.0 in-distribution, 0.96 at 2×); B1A never | MEASURED | 2 | PROVISIONAL, not reliable | Mechanism available, emergence unreliable at 6% signal | Sparse synthetic data; benchmark choice |
| I255, I256 | A025n vs B1A on mixed text and parity data | cost to final Q 0.939; BPB 0.017–0.026 lower at 750 updates, two seeds | ESTIMATED / MEASURED | 2 | PROVISIONAL | Advantage appears regardless of parity learning | Below the frozen 0.90 criterion |
| I246, I250 | Context use at this scale | no softmax model copies verbatim beyond about 2,000 tokens; exact n-gram heads copy at any gap | MEASURED | 1 | SUPPORTED | Long-context route weak at this scale | This data only |
| I209 | A010 per-update ratio, 4,096 → 8,192 context | 0.887 → 0.942 | MEASURED | 1 | SUPPORTED | Longer context does not help A010 | One session |

## Superseded or quarantined

| ID | Former claim | Why | Status |
|---|---|---|---|
| I158 | Pure delta at 0.587–0.594 | AdamW only; reversed under Muon (I177) | SUPERSEDED |
| I188 | A010 at 0.570 | Baseline strengthened | SUPERSEDED |
| I222 | A019 at 0.530 at intermediate Q | Final-Q and D2 comparisons (I240) | SUPERSEDED |
| I241 | Recall cost 0.36–0.69 against all tested Transformers | Biased estimator (I245) | SUPERSEDED |
| I247 | Windowed B1A 10–30% cheaper per update (estimate) | Measured 8.6% (I252) | SUPERSEDED |
| I283, I284 | Counted organization 0.163 / 0.179 | Bridged TF-LGN cost, corrected to 0.172 / 0.189 (I313) | SUPERSEDED |
| I330 | Chunked inference without overlap | Phase weak spot; fixed by overlap (I331) | SUPERSEDED |
| I337 | Macro-only claims | Hid the English gap (I338) | REVOKED |
| I183, I186 | Early per-update ratios | Uncontrolled core placement | QUARANTINED |
| I324, I325 | "Unseen Indonesian Wikipedia" as text outside training | In-distribution held-out text (I341) | RELABELLED |
| I316 (headline) | Breakthrough gate passed on average | Diagnostic under charter v1.1; 0.26–0.54 against partial optimized opponents (I399); about 1.0 at 20M on web text (I404) | REVOKED as headline |
| architecture doc | Table counting costs 0.1–0.2% of training | Measured 0.65% (I359) | SUPERSEDED |

## Under evaluation

Nothing. The primary lane has been paused since 2026-10-15 13:53 UTC. R161 (the repetition test listed here on 10 Oct) finished the same day; its conclusion is above and its exact outcome is withheld.

Closed since the 2026-10-10 snapshot: R161–R219 (laptop: repetition, input memory, inference side, partial FAIR-OPT, mechanism probes; GPU from 14 Oct: scale point, vocabulary calibration, candidate screens, published levers, a small Indonesian-heavy model, hybrid, mixture of experts). Closed before it: R88–R160.

## Figures

- [../figures/counted-path.svg](../figures/counted-path.svg): counted organization, training cost to `Q_N` step by step.
- [../figures/cost-to-q.svg](../figures/cost-to-q.svg): CIR mixers, cost to matched Q, D1 and D2, one session.
- [../figures/baseline-history.svg](../figures/baseline-history.svg): CIR cost ratio as the baseline was strengthened, ending with A025 against B1A.
