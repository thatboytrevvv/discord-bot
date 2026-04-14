#!/bin/bash
# Setup script for pre-commit hooks
# Run this after cloning the repository to enable pre-commit hooks

set -e

echo "Setting up pre-commit hooks for discord-bot..."

# Check if pre-commit is installed
if ! command -v pre-commit &> /dev/null; then
    echo "pre-commit is not installed. Installing..."
    if command -v pip3 &> /dev/null; then
        pip3 install pre-commit
    elif command -v pip &> /dev/null; then
        pip install pre-commit
    else
        echo "ERROR: pip is not installed. Please install pip first."
        echo "  Ubuntu/Debian: sudo apt-get install python3-pip"
        echo "  macOS: brew install pre-commit"
        exit 1
    fi
fi

# Install the hooks
echo "Installing pre-commit hooks..."
pre-commit install

echo ""
echo "✓ Pre-commit hooks installed successfully!"
echo ""
echo "The hooks will now run automatically on each commit."
echo "To run manually on all files: pre-commit run --all-files"
echo "To skip hooks for a commit: git commit --no-verify"
