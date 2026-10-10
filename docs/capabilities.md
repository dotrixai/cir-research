# Capabilities

**Better BPB is not general intelligence.** BPB measures compression of text. Two models with equal BPB can differ in recall, copying and state tracking, and a lookup module can lower BPB without adding capability. At about 4M parameters many capabilities cannot be measured at all; where that is the case it is stated as NOT YET ESTABLISHED.

Comparisons are A010 against the strongest relevant Transformer at the same scale, at 1,500 updates, unless stated. Probes are exploratory (frozen predictions, one evaluation set) unless marked otherwise.

| Capability | Current result | Status | Limitation |
|---|---|---|---|
| Language prediction (BPB) | Better than gated full-attention and local-global Transformers (0.034–0.041 lower BPB, two seeds). Against B1A: 1.23–1.27× the cost to the same BPB; tie at equal compute | WORSE against the cheapest Transformer | Small bilingual corpus, BPE 2,048 |
| Short-range copying | Copy gain at distance 256: A010 1.57 bits/token vs 1.45 for the gated full-attention Transformer | BETTER against Transformers without n-gram heads (PROVISIONAL) | 24 samples per distance; Muon-trained models only |
| Long verbatim copying | Gain at gap 2,560: about 0.04 bits/token for A010 and B1A (≈ none). Models with exact n-gram heads keep about 3 bits/token at every gap | WORSE than models with exact n-gram heads; no softmax model at this scale copies beyond about 2,000 tokens | 32 samples per gap |
| Associative recall (key-value, random order) | Parity or slightly better vs the gated full-attention Transformer (two seeds). Cost to recall: 0.36–0.50 vs expensive Transformers, 0.74–1.0 vs the cheapest | MIXED; marginal against the cheapest Transformer (CONTESTED) | Synthetic probe; one seed for B1A |
| Bracket closing (proxy for state tracking) | About 1 bit/token better on closing brackets 17–128 tokens from the opener (two seeds) | BETTER (PROVISIONAL) | Small samples (323 and 86 brackets); compared with the gated full-attention Transformer only |
| Synthetic state tracking (tiny models, 2 seeds) | Parity: negative-eigenvalue recurrence extrapolates 64 → 256 tokens at 0.96–0.98; the current CIR mixer, tiny B1A and tiny full Transformer stay at chance. Modular counting: unsolved. Permutations (S3): one seed of two | SUPPORTED for parity; NOT ESTABLISHED for harder tasks | Mechanism is prior art; Transformers also failed in-distribution at this budget, so not a complexity separation |
| State tracking inside the language model (A025n vs B1A) | Learned parity in 1 of 3 runs (1.0 in-distribution, 0.96 at 2× length, 0.59 at 4×); B1A never, through 1,500 updates | PROVISIONAL, not reliable | About 6% sparse synthetic data; R88 tests a stronger signal |
| Long copying, counted organization | Copy gain 3.1–3.3 bits for 64-token segments at distance 512, above TF-LGN's 2.89, via the counted pointer | SUPPORTED | One probe design |
| Exact single-token recall, counted organization | 0.996–0.999 (N = 8 / 32) with the trained gate; 0.21–0.24 with fixed weights | SUPPORTED, gate required | Lookup of single tokens, not general associative reasoning |
| Synthetic state tracking, harder tasks (tiny models) | Two delta steps per token solve S3 and the A5 word problem with length extrapolation; six-layer Transformers fail. A one-layer Transformer with chain-of-thought reaches the A5 target more cheaply | Capability SUPPORTED; cost advantage FALSIFIED | Synthetic; tiny models |
| State tracking inside the LM, stronger signal | With 15% parity data, A025n learned parity on the seed that failed at 6% (1.0 in-distribution, 0.85 at 2×); B1A did not. S3 inside the LM: not learned by either | SUPPORTED for parity; NOT ESTABLISHED for S3 | Synthetic data mixed into text |
| Long-range memory (use of distant context) | Softmax models gain almost nothing from tokens beyond about 2,000 positions on this data; restricting attention to a window costs A010 as much BPB as B1A | NO ADVANTAGE FOUND | Data rarely needs long context |
| Grammar | All 4M models near chance with earlier instruments | NOT YET ESTABLISHED (instrument unreliable at this scale) | Needs a stronger instrument or larger models |
| Relational binding | Earlier instruments too weak to separate models | NOT YET ESTABLISHED (instrument unreliable) | As above |
| Reasoning / computation | Not tested | NOT YET ESTABLISHED | Not measurable at 4M |
| Coherent generation | Fails for every 4M model, CIR and Transformer alike | NOT YET ESTABLISHED | Scale |
| Robustness | Not tested | NOT YET ESTABLISHED | |
| Generalization across domains | BPB advantage over earlier baselines appears in every domain (English, Indonesian, Indonesian Wikipedia, stories) | SUPPORTED against earlier baselines only | Same four domains used throughout |

Machine-readable: [../results/capability-status.csv](../results/capability-status.csv).

## Methods (high level)

- **Copy gain:** a text segment is repeated after a gap; gain = loss on the first occurrence minus loss on the second.
- **Associative recall:** N random word-token key→value pairs after a natural-text prefix, then keys queried in random order; accuracy among the N candidate values.
- **Bracket closing:** per-token loss on closing brackets grouped by distance to the matching opener.
- **Context use:** per-position loss buckets; inference-time attention windows to see how much each model relies on distant tokens.

Cost to capability uses isotonic curves and the first crossing for all arms (see [cost-to-capability.md](cost-to-capability.md#associative-recall-corrected-estimator)).
