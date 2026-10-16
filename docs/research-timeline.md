# Research timeline

Major turning points only. All dates 2026 (UTC). Rows from 10 October onward were written on 16 October; exact outcomes of R161–R219 are withheld ([publication-policy.md](publication-policy.md#withheld-results)). Earlier work (before 24 September) explored recurrent and memory architectures at shorter contexts and is summarized in the first row.

| Date | Turning point | Belief change |
|---|---|---|
| Before 24 Sep | Exploration of delta-rule memory architectures, binding and recall instruments, short contexts | Instruments for binding and grammar found too weak at this scale |
| 24 Sep | Formal falsification report: a pure delta-rule memory model does not reach matched quality at much lower cost than a strong Transformer, as originally framed (contexts up to 4,096) | One narrow condition left open |
| 26 Sep | Narrow signal: at 4,096 context and batch 8, pure delta reaches 0.587–0.594 (two seeds, AdamW on both sides) | First signal-gate claim, explicitly narrow |
| 27 Sep | **Optimizer reversal:** with Muon on both sides the Transformer wins by 0.051 BPB | Pure-delta claim withdrawn |
| 27 Sep | **Mechanism:** Muon makes final-layer induction heads form early; early layers of the Transformer attend almost uniformly | The advantage was slow Transformer learning; design A010 = recurrence for summary + one softmax layer for retrieval |
| 27 Sep | A010 at 0.570 against a Muon Transformer (one seed) | Hybrid hypothesis supported |
| 27–28 Sep | Canonical cost instrument; uncontrolled timing sessions quarantined | Cost ratios comparable only within valid sessions |
| 30 Sep | **Two-seed confirmation** against the gated full-attention Transformer: 0.034 lower BPB, cost 0.587–0.625 | First REPRODUCED result |
| 1 Oct | **Stronger baseline:** gated local-global Transformer, 9% cheaper per update; A010 holds at 0.633–0.643 in two seeds, 0.78–0.82 at early quality | Claim narrowed |
| 2 Oct | **First scaling point:** width 448, cost 0.719 (tokens fixed) | Signal gate still passed, advantage shrinking with width |
| 2 Oct | Static n-gram heads (A019): 0.530 at intermediate quality | First candidate near the 0.50 gate; later superseded |
| 3 Oct | **Generic-module threat:** Engram helps the Transformer more; n-gram heads on both sides erase the recurrent-specific edge | Two denominators (D1, D2) adopted; methodology v2.1 and first-principles reset |
| 3 Oct | A019 reaches 0.50 vs D1 at final quality, 0.84 vs D2 | Interesting gate only under D1, from a prior-art module |
| 3 Oct | **Cheapest Transformer found (B1A):** one global attention layer matches the local-global Transformer at half the cost per update | BPB claim lost; B1A becomes mandatory comparator |
| 4 Oct | Equal-compute attack gives a BPB tie; recall-cost estimator found biased and corrected (0.74–1.0) | No robust advantage over the cheapest fair Transformer |
| 4 Oct | Analytic (Amdahl) bound: mixer substitution cannot reach 0.50 at 4,096 context; long-copy probes rule out the long-context recurrence route at this scale | Search redirected to state tracking and new primitives |
| 4 Oct | **Cheapest hybrid breaks even:** A025 reaches 0.985× B1A (0.949× optimized); windowed B1A measured only 8.6% cheaper per update | Delta-hybrid mixer family closed for BPB at context ≤ 4,096; first-principles reset; learning-rule axis also gives no CIR-specific lever |
| 4 Oct | **State tracking (synthetic):** negative-eigenvalue recurrence learns and extrapolates parity; tiny Transformers do not | Narrow capability asymmetry supported; mechanism is prior art |
| 4–5 Oct | **State tracking inside the LM:** learned in 1 of 3 runs; B1A never; mixed-data BPB advantage replicates regardless | Capability claim downgraded to "can emerge, not reliably" |
| 5 Oct | Formal-language pre-pretraining proposed as a token-saving lever that may depend on organization (R89, H033) | New direction under test |
| 5 Oct | **Stronger parity signal (15%)**: A025n learns parity on the seed that failed; B1A does not. Formal-language pre-pretraining hurts at 4M | Parity in the LM supported; H033 not supported |
| 6 Oct | Two delta steps per token solve S3 and A5 in tiny models; a one-layer Transformer with chain-of-thought is cheaper | **State-tracking cost claim falsified**; capability stands |
| 6 Oct | **Counted n-gram prior** on exactly the training tokens helps every architecture; masked metric adopted | Generic lever measured under D1 |
| 7 Oct | Small Transformer + counted prior + cache: 0.172–0.189× TF-LGN (corrected), two seeds | 0.20 gate passed under D1; prior art acknowledged |
| 8 Oct | Trained gate 0.0995–0.101×; chunked training 0.077–0.083×; width 128 (A039) **0.0625–0.0634×**; TF-LGN cost correction (~5%) | 0.10 gate passed on average under D1 |
| 9 Oct | Inference 0.48×; budget ladder flat (0.048–0.067); unseen Indonesian Wikipedia 0.053–0.055×; phase weak spot found via an outside tip and fixed | Claim extended to inference and robustness, still averaged |
| 10 Oct | **Per-language correction:** Indonesian 0.032×, English 0.149× at best; English advantage absent at 2× and 4× budget | Claims reported per language; R161 tests data repetition |
| 10 Oct | **Language gap traced:** repetition tests (R161, R164) and a large English corpus (R172) point to data repetition and the evaluation set, not language. Corrections: eval-set provenance, tokenizer coverage, table cost | Per-language claims reinterpreted; corrections published 16 Oct |
| 11 Oct | Hashed n-gram input memory joins the organization (A051); inference side measured (outcomes withheld) | Best laptop-scale system A051; all parts prior art |
| 12 Oct | **Charter v1.1:** the primary objective is training compute to matched capability against the strongest optimized Transformer system (FAIR-OPT); Transformers allowed, novelty optional. Methodology V2.4–V2.5 | Every ratio against plain Transformers becomes diagnostic |
| 13 Oct | **Partial FAIR-OPT attack:** 0.26–0.54 at ≤ 4M; every component of A051 and their combination found in published work; five first-principles cycles find no original lever (stop rule) | Complete FAIR-OPT expected ≈ 1 (hypothesis); laptop-scale lever search stopped |
| 14 Oct | **First GPU scale point** (A100, 4.7–18.9M): the counted organization ≈ 1.0 on in-distribution web text. A published 20M recipe needs ≈ 0.58× the time of plain Transformers; five candidates screened against it, none ≤ 0.75 | Counted organization not scaled further; candidate search moves to published architecture classes |
| 15 Oct | Published levers, a gated delta hybrid (20M, 85M) and a mixture of experts (85M) on the strong recipe: small FLOP gains, no wall-clock gain, far from 0.75 | No route to the signal gate within the program's resources |
| 15 Oct | **The owner pauses the primary lane** (13:53 UTC) and chooses a new direction: research tasks for AI research agents built from the CIR record (14:59 UTC) | See [direction-change.md](direction-change.md) |
| 16 Oct | Public update; exact outcomes of R161–R219 withheld as answer keys of unpublished tasks | Publication exception, dated |
