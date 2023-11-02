<#
.SYNOPSIS
  Helper script create virtual environment using Poetry.

.DESCRIPTION
  This script will detect Python installation, create venv with Poetry
  and install all necessary packages from `poetry.lock` or `pyproject.toml`.

.EXAMPLE

PS> .\manage.ps1

.EXAMPLE

Print verbose information from Poetry:
PS> .\manage.ps1 create-env --verbose

#>

$script_dir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$repo_root = (Get-Item $script_dir).parent.FullName

if (-not (Test-Path 'env:POETRY_HOME')) {
    $env:POETRY_HOME = "$root\.poetry"
}

$FunctionName=$ARGS[0]
$arguments=@()
if ($ARGS.Length -gt 1) {
    $arguments = $ARGS[1..($ARGS.Length - 1)]
}

function Exit-WithCode($exitcode) {
   # Only exit this host process if it's a child of another PowerShell parent process...
   $parentPID = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId=$PID" | Select-Object -Property ParentProcessId).ParentProcessId
   $parentProcName = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId=$parentPID" | Select-Object -Property Name).Name
   if ('powershell.exe' -eq $parentProcName) { $host.SetShouldExit($exitcode) }

   exit $exitcode
}

function Install-Poetry() {
    Write-Host ">>> Installing Poetry ... "
    $python = "python"
    if (Get-Command "pyenv" -ErrorAction SilentlyContinue) {
        if (-not (Test-Path -PathType Leaf -Path "$($repo_root)\.python-version")) {
            $result = & pyenv global
            if ($result -eq "no global version configured") {
                Write-Host "!!! Using pyenv but having no local or global version of Python set." -ForegroundColor Yellow
                Exit-WithCode 1
            }
        }
        $python = & pyenv which python

    }

    $env:POETRY_HOME="$repo_root\.poetry"
    (Invoke-WebRequest -Uri https://install.python-poetry.org/ -UseBasicParsing).Content | & $($python) -
}

function Show-Usage() {
    $usage = @'
    Valhalla  build tool

    Usage: ./manage.ps1 [command]

    Available commands:
            create-env                    Install Poetry and update venv by lock file

'@

    Write-Host $usage -ForegroundColor Gray
}

function Initialize-Environment
{
    Write-Host ">>>  Reading Poetry ... " -NoNewline
    if (-not(Test-Path -PathType Container -Path "$( $env:POETRY_HOME )\bin"))
    {
        Write-Host "NOT FOUND" -ForegroundColor Yellow
        Install-Poetry
        Write-Host "INSTALLED" -ForegroundColor Cyan
    }
    else
    {
        Write-Host "OK" -ForegroundColor Green
    }

    if (-not(Test-Path -PathType Leaf -Path "$( $repo_root )\poetry.lock"))
    {
        Write-Host ">>> Installing virtual environment and creating lock."
    }
    else
    {
        Write-Host ">>> Installing virtual environment from lock."
    }
    $startTime = [int][double]::Parse((Get-Date -UFormat %s))
    & "$env:POETRY_HOME\bin\poetry" config virtualenvs.in-project true --local
    & "$env:POETRY_HOME\bin\poetry" config virtualenvs.create true --local
    & "$env:POETRY_HOME\bin\poetry" install --no-root $poetry_verbosity --ansi
    if ($LASTEXITCODE -ne 0)
    {
        Write-Host "!!! Poetry command failed." -ForegroundColor Red
        Exit-WithCode 1
    }

    $endTime = [int][double]::Parse((Get-Date -UFormat %s))
    $duration = $endTime - $startTime
    Write-Host ">>> Virtual environment created in $duration secs." -ForegroundColor Green
}

function Main {
    if ($null -eq $FunctionName) {
        Show-Usage
        return
    }
    $FunctionName = $FunctionName.ToLower() -replace "\W"
    if ($FunctionName -eq "createenv") {
        Initialize-Environment
    } else {
        Write-Host "Unknown command ""$FunctionName"""
        Show-Usage
    }
}

Main
