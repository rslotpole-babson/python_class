#!/bin/bash
# Exit immediately if any command fails
set -e

# Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up PowerShell profile for VS Code (if needed)
mkdir -p /home/vscode/.config/powershell
PROFILE="/home/vscode/.config/powershell/Microsoft.PowerShell_profile.ps1"
touch "$PROFILE"
echo "if (Test-Path venv/bin/Activate.ps1) { . venv/bin/Activate.ps1 }" >> "$PROFILE"
