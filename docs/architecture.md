# Architecture

This document describes candidates and baselines at the level needed to evaluate the research claims. Exact parameterizations, internal block design, kernels and implementation details are not published ([publication-policy.md](publication-policy.md)).

All arms in a comparison share the same model width, depth (3 layers), block design (gating, normalization, channel mixing), tokenizer, data stream and training budget. They differ in the token-mixing primitive per layer, and each arm's learning rate is screened separately.

## Candidates

| ID | Layer 0 | Layer 1 | Layer 2 | Status |
|---|---|---|---|---|
| A010 | delta-rule recurrent mixer | delta-rule recurrent mixer | full causal softmax attention (RoPE) | strongest reproduced candidate; contested against B1A |
| A019 | delta-rule recurrent mixer | delta-rule recurrent mixer | static n-gram heads, no softmax | contested; advantage comes from a generic module |
| A015 | as A010, plus an Engram-style memory | | | discovery only; comparison not continued |
| A025 | thin delta-rule mixer added to B1A | thin delta-rule mixer added to B1A | global attention (as B1A) | closed: breaks even with B1A (R81, R82) |
| A025n | as A025, with recurrent transitions allowed negative eigenvalues (same cost per update) | | | state-tracking experiments (R83–R88) |
| A026 | as A010, with transitions allowed negative eigenvalues | | | not run; A025n used instead |

### A010: why this shape

A010 came from mechanistic diagnosis, not search:

1. In Transformers trained at this scale, the early layers attend almost uniformly: they compute a broad context average. A recurrent state does this more cheaply and handles novel tokens and long recurrences better.
2. Content-based retrieval (copying rare repeated tokens, key-value recall) needs induction heads, which form in a softmax layer and form early under the Muon optimizer.

So A010 gives each function the cheapest primitive found sufficient: recurrence for summarization in layers 0–1, one softmax layer for retrieval at the end. Probes show the two effects are nearly additive and that no token class favored the gated Transformer it was compared with (I190). Later probes found the division of labor holds: the softmax layer forms cleaner induction heads, and A010's recall does not depend on the recurrent context.

The delta-rule layers use a matrix-valued state updated with an error-correcting (delta) write and a learned decay, trained with a chunkwise-parallel form. The chunkwise form is adopted from published work; it is not claimed as novel.

### A025 and A025n: thin hybrids on the cheapest Transformer

A025 adds a narrow delta-rule mixer to each of B1A's two mixer-free layers. It was the cheapest possible member of the hybrid family: about 1.18× B1A's cost per update. It kept roughly 35–40% of A010's update-efficiency advantage, which is just enough to break even (0.985×). A025n changes only the range of the recurrent transition so that it can take negative eigenvalues, a known requirement for state tracking in linear recurrent models. The change costs nothing per update.

### A019: static n-gram heads

A019 replaces A010's softmax layer with several static heads that look up what followed earlier exact matches of the recent context (n-gram heads, a mechanism described in published work). It reached the cheapest ratio seen against a standard Transformer (0.50 at final quality, one seed) but the same heads help a Transformer almost equally (0.84 under D2). Exact n-gram indices copy verbatim spans at any distance (about 3 bits per token of copy gain at every tested gap), which no softmax model at this scale does beyond about 2,000 tokens.

## Baselines

| Name | Description | Role |
|---|---|---|
| TFSR | Transformer with RoPE, standard block | early baseline |
| Gated full-attention Transformer | same gated block as CIR arms, full causal attention in all 3 layers | strongest in quality tested |
| Gated local-global Transformer (TF-LG) | windowed attention (512) in layers 0–1, full attention in layer 2 | previous cheapest baseline (D1) |
| TF-LG + n-gram heads (TF-LGN) | TF-LG with the global layer replaced by the same n-gram heads as A019 | D2 baseline for A019 |
| TF-LG + Engram | TF-LG with an Engram-style hashed n-gram memory | D2 baseline for A015 |
| **B1A** | no token mixer in layers 0–1; one global attention layer (RoPE) in layer 2 | **current cheapest baseline (frontier)** |
| B1A wide | B1A widened to 448 so its cost per update matches A010 | equal-compute attack |

B1A was found by CIR's baseline lane by asking whether the Transformer needed its lower mixing layers at all. At this scale it does not: removing them halves cost per update with no BPB loss. Published work reaches similar conclusions at large scale (PAR Transformer; attention-layer dropping in large models), so B1A is treated as a legitimate baseline rather than a small-scale artifact.

## Prior art

CIR makes no novelty claim for any component above. Closest published work:

| Component | Prior art |
|---|---|
| Delta-rule recurrent mixers, chunkwise training | DeltaNet (Yang et al., 2024, arXiv:2406.06484); Gated DeltaNet |
| Hybrid recurrent layers plus a few attention layers | Several published hybrids, including production models that pair Gated DeltaNet layers with periodic full attention |
| Negative eigenvalues for state tracking | Grazzi et al., ICLR 2025, arXiv:2411.12537; DeltaProduct, arXiv:2502.10297; RWKV-7, arXiv:2503.14456 |
| Expressivity limits of Transformers and SSMs | Merrill, Petty, Sabharwal, ICML 2024, arXiv:2404.08819 |
| n-gram heads | Akyürek et al., ICML 2024, arXiv:2401.12973 |
| Engram memory | DeepSeek-AI, arXiv:2601.07372 |
| n-gram embeddings | Over-Tokenized Transformer, arXiv:2501.16975; N-Grammer, arXiv:2207.06366; LongCat n-gram embeddings, arXiv:2601.21204 |
| Unbounded n-gram indices | Infini-gram, arXiv:2401.17377 |
| Fewer attention layers | PAR Transformer, arXiv:2009.04534; "What Matters in Transformers?", arXiv:2406.15786 |
| Muon optimizer | Jordan, 2024 (blog); Muon on associative memory, arXiv:2509.26030 |
| Formal-language pre-pretraining | Hu et al., ACL 2025, arXiv:2502.19249; neural cellular automata pre-pretraining, arXiv:2603.10055 |

What CIR contributes so far is the measurement discipline (matched-capability cost accounting against deliberately strengthened baselines) and the resulting map of which primitives matter at this scale, not a new architecture.
