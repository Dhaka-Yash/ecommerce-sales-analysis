# PowerShell script to help set up GitHub repository
# Run this script from the project directory

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Repository Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "[OK] Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Git is not installed. Please install Git first." -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/downloads" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Step 1: Initializing Git repository..." -ForegroundColor Yellow

# Initialize git if not already initialized
if (Test-Path .git) {
    Write-Host "[INFO] Git repository already initialized" -ForegroundColor Blue
} else {
    git init
    Write-Host "[OK] Git repository initialized" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 2: Adding all files..." -ForegroundColor Yellow
git add .
Write-Host "[OK] Files added to staging area" -ForegroundColor Green

Write-Host ""
Write-Host "Step 3: Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: E-commerce Sales Performance Analysis Project"
Write-Host "[OK] Initial commit created" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Create a new repository (e.g., 'ecommerce-sales-analysis')" -ForegroundColor White
Write-Host "3. DO NOT initialize with README, .gitignore, or license" -ForegroundColor White
Write-Host "4. Copy the repository URL" -ForegroundColor White
Write-Host ""
Write-Host "5. Run these commands (replace URL with your repository URL):" -ForegroundColor Yellow
Write-Host "   git remote add origin https://github.com/Dhaka-Yash/YOUR-REPO-NAME.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "Or run this script again after creating the repository:" -ForegroundColor Yellow
Write-Host "   .\setup_github.ps1 -Push -RepoName 'your-repo-name'" -ForegroundColor Cyan
Write-Host ""

# Check if user wants to push now
$pushNow = Read-Host "Do you want to add remote and push now? (y/n)"
if ($pushNow -eq 'y' -or $pushNow -eq 'Y') {
    $repoName = Read-Host "Enter your GitHub repository name"
    if ($repoName) {
        Write-Host ""
        Write-Host "Adding remote origin..." -ForegroundColor Yellow
        git remote add origin "https://github.com/Dhaka-Yash/$repoName.git"
        Write-Host "[OK] Remote added" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "Setting branch to main..." -ForegroundColor Yellow
        git branch -M main
        Write-Host "[OK] Branch set to main" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
        Write-Host "You may be prompted for GitHub credentials" -ForegroundColor Blue
        git push -u origin main
        
        Write-Host ""
        Write-Host "[SUCCESS] Project uploaded to GitHub!" -ForegroundColor Green
        Write-Host "Visit: https://github.com/Dhaka-Yash/$repoName" -ForegroundColor Cyan
    }
}
