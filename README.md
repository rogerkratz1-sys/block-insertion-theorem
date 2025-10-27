# block-insertion-theorem

Contains a JSON Schema at schema/block-insertion.schema.json, and example fixtures in data/examples.

Validate a fixture with PowerShell:
Get-Content data\examples\example-001.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'parsed OK'

Validate schema syntax with PowerShell:
Get-Content schema\block-insertion.schema.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'schema OK'
## Reproducibility

Repository snapshot: https://github.com/rogerkratz1-sys/block-insertion-theorem.git  
DOI: 10.5281/zenodo.17451500  
Version: v1.0.0  
Commit: 61ef5c7a6e3c478617809ee0a7fe1fed398027ef  

To reproduce or verify this snapshot:
git clone https://github.com/rogerkratz1-sys/block-insertion-theorem.git
cd block-insertion-theorem
git checkout 61ef5c7a6e3c478617809ee0a7fe1fed398027ef
