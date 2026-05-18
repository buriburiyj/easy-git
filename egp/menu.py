# -*- coding: utf-8 -*-
"""메인 메뉴 라우터"""
import os
import sys
from . import ui, git_core, config
from .ui import C, GoBack
from .features import (
    upload, diff_view, branch, stash, undo,
    log_view, remote, conflict, gitignore, stats, backup,
)


def select_repo():
    cwd = os.getcwd()
    recent = config.get_recent_repos()

    items = []
    if git_core.is_repo(cwd):
        items.append({
            "icon": "📁", "label": os.path.basename(cwd) or cwd,
            "desc": "current", "value": cwd
        })
    for r in recent:
        if r != cwd and git_core.is_repo(r):
            items.append({
                "icon": "📁", "label": os.path.basename(r),
                "desc": "recent", "value": r
            })

    if items:
        items.append(None)
    items.append({"icon": "✏ ", "label": "경로 직접 입력", "value": "__manual__"})
    items.append({"icon": "🚪", "label": "종료", "value": "__exit__"})

    try:
        choice = ui.select_menu("Select repository", items,
                                prompt="저장소를 선택하세요")
    except GoBack:
        sys.exit(0)

    if choice == "__exit__":
        sys.exit(0)
    if choice == "__manual__":
        return _manual_path()

    config.add_recent_repo(choice)
    return choice


def _manual_path():
    while True:
        try:
            p = ui.text_input("Git 폴더 경로")
        except GoBack:
            return select_repo()
        if not p:
            continue
        p = os.path.expanduser(p.strip().strip('"').strip("'"))
        if not os.path.isdir(p):
            ui.error("존재하지 않는 폴더")
            ui.pause()
            continue
        if not git_core.is_repo(p):
            ui.warn("Git 저장소가 아닙니다")
            try:
                if ui.confirm("git init 할까요?", False):
                    git_core.run(["init"], p)
                    ui.success("초기화 완료")
                    ui.pause()
                    config.add_recent_repo(p)
                    return p
            except GoBack:
                continue
            continue
        config.add_recent_repo(p)
        return p


def show_main_menu(repo):
    br = git_core.branch(repo)
    rem = git_core.remote_url(repo)
    files = git_core.changed_files(repo)
    unpushed = git_core.unpushed_count(repo)

    name = os.path.basename(repo)
    ui.header(name)

    ui.status_line("branch", f"{C.GREEN}{br}{C.R}")
    if rem:
        ui.status_line("remote", f"{C.CYAN}{ui.shorten(rem, 50)}{C.R}")
    else:
        ui.status_line("remote", f"{C.GRAY}(설정 안 됨){C.R}", C.YELLOW)
    ui.status_line(
        "status",
        f"{C.YELLOW}{len(files)} changed{C.R}   {C.GRAY}·{C.R}   {C.PURPLE}{unpushed} unpushed{C.R}",
    )
    print()
    print()

    items = [
        {"category": "WORKFLOW"},
        {"icon": "🚀", "label": "업로드",     "desc": "add · commit · push",    "value": "upload"},
        {"icon": "👀", "label": "미리보기",   "desc": "colored diff",           "value": "diff"},
        {"icon": "⬇ ", "label": "가져오기",   "desc": "pull from remote",       "value": "pull"},
        {"icon": "📜", "label": "커밋 기록",  "desc": "recent commits",         "value": "log"},
        None,
        {"category": "BRANCH"},
        {"icon": "🌿", "label": "브랜치",     "desc": "switch · merge · delete", "value": "branch"},
        {"icon": "📦", "label": "임시저장",   "desc": "stash",                  "value": "stash"},
        {"icon": "↩ ", "label": "되돌리기",   "desc": "reset · revert",         "value": "undo"},
        {"icon": "⚔ ", "label": "충돌 해결",  "desc": "merge conflict",         "value": "conflict"},
        None,
        {"category": "TOOLS"},
        {"icon": "🔗", "label": "원격 저장소", "desc": "configure remote",       "value": "remote"},
        {"icon": "🚫", "label": ".gitignore", "desc": "templates",              "value": "gitignore"},
        {"icon": "📊", "label": "통계",        "desc": "contributors",           "value": "stats"},
        {"icon": "💾", "label": "백업",        "desc": "zip archive",            "value": "backup"},
        None,
        {"icon": "🔄", "label": "저장소 변경", "value": "switch"},
        {"icon": "🚪", "label": "종료",        "value": "exit"},
    ]

    # 메뉴를 그릴 때는 header를 다시 부르지 않도록 별도 그리기
    return _draw_main_with_status(repo, items)


def _draw_main_with_status(repo, items):
    """상태 + 메뉴 통합 그리기"""
    from .ui import _draw_menu, hide_cursor, show_cursor, read_key
    import egp.keys as kmod

    selectable = [i for i, it in enumerate(items)
                  if it and "value" in it]
    idx = selectable[0]

    hide_cursor()
    try:
        while True:
            _draw_main_screen(repo, items, idx)
            k = read_key()
            if k == kmod.UP:
                pos = selectable.index(idx)
                idx = selectable[(pos - 1) % len(selectable)]
            elif k == kmod.DOWN:
                pos = selectable.index(idx)
                idx = selectable[(pos + 1) % len(selectable)]
            elif k == kmod.ENTER:
                return items[idx]["value"]
            elif k in (kmod.QUIT, kmod.ESC):
                raise GoBack()
            elif isinstance(k, str) and k.isdigit():
                n = int(k)
                if 1 <= n <= len(selectable):
                    return items[selectable[n - 1]]["value"]
    finally:
        show_cursor()


def _draw_main_screen(repo, items, idx):
    br = git_core.branch(repo)
    rem = git_core.remote_url(repo)
    files = git_core.changed_files(repo)
    unpushed = git_core.unpushed_count(repo)

    name = os.path.basename(repo)
    ui.header(name)

    ui.status_line("branch", f"{C.GREEN}{br}{C.R}")
    if rem:
        ui.status_line("remote", f"{C.CYAN}{ui.shorten(rem, 50)}{C.R}")
    else:
        ui.status_line("remote", f"{C.GRAY}(설정 안 됨){C.R}", C.YELLOW)
    ui.status_line(
        "status",
        f"{C.YELLOW}{len(files)} changed{C.R}   {C.GRAY}·{C.R}   {C.PURPLE}{unpushed} unpushed{C.R}",
    )
    print()
    print()

    from .ui import dwidth
    for i, it in enumerate(items):
        if it is None:
            print()
            continue
        if "category" in it:
            print(f"  {C.GRAY}{it['category']}{C.R}")
            print()
            continue

        is_sel = i == idx
        icon = it.get("icon", " ")
        label = it["label"]
        desc = it.get("desc", "")

        if is_sel:
            line = f"  {C.CYAN}→{C.R}  {icon}  {C.B}{C.CYAN}{label}{C.R}"
            if desc:
                pad = " " * max(2, 18 - dwidth(label))
                line += f"{pad}{C.CYAN}{desc}{C.R}"
        else:
            line = f"     {icon}  {label}"
            if desc:
                pad = " " * max(2, 18 - dwidth(label))
                line += f"{pad}{C.GRAY}{desc}{C.R}"
        print(line)

    ui.footer("↑↓  이동      ↵  선택      1-9  단축      q  종료")


ACTIONS = {
    "upload": upload.run,
    "diff": diff_view.run,
    "pull": lambda repo: _pull(repo),
    "log": log_view.run,
    "branch": branch.run,
    "stash": stash.run,
    "undo": undo.run,
    "conflict": conflict.run,
    "remote": remote.run,
    "gitignore": gitignore.run,
    "stats": stats.run,
    "backup": backup.run,
}


def _pull(repo):
    ui.header("Pull")
    print(f"  {C.B}git pull{C.R}")
    print()
    git_core.run(["pull"], repo, capture=False)
    ui.pause()


def run_app():
    repo = select_repo()
    while True:
        try:
            choice = show_main_menu(repo)
        except GoBack:
            try:
                if ui.confirm("정말 종료할까요?", True):
                    ui.goodbye()
                    return
            except GoBack:
                continue
            continue

        if choice == "exit":
            ui.goodbye()
            return
        if choice == "switch":
            repo = select_repo()
            continue

        action = ACTIONS.get(choice)
        if not action:
            continue

        try:
            action(repo)
        except GoBack:
            continue
