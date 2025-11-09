# AI Teacher Assistant - Git Installation & Push Script
# Run this script in PowerShell as Administrator

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Git Installation & GitHub Push Guide" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Check if Git is already installed
Write-Host "Step 1: Checking if Git is installed..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>$null
    if ($gitVersion) {
        Write-Host "✓ Git is already installed: $gitVersion" -ForegroundColor Green
        $skipInstall = $true
    }
} catch {
    Write-Host "✗ Git is not installed" -ForegroundColor Red
    $skipInstall = $false
}

if (-not $skipInstall) {
    Write-Host "`nStep 2: Download Git installer..." -ForegroundColor Yellow
    Write-Host "Opening Git download page in your browser..." -ForegroundColor White
    Start-Process "https://git-scm.com/download/win"
    
    Write-Host "`nPlease:" -ForegroundColor Cyan
    Write-Host "1. Download 'Git for Windows' (64-bit recommended)" -ForegroundColor White
    Write-Host "2. Run the installer" -ForegroundColor White
    Write-Host "3. Use ALL DEFAULT SETTINGS (just click Next)" -ForegroundColor White
    Write-Host "4. After installation, CLOSE this PowerShell window" -ForegroundColor White
    Write-Host "5. Open a NEW PowerShell window" -ForegroundColor White
    Write-Host "6. Run this script again`n" -ForegroundColor White
    
    Read-Host "Press Enter to exit and install Git"
    exit
}

Write-Host "`nStep 3: Configure Git (first time setup)..." -ForegroundColor Yellow
Write-Host "Enter your name (for Git commits):" -ForegroundColor Cyan
$userName = Read-Host
Write-Host "Enter your email (your GitHub email):" -ForegroundColor Cyan
$userEmail = Read-Host

git config --global user.name "$userName"
git config --global user.email "$userEmail"
Write-Host "✓ Git configured successfully!" -ForegroundColor Green

Write-Host "`nStep 4: Navigate to project directory..." -ForegroundColor Yellow
Set-Location "d:\Documents\UNI\3rd  Year\Application of Ai\Project"
Write-Host "✓ Current directory: $(Get-Location)" -ForegroundColor Green

Write-Host "`nStep 5: Initialize Git repository..." -ForegroundColor Yellow
git init
Write-Host "✓ Git repository initialized!" -ForegroundColor Green

Write-Host "`nStep 6: Add all files to Git..." -ForegroundColor Yellow
git add .
Write-Host "✓ Files staged for commit!" -ForegroundColor Green

Write-Host "`nStep 7: Check what will be committed..." -ForegroundColor Yellow
Write-Host "Files to be committed:" -ForegroundColor Cyan
git status --short

Write-Host "`nStep 8: Create initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: AI-Powered Teacher Assistant System"
Write-Host "✓ Initial commit created!" -ForegroundColor Green

Write-Host "`nStep 9: Add remote repository..." -ForegroundColor Yellow
$repoUrl = "https://github.com/Sambhav-Ja1n/AI-Powered-Productivity-engine-for-teachers.git"
git remote add origin $repoUrl
Write-Host "✓ Remote repository added!" -ForegroundColor Green

Write-Host "`nStep 10: Prepare to push..." -ForegroundColor Yellow
git branch -M main
Write-Host "✓ Branch set to 'main'!" -ForegroundColor Green

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  READY TO PUSH TO GITHUB!" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Next: Push your code to GitHub" -ForegroundColor Yellow
Write-Host "Command: git push -u origin main`n" -ForegroundColor White

Write-Host "When you run the push command, you'll be asked for:" -ForegroundColor Cyan
Write-Host "- GitHub Username: Sambhav-Ja1n" -ForegroundColor White
Write-Host "- Password: Use Personal Access Token (NOT your GitHub password)`n" -ForegroundColor White

Write-Host "How to get Personal Access Token:" -ForegroundColor Yellow
Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor White
Write-Host "2. Click 'Generate new token (classic)'" -ForegroundColor White
Write-Host "3. Give it a name: 'Teacher Assistant Push'" -ForegroundColor White
Write-Host "4. Select scope: 'repo' (check the box)" -ForegroundColor White
Write-Host "5. Click 'Generate token'" -ForegroundColor White
Write-Host "6. Copy the token (it starts with 'ghp_...')" -ForegroundColor White
Write-Host "7. Use this token as your password`n" -ForegroundColor White

$ready = Read-Host "Ready to push? Type 'yes' to continue"

if ($ready -eq "yes") {
    Write-Host "`nPushing to GitHub..." -ForegroundColor Yellow
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✓✓✓ SUCCESS! ✓✓✓" -ForegroundColor Green
        Write-Host "Your project is now on GitHub!" -ForegroundColor Green
        Write-Host "`nView it at: https://github.com/Sambhav-Ja1n/AI-Powered-Productivity-engine-for-teachers`n" -ForegroundColor Cyan
    } else {
        Write-Host "`n✗ Push failed. Common issues:" -ForegroundColor Red
        Write-Host "1. Wrong username/password" -ForegroundColor White
        Write-Host "2. Need to use Personal Access Token instead of password" -ForegroundColor White
        Write-Host "3. Repository might need force push`n" -ForegroundColor White
        Write-Host "Try again with: git push -u origin main --force" -ForegroundColor Yellow
    }
} else {
    Write-Host "`nPush cancelled. Run when ready:" -ForegroundColor Yellow
    Write-Host "git push -u origin main`n" -ForegroundColor White
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Script Complete!" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Read-Host "Press Enter to exit"
