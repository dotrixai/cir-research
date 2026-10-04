# Falsified and superseded

Results CIR no longer believes, and why. Each one reduced uncertainty: it closed a branch of the search or fixed a measurement. Implementation details of failed candidates are summarized, not disclosed.

## Claims withdrawn or superseded

| Former claim | What changed | Status | Evidence |
|---|---|---|---|
| Pure delta-rule recurrence reaches matched quality at 0.587–0.594× the cost of a Transformer (4,096 context, batch 8, two seeds) | Held only when both models used AdamW. With Muon on both sides, the Transformer overtook recurrence after about 500 updates and finished 0.051 BPB better. Credence that pure delta is competitive with a Muon Transformer: about 5% | SUPERSEDED | I158, I177 |
| "No model copies in context" (early copy probe) | An artifact of AdamW-trained models before induction heads formed. Muon-trained attention models copy 1.4–1.6 bits/token at distance 256 | SUPERSEDED | I192 |
| A010 at 0.570× against the earlier RoPE Transformer (one seed) | Baseline strengthened twice (gated blocks, local-global attention); see [baseline-adversary.md](baseline-adversary.md) | SUPERSEDED by two-seed results against stronger baselines | I188, I203, I211 |
| "Full attention is the strongest Transformer baseline" | A gated local-global Transformer reached nearly equal quality 9% cheaper per update; later B1A at half the cost | REVOKED | I209, I242 |
| A019 at 0.530 at intermediate quality | Measured at 750 updates against a baseline without the same module. Final-quality and D2 comparisons give 0.50 (D1) and 0.84 (D2) | SUPERSEDED | I222, I240 |
| A010 BPB cost advantage at intermediate quality against the cheapest Transformer of the time | A Transformer with n-gram heads beat A010 from 500 updates at about 0.8× the per-update cost of the local-global Transformer | FALSIFIED | I228 |
| Associative-recall cost 0.36–0.69× against all tested Transformers (two seeds) | Estimator bias: the comparator was charged its full 1,500 updates although its recall had plateaued. Corrected: 0.74–1.0× against the cheapest Transformers | SUPERSEDED | I241, I245 |
| A010 keeps a BPB cost advantage over every Transformer tested | B1A (one attention layer) matches the previous baseline at 0.50× per-update cost; A010 is 1.23–1.27× against it | FALSIFIED against the frontier baseline | I242, I248 |

## Directions ruled out

| Direction | Result | Evidence |
|---|---|---|
| Longer context as the route to the 0.50 gate for A010 | A010's per-update ratio against the local-global Transformer worsened from 0.887 to 0.942 going from 4,096 to 8,192 tokens | I209 |
| Recurrence plus a small local attention window (A008) | All four criteria failed; the local branch was sharp but not content-selective, and it cost more per update than the Transformer | I176, I179 |
| A cheaper final layer using a local window plus a cache of high-surprisal positions (A014) | Surprisal-based selection was no better than random | I185 |
| Per-head hybrid final layer: some softmax heads, some recurrent (A016) | Retrieval function was spread across 4 of 5 attention heads; the split could not keep it | I202 |
| Static lookup replacing in-context recall | Lookup cannot perform key-value recall on unseen pairs; a softmax layer remains necessary for it | I200 |
| Recurrent state replacing distant attention | Restricting attention to a window costs A010 as much BPB as B1A, and A010's state carries about 0% of verbatim copies past the window | I247, I250 |
| Long-context recurrence route at this scale (hypothesis H031) | Softmax models at 4M copy almost nothing beyond about 2,000 tokens even with full attention; only exact n-gram indices are distance-independent, and those are a generic module. Credence about 5% | I246, I250 |
| An organization with no learned mixer at all (n-gram heads only) | Considered and rejected before running: an artifact of the shallow, lookup-favoring regime that literature shows does not hold at scale | I250, literature |
| An implementation optimization for A010's recurrent kernel | Numerically equivalent but not faster for A010 (memory-bound); the same idea did help a thinner mixer, now under test | I181, I249 |
| A selective-backward learning-rule idea (A023) | Cheap tier-1 test gave weak support; deferred | I226 |

## Measurement and method errors found

| Error | Consequence | Fix | Evidence |
|---|---|---|---|
| Timing sessions with uncontrolled core placement | Per-update ratios varied more than the effects measured | QUARANTINED; canonical instrument with pinned cores and calibration | I183, I186 |
| Historical wall-clock training times | Not comparable across runs | QUARANTINED | I84 |
| Cost sessions under background load | Several sessions failed validity checks | Kept as INVALID records; automatic wait-for-quiet and re-measurement | R55, R60, R72 |
| Ranking architectures at 250 updates | Rank correlation 0.09 with final results | Discovery runs moved to 750 updates (rank correlation 0.94) | I197 |
| Learning rate of a baseline inherited from another family | Claims against it may favor CIR | Claims CONTESTED; per-family screening mandatory | red-team, 3 Oct |
| Endpoint-cost estimator for capability | Biased toward CIR | Isotonic curves, first crossing for all arms, fixed Q grid | I245 |
| A ratio criterion with a noisy denominator | A prediction "passed" on noise | Ratio criteria must require a significant denominator | I250 |
| An unverified FLOP claim in the ledger (windowed attention savings) | Understated a baseline threat (17% vs up to 30%) | Corrected with an explicit block count; arithmetic claims are now computed before being recorded | I247 |
| Screening a candidate at intermediate quality | Fast early gains from static modules looked like a cost breakthrough | Promotion requires multi-Q curves including final Q and a matched-module baseline | I222, I240 |

## Hypotheses falsified or weakened

| Hypothesis | Outcome |
|---|---|
| The recurrent advantage under AdamW is structural | Falsified: it reflected slow induction-head formation |
| Engram complements recurrence more than attention | Weakened to about 10%: it helps the Transformer more |
| Static n-gram heads give only an early advantage that decays to zero | Partly wrong: against a plain Transformer the advantage persisted (0.034 BPB at 1,500); against A010 and a Transformer with the same heads it decayed to about zero |
| The hybrid's distinctive advantage is in-context recall | Weakened to marginal (about 35%) after estimator correction and the B1A attack |
| Width shrinkage of the advantage occurs only on repeated data | Weakened to about 25%: it also appears on fresh data |
| A recurrent organization without global attention matches a one-attention Transformer at 16–32K context for ≤ 0.5× cost | Weakened from about 25% to about 5% |
