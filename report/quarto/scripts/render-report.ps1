param(
  [switch]$Pdf
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..\..\..")
$paper = Join-Path $repoRoot "report\quarto\paper.qmd"
$outputDir = Join-Path $repoRoot "report\generated"

if (-not (Get-Command quarto -ErrorAction SilentlyContinue)) {
  Write-Error "Quarto is not installed or not available on PATH. Install Quarto, reopen PowerShell, then run: quarto --version"
}

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

Write-Host "Rendering DOCX..."
& quarto render $paper --to docx --output-dir $outputDir
if ($LASTEXITCODE -ne 0) {
  throw "DOCX render failed with exit code $LASTEXITCODE"
}

if ($Pdf) {
  Write-Host "Rendering optional PDF via Typst..."
  & quarto render $paper --to typst --output-dir $outputDir
  if ($LASTEXITCODE -ne 0) {
    throw "PDF render failed with exit code $LASTEXITCODE"
  }
}

Write-Host "Render complete. Output directory: $outputDir"
