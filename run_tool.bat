@echo off
chcp 65001 >nul
cd /d "%~dp0"

set NEED_INSTALL=0

:: 1. 가상환경(.venv) 존재 여부 확인 및 자동 생성
if not exist ".venv\Scripts\python.exe" (
    echo [INFO] Python 가상환경(.venv)을 생성합니다...
    where py >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        py -3 -m venv .venv
    ) else (
        python -m venv .venv
    )
    set NEED_INSTALL=1
)

:: 2. 의존성(Pillow 등) 설치 여부 확인
.venv\Scripts\python.exe -c "import PIL" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    set NEED_INSTALL=1
)

if "%NEED_INSTALL%"=="1" (
    echo [INFO] 의존성 패키지(Pillow 등)를 설치 중입니다...
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\pip.exe install -r requirements.txt
    echo [INFO] 패키지 설치 완료.
)

:: 3. 유틸리티 스크립트 실행
echo.
.venv\Scripts\python.exe tools\hello_world.py %*
echo.

pause
