# Quick Installation Script for AI Teacher Assistant System

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "AI Teacher Assistant System - Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/4] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Install packages
Write-Host "[2/4] Installing required packages..." -ForegroundColor Yellow
Write-Host "This may take a few minutes on first run..." -ForegroundColor Gray
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install packages." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "Packages installed successfully!" -ForegroundColor Green
Write-Host ""

# Create data directory
Write-Host "[3/4] Creating data directory..." -ForegroundColor Yellow
if (-not (Test-Path "data")) {
    New-Item -ItemType Directory -Path "data" | Out-Null
}
Write-Host "Data directory ready." -ForegroundColor Green
Write-Host ""

# Complete
Write-Host "[4/4] Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Ready to launch!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your API Key is configured in .env file" -ForegroundColor White
Write-Host "Model: llama-3.3-70b-versatile" -ForegroundColor White
Write-Host ""
Write-Host "Starting Streamlit application..." -ForegroundColor Yellow
Write-Host ""

# Run Streamlit
streamlit run app.py

Read-Host "Press Enter to exit"
