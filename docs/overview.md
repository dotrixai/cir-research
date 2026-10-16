# Overview

CIR is DotrixAI's first major research program. It asks one question: how little training compute is needed to reach a given capability, compared with a strong, optimized Transformer system? Since 12 October 2026 the answer may itself be Transformer-based; novelty is optional ([objective.md](objective.md)).

**Status (16 October 2026): the primary research lane is paused** since 15 October. See [direction-change.md](direction-change.md).

## What CIR is

- A research program, not a product. Nothing here is a finished or final architecture.
- A comparison discipline. Every candidate is measured against strong, deliberately strengthened Transformer baselines on total cost to reach matched capability.
- An evidence log. Positive, negative and superseded results are all published, each with an epistemic status. One dated exception: exact outcomes of 10–15 October 2026 are withheld for now ([publication-policy.md](publication-policy.md#withheld-results)).

## What CIR is not

- Not a claimed Transformer replacement.
- Not validated beyond small scale (up to about 7M parameters on one laptop CPU; 4.7–85M parameters for one epoch on one rented A100, one seed).
- Not commercially available or licensed.

## Where the program stands

At the time of the [current snapshot](current-state.md):

- **The primary objective was not reached.** No candidate reached the signal gate (≤ 0.75) in training compute against a strong published recipe at 20M or 85M parameters.
- **CIR-specific architectures** (delta-rule recurrent mixers and hybrids) were closed for general language modeling at small scale on 4 October.
- **The generic counted organization** (a small Transformer with counted n-gram statistics, a cache, a pointer and a trained gate; later also a hashed n-gram input memory) looked very cheap against plain Transformers (0.04–0.06×) but is built entirely from published parts. Against opponents with the same published parts it is at 0.26–0.54 at ≤ 4M, and at the first GPU scale point about 1.0 on web text like the training data.
- **No original training-compute lever was found;** the laptop-scale search was stopped by its own rule on 13 October.
- **The primary lane was paused on 15 October.** The record is being turned into research tasks for AI research agents.

Every earlier public snapshot is kept in [research-log.md](research-log.md).

## How to read this repository

1. [direction-change.md](direction-change.md): why the primary lane was paused in October 2026.
2. [objective.md](objective.md): what is being minimized and how numbers are labeled.
3. [current-state.md](current-state.md): the dated snapshot, and [research-log.md](research-log.md) for its history.
4. [../results/current-evidence.md](../results/current-evidence.md): the evidence table.
5. [baseline-adversary.md](baseline-adversary.md) and [falsified-and-superseded.md](falsified-and-superseded.md): how claims changed.
6. [limitations.md](limitations.md): what the results cannot tell you.

## Identifiers

IDs match DotrixAI's internal ledgers so later publications can be traced back:

| Prefix | Meaning |
|---|---|
| `A###` | Architecture candidate |
| `R###` | Experiment (run) |
| `I###` | Evidence item |
| `H###` | Hypothesis |

Internal ledgers are not published; the IDs are provided for traceability.

## Glossary

| Term | Meaning |
|---|---|
| BPB | Bits per byte on held-out text, macro-averaged over English and Indonesian evaluation sets |
| Q | Matched quality or capability level |
| update | One optimizer step; at batch 8 and 4,096 tokens, 32,768 tokens |
| ρ_u | Relative number of updates (tokens) needed to reach Q |
| ρ_c | Relative cost per update, from a canonical timing session |
| D1 / D2 | Denominators: standard Transformer / Transformer with the same generic modules |
| Muon | An orthogonalized-update optimizer (Jordan, 2024) |
| FAIR-OPT | The strongest optimized Transformer-based system for matched Q; the primary denominator since 12 Oct 2026 |
| FO-L1 | A dated strong small-model recipe at 20M parameters, used as a partial FAIR-OPT on the GPU |
| U | One epoch of the GPU training stream (0.38B tokens); 0.5U is half an epoch |
