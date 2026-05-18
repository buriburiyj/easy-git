# -*- coding: utf-8 -*-
"""👀 변경 미리보기"""
import os
from pathlib import Path
from .. import ui, git_core
from ..ui import C, GoBack


def run(repo):
    files = git_core.changed_files(repo)
    if not files:
        ui.header("Preview")
        ui.info("변경 파일 없음")
        ui.pause()
        return

    items = [{"icon": "📄", "label": f["name"],
              "desc": f["label"], "value": f} for f in files]
    items.append(None)
    items.append({"icon": "🔍", "label": "전체 보기", "value": "__all__"})

    choice = ui.select_menu("Preview", items, prompt="미리볼 파일을 선택하세요")
    targets = files if choice == "__all__" else [choice]

    ui.header("Preview")
    for f in targets:
        label = "new" if f["status"] == "??" else "modified"
        print(f"  {C.B}{f['name']}{C.R}{' ' * max(2, 40 - ui.dwidth(f['name']))}{C.GRAY}{label}{C.R}")
        print(f"  {C.GRAY}{'╶' * (ui.term_width() - 8)}{C.R}")
        print()

        if f["status"] == "??":
            try:
                content = Path(os.path.join(repo, f["name"])).read_text(
                    encoding="utf-8", errors="replace"
                )
                for line in content.splitlines()[:40]:
                    print(f"    {C.GREEN}+ {line}{C.R}")
                if len(content.splitlines()) > 40:
                    print(f"    {C.GRAY}... ({len(content.splitlines())-40}줄 생략){C.R}")
            except Exception:
                print(f"    {C.GRAY}(바이너리 파일){C.R}")
        else:
            r = git_core.run(["diff", "--", f["name"]], repo)
            for line in r.stdout.splitlines()[:60]:
                if line.startswith("+") and not line.startswith("+++"):
                    print(f"    {C.GREEN}{line}{C.R}")
                elif line.startswith("-") and not line.startswith("---"):
                    print(f"    {C.RED}{line}{C.R}")
                elif line.startswith("@@"):
                    print(f"    {C.CYAN}{line}{C.R}")
                else:
                    print(f"    {C.GRAY}{line}{C.R}")
        print()
        print()

    ui.pause()
