# verify-checksums.ps1
$expected = @{
  "docs/appendix-III.docx" = "6EA6FC26A41EBFF431EBAF8DF1626370F17EAA7C61935797C43C60CF74613F02"
  "docs/appendix-IV.docx"  = "0A1BB3E483AE4412E9E2B30BA7AE75CBCC6689B9B40D6152A9830D42879C728E"
}
$ok = $true
foreach ($path in $expected.Keys) {
  if (-not (Test-Path $path)) { Write-Host "MISSING: $path"; $ok = $false; continue }
  $h = (Get-FileHash $path -Algorithm SHA256).Hash
  if ($h -ne $expected[$path]) { Write-Host "MISMATCH: $path`n  expected: $($expected[$path])`n  actual:   $h"; $ok = $false } else { Write-Host "OK: $path" }
}
if ($ok) { Write-Host "All checksums match." ; exit 0 } else { Write-Host "One or more mismatches found." ; exit 2 }
