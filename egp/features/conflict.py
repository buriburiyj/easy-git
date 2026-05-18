# -*- coding: utf-8 -*-
"""⚔ 충돌 해결"""
import subprocess
from .. import ui, git_core
from ..ui import C, GoBack


def run(repo):
    r = git_core.run(["diff", "--name-only", "--diff-filter=U"], repo)
    conflicts = [l for l in r.stdout.splitlines() if l.strip()]

    if not conflicts:
        ui.header("Conflicts")
        ui.success("충돌 없음!")
        ui.pause()
        return

    ui.header("Conflicts")
    print(f"  {C.YELLOW}⚠{C.R}   {len(conflicts)}개 파일에 충돌이 있습니다")
    print()
    print(f"  {C.GRAY}FILES{C.R}")
    print()
    for f in conflicts:
        print(f"  {C.RED}✗{C.R}   {f}")
    print()
    print()

    items = [
        {"category": "RESOLVE"},
        {"icon": "📝", "label": "에디터로 열기",    "desc": "open in VS Code", "value": "editor"},
        {"icon": "⬅ ", "label": "내 버전 적용",     "desc": "use ours",        "value": "ours"},
        {"icon": "➡ ", "label": "상대 버전 적용",   "desc": "use theirs",      "value": "theirs"},
        {"icon": "✋", "label": "병합 중단",         "desc": "abort merge",     "value": "abort"},
        {"icon": "✅", "label": "해결 완료",         "desc": "mark resolved",   "value": "done"},
    ]

    try:
        choice = ui.select_menu("Conflicts", items)
    except GoBack:
        return

    if choice == "editor":
        for f in conflicts:
            subprocess.run(["code", f], cwd=repo)
        ui.info("수정 후 '해결 완료'를 선택하세요")
        ui.pause()
    elif choice == "ours":
        for f in conflicts:
            git_core.run(["checkout", "--ours", f], repo)
            git_core.run(["add", f], repo)
        ui.success("내 버전 적용됨")
        ui.pause()
    elif choice == "theirs":
        for f in conflicts:
            git_core.run(["checkout", "--theirs", f], repo)
            git_core.run(["add", f], repo)
        ui.success("상대 버전 적용됨")
        ui.pause()
    elif choice == "abort":
        if ui.confirm("merge 중단?", False):
            git_core.run(["merge", "--abort"], repo, capture=False)
            ui.success("중단됨")
            ui.pause()
    elif choice == "done":
        git_core.run(["commit", "--no-edit"], repo, capture=False)
        ui.success("커밋 완료")
        ui.pause()
