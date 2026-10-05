# Research timeline

Major turning points only. All dates 2026 (UTC). Earlier work (before 24 September) explored recurrent and memory architectures at shorter contexts and is summarized in the first row.

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
