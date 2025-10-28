### Project overview

block-insertion-theorem is a reproducible reference implementation of a combinatorial/statistical result about block insertion and pairwise relations. The repository provides a formal JSON schema for the block‑insertion data model, example fixtures that demonstrate minimal and maximal valid records, exact‑inference scripts that compute hypergeometric/binomial probabilities and p‑values, and a Monte Carlo routine to validate analytic moments and tail probabilities. The release is archival (Zenodo DOI recorded in the README) and includes verification tooling to validate release binaries and checksums so reviewers can confirm provenance and integrity. This project is intended for researchers and reviewers who require exact inference, reproducible examples, and archival metadata for long‑term citation.

### Repository organization

- schema contains the authoritative JSON Schema: **schema/block-insertion.schema.json**; use it to validate any example or produced record.
- data/examples contains example fixtures including minimal and maximal valid records used for CI and manual checks.
- scripts contains analysis and utility scripts: **exact_inference.py** (hypergeometric/binomial pmf and exact p‑value calculator), **monte_carlo.py** (empirical p‑value simulations with seed control), and **verify-checksums.ps1** (verifier for appendix binaries).
- ci (or .github/workflows) should contain schema validation and unit tests that run the example fixtures and the Monte Carlo smoke test.
- appendix contains metadata files for release: **CITATION.md**, **CHECKSUMS.md**, **CONTACT.md**, and a DOI/commit record for archival provenance.
To validate locally use the provided PowerShell validation examples, and to reproduce statistical results run the exact_inference and monte_carlo scripts with the documented parameters and seeds.
