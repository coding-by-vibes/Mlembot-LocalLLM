@echo off
echo ==============================
echo Local Mlembot Launching
echo ==============================

REM Create venv if missing
if not exist localmlembot (
    echo [1/4] Creating virtual environment...
    python -m venv localmlembot
)

REM Activate venv
echo [2/4] Activating virtual environment...
call localmlembot\Scripts\activate.bat

if errorlevel 1 (
    echo ❌ Failed to activate venv
    pause
    exit /b 1
)

REM Install dependencies (optional on relaunch)
echo [3/4] Installing/updating requirements...
call localmlembot\Scripts\python.exe -m pip install -r requirements.txt

REM Run the bot
echo [4/4] Starting bot...
call localmlembot\Scripts\python.exe main.py

REM Optional: deactivate
call localmlembot\Scripts\deactivate.bat
echo Bot shut down.
pause