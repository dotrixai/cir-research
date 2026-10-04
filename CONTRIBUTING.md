# Contributing

This repository documents active research. It is not a software project, and it does not accept code. Contributions that make the research more accurate are welcome.

## Especially welcome

- **Corrections:** a number that does not match its stated source, an inconsistency between documents, a claim stated more strongly than its evidence supports.
- **Benchmark criticism:** a baseline that should be stronger, a confound we missed, a metric that misleads.
- **Reproducibility feedback:** what you would need in order to evaluate a claim independently.
- **Literature pointers:** prior work that overlaps with a candidate, a baseline improvement we have not tried, results at larger scale that bear on our hypotheses.
- **Technical discussion and research collaboration.**

## How

- Open an issue. Reference the document and the evidence ID (`I###`, `R###`, `A###`) where possible.
- For a cheaper or stronger Transformer baseline, describe the change and why it is fair (generic, not tuned to the test set).
- For collaboration, use the contact on https://dotrixai.com/contact.

## What to expect

Every substantive issue is read. Not every suggestion will be adopted, and some questions touch implementation details we do not publish (see [docs/publication-policy.md](docs/publication-policy.md)). When a correction changes a result, the change is recorded in the affected document and the old value is marked, not silently replaced.

Please do not post secrets, personal data or anything you are not entitled to share. For security issues, see [SECURITY.md](SECURITY.md).
