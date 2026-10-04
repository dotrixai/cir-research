# Overview

CIR is DotrixAI's first major research program. It asks one question: can a different architecture or learning system reach the same capability as a strong Transformer for substantially less total cost?

## What CIR is

- A research program, not a product. Nothing here is a finished or final architecture.
- A comparison discipline. Every candidate is measured against strong, deliberately strengthened Transformer baselines on total cost to reach matched capability.
- An evidence log. Positive, negative and superseded results are all published, each with an epistemic status.

## What CIR is not

- Not a claimed Transformer replacement.
- Not validated beyond small scale (about 4M to 7M parameters, one laptop CPU).
- Not commercially available or licensed.

## Where the program stands

At the time of the [current snapshot](current-state.md), the strongest reproduced CIR candidate (A010) beats several strong Transformer baselines on cost to matched BPB, in two seeds. CIR's own baseline attack then found a cheaper Transformer (B1A) against which that advantage disappears. The program objective has not been reached. Current work tests whether any remaining structural asymmetry exists (state tracking, very long contexts) and whether a cheaper hybrid can beat B1A.

## How to read this repository

1. [objective.md](objective.md): what is being minimized and how numbers are labeled.
2. [current-state.md](current-state.md): the dated snapshot.
3. [../results/current-evidence.md](../results/current-evidence.md): the evidence table.
4. [baseline-adversary.md](baseline-adversary.md) and [falsified-and-superseded.md](falsified-and-superseded.md): how claims changed.
5. [limitations.md](limitations.md): what the results cannot tell you.

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
