# block-insertion-theorem

Contains a JSON Schema at schema/block-insertion.schema.json, and example fixtures in data/examples.

Validate a fixture with PowerShell:
Get-Content data\examples\example-001.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'parsed OK'

Validate schema syntax with PowerShell:
Get-Content schema\block-insertion.schema.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'schema OK'
## Reproducibility

**Repository**: https://github.com/rogerkratz1-sys/block-insertion-theorem.git  
**Snapshot commit**: d65b6554682e637bedbcf916f26495867e00dc18
  
**Archival DOI**: DOI:10.XXXX/zenodo.YYYYYYY  # replace with minted DOI after archiving

To reproduce key results locally:

- Validate BlockSummary JSONs:
  - Windows PowerShell: python .\metadata\validate_block_summaries.py
  - Requires: Python with jsonschema installed (python -m pip install --user jsonschema)

- Regenerate aggregated results:
  - python .\results\scripts\aggregate_results.py

- Regenerate a single index (example for index 5):
  - Replace with your generator command; example: python .\results\scripts\generate_index.py --index 5 --out .\results\per_run\blocks_index_5.json

Metadata and checksums:
- metadata/commit_hash.txt contains the exact commit used for the snapshot.
- metadata/manifest_checksums.sha256 contains SHA-256 checksums for per_run JSON outputs.
