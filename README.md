### Project overview

block-insertion-theorem is a reproducible reference implementation of a combinatorial result about block insertion and counting linear extensions of posets. The repository provides a formal JSON schema for the block‑insertion data model, example fixtures that demonstrate minimal and maximal valid records, deterministic insertion‑bound bookkeeping routines for integrating the Block Insertion Theorem into enumeration workflows, and release verification tooling to validate binaries and checksums so reviewers can confirm provenance and integrity. This project is intended for researchers and reviewers who require reproducible examples, reference‑grade documentation, and archival metadata for long‑term citation.

---

### Repository organization

- schema contains the authoritative JSON Schema: **schema/block-insertion.schema.json**; use it to validate any example or produced record.  
- data/examples contains example fixtures including minimal and maximal valid records used for CI and manual checks.  
- scripts contains implementation and utility scripts: insertion and bookkeeping routines, unit-test helpers, and **verify-checksums.ps1** (verifier for appendix binaries).  
- ci (or .github/workflows) should contain schema validation and unit tests that run the example fixtures and smoke tests for the insertion routines.  
- appendix contains metadata files for release: **CITATION.md**, **CHECKSUMS.md**, **CONTACT.md**, and a DOI/commit record for archival provenance.

---

### Quick start

- Validate schema (PowerShell):
```powershell
Get-Content schema\block-insertion.schema.json -Raw | Out-String | ConvertFrom-Json > $null; Write-Output 'schema OK'

<!-- README: clarify scope and remove stats; edited 2025-10-29T18:54:41.5932562-07:00 -->
