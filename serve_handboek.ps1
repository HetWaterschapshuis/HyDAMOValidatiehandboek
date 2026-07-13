$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $repoRoot ".venv"
$activateScript = Join-Path $venvPath "Scripts\\Activate.ps1"
$venvPython = Join-Path $venvPath "Scripts\\python.exe"

Set-Location $repoRoot

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "uv is niet gevonden. Installeer uv eerst voordat je dit script gebruikt."
}

if (-not (Test-Path $venvPath) -or -not (Test-Path $venvPython)) {
    Write-Host "Virtual environment ontbreekt. Bouwen van .venv en synchroniseren van dependencies..."
    uv venv
    uv pip sync requirements.txt
}

if (-not (Test-Path $activateScript)) {
    throw "Activatiescript niet gevonden op $activateScript"
}

. $activateScript
$env:NO_MKDOCS_2_WARNING = "1"
mkdocs serve -f mkdocs.yml
