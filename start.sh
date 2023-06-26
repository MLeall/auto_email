#!/bin/bash

if [ -d ".venvAuto_email" ]; then
    echo "Virtual environment already exists. Skipping requirement installation."
else
    python -m venv .venvAuto_email
    source .venvAuto_email/bin/activate
    pip install -r requirements.txt
fi

python auto_email.py
deactivate