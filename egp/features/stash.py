# -*- coding: utf-8 -*-
"""📦 임시저장"""
from .. import ui, git_core
from ..ui import C, GoBack


def run(repo):
    while True:
        items = [
            {"category": "ACTIONS"},
            {"icon": "💾", "label": "현재 저장",     "desc": "save current",  "value": "save"},
            {"icon": "📥", "label": "복원",          "desc": "pop latest",    "value": "pop"},
            {"icon": "👁 ", "label": "내용 보기",     "desc": "show diff",     "value": "show"},
            {"icon": "🗑 ", "label": "모두 삭제",     "desc": "clear all",     "value": "clear"},
        ]
        try:
            choice = ui.select_menu("Stash", items)
        except GoBack:
            return

        try:
            if choice == "save":
                m = ui.text_input("메모 (선택)")
                args = ["stash", "push"]
                if m:
                    args += ["-m", m]
                git_core.run(args, repo, capture=False)
                ui.pause()
            elif choice == "pop":
                git_core.run(["stash", "pop"], repo, capture=False)
                ui.pause()
            elif choice == "show":
                ui.header("Stash diff")
                git_core.run(["stash", "show", "-p"], repo, capture=False)
                ui.pause()
            elif choice == "clear":
                if ui.confirm("모든 stash 삭제?", False):
                    git_core.run(["stash", "clear"], repo, capture=False)
                    ui.pause()
        except GoBack:
            continue
