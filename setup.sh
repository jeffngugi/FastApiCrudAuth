#!/bin/bash

# Setup script for FastAPI CRUD application
# This script creates a virtual environment and installs all dependencies

# Ensure Python 3.9+ is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}')
major=$(echo $python_version | cut -d. -f1)
minor=$(echo $python_version | cut -d. -f2)

if [ "$major" -lt 3 ] || [ "$major" -eq 3 -a "$minor" -lt 9 ]; then
    echo "Error: Python 3.9 or higher is required."
    echo "Current version: $python_version"
    exit 1
fi

echo "Using Python $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        exit 1
    fi
    echo "Virtual environment created successfully."
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -e .

echo "Installation complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To start the application with Uvicorn (full API functionality):"
echo "  uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload"
echo ""
echo "To start the application with Gunicorn (production mode):"
echo "  gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app"
echo ""