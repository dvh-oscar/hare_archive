#!/usr/bin/env bash
set -e

# 스크립트 위치(프로젝트 루트)로 이동
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

NEED_INSTALL=0

# 1. 가상환경(.venv) 존재 여부 확인 및 자동 생성
if [ ! -d ".venv" ] || [ ! -f ".venv/bin/python" ]; then
    echo "📦 Python 가상환경(.venv)을 생성합니다..."
    python3 -m venv .venv
    NEED_INSTALL=1
fi

# 2. 의존성(Pillow 등) 설치 여부 확인
if ! .venv/bin/python -c "import PIL" >/dev/null 2>&1; then
    NEED_INSTALL=1
fi

if [ "$NEED_INSTALL" = "1" ]; then
    echo "📦 의존성 패키지(Pillow 등)를 설치 중입니다..."
    .venv/bin/pip install --upgrade pip || true
    .venv/bin/pip install -r requirements.txt
    echo "✅ 패키지 설치 완료."
fi

# 3. 유틸리티 스크립트 실행
echo ""
.venv/bin/python tools/standing_illust.py "$@"
