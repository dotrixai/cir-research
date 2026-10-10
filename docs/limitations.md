# Limitations

What the current results cannot tell you.

## Scope

- **Small models.** Counted organization: networks of 0.57–1.43M parameters. CIR mixers: about 4M effective parameters, at most about 7M. Only 3 layers.
- **Short training.** At most 1,500 updates (about 49M tokens), below compute-optimal budgets; cosine schedule fixed to that horizon. Behavior beyond it is unknown.
- **One context length.** Main results at 4,096 tokens; one measurement at 8,192.
- **One batch size.** Batch 8. Recurrent cost per update is strongly batch-dependent.
- **One machine.** One commodity laptop CPU, two pinned performance cores, PyTorch eager mode. No GPU results. CPU cost estimates may not transfer to GPU or cluster training.
- **Narrow data.** English and Indonesian text, BPE vocabulary of 2,048 (Indonesian fragments into about 3.7 tokens per word). Quality is macro-averaged BPB, half-weighted on a small Indonesian evaluation set.

## Evidence quality

- **Seeds.** Only the main A010 comparisons have two seeds. Results against the current cheapest baseline (B1A) use one seed.
- **Session-to-session variance.** Per-update cost ratios for the same pair vary by about ±3% between timing sessions.
- **Capability instruments.** Grammar, binding, reasoning and generation cannot be measured reliably at this scale. Capability probes are exploratory and use modest sample sizes.
- **Learning rates.** Screened on a two-point grid; one earlier baseline used an inherited learning rate.
- **Cost accounting.** Cost is training time on the canonical instrument. Energy, memory, data and infrastructure costs are not yet separately accounted.

## Interpretation

- **Baselines keep improving.** Several results have already been weakened or reversed by stronger baselines, and further cheaper Transformers may exist.
- **Generic modules.** Results without generic modules (Engram, n-gram heads) do not hold once both sides use them.
- **Shallow-model regime.** Three-layer models are the regime most favorable to lookup modules, which may distort the relative value of recurrence and modules.
- **Prior art.** All components have close published equivalents. No architectural novelty is claimed.
- **Scale.** Nothing here establishes behavior at 100M+ parameters, and projections suggest mixer-substitution savings shrink with width.

## Counted organization specifically

- **Language and repetition.** The English corpus (3.86M tokens) repeats quickly; the English advantage fades with budget. Whether this is repetition or language is open (R161).
- **Deployment.** Decode cost unmeasured; count tables about 434 MB; the gate needs about 4,000 tokens of in-domain text and does not transfer across languages.
- **Metric.** Bits per token on positions whose 12-token context is unseen in training. This removes credit for duplicates but differs from plain BPB.
- **Prior art.** The organization is known; no novelty is claimed.
- **D2.** A Transformer given the same counted tools has not been compared; no D2 claim is made.

## Open questions

1. Is the counted organization's advantage about data repetition or about language? (R161)
2. Does English reach ≤ 0.10× with a larger corpus or a larger network?
3. Does the advantage hold against larger Transformers above 4× budget, and at 30M+ parameters?
4. What are decode cost and memory-constrained cost?
5. Is there any CIR-specific primitive that reduces dense computation for language quality (D2)? None is known.
6. Can state tracking be made to matter for language at any affordable scale?
