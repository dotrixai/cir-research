# Limitations

What the current results cannot tell you.

## Scope

- **Small models.** About 4M effective parameters for the main results; at most about 7M. Only 3 layers.
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

## Open questions

1. Does any structural cost asymmetry between recurrence and attention exist outside this regime (longer context, larger models)? At ≤ 4,096 tokens and about 4M parameters, the answer for mixer substitution is no (R81, R82, analytic bound).
2. Can the state-tracking asymmetry be made to emerge reliably inside a language model, and is it worth anything for language? (R88)
3. Does formal-language pre-pretraining save tokens, and does the saving depend on organization? (R89, H033)
4. Is there a regime, such as very long context with real long-range needs, where O(1)-per-token state beats O(T) attention on total cost?
5. How do the cost ratios change on GPUs and at 100M+ parameters? This is beyond the current CPU budget.
6. How should the denominator be defined when generic modules make the "strong Transformer" a moving target? Currently both D1 and D2 are reported.
