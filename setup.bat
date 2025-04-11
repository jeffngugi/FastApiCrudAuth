@echo off
REM Setup script for FastAPI CRUD application (Windows)
REM This script creates a virtual environment and installs all dependencies

echo Checking Python version...
python --version > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
for /f "tokens=1,2 delims=." %%a in ("%python_version%") do (
    set major=%%a
    set minor=%%b
)

if %major% LSS 3 (
    echo Error: Python 3.9 or higher is required.
    echo Current version: %python_version%
    exit /b 1
) else if %major% EQU 3 (
    if %minor% LSS 9 (
        echo Error: Python 3.9 or higher is required.
        echo Current version: %python_version%
        exit /b 1
    )
)

echo Using Python %python_version%

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Failed to create virtual environment.
        exit /b 1
    )
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -e .

echo.
echo Installation complete!
echo.
echo To activate the virtual environment, run:
echo   .venv\Scripts\activate.bat
echo.
echo To start the application with Uvicorn (full API functionality):
echo   uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
echo.
echo To start the application with Gunicorn (production mode):
echo   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
echo.

pause