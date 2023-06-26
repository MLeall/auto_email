@echo off

if exist ".venvAuto_email" (
    echo Virtual environment already exists. Skipping requirement installation.
) else (
    python -m venv .venvAuto_email
    pip install -r requirements.txt
)

cd .venvAuto_email\Scripts
call Activate.bat
cd ..
cd ..
python auto_email.py
call Deactivate.bat