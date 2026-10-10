# Research log

Dated public snapshots of CIR, newest first. Entries marked *as published* reproduce text exactly as it first appeared on [dotrixai.com/cir](https://dotrixai.com/cir); later evidence may have changed them. The evidence IDs in brackets point to the internal ledger.

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
