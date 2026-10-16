# Objective

## The ratio (charter v1.1, since 12 October 2026)

```
minimize  R_train(Q) = TrainCompute(CIR, Q) / TrainCompute(strongest optimized Transformer system, Q)
```

for a declared capability target `Q` and a declared regime (languages, data, context, hardware, budget). `Q` is matched capability: both systems must actually reach it before their costs are compared. A ratio of 0.5 would mean the same capability for half the training compute. This is the objective, not a result.

On 12 October 2026 the owner clarified the objective (charter v1.1):

- **Training compute is primary.** All computation needed to obtain the trained system counts: pretraining, auxiliary training such as gates or memories, model-dependent precomputation and index construction, repeated or staged training, and necessary preprocessing.
- **The denominator is the strongest optimized Transformer-based system** for the same `Q` and resources, which may use every transferable published technique (optimizers, tokenizers, schedules, external memory, retrieval, conditional computation). This is called **FAIR-OPT**.
- **Transformers are allowed.** A CIR system may be Transformer-based, hybrid or new. Published techniques may be recombined with attribution.
- **Novelty is optional.** An original mechanism is a valuable additional result, never a condition of success.
- **Whole-system economics are a strong secondary objective,** reported separately: inference, memory, energy, data and deployment cost. Inference savings are never presented as training savings.

The primary lane that pursued this objective was paused on 15 October 2026 ([direction-change.md](direction-change.md)). The charter itself is unchanged.

### Before 12 October

Earlier results used the ratio `TotalCost(CIR, Q) / TotalCost(Strong Transformer, Q)`, with cost measured as training time on a canonical CPU instrument, and reported two denominators: D1 (a strong standard Transformer) and D2 (the same Transformer with every generic module the candidate uses). Commodity CPUs were the primary design target. Those results remain valid measurements; under v1.1 they are diagnostic, not primary claims.

## Why not a single proxy

| Proxy | Why it is not the target |
|---|---|
| FLOPs | Ignores memory traffic, utilization and kernel overhead |
| Parameter count | Active compute can differ greatly |
| BPB | One view of capability; lookup modules can lower loss without adding capability |
| Tokens per second | Says nothing about the quality reached |
| Wall-clock per step | Depends on hardware and implementation |
| Inference speed | Leaves out training cost |

Compute is reported in explicit units: measured time on named hardware, and counted FLOPs, side by side. GPU hours and CPU hours are never added as interchangeable quantities.

## Impact gates

| Gate | Meaning |
|---|---|
| ≤ 0.75× | Signal |
| ≤ 0.50× | Strongly interesting (about 2× less training compute) |
| ≤ 0.20× | Potential industry-level impact (about 5×) |
| ≤ 0.10× | Potential major breakthrough (about 10×) |

Since 12 October the gates apply to `R_train` against FAIR-OPT. The gates are a scale of impact, not targets to be manipulated. Current status per gate is in [current-state.md](current-state.md#gate-status).

## Denominators

| Denominator | What it is | Role |
|---|---|---|
| **FAIR-OPT** | the strongest credible optimized Transformer-based system for the same `Q` and resources, including transferable published techniques | **primary** (since 12 Oct) |
| **FAIR-PARTIAL** | a strong opponent given selected matching components (for example the same input memory) | attribution: why did CIR improve? |
| **D1** | a plain or standard Transformer with fair, generic improvements | diagnostic only |
| **D2** | the same Transformer given every generic module the candidate uses | diagnostic for novelty: what is specific to CIR? |

No complete FAIR-OPT has been built at any scale. The dated partial versions used so far are described in [current-state.md](current-state.md#comparators).

## Number labels

| Label | Meaning |
|---|---|
| MEASURED | Read directly from an instrument (BPB, time per update) |
| ESTIMATED | Computed from measurements (a cost ratio at matched Q) |
| PROJECTED | Extrapolated beyond what was run (another scale or hardware) |
| HYPOTHESIS | A belief not yet measured, with a stated credence where useful |

The labels are never mixed in one number.
