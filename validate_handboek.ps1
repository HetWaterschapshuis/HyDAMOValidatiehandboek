$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$mkdocsExe = Join-Path $repoRoot ".venv\Scripts\mkdocs.exe"

& $mkdocsExe build --strict