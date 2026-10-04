# Publication policy

DotrixAI intends to publish enough methodology, benchmark conditions, results and limitations for CIR's technical claims to be independently evaluated. It does not intend to publish everything needed to reproduce proprietary implementations.

## Published here

- The objective, gates, denominators and number labels.
- The research methodology at the level of decision rules.
- Experimental regimes: model sizes, context, batch, token budgets, data languages, hardware.
- Results: BPB differences, cost ratios, per-update ratios, capability probe outcomes, with epistemic status and evidence IDs.
- Negative, superseded and invalidated results, and errors in the research process.
- High-level descriptions of candidates and baselines, and their closest prior art.

## Not published

- Source code, kernels and runtime techniques.
- Exact parameterizations, initializations and internal block design of candidates.
- Candidate ideas still under investigation, beyond a one-line description.
- Model weights, checkpoints, training data dumps and logs.
- Internal ledgers, operational notes and tooling.

## Principles

- Every quantitative claim here is traceable to an internal evidence item (`I###`) or experiment (`R###`).
- A claim is never stated more strongly here than in the internal record.
- When later evidence weakens a claim, this repository is updated and the old claim is marked, not deleted.
- Reproducibility materials (protocols, evaluation definitions, selected checkpoints or code) may be released for specific major claims when they are ready. That is a decision per claim, not a promise.

## Updates

This repository is a snapshot. The date at the top of [current-state.md](current-state.md) is authoritative. The website page at https://dotrixai.com/cir summarizes the same state.
