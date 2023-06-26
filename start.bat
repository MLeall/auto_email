@echo off

set "current_path=%CD%"
if exist ".venvAuto_email" (
    echo Virtual environment already exists. Skipping requirement installation.
    cd .venvAuto_email\Scripts
    call activate.bat
) else (
    echo Creating virtual environment, please wait...
    python -m venv .venvAuto_email
    echo Virtual environment created sucessefull.
    cd .venvAuto_email\Scripts
    call activate.bat
    cd %current_path%
    pip install -r requirements.txt
)

cd %current_path%
python auto_email.py
call deactivate.bat
echo Done. You may close this now.
pause