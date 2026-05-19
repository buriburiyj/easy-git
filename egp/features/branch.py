# -*- coding: utf-8 -*-
"""🌿 브랜치 관리"""
from ... import ui, git_core
from ..ui import C, GoBack


def run(repo):
    while True:
        cur = git_core.branch(repo)
        items = [
            {"category": "ACTIONS"},
            {"icon": "🔀", "label": "전환",       "desc": "checkout",           "value": "checkout"},
            {"icon": "✨", "label": "새 브랜치",   "desc": "create",             "value": "create"},
            {"icon": "🔗", "label": "병합",       "desc": "merge into current", "value": "merge"},
            {"icon": "🗑 ", "label": "삭제",       "desc": "delete",             "value": "delete"},
            {"icon": "🏷 ", "label": "이름 변경",  "desc": "rename",             "value": "rename"},
        ]
        try:
            choice = ui.select_menu(f"Branch  ·  {cur}", items)
        except GoBack:
            return

        try:
            if choice == "checkout":
                _checkout(repo)
            elif choice == "create":
                n = ui.text_input("새 브랜치 이름")
                if n:
                    git_core.run(["checkout", "-b", n], repo, capture=False)
                    ui.pause()
            elif choice == "merge":
                _merge(repo, cur)
            elif choice == "delete":
                _delete(repo, cur)
            elif choice == "rename":
                n = ui.text_input("새 이름")
                if n:
                    git_core.run(["branch", "-m", n], repo, capture=False)
                    ui.pause()
        except GoBack:
            continue


def _branches(repo):
    r = git_core.run(["branch", "--format=%(refname:short)"], repo)
    return [b for b in r.stdout.splitlines() if b]


def _checkout(repo):
    branches = _branches(repo)
    items = [{"icon": "🌿", "label": b, "value": b} for b in branches]
    choice = ui.select_menu("Switch branch", items)
    git_core.run(["checkout", choice], repo, capture=False)
    ui.pause()


def _merge(repo, cur):
    branches = [b for b in _branches(repo) if b != cur]
    if not branches:
        ui.warn("병합 가능한 브랜치 없음")
        ui.pause()
        return
    items = [{"icon": "🔗", "label": b, "value": b} for b in branches]
    choice = ui.select_menu(f"Merge into {cur}", items)
    if ui.confirm(f"'{choice}' → '{cur}' 병합?", True):
        git_core.run(["merge", choice], repo, capture=False)
        ui.pause()


def _delete(repo, cur):
    branches = [b for b in _branches(repo) if b != cur]
    if not branches:
        ui.warn("삭제할 브랜치 없음")
        ui.pause()
        return
    items = [{"icon": "🗑 ", "label": b, "value": b} for b in branches]
    choice = ui.select_menu("Delete branch", items)
    if ui.confirm(f"'{choice}' 정말 삭제?", False):
        git_core.run(["branch", "-D", choice], repo, capture=False)
        ui.pause()
