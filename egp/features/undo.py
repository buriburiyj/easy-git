# -*- coding: utf-8 -*-
"""↩ 되돌리기"""
from ... import ui, git_core
from ..ui import C, GoBack


def run(repo):
    items = [
        {"icon": "📌", "label": "마지막 커밋 취소",     "desc": "keep changes",     "value": "soft"},
        {"icon": "💥", "label": "마지막 커밋 삭제",     "desc": "discard all  ⚠",   "value": "hard"},
        {"icon": "📄", "label": "파일 변경 되돌리기",   "desc": "checkout files",   "value": "checkout"},
        {"icon": "✏ ", "label": "커밋 메시지 수정",     "desc": "amend message",    "value": "amend"},
    ]
    try:
        choice = ui.select_menu("Undo", items,
                                prompt=f"{C.YELLOW}⚠{C.R}  주의: 일부 작업은 되돌릴 수 없습니다")
    except GoBack:
        return

    if choice == "soft":
        if ui.confirm("마지막 커밋 취소? (변경사항 유지)", True):
            git_core.run(["reset", "--soft", "HEAD~1"], repo, capture=False)
            ui.success("커밋 취소됨")
            ui.pause()
    elif choice == "hard":
        if ui.confirm(f"{C.RED}정말 모든 변경을 삭제?{C.R}", False):
            if ui.confirm(f"{C.RED}한 번 더 확인합니다{C.R}", False):
                git_core.run(["reset", "--hard", "HEAD~1"], repo, capture=False)
                ui.success("완전 삭제 완료")
                ui.pause()
    elif choice == "checkout":
        files = git_core.changed_files(repo)
        if not files:
            ui.info("변경 파일 없음")
            ui.pause()
            return
        items_f = [{"label": f["name"], "value": f, "meta": f"{f['color']}{f['code']}{C.R}"}
                   for f in files]
        sel = ui.checklist("Revert files", items_f, prompt="되돌릴 파일을 선택하세요")
        for f in sel:
            git_core.run(["checkout", "--", f["name"]], repo)
            ui.success(f"되돌림: {f['name']}")
        ui.pause()
    elif choice == "amend":
        new = ui.text_input("새 커밋 메시지")
        if new:
            git_core.run(["commit", "--amend", "-m", new], repo, capture=False)
            ui.success("메시지 수정됨")
            ui.pause()
