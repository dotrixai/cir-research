# Research log

Dated public snapshots of CIR, newest first. Entries marked *as published* reproduce text exactly as it first appeared on [dotrixai.com/cir](https://dotrixai.com/cir); later evidence may have changed them. The evidence IDs in brackets point to the internal ledger.

Entries from 10 October (after 07:47 UTC) to 16 October were written on 16 October from the dated internal record. Exact outcomes of experiments R161–R219 are withheld for now ([publication-policy.md](publication-policy.md#withheld-results)).

## 2026-10-16, 13:00 UTC

- **The primary research lane is paused.** The owner paused it on 15 October at 13:53 UTC. The target, a training-compute advantage over a strong optimized Transformer system at matched capability, was not reached. Reasons and evidence: [direction-change.md](direction-change.md).
- **New direction.** The CIR record (pre-registered experiments, frozen predictions, measured outcomes, documented mistakes) is being turned into research tasks for AI research agents: forecasting, auditing and a training-efficiency environment. A first sample exists and is not public.
- **Some results are withheld.** Exact outcomes of R161–R219 are answer keys of those forecasting tasks. This snapshot publishes conclusions, evidence IDs and a few headline values.
- **The charter is unchanged** (v1.1). The program's long-term objective is an open owner decision.

## 2026-10-15, daily summary

- **The strong recipe at 85M.** The same recipe at 85M parameters (width 768, 12 layers) became the 85M reference. [I413]
- **Published architecture shifts gave small FLOP gains and no time gains.** Cheap published levers (Canon layers, gated attention, sequence-length warmup), a gated delta hybrid (20M and 85M) and a mixture of experts (85M) all stayed far from 0.75. The hybrid's early advantage faded during training. [I410, I412–I414]
- **A small Indonesian-heavy model** was trained with the strong recipe as a test for CPU deployment (secondary objective). [I411]
- **13:53 UTC: the owner paused the primary lane.** The last GPU run (R219) finished six minutes later and was closed as bookkeeping. **14:59 UTC:** the owner chose the new direction.

## 2026-10-14, daily summary

- **First GPU scale point.** Dense Transformers of 4.7–18.9M non-embedding parameters, one epoch of 0.38B tokens of English and Indonesian web text, one A100. Against published n-gram interpolation the counted organization reached 0.51–0.57 on Wikipedia text and about 1.0 on web text like the training data; in-window copying carried all of the remaining edge. Scaling the organization further was not recommended. [I404]
- **A published recipe raised the bar.** A strong small-model recipe (FO-L1) needs about 0.58× the time and 0.43× the FLOPs of plain Transformers at matched quality. Five candidates (a mixture of experts, depth-attention residuals, counted predictive embeddings, width growth, an exact-copy feature) were screened against it; none reached 0.75. Count and copy channels helped early, then faded. [I406]
- **Knowledge base.** 118 external sources were verified and added. The main lesson: published efficiency claims shrink against strong baselines and at scale, except conditional sparsity and shifts in scaling exponents, reported at far larger scales. [I405]

## 2026-10-13, daily summary

- **First attack with partial optimized opponents.** The same networks with published n-gram interpolation, with or without a published input memory: A051's ratio rose from about 0.04–0.06 against plain Transformers to 0.26–0.54 at ≤ 4M. [I399]
- **Every component is published.** A prior-art check found every part of A051, and the combination, in the modded-nanogpt lineage (including PR #380). A complete optimized opponent is expected near 1 (hypothesis). [I399]
- **What carries the edge.** Mostly in-window copying by the cache and the pointer, not memorized text. [I401]
- **Stop rule.** Five first-principles cycles (12–13 Oct) found no original training-compute lever; the pre-registered stop rule for laptop-scale search fired. [I400–I403]

## 2026-10-12, daily summary

- **Charter v1.1.** The owner clarified CIR's objective: training compute to reach matched capability against the strongest optimized Transformer system (FAIR-OPT). Transformers are allowed and novelty is optional; inference and CPU cost are reported separately. Results against plain Transformers are diagnostic from now on. See [objective.md](objective.md).
- **Methodology V2.4 and V2.5.** Every session binds to the charter and the method; every claim names FAIR-OPT as the primary denominator; experiment cards with frozen predictions, post-run audits and architecture-sync checks are enforced by tools.
- **Laptop work on the input memory** (size, data, word classes, quantization, a stronger opponent with the same memory) continued. Outcomes withheld. [I388–I398]

## 2026-10-11, daily summary

- **A hashed n-gram input memory joined the organization** (A051). Prior art: Over-Encoding and the modded-nanogpt lineage. [I370, I371]
- **Inference side measured (10–11 Oct):** token-by-token decoding in PyTorch and in a compiled C runtime, table size, quantization and speculative decoding with counted drafts. Outcomes withheld. [I355, I356, I376, I377, I379, I387]

## 2026-10-10, after the 07:47 UTC snapshot

- **The language gap is mainly repetition and evaluation, not language.** R161 cut the Indonesian corpus to the English size; R164 scored the same runs on held-out Indonesian Wikipedia; R172 trained English on a large corpus. Together they trace the gap to data repetition and to the evaluation set's relation to training. [I345, I346, I362]
- **Correction: "unseen Indonesian Wikipedia" is not a domain shift.** It is held-out text from the training distribution. The Indonesian set used for per-language claims (UD Indonesian-GSD, news and blogs) is the one outside it. [I341]
- **Correction: the tokenizer saw little Indonesian** (about 1.6% of its training text), so Indonesian words split into short, predictable pieces. Per-token ratios across languages are tokenizer-specific. [I350]
- **Correction: building the count tables costs about 0.65% of training time** (measured), not 0.1–0.2% as stated earlier. Ratios rise by less than 1%. [I359]

## 2026-10-10, 07:47 UTC

- **The advantage differs sharply by language.** The 0.06× average is carried mostly by Indonesian (0.032×). In English the best configuration reaches 0.149×, and the cheapest configuration (A039) does not reach TF-LGN quality at all. [I337–I339]
- **In English the gain fades as data repeats.** Against B1A at equal budget, English goes 0.053× (0.5×) → 0.121× (1×) → not reached (2×, 4×). The English corpus is seen up to 12.7 times; an epoch-regime test (R160) failed its frozen prediction. [I340]
- **A causal test is running.** R161 cuts the Indonesian corpus to the English size.
- **Every claim is now reported per language.** Methodology V2.3 also requires full-system accounting (tables, gate fitting, prefill, decode, memory) and per-domain incumbents.

## 2026-10-09, daily summary

- **Inference cost measured.** A cheaper-inference variant trains at 0.065–0.066× and prefills at 0.48× TF-LGN, two seeds; decode not measured. [I321–I328]
- **The ratio holds across four budgets.** Against B1A on the same budget: 0.048 / 0.063 / 0.067 / 0.066 at 0.5× / 1× / 2× / 4× (average). A loss-curve fit gives an equivalent-compute multiplier of about 15×, partly reflecting the fixed-size opponent's limit. [I326, I332, I334]
- **It survives unseen text.** Indonesian Wikipedia, absent from training: 0.053 / 0.055× TF-LGN, two seeds. [I324, I325]
- **A weak spot found through an outside tip.** Chunk starts scored 0.13 bits worse; overlapping chunks by 128 tokens removed it (training 0.062×, inference 0.49×). [I330, I331, I333]

## 2026-10-08, daily summary

- **A trained gate reaches the 0.10 gate.** 0.0995 / 0.101× TF-LGN, two seeds. [I298, I314]
- **Chunked training and a smaller network.** Width 192: 0.083 / 0.077×; width 128 (0.82M parameters, A039): 0.0625 / 0.0634×, two seeds. [I308, I315, I316, I318]
- **Own accounting corrected.** TF-LGN's cost per token had been bridged through another model and was about 5% low; all ratios became 4–5.5% less favourable. [I313]
- **Not a CIR architecture result.** The organization is a small Transformer plus classic counting; close prior art exists (modded-nanogpt PR #380).

## 2026-10-07, daily summary

- **Counted statistics pass the 0.20 gate.** A small one-attention Transformer with counted n-gram tables and a context cache: 0.172 / 0.189× TF-LGN, two seeds (corrected; first reported as 0.163 / 0.179). [I283, I284, I313]
- **Capability checks narrowed the claim.** At this stage long copying was weaker than TF-LGN and recall was fragile; the claim was limited to predictive quality. [I286]
- **Recurrence gains no edge from counting.** A context cache helped a pure recurrent model six times more than an attention model, but the recurrent model's higher cost per token erased it. [I281]

## 2026-10-06, daily summary

- **Harder state tracking, then a cheaper rival.** Recurrence with two update steps per token solved permutation tasks (S3, and the A5 word problem) that six-layer small Transformers failed; a one-layer Transformer with chain-of-thought reached the target more cheaply. The state-tracking cost claim was withdrawn. [I259, I264, I266–I268]
- **S3 inside the language model was not learned** by either organization. [I261, I262]
- **Counting enters the program.** N-gram statistics counted from exactly the same training tokens improved every architecture: a generic lever, measured under D1. [I269–I272]
- **A stricter quality metric.** Bits are scored only where the 12-token context never appears in training. [I270]

## 2026-10-05, evening

- **A stronger signal makes parity emerge.** With 15% parity examples, A025n learned parity on the seed that failed at 6%; B1A again did not. [I258]
- **Formal-language pre-pretraining hurts at this size.** BPB rose by 0.025 (B1A) and 0.050 (A025) at 750 updates; H033 not supported. [I260]

## 2026-10-05, 15:05 UTC (as published)

- **The cheapest hybrid only breaks even.** A025 adds thin recurrent mixers to B1A. It reached B1A's BPB at 0.985× the cost, 0.949× optimized. Both frozen criteria failed, so this hybrid family is closed here.
- **One real asymmetry: state tracking.** Recurrence that allows negative eigenvalues learned parity and extrapolated it. Small Transformers, including B1A, never learned it. The mechanism is prior art.
- **Inside a language model it is unreliable.** Trained on text with 6% parity examples, A025n learned parity in one of three runs. B1A never did. This is a narrow capability result, not a cost result.
- **Next: a stronger signal and formal languages.** R88 raises the parity share to 15%. R89 tests whether a short formal language warm up saves tokens. It also asks for which organization.

## 2026-10-04, 07:27 UTC (as published)

- **A cheaper Transformer erased the BPB advantage.** A Transformer with a single global attention layer matched our previous baseline. It did so at about half the cost per token. Against it, our strongest candidate has no cost advantage in BPB.
- **A bias in our recall estimator was found and corrected.** The earlier recall cost figure of 0.36 to 0.69 favoured CIR. Corrected, the advantage against the cheapest Transformers is marginal: 0.74 to 1.0.
- **R81 interim: the cheaper hybrid keeps little of the margin.** At 750 updates, A025 keeps about 15% of A010's BPB margin over B1A. The BPB criterion will likely fail. The formal verdict is still pending.
- **The long context route narrowed further.** No softmax model at this scale copies text from beyond about 2,000 tokens. The recurrent state carries almost none either. Only exact n gram lookup copies at any distance.

## 2026-10-04, 06:05 UTC (as published)

- **A cheaper Transformer erased the BPB advantage.** A Transformer with a single global attention layer matched our previous baseline. It did so at about half the cost per token. Against it, our strongest candidate has no cost advantage in BPB.
- **A bias in our recall estimator was found and corrected.** The earlier recall cost figure of 0.36 to 0.69 favoured CIR. Corrected, the advantage against the cheapest Transformers is marginal: 0.74 to 1.0.
- **An analytic bound narrowed the search.** At 4,096 tokens of context, replacing attention alone cannot reach the 0.50 gate. This holds even if the replacement were free. The search is moving to other primitives.
- **R81 is running.** R81 adds thin recurrent mixers to the cheapest Transformer. Success and failure criteria were frozen before the run.
