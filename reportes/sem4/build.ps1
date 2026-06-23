# Compila avances_sem4.tex localmente (MiKTeX + Biber).
# Uso:  pwsh -File build.ps1     (desde la carpeta sem4/)
$ErrorActionPreference = 'Stop'
$bin = "$env:USERPROFILE\scoop\apps\latex\current\texmfs\install\miktex\bin\x64"
if (Test-Path $bin) { $env:PATH = "$bin;$env:PATH" }
$doc = 'avances_sem4'
Write-Host "== pdflatex (1/3) ==" -ForegroundColor Cyan
pdflatex -interaction=nonstopmode "$doc.tex" | Out-Null
Write-Host "== biber ==" -ForegroundColor Cyan
biber $doc | Out-Null
Write-Host "== pdflatex (2/3) ==" -ForegroundColor Cyan
pdflatex -interaction=nonstopmode "$doc.tex" | Out-Null
Write-Host "== pdflatex (3/3) ==" -ForegroundColor Cyan
pdflatex -interaction=nonstopmode "$doc.tex" | Out-Null
if (Test-Path "$doc.pdf") { Write-Host "OK -> $doc.pdf" -ForegroundColor Green }
else { Write-Host "FALLÓ: revisa $doc.log" -ForegroundColor Red; exit 1 }
