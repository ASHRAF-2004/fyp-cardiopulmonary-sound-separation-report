$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..\..\..")
$paper = Join-Path $repoRoot "report\quarto\paper.qmd"
$bib = Join-Path $repoRoot "literature-review\references\references.bib"
$docx = Join-Path $repoRoot "report\generated\paper.docx"
$pdf = Join-Path $repoRoot "report\generated\paper.pdf"

$checks = @(
  @{ Name = "paper.qmd exists"; Pass = Test-Path $paper },
  @{ Name = "literature-review references.bib exists"; Pass = Test-Path $bib },
  @{ Name = "Quarto available on PATH"; Pass = [bool](Get-Command quarto -ErrorAction SilentlyContinue) },
  @{ Name = "DOCX output exists"; Pass = Test-Path $docx },
  @{ Name = "PDF output exists"; Pass = Test-Path $pdf }
)

foreach ($check in $checks) {
  if ($check.Pass) {
    Write-Host "PASS: $($check.Name)"
  } else {
    Write-Host "FAIL: $($check.Name)"
  }
}

Write-Host ""
Write-Host "Manual DOCX checks still required: page numbering, margins, fonts, table/figure lists, captions, APA references, and appendices."
