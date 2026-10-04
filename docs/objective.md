# Objective

## The ratio

```
minimize  TotalCost(CIR, Q) / TotalCost(Strong Transformer, Q)
```

for a target capability `Q`. Equivalently: maximize useful language capability per unit of total economic training cost.

`Q` is matched capability. A ratio of 0.5 would mean the same capability at half the total cost. This is the objective, not a result.

## Why not a single proxy

| Proxy | Why it is not the target |
|---|---|
| FLOPs | Ignores memory traffic, utilization and kernel overhead |
| Parameter count | Active compute can differ greatly |
| BPB | One view of capability; lookup modules can lower loss without adding capability |
| Tokens per second | Says nothing about the quality reached |
| Wall-clock per step | Depends on hardware and implementation |
| Inference speed | Leaves out training cost |

## What total cost can include

Wall-clock, CPU/GPU hours, energy, RAM, bandwidth, activation memory, optimizer state, parameter traffic, data exposure, communication, node count, hardware rental or amortization. In current experiments, cost is measured as training time on a canonical CPU instrument (see [cost-to-capability.md](cost-to-capability.md)); the other components are not yet separately accounted.

## Priorities

1. Algorithmic efficiency
2. Cost-to-capability
3. Viability on commodity CPUs (the primary design target, not an artificial restriction)
4. Feasibility on small hardware
5. Scalability
6. Hardware portability
7. Inference efficiency

A mathematical improvement that reduces fundamental computation and also helps on GPUs is stronger than a CPU-specific trick.

## Impact gates

| Gate | Meaning |
|---|---|
| ≤ 0.75× | Signal |
| ≤ 0.50× | Strongly interesting (about 2× cheaper) |
| ≤ 0.20× | Potential industry-level impact (about 5× cheaper) |
| ≤ 0.10× | Potential major breakthrough (about 10× cheaper) |

The gates are a scale of impact, not targets to be manipulated. Current status per gate is in [current-state.md](current-state.md#gate-status).

## Denominators

- **D1:** a strong standard Transformer with fair improvements (positional encoding, gating, normalization, local/global attention, optimizer, learning-rate tuning).
- **D2:** the same Transformer given every generic module the candidate uses (for example n-gram heads or an Engram memory). D2 measures the contribution specific to CIR.
- **Frontier:** the cheapest fair Transformer known at the time of the claim. Currently B1A. Every new claim must be compared against it.

## Number labels

| Label | Meaning |
|---|---|
| MEASURED | Read directly from an instrument (BPB, time per update) |
| ESTIMATED | Computed from measurements (a cost ratio at matched Q) |
| PROJECTED | Extrapolated beyond what was run (another scale or hardware) |

The three are never mixed in one number.
