# -*- coding: utf-8 -*-
"""💾 백업 zip"""
import os
import zipfile
from datetime import datetime
from ... import ui
from ..ui import C, GoBack


def run(repo):
    name = os.path.basename(repo.rstrip("/"))
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default = os.path.expanduser(f"~/Desktop/{name}_{stamp}.zip")

    ui.header("Backup")
    print(f"  {C.GRAY}PROJECT{C.R}     {C.B}{name}{C.R}")
    print(f"  {C.GRAY}PATH{C.R}        {C.CYAN}{default}{C.R}")
    print()
    print()

    try:
        out = ui.text_input("저장 경로", default)
        skip_git = ui.confirm(".git 폴더 제외?", True)
        skip_dep = ui.confirm("node_modules / __pycache__ 제외?", True)
    except GoBack:
        return

    print()
    ui.info("압축 중...")
    count = 0
    try:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(repo):
                if skip_git and ".git" in dirs:
                    dirs.remove(".git")
                if skip_dep:
                    for skip in ("node_modules", "__pycache__", ".venv", "venv"):
                        if skip in dirs:
                            dirs.remove(skip)
                for f in files:
                    full = os.path.join(root, f)
                    arc = os.path.relpath(full, repo)
                    zf.write(full, arc)
                    count += 1
        size = os.path.getsize(out) / 1024 / 1024

        print()
        ui.step_done("files", f"{count} files")
        ui.step_done("size", f"{size:.1f} MB")
        ui.step_done("path", out)
        print()
        print(f"  {C.GREEN}🎉  백업 완료{C.R}")
    except Exception as e:
        ui.error(f"백업 실패: {e}")
    ui.pause()
