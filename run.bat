@echo off
echo ========================================
echo AI Teacher Assistant System - Setup
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found! Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo.

echo [2/4] Installing required packages...
echo This may take a few minutes on first run...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install packages.
    pause
    exit /b 1
)
echo.

echo [3/4] Creating data directory...
if not exist "data" mkdir data
echo Data directory ready.
echo.

echo [4/4] Setup complete!
echo.
echo ========================================
echo Ready to launch!
echo ========================================
echo.
echo Your API Key is configured in .env file
echo Model: llama-3.3-70b-versatile
echo.
echo Starting Streamlit application...
echo.

streamlit run app.py

pause
