if (-not $PSScriptRoot) {
    throw "path to script root could not be determined."
}
Set-Location $PSScriptRoot

Start-Process "code" -ArgumentList "SCM.code-workspace" -WindowStyle Hidden


$process = Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
if ($null -eq $process) {
    Write-Host "Docker Desktop is not running. Starting now..."
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    do {
        Start-Sleep -Seconds 5
        $ready = docker info 2>$null
    } until ($ready)
    Write-Host "Docker is ready!"
}
else { Write-Host "Docker Desktop is already running." }

$containers = @("attendance-web-1", "attendance-db-1")
$running = docker ps --format "{{.Names}}"
if ($containers | Where-Object { $running -contains $_ }) {
    Write-Host "atleast 1 of 2 containers is already running. skipping docker build and up."
}
else {
    docker-compose build
    docker-compose up -d
}
Start-Process "powershell.exe" -ArgumentList "-NoExit", "-Command Set-Location '$PSScriptRoot'"
Write-Host "Will close in 10 seconds..."
Start-Sleep -Seconds 10