# Current evidence

Snapshot: 2026-10-10 07:47 UTC. Regime unless stated: 3 layers, 4,096-token context, batch 8, up to 1,500 updates (about 49M tokens), English and Indonesian text, one laptop CPU. Counted organization: networks of 0.82–1.43M parameters, quality measured as bits per token on positions with unseen 12-token context. CIR mixers: about 4M effective parameters. Status vocabulary: [docs/methodology.md](../docs/methodology.md#12-epistemic-status). Machine-readable: [evidence-table.csv](evidence-table.csv).

## Counted organization (generic, D1)

| ID | Finding | Value | Label | Seeds | Status | Interpretation | Main limitation |
|---|---|---|---|---|---|---|---|
| I316, I318 | A039 vs TF-LGN, average EN+ID | training cost to `Q_N` 0.0625 / 0.0634 | ESTIMATED | 2 | REPRODUCED | Cheapest organization measured; passes 0.10 on average | Generic, prior art (modded-nanogpt PR #380) |
| I338, I339 | Per language | Indonesian 0.032; English 0.149 at best; A039 does not reach English `Q_N` | ESTIMATED | 1 | SUPPORTED | Breakthrough level in Indonesian only | Repetition differs by language |
| I340 | English vs B1A across budgets | 0.053 / 0.121 / not reached / not reached (0.5×–4×) | ESTIMATED | 1 | CONTESTED | English gain fades as data repeats | Cause under test (R161) |
| I326, I332 | Average vs B1A across budgets | 0.048 / 0.063 / 0.067 / 0.066 | ESTIMATED | 1 | SUPPORTED | Flat across an eightfold budget range | Fixed-size opponent |
| I334 | Ladder fit | equivalent-compute multiplier 14.8–17.9× | ESTIMATED | 1 | PROVISIONAL | Large within the tested range | Partly the opponent's capacity limit |
| I321, I323, I328 | Cheaper-inference variant | training 0.065 / 0.066; prefill 0.48× TF-LGN | ESTIMATED / MEASURED | 2 | REPRODUCED | Cheaper to read text too | Decode unmeasured; tables about 434 MB |
| I324, I325 | Unseen Indonesian Wikipedia | 0.053 / 0.055 | ESTIMATED | 2 | REPRODUCED | Survives text outside training | Gate tuned in-domain |
| I299, I309 | Copy and recall | copy 3.1–3.3 bits (TF-LGN 2.89); recall 0.99 with gate | MEASURED | 1–2 | SUPPORTED | Counted pointer copies and looks up well | Single-token lookup |
| I291, I293, I312, I335 | Frontier attacks | four opponent routes all cost more | ESTIMATED | 1 | SUPPORTED (STRONG for `Q_N`) | Claim held at this scale | Unattacked above 4× budget |

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

## Under evaluation

| ID | Question | State |
|---|---|---|
| R161 | With the Indonesian corpus cut to the English size, does the Indonesian advantage collapse? | Training |

Closed since the 2026-10-05 snapshot: R88 (parity emerges with 15% signal), R89 (formal-language pre-pretraining hurts at 4M), R90–R97 (state-tracking capability real, cost falsified), R98–R160 (counted organization, see above).

## Figures

- [../figures/counted-path.svg](../figures/counted-path.svg): counted organization, training cost to `Q_N` step by step.
- [../figures/cost-to-q.svg](../figures/cost-to-q.svg): CIR mixers, cost to matched Q, D1 and D2, one session.
- [../figures/baseline-history.svg](../figures/baseline-history.svg): CIR cost ratio as the baseline was strengthened, ending with A025 against B1A.
