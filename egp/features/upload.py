# -*- coding: utf-8 -*-
"""🚀 업로드 (add · commit · push)"""
from ... import ui, git_core
from ..ui import C, GoBack


TEMPLATES = [
    {"icon": "✨", "label": "feat",     "desc": "새 기능 추가",     "value": ("✨", "feat")},
    {"icon": "🐛", "label": "fix",      "desc": "버그 수정",        "value": ("🐛", "fix")},
    {"icon": "📝", "label": "docs",     "desc": "문서 업데이트",    "value": ("📝", "docs")},
    {"icon": "♻ ", "label": "refactor", "desc": "리팩토링",         "value": ("♻", "refactor")},
    {"icon": "🎨", "label": "style",    "desc": "코드 스타일",      "value": ("🎨", "style")},
    {"icon": "⚡", "label": "perf",     "desc": "성능 개선",        "value": ("⚡", "perf")},
    {"icon": "✅", "label": "test",     "desc": "테스트",           "value": ("✅", "test")},
    {"icon": "🔧", "label": "chore",    "desc": "설정 · 빌드",      "value": ("🔧", "chore")},
    None,
    {"icon": "✏ ", "label": "custom",   "desc": "직접 입력",        "value": None},
]


def run(repo):
    files = git_core.changed_files(repo)
    if not files:
        ui.header("Upload")
        ui.info("변경된 파일이 없습니다")
        ui.pause()
        return

    # 1) 파일 선택 (체크리스트)
    items = []
    for f in files:
        size = f"  {C.GRAY}{f['size']:>6}{C.R}" if f["size"] else f"  {C.GRAY}     —{C.R}"
        meta = f"{f['color']}{f['code']}{C.R}{size}"
        items.append({
            "label": f["name"],
            "value": f,
            "meta": meta,
        })

    selected = ui.checklist("Upload", items, prompt="업로드할 파일을 선택하세요")
    if not selected:
        ui.warn("선택된 파일이 없습니다")
        ui.pause()
        return

    # 2) 커밋 타입
    tpl = ui.select_menu("Commit type", TEMPLATES, prompt="커밋 타입을 선택하세요")

    if tpl is None:
        msg = ui.text_input("커밋 메시지", "변경 내용 업데이트")
    else:
        emo, key = tpl
        ui.header("Commit message")
        print(f"  {emo}  {C.B}{key}:{C.R}")
        print()
        extra = ui.text_input("상세 설명")
        msg = f"{emo} {key}: {extra}" if extra else f"{emo} {key}"

    # 3) push 여부
    push = ui.confirm(f"{len(selected)}개 파일을 커밋하고 push 합니다", True)

    # 4) 실행
    ui.header("Uploading")
    total = 3 if push else 2

    ui.step_now("add", f"{len(selected)} files")
    print()
    for f in selected:
        r = git_core.run(["add", "--", f["name"]], repo)
        if r.returncode != 0:
            ui.error(f"{f['name']}: {r.stderr.strip()}")
            ui.pause()
            return
    ui.header("Uploading")
    ui.step_done("add", f"{len(selected)} files staged")

    ui.step_now("commit", "")
    r = git_core.run(["commit", "-m", msg], repo)
    if r.returncode != 0:
        ui.error(r.stderr.strip() or r.stdout.strip())
        ui.pause()
        return

    # 커밋 해시 추출
    hash_r = git_core.run(["rev-parse", "--short", "HEAD"], repo)
    short_hash = hash_r.stdout.strip()

    ui.header("Uploading")
    ui.step_done("add", f"{len(selected)} files staged")
    ui.step_done("commit", f"{short_hash}   {msg}")

    if push:
        ui.step_now("push", "origin ...")
        print()
        if not git_core.has_upstream(repo):
            br = git_core.branch(repo)
            git_core.run(["push", "-u", "origin", br], repo, capture=False)
        else:
            git_core.run(["push"], repo, capture=False)

        ui.header("Done")
        ui.step_done("add", f"{len(selected)} files staged")
        ui.step_done("commit", f"{short_hash}   {msg}")
        ui.step_done("push", "origin")

    print()
    print(f"  {C.GREEN}🎉  업로드 완료{C.R}")
    ui.pause()
