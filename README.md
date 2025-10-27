[![DOI](https://zenodo.org/badge/428375523.svg)](https://zenodo.org/badge/latestdoi/428375523)

# block-insertion-theorem

Contains a JSON Schema at schema/block-insertion.schema.json, and example fixtures in data/examples.

Validate a fixture with PowerShell:
Get-Content data\examples\example-001.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'parsed OK'

Validate schema syntax with PowerShell:
Get-Content schema\block-insertion.schema.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'schema OK'
## Reproducibility


> Note: To verify the appendix binaries, run the included verifier from the repository root:
> 
> PowerShell: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; .\verify-checksums.ps1
> 
> The script prints OK/MISMATCH for each file and sets the process exit code to 0 on success.
Repository snapshot: https://github.com/rogerkratz1-sys/block-insertion-theorem.git  
DOI: 10.5281/zenodo.17451500  
Version: v1.0.0  
Commit: 075948ad96d5063bfbf5d38fde75e74c6927a4d5

To reproduce or verify this snapshot:
git clone https://github.com/rogerkratz1-sys/block-insertion-theorem.git
cd block-insertion-theorem
git checkout 075948ad96d5063bfbf5d38fde75e74c6927a4d5

## Citation
Kratz R. block-insertion-theorem v1.0.0. Zenodo. 2025. DOI: 10.5281/zenodo.17451500. Commit: 075948ad96d5063bfbf5d38fde75e74c6927a4d5. Repository: https://github.com/rogerkratz1-sys/block-insertion-theorem.


