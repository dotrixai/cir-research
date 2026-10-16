# Direction change, October 2026

**Written:** 2026-10-16, from the CIR record as of 13:00 UTC. **Decision:** 2026-10-15, 13:53 UTC, by the owner of DotrixAI.

## In short

- **CIR's primary research lane is paused.** It searched for a system that reaches matched capability with substantially less training compute than a strong, optimized Transformer system. That target was not reached.
- **Why.** Against fair opponents built from published parts, every advantage we found either belonged to those published parts or faded as models, data and training grew. Five first-principles cycles found no original training-compute lever. The routes still open (published hybrid and mixture-of-experts classes at much larger scale) need far more compute than the program has.
- **What continues.** The record. CIR's pre-registered experiments, frozen predictions, measured outcomes and documented mistakes are being turned into research tasks for AI research agents. This repository stays public, and its dated history is kept as it was written.
- **What did not change.** The charter. Whether CIR's long-term objective changes is an open decision of the owner.

## How it unfolded

| Date (2026, UTC) | Event | Evidence |
|---|---|---|
| 10 Oct | Follow-up tests trace the English–Indonesian gap mainly to data repetition and to the evaluation set, not to language. Three corrections to earlier public claims (see [falsified-and-superseded.md](falsified-and-superseded.md#corrections-published-on-2026-10-16)) | I341, I345, I346, I350, I359, I362 |
| 11 Oct | A hashed n-gram input memory joins the best laptop-scale system (A051) | I370, I371 |
| 12 Oct | The owner clarifies the objective (charter v1.1): training compute to matched capability against the strongest optimized Transformer system. Transformers are allowed and novelty is optional. Ratios against plain Transformers become diagnostic | charter v1.1, methodology V2.5 |
| 13 Oct | First attack with partial optimized opponents built from published parts: 0.26–0.54 at ≤ 4M parameters. Every component of A051, and the combination, is found in published work. Five first-principles cycles find no original lever, and the stop rule for laptop-scale search fires | I399–I403 |
| 14 Oct | First GPU runs (one A100; 4.7–18.9M non-embedding parameters; one epoch of 0.38B tokens). The counted organization's edge is about 1.0 on web text like the training data. A strong published recipe needs about 0.58× the time of plain Transformers at matched quality, and none of five candidates beats it by the signal gate | I404, I406 |
| 15 Oct | Cheap published levers, a gated delta hybrid and a mixture of experts on the strong recipe at 20M and 85M parameters. Small FLOP gains, none in wall-clock time, none near 0.75 | I410, I412–I414 |
| 15 Oct, 13:53 | The owner pauses the primary lane | owner decision (CC-006) |
| 15 Oct, 14:59 | The owner chooses the new direction: research tasks, benchmarks and environments for AI research agents, built from the CIR record | owner decision (CC-006) |
| 16 Oct | A first sample set is built (not public). This update | |

## Why the direction changed

### 1. The fair bar is a strong published recipe, not a plain Transformer

Our headline results through 10 October compared the counted organization with plain or moderately tuned Transformers. Under the clarified charter the primary comparator is the strongest optimized Transformer system: a Transformer that may use every transferable published technique, including n-gram memories, caches, optimizers and schedules (FAIR-OPT, see [objective.md](objective.md)).

That bar is much higher. At 20M parameters a published small-model recipe (a dense core plus a hashed n-gram input memory, value embeddings, skip connections, a logit softcap and a warmup-stable-decay schedule; internally FO-L1) needed about **0.58× the time** (MEASURED) and **0.43× the FLOPs** (ESTIMATED) of a family of plain Transformers to reach the same quality, the quality the recipe reaches after half an epoch [I406]. Much of what looks like a large win against a plain Transformer is already inside such recipes.

### 2. Our advantage belonged to published parts

Every component of the best system (a small one-attention Transformer, a hashed n-gram input memory, counted n-gram tables, a document cache, a longest-match pointer and a learned gate) has published prior art, and so does their combination, in the modded-nanogpt lineage including PR #380 [I399]. The ratio moved as opponents received the same published parts:

| Opponent | Training cost of the best system to the opponent's quality | Scale | Label | Evidence |
|---|---|---|---|---|
| Plain dense Transformer (D1, diagnostic) | 0.038 (English), 0.055 (Indonesian Wikipedia) | 0.8–3M parameters, laptop CPU, one epoch | ESTIMATED | I370, I396 |
| The same networks with published n-gram interpolation, with or without a published input memory (partial FAIR-OPT) | 0.26–0.54 | ≤ 4M, laptop CPU | ESTIMATED | I399 |
| Published n-gram interpolation, first GPU scale point (counted organization) | 0.51–0.57 on Wikipedia text; about 1.0 on web text like the training data | 4.7–18.9M, one A100 | ESTIMATED | I404 |

A complete FAIR-OPT, which would include every published part we use, is expected to bring the ratio to about 1. This is a HYPOTHESIS; it was not measured.

### 3. What remained faded with scale and training

- At laptop scale, what remained against partial opponents was carried mostly by in-window copying (the cache and the pointer), not by memorized text [I401].
- At 20M on the GPU, copying carried all of it, and the edge disappeared on web text [I404].
- Counted and copy input channels speed up early training on the strong recipe, then fade before about a fifth of an epoch [I406]. The gated delta hybrid showed the same early-then-fading pattern [I412].
- This repeats an older pattern in the program: on the laptop the counted gain shrank as the network grew [I342], and the CIR mixers' advantage shrank with width (2 Oct).

### 4. No original lever

Five first-principles cycles (12–13 Oct) derived candidate training-compute primitives from requirements and then searched prior art. No candidate passed both the prior-art check and a minimum value bound, so the stop rule for laptop-scale search, written down in advance, fired on 13 October [I400–I403]. Our current subjective credence that an original CIR training-compute lever exists in this design space is about 3%.

### 5. FLOP savings are not time savings

The published levers we added to the strong recipe, the gated delta hybrid and the mixture of experts each saved some FLOPs at matched quality, far from the signal gate. None saved wall-clock time with the kernels and dispatch we had [I410, I412–I414]. A claim about training cost has to survive a time measurement on real hardware, not only a FLOP count.

### 6. The remaining routes need far more compute

The literature we verified (118 sources added on 14 Oct) shows a consistent pattern. Most published efficiency claims shrink against strong baselines and at scale. The ones reported to keep or grow their advantage are conditional sparsity (mixtures of experts) and architecture shifts that change scaling exponents, and they are reported at scales far beyond ours [I405]. Testing them fairly needs efficient kernels, several seeds and model sizes well above 85M parameters. That is beyond the program's current resources.

### 7. The record itself is valuable

Most experiments were pre-registered: predictions and pass/fail criteria were frozen before results existed, outcomes were measured by the experiments' own scripts, and mistakes were logged. That record shows how real research judgments turned out. It is the basis of the new direction.

## The new direction

DotrixAI is building research tasks for evaluating and training AI research agents from the CIR record:

- **Forecasting:** predict the measured outcome of a real pre-registered experiment from what was known before it ran.
- **Auditing:** find the methodological flaw, or confirm validity, in real situations from the program.
- **A training-efficiency environment:** an agent changes a small model's training recipe to reach a fixed quality with less compute, under a sealed evaluation, a causality check and honest compute accounting.

A first sample exists. It is not public.

## What is withheld, and why

Exact outcomes of experiments R161–R219 (10–15 October 2026) are withheld for now. They are the answer keys of unpublished forecasting tasks, and publishing them would turn those tasks into lookup questions. This update states the conclusions needed to explain the decision, with evidence IDs, and the few headline values above. The forecasting tasks that these conclusions touch are flagged internally.

This is a deliberate, dated exception to the publication policy ([publication-policy.md](publication-policy.md#withheld-results)). The results may be published in full later.

## What would reopen the primary lane

- An owner decision to restart it, with a compute budget.
- New evidence that a lever's advantage grows with scale within a budget we can test.

Drafted but not run: a fine-grained mixture of experts with padding-free dispatch (S6) and a combined run (S7).
