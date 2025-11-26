if (-not $PSScriptRoot) {
    throw "Skriptpfad konnte nicht ermittelt werden."
}
Set-Location $PSScriptRoot

Start-Process "code" -ArgumentList "attendance.code-workspace" -WindowStyle Hidden

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
Read-Host "press enter to exit"