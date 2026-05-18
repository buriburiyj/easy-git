# -*- coding: utf-8 -*-
"""🔗 원격 저장소"""
from .. import ui, git_core
from ..ui import C, GoBack


def run(repo):
    while True:
        r = git_core.run(["remote", "-v"], repo)
        ui.header("Remote")

        if r.stdout.strip():
            print(f"  {C.GRAY}CURRENT{C.R}")
            print()
            for line in r.stdout.splitlines():
                print(f"  {C.GREEN}●{C.R}   {line}")
            print()
            print()
        else:
            ui.warn("설정된 원격 저장소가 없습니다")
            print()

        items = [
            {"category": "ACTIONS"},
            {"icon": "➕", "label": "origin 추가",   "desc": "add remote",   "value": "add"},
            {"icon": "🔄", "label": "URL 변경",      "desc": "change url",   "value": "change"},
            {"icon": "❌", "label": "remote 삭제",   "desc": "remove",       "value": "remove"},
        ]

        try:
            # 메뉴를 다시 그려야 하므로 별도 호출
            choice = ui.select_menu("Remote", items)
        except GoBack:
            return

        try:
            if choice == "add":
                url = ui.text_input("저장소 URL (https:// 또는 git@)")
                if url:
                    git_core.run(["remote", "add", "origin", url], repo, capture=False)
                    ui.success("추가됨")
                    ui.pause()
            elif choice == "change":
                url = ui.text_input("새 URL")
                if url:
                    git_core.run(["remote", "set-url", "origin", url], repo, capture=False)
                    ui.success("변경됨")
                    ui.pause()
            elif choice == "remove":
                n = ui.text_input("삭제할 remote 이름", "origin")
                if n and ui.confirm(f"'{n}' 삭제?", False):
                    git_core.run(["remote", "remove", n], repo, capture=False)
                    ui.success("삭제됨")
                    ui.pause()
        except GoBack:
            continue
