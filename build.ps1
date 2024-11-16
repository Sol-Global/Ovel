if (-Not (Test-Path -Path ".venv")) {
    python -m venv .venv
    . .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
} else {
    . .\.venv\Scripts\Activate.ps1
}

$pyfigletFontsPath = ".venv/Lib/site-packages/pyfiglet/fonts"
pyinstaller --onefile --name Ovel --hidden-import=numpy --hidden-import=colorama --hidden-import=pyfiglet --hidden-import=pyfiglet.fonts --hidden-import=colorama.Fore --hidden-import=colorama.Back --hidden-import=colorama.Style --hidden-import=colorama.Init --add-data "$pyfigletFontsPath;pyfiglet/fonts" main.py