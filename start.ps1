if (Test-Path -Path ".venvAuto_email" -PathType Container) {
    Write-Host "Virtual environment already exists. Skipping requirement installation."
}
else {
    python -m venv .venvAuto_email
    pip install -r requirements.txt
}

cd venvAuto_email\Scripts
.\Activate.ps1
cd ..
cd ..
python .\auto_email.py
deactivate