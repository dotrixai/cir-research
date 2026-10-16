# Limitations

What the current results cannot tell you. Updated 2026-10-16; the primary lane has been paused since 15 October ([direction-change.md](direction-change.md)).

## Scope

- **Small models.** Laptop phase: counted organization 0.57–3M parameters, CIR mixers about 4M effective (at most about 7M), 3 layers. GPU phase: dense Transformers of 4.7–18.9M non-embedding parameters, and the strong recipe at 20M and 85M. Nothing larger was run.
- **Short training.** Laptop runs up to 1,500 updates (about 49M tokens), occasionally 3,000–6,000. GPU runs one epoch of 0.38B tokens. Behavior with more data, multiple epochs at scale or longer schedules is unknown.
- **Few hardware types.** One commodity laptop CPU (two pinned cores, PyTorch eager mode, plus a compiled C runtime for decoding) and one rented A100 GPU. Kernels mattered: FLOP savings did not carry over into time with the implementations available.
- **Narrow data.** English and Indonesian. Laptop: WikiText-2 or WikiText-103, Indonesian Wikipedia, short stories, BPE vocabulary 2,048. GPU: FineWeb-Edu and FineWeb-2 web text, BPE vocabulary 32,768.
- **One context regime per phase.** Laptop: 4,096 tokens (training on 1,024-token chunks for the counted organization). GPU: 1,024 tokens.

## Evidence quality

- **Seeds.** GPU results use one seed. Laptop results use one or two.
- **Session-to-session variance.** Per-update cost ratios for the same pair vary by about ±3% between laptop timing sessions; GPU time per update was anchored within each session.
- **Capability instruments.** At ≤ 4M parameters grammar, binding, reasoning and generation cannot be measured reliably. BLiMP was used as a guard on the GPU and varies by about ±3 points between identical runs.
- **Withheld results.** Exact outcomes of R161–R219 are withheld for now, so readers cannot check those conclusions against numbers yet ([publication-policy.md](publication-policy.md#withheld-results)).
- **Partial opponents.** No complete FAIR-OPT was built at any scale. The opponents used are dated partial versions.

## Interpretation

- **Baselines keep improving.** Most CIR results were weakened or reversed by stronger baselines; the strongest published recipes moved the bar further than any candidate moved.
- **Generic modules.** Results that depend on n-gram memories, caches or input memories do not hold once the opponent uses the same published modules.
- **Shallow-model regime.** Three-layer laptop models are the regime most favorable to lookup modules; the GPU point confirmed that their value shrinks with scale.
- **Prior art.** Every component of the best system, and the combination, has close published equivalents. No architectural novelty is claimed.
- **Scale.** Nothing here establishes behavior at 100M+ parameters.

## Counted organization specifically

- **Repetition and evaluation sets.** The earlier English–Indonesian gap came mainly from data repetition and from evaluation sets with different relations to the training text, not from language.
- **Tokenizer.** The laptop tokenizer was trained with about 1.6% Indonesian text; per-token ratios across languages are tokenizer-specific.
- **Metric.** Bits per token on positions whose 12-token context is unseen in training. This removes credit for duplicates but differs from plain BPB, and it is a partial overlap control, not a full contamination proof.
- **Memory.** Count tables need hundreds of megabytes at laptop scale (about 434 MB) and far more for large corpora.
- **The gate** needs a few thousand tokens of in-domain text and does not transfer across languages.

## Open questions

1. Does any training-compute lever keep or grow its advantage against a complete FAIR-OPT as scale grows (for example fine-grained mixtures of experts with efficient dispatch)? Not tested.
2. How do the GPU-phase conclusions hold across seeds and at 100M+ parameters? Not tested.
3. Can capability beyond predictive quality (grammar, binding, reasoning) be matched at lower training compute? Not measurable at the scales run.
4. Is there any CIR-original primitive that reduces training compute? None is known; credence about 3%.
