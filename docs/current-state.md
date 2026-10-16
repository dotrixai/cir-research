# Current state

**Snapshot:** 2026-10-16 13:00 UTC (previous snapshots: 2026-10-10 07:47 UTC, 2026-10-05 15:00 UTC, 2026-10-04 07:15 UTC; see [research-log.md](research-log.md))

> **This document reflects an evolving research program and may change as new experiments strengthen or falsify current hypotheses.**

## Status

- **The primary research lane is paused** since 2026-10-15 13:53 UTC, by decision of the owner. No experiment is running and none is queued.
- **Why:** the primary target was not reached, and the routes still open need far more compute than the program has. The full reasoning is in [direction-change.md](direction-change.md).
- **New direction:** DotrixAI is turning the CIR record into research tasks for AI research agents. A first sample exists and is not public.
- **The charter is unchanged** (v1.1 of 12 October 2026). Whether CIR's long-term objective changes is an open owner decision.
- **Withheld:** exact outcomes of experiments R161–R219 (10–15 Oct) are withheld for now, because they are answer keys of unpublished forecasting tasks. This snapshot gives conclusions with evidence IDs and a few headline values ([publication-policy.md](publication-policy.md#withheld-results)).

## Summary

- **Primary objective: not reached.** No candidate reached the signal gate (≤ 0.75) in training compute to matched quality against a strong published recipe at 20M or 85M parameters [I406, I410, I412–I414].
- **The best laptop-scale system is generic and published.** A051 (a small one-attention Transformer, a hashed n-gram input memory, counted n-gram tables, a cache, a pointer and a learned gate) reaches a plain dense Transformer's quality at 0.038× (English) and 0.055× (Indonesian Wikipedia) of its training cost (ESTIMATED, diagnostic). Against partial optimized opponents built from the same published parts the ratio is 0.26–0.54 (ESTIMATED) [I370, I396, I399]. Every component, and the combination, has prior art.
- **The counted organization did not survive the first scale-up.** At 4.7–18.9M parameters on one A100 its edge over published n-gram interpolation is 0.51–0.57 on Wikipedia text and about 1.0 on web text like the training data; in-window copying carries all of what remains [I404].
- **Strong recipes move the bar.** A published small-model recipe needs about 0.58× the time (MEASURED) and 0.43× the FLOPs (ESTIMATED) of plain Transformers at matched quality at 20M [I406].
- **Advantages faded with scale and training,** and FLOP savings did not become time savings with the kernels we had [I406, I410, I412–I414].
- **No original lever.** Five first-principles cycles found none; the stop rule for laptop-scale search fired on 13 October [I400–I403].

## Experimental regimes

| Item | Laptop phase (to 13 Oct) | GPU phase (14–15 Oct) |
|---|---|---|
| Hardware | one laptop CPU (Intel Core i5-13420H), two pinned performance cores | one rented NVIDIA A100 (40 GB) |
| Networks | 0.8–3M parameters (counted organization); CIR mixers up to about 7M earlier | dense Transformers of 4.7–18.9M non-embedding parameters; the strong recipe at 20M and 85M |
| Data | English WikiText-2 (3.86M tokens) or WikiText-103 (191M tokens, seen less than once); Indonesian Wikipedia (31.2M); short stories | one epoch of 0.38B tokens of English (FineWeb-Edu) and Indonesian (FineWeb-2) web text |
| Tokenizer | BPE, vocabulary 2,048 | BPE, vocabulary 32,768 |
| Quality | bits per token on positions whose 12-token context does not occur in training | the same masked metric (14 Oct); bits per byte on four core evaluation sets (15 Oct); BLiMP as a grammar guard |
| Seeds | one or two | one |

## Comparators

| Name | Role |
|---|---|
| FAIR-OPT | the strongest optimized Transformer system for matched quality; the primary denominator since 12 Oct. Not fully built at any scale |
| FO-L1 | a dated strong small-model recipe at 20M (dense core, hashed n-gram input memory, value embeddings, skips, softcap, warmup-stable-decay); a partial FAIR-OPT and the comparator of the 14–15 Oct screens |
| dense85 | the same recipe at 85M (width 768, 12 layers) |
| FO-2-lite, FO-2+3-lite | partial optimized opponents at ≤ 4M: the same networks plus published n-gram interpolation, with or without a published input memory |
| TF-LGN, B1A | the laptop comparators through 10 Oct; now diagnostic |

## Results since 10 October

Exact values are withheld unless listed (see Status).

| Question | Conclusion | Value | Label | Evidence |
|---|---|---|---|---|
| Is the English–Indonesian gap about language? (R161, R164, R172) | Mainly data repetition and the evaluation set's relation to the training text, not language. With English text seen less than once, English behaves like Indonesian | withheld | | I345, I346, I362 |
| Does a hashed n-gram input memory help the organization? (R184, R188) | Yes; it joined the best system (A051). Prior art: Over-Encoding and the modded-nanogpt lineage | withheld | | I370, I371 |
| A051 against a plain dense Transformer (diagnostic) | | 0.038 (English) / 0.055 (Indonesian Wikipedia) | ESTIMATED | I370, I396 |
| A051 against partial optimized opponents, ≤ 4M (R211) | Survives at this scale | 0.26–0.54 | ESTIMATED | I399 |
| What carries the remaining edge? (R212) | Mostly in-window copying, not memorized text | withheld | | I401 |
| Is there an original training-compute lever at laptop scale? (DE_NOVO 21–25) | None found; stop rule fired | | | I400–I403 |
| The counted organization at 4.7–18.9M on GPU (R213) | Edge shrinks, and disappears on web text; copying carries all of it | 0.51–0.57 Wikipedia text; about 1.0 web text | ESTIMATED | I404 |
| A published small-model recipe against plain Transformers at 20M (R214) | The bar rises sharply | 0.58× time / 0.43× FLOPs | MEASURED / ESTIMATED | I406 |
| Five candidates against that recipe at 20M (R214) | None reaches 0.75. Count and copy channels help early, then fade | withheld | | I406 |
| Cheap published levers on the recipe at 20M (R215) | Small FLOP gains, no wall-clock gain | withheld | | I410 |
| A gated delta hybrid at 20M and 85M; a mixture of experts at 85M (R217–R219) | Small FLOP gains, far from 0.75; slower per update in our implementations | withheld | | I412–I414 |
| Inference side: decoding, table size, quantization, speculative decoding (10–12 Oct) | Measured | withheld | | I355, I356, I376, I377, I379, I384, I387, I394 |
| Table construction cost (accounting) | Larger than first stated, still under 1% of training | about 0.65% of training time | MEASURED | I359 |

## Gate status

| Gate | Primary: strong optimized Transformer system | Partial optimized opponents | Plain Transformers (diagnostic) |
|---|---|---|---|
| ≤ 0.75 signal | **Not reached** | Passed at ≤ 4M (0.26–0.54); not at 20M on web text | Passed |
| ≤ 0.50 interesting | **Not reached** | Partly at ≤ 4M | Passed |
| ≤ 0.20 industry-level | **Not reached** | Not reached | Passed |
| ≤ 0.10 breakthrough-level | **Not reached** | Not reached | Passed at ≤ 3M (0.038–0.063) |

Passes against plain Transformers are diagnostic only (charter v1.1). They do not count toward the primary objective.

## Active and queued work

None. Drafted but not run: a fine-grained mixture of experts with padding-free dispatch (S6) and a combined run (S7). They run only if the owner restarts the primary lane.

## What would reopen the primary lane

- An owner decision to restart it, with a compute budget.
- New evidence that a lever's advantage grows with scale within a budget the program can test.

## Earlier phases

The CIR-specific recurrent mixers (A010, A025) were closed for general language modeling at this scale on 4 October; see [falsified-and-superseded.md](falsified-and-superseded.md). The counted organization's results through 10 October remain in [research-log.md](research-log.md) and [../results/current-evidence.md](../results/current-evidence.md) with updated statuses.
