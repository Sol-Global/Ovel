if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Would you like to install it now? (Y/N)"
    $response = Read-Host
    if ($response -eq 'Y' -or $response -eq 'y') {
        winget install -e --id Python.Python.3
        if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
            Write-Error "Python installation failed. Please install Python manually and try again."
            exit 1
        }
    } else {
        Write-Error "Python is not installed. Please install Python and try again."
        exit 1
    }
}

if (-Not (Test-Path -Path ".venv")) {
    python -m venv .venv
    . .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
} else {
    . .\.venv\Scripts\Activate.ps1
}

$fontPathFile = "fontPath.txt"
if (Test-Path -Path $fontPathFile) {
    $pyfigletFontsPath = Get-Content -Path $fontPathFile
} else {
    Write-Host "Please enter the path to pyfiglet fonts:"
    $pyfigletFontsPath = Read-Host
    Set-Content -Path $fontPathFile -Value $pyfigletFontsPath
}

pyinstaller --onefile --name Ovel --hidden-import=numpy --hidden-import=colorama --hidden-import=pyfiglet --hidden-import=pyfiglet.fonts --hidden-import=colorama.Fore --hidden-import=colorama.Back --hidden-import=colorama.Style --hidden-import=colorama.Init --add-data "$pyfigletFontsPath;pyfiglet/fonts" main.py