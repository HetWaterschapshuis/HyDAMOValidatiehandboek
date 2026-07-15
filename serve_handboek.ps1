$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$venvPath = Join-Path $repoRoot ".venv"
$venvPython = Join-Path $venvPath "Scripts\python.exe"
$mkdocsExe = Join-Path $venvPath "Scripts\mkdocs.exe"

if (-not (Test-Path $venvPython)) {
    uv venv
    uv pip install --python $venvPython -r requirements.txt
}

$env:NO_MKDOCS_2_WARNING = "1"

& $mkdocsExe serve -f mkdocs.yml
