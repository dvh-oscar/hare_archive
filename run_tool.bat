@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1

set NEED_INSTALL=0

:: 1. 가상환경(.venv) 존재 여부 확인 및 자동 생성
if not exist ".venv\Scripts\python.exe" (
    echo [INFO] Python 가상환경[.venv]을 생성합니다...
    where py >nul 2>&1 && (
        py -3 -m venv .venv
    ) || (
        python -m venv .venv
    )
    set NEED_INSTALL=1
)

:: 가상환경 생성 실패 시 중단
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Python 가상환경 생성에 실패했습니다. Python 설치 여부를 확인해주세요.
    pause
    exit /b 1
)

:: 2. 의존성(Pillow 등) 설치 여부 확인
.venv\Scripts\python.exe -c "import PIL" >nul 2>&1
if errorlevel 1 (
    set NEED_INSTALL=1
)

if "%NEED_INSTALL%"=="1" (
    echo [INFO] 의존성 패키지[Pillow 등]를 설치 중입니다...
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\pip.exe install -r requirements.txt
    echo [INFO] 패키지 설치 완료.
)

:: 3. 유틸리티 스크립트 실행
echo.
.venv\Scripts\python.exe tools\standing_illust.py %*
echo.

pause
