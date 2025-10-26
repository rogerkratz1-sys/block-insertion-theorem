# block-insertion-theorem

Contains a JSON Schema at schema/block-insertion.schema.json, and example fixtures in data/examples.

Validate a fixture with PowerShell:
Get-Content data\examples\example-001.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'parsed OK'

Validate schema syntax with PowerShell:
Get-Content schema\block-insertion.schema.json -Raw | Out-String | ConvertFrom-Json > ; Write-Output 'schema OK'
