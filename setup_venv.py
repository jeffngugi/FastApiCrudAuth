#!/usr/bin/env python3
"""
Setup script to create a virtual environment and install dependencies for the FastAPI CRUD app.
This script works on all platforms (Windows, macOS, Linux).
"""

import os
import platform
import subprocess
import sys
import venv
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.9 or higher."""
    if sys.version_info < (3, 9):
        print(f"Error: Python 3.9 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"Using Python {sys.version}")

def create_venv():
    """Create a virtual environment if it doesn't exist."""
    venv_dir = Path(".venv")
    if not venv_dir.exists():
        print("Creating virtual environment...")
        try:
            venv.create(venv_dir, with_pip=True)
            print("Virtual environment created successfully.")
        except Exception as e:
            print(f"Error: Failed to create virtual environment: {e}")
            sys.exit(1)
    else:
        print("Virtual environment already exists.")
    return venv_dir

def get_venv_python_path(venv_dir):
    """Get the path to the Python executable in the virtual environment."""
    if platform.system() == "Windows":
        return venv_dir / "Scripts" / "python.exe"
    else:
        return venv_dir / "bin" / "python"

def get_venv_pip_path(venv_dir):
    """Get the path to the pip executable in the virtual environment."""
    if platform.system() == "Windows":
        return venv_dir / "Scripts" / "pip.exe"
    else:
        return venv_dir / "bin" / "pip"

def install_dependencies(venv_pip):
    """Install dependencies using pip in the virtual environment."""
    print("Upgrading pip...")
    try:
        subprocess.run([str(venv_pip), "install", "--upgrade", "pip"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading pip: {e}")
        sys.exit(1)

    print("Installing dependencies...")
    try:
        subprocess.run([str(venv_pip), "install", "-e", "."], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def print_activation_instructions(venv_dir):
    """Print instructions for activating the virtual environment."""
    print("\nInstallation complete!")
    print("\nTo activate the virtual environment:")
    
    if platform.system() == "Windows":
        print(f"  {venv_dir}\\Scripts\\activate.bat")
    else:
        print(f"  source {venv_dir}/bin/activate")
    
    print("\nTo start the application with Uvicorn (full API functionality):")
    print("  uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload")
    
    print("\nTo start the application with Gunicorn (production mode):")
    print("  gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app")

def main():
    """Main function to set up the environment."""
    check_python_version()
    venv_dir = create_venv()
    venv_pip = get_venv_pip_path(venv_dir)
    install_dependencies(venv_pip)
    print_activation_instructions(venv_dir)

if __name__ == "__main__":
    main()