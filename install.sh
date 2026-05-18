#!/bin/bash
# Easy Git - macOS 설치 스크립트
set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
GRAY='\033[0;90m'
NC='\033[0m'

INSTALL_DIR="$HOME/.easy-git"
BIN_DIR="/usr/local/bin"
BIN_NAME="gitup"

echo ""
echo -e "  ${CYAN}✦${NC}  ${BOLD}Easy Git 설치${NC}"
echo -e "  ${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "  ${RED}✗${NC}  macOS 전용입니다."
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo -e "  ${RED}✗${NC}  Python 3가 필요합니다."
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo -e "  ${RED}✗${NC}  Git이 필요합니다."
    exit 1
fi

echo -e "  ${GREEN}✓${NC}  환경 확인 완료"

mkdir -p "$INSTALL_DIR"

if [ -f "easy_git.py" ]; then
    cp -R . "$INSTALL_DIR/"
    echo -e "  ${GREEN}✓${NC}  파일 복사 완료"
else
    echo -e "  ${YELLOW}⠙${NC}  파일 다운로드 중..."
    curl -fsSL https://github.com/USERNAME/easy-git/archive/main.tar.gz | \
        tar -xz -C "$INSTALL_DIR" --strip-components=1
    echo -e "  ${GREEN}✓${NC}  다운로드 완료"
fi

chmod +x "$INSTALL_DIR/easy_git.py"

if [ -w "$BIN_DIR" ]; then
    ln -sf "$INSTALL_DIR/easy_git.py" "$BIN_DIR/$BIN_NAME"
else
    sudo ln -sf "$INSTALL_DIR/easy_git.py" "$BIN_DIR/$BIN_NAME"
fi

echo -e "  ${GREEN}✓${NC}  gitup 명령 등록 완료"
echo ""
echo -e "  ${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  🎉  설치 완료!"
echo ""
echo -e "  이제 어디서든 ${CYAN}gitup${NC} 명령으로 실행할 수 있습니다."
echo ""
echo -e "  예시:"
echo -e "    ${YELLOW}cd ~/projects/my-app${NC}"
echo -e "    ${YELLOW}gitup${NC}"
echo ""
