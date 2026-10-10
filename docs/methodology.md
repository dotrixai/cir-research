# Methodology

A compressed public summary of the CIR research method (internal version 2.1, adopted 2026-10-03). It describes how decisions are made, not how candidates are implemented.

## 1. Objective and metric

The primary metric is total cost to reach capability `Q` ([objective.md](objective.md)), reported as a curve over several quality levels, not one endpoint. Cost is decomposed as `TotalCostRatio(Q) ≈ ρ_u × ρ_c` and both factors are tracked separately ([cost-to-capability.md](cost-to-capability.md)).

Every number is labeled MEASURED, ESTIMATED or PROJECTED, and the three are never mixed.

## 2. Strong-baseline rule

The economic baseline is a reasonably tuned strong Transformer. Other families (GRU, SSMs, RWKV, DeltaNet) serve as diagnostic baselines only. The Transformer is strengthened with every fair improvement available: positional encoding, local mixing, gating, normalization, optimizer, learning-rate schedule, block design, local/global attention, generic modules, implementation. A dedicated baseline lane acts as an adversary and tries to make the Transformer beat CIR ([baseline-adversary.md](baseline-adversary.md)). The current architecture is never protected.

Rules added after mistakes:

- Every comparator family gets its own learning-rate screen; inherited learning rates are labeled and dependent claims are CONTESTED until attacked.
- Every cost claim must survive a "remove the mixing layers" attack and an equal-compute (wider baseline) attack before it is stated.

## 3. Hypothesis freezing

Before a confirmation run, the protocol is frozen in writing: arms, budget, seeds, pass/fail criteria, predictions with subjective probabilities, and the interpretation of each outcome. Amendments made after freezing are recorded with timestamps and reasons. Ratio-type criteria must require a denominator that is statistically meaningful.

## 4. Discovery vs confirmation

- **Discovery:** short runs (750 updates), one seed, cheap probes. Purpose: find signals and kill ideas early.
- **Confirmation:** full run (1,500 updates), a second seed, baseline attacks, canonical cost measurement, capability battery.

An early screening rule was replaced after measurement: architecture rankings at 250 updates had a rank correlation of 0.09 with final results (0.77 at 500, 0.94 at 750). 250 updates is now used only to pick a learning rate within one architecture.

## 5. Experiment selection by expected value of information

The queue is not first-in-first-out. Candidate experiments are ranked by expected value of information: how likely the result is to change a decision, how many hypotheses it discriminates, its compute and wall-clock cost, its dependencies and its confound risk. A decision board records the ranking and is revised as evidence arrives.

## 6. Multi-fidelity promotion funnel

```
idea → math sanity → prior-art check → cheap synthetic test → short language signal
     → mechanism validation → strong-baseline attack → replication
     → capability battery → scaling → economic validation
```

Compute tiers run from analysis (math, literature, profiling) through synthetic tests, tiny models, small language models, scale validation and final economic evaluation. Ideas earn expensive compute through evidence. Evaluation-only probes on existing checkpoints have been the cheapest way to kill or open branches.

## 7. Mechanistic diagnosis

A result is explained before it is built upon: attention-pattern probes, per-token-class loss decomposition, ablations, context-use probes and profiler breakdowns. Example: the finding that Muon makes Transformer induction heads form early explained why an early recurrent advantage disappeared, and led to the hybrid A010.

## 8. First-principles and de-novo discovery

When a candidate family plateaus, a generic module erases its advantage, or a bound shows the next gate is unreachable, a de-novo cycle is triggered:

- Define the bottleneck without naming an architecture.
- Derive minimum information and operation requirements and rough cost floors.
- Construct primitives from those requirements, then search prior art by equation and operation.
- Record rediscoveries as rediscoveries. Novelty is never forced.

Each generation cycle must include an exploitative candidate, a radical recombination and a de-novo candidate. Before a new candidate is frozen, its best possible advantage is bounded analytically (for example an Amdahl-style bound on the fraction of cost it can replace).

## 9. Capability evaluation

BPB is not an intelligence score. Capabilities are evaluated separately where instruments are reliable: copying, associative recall, bracket closing, context use. Where instruments are unreliable at the current scale (grammar, binding, reasoning, generation), this is stated rather than inferred ([capabilities.md](capabilities.md)). Cost to a capability uses monotone-smoothed curves and the first crossing for every arm.

## 10. Scaling

Scale is earned: reproducible signal, credible mechanism, fair baseline, stable measurement first. Parameters, context, batch and data are varied separately where possible ([scaling.md](scaling.md)).

## 11. Cost measurement integrity

A canonical timing instrument (fixed pinned cores, matrix-multiply calibration, repeated rounds, spread and load limits) defines `ρ_c`. Sessions that fail validity checks are kept as invalid records and re-measured. Ratios are compared only within one valid session, because the same ratio varies by about ±3% between sessions. Timing never runs alongside training.

## 12. Epistemic status

| Status | Meaning |
|---|---|
| VALIDATED | Confirmed under the full confirmation protocol, including the current frontier baseline |
| REPRODUCED | Same protocol, two seeds, same outcome |
| SUPPORTED | Evidence consistent with the claim, not yet confirmed |
| PROVISIONAL | One run or one session; plausible but unreplicated |
| PRELIMINARY | Interim or exploratory, no formal verdict |
| UNDER EVALUATION | Experiment running |
| CONTESTED | A stronger baseline or known confound threatens the result |
| SUPERSEDED | Replaced by better evidence or a corrected method |
| QUARANTINED | Measurement suspected invalid; excluded from reasoning |
| INVALID | Measurement failed validity checks |
| FALSIFIED | Prediction or hypothesis contradicted by evidence |
| REVOKED | Prior belief withdrawn |

Superseded and revoked items are kept for history but excluded from active reasoning.

## 13. Knowledge red-team

After every few meaningful evidence updates, accepted conclusions are attacked: inherited settings, estimator bias, untested baselines, hidden assumptions. Errors in the research process itself (wrong arithmetic, biased estimators, misleading screens) are logged with the rule changed to prevent recurrence.

## 14. Prior-art review

Literature search follows a staged pipeline: a decision-relevant question, terminology discovery, primary sources, extraction, comparison with CIR, synthesis, action. Every candidate idea is searched adversarially against published work before claims of novelty, and literature is consulted before expensive runs that ask whether something is an artifact of small scale.

## 15. Periodic first-principles reset

After major evidence changes, the board is rebuilt from: known facts, revoked beliefs, strongest evidence, strongest counter-evidence, bottlenecks, hidden assumptions, required primitives, alternative families and the highest-value next questions.

## 16. Changes in versions 2.2 and 2.3

Version 2.2 (2026-10-06) turned several guidelines into enforced gates:

- **Baseline Frontier Gate.** Before a cost claim enters confirmation, the cheapest known opponent routes must be attacked. Frontier status is UNATTACKED, PROVISIONAL, STRONG or REOPENED.
- **Economic Feasibility Gate.** Before a family receives many runs, a best-case cost floor and the required update efficiency are written down (the Amdahl bound on mixer substitution came from this).
- **Breakthrough mode** when a family has no plausible path to the next gate.
- **Learning efficiency (ρ_u)** as a research lane of its own.

Version 2.3 (2026-10-10) added rules for turning evidence into systems:

- **Best-known-system register.** A small Pareto set of incumbents per quality target, language, budget, hardware and training/inference trade-off, each with provenance (known prior art, adapted, recombination, implementation optimization, possibly novel).
- **Integration decisions.** Every meaningful result gets an explicit ADOPT / ADAPT / TEST / DEFER / REJECT decision for the incumbent.
- **Full-system accounting.** Table building, data exposure, gate fitting, training, prefill, decode, memory and serving are all recorded. **Averages across languages may not hide a failing language**: claims are reported per language.
- **Attribution.** Imported mechanisms carry provenance and are never claimed as inventions. Improvements from known methods are reported as systems or organization advances, not CIR-specific architecture advances.

