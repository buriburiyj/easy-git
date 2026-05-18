# -*- coding: utf-8 -*-
"""UI 렌더링 - 미니멀 디자인"""
import os
import sys
import re
import shutil
import unicodedata
from . import keys as kmod
from .keys import read_key, hide_cursor, show_cursor


class C:
    R = "\033[0m"
    B = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"


class GoBack(Exception):
    """q/ESC로 메뉴 복귀"""
    pass


# ─────── 폭 계산 ───────
def term_width(default=72):
    try:
        return min(shutil.get_terminal_size().columns, 100)
    except Exception:
        return default


def strip_ansi(s):
    return re.sub(r"\033\[[0-9;]*m", "", s)


def dwidth(s):
    s = strip_ansi(s)
    w = 0
    for ch in s:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            w += 2
        elif ord(ch) > 0x1F300:
            w += 2
        else:
            w += 1
    return w


# ─────── 화면 제어 ───────
def clear():
    os.system("clear")


# ─────── 헤더 ───────
def header(subtitle=""):
    """모든 페이지 공통 상단"""
    clear()
    w = term_width()
    print()
    title = f"{C.CYAN}✦{C.R}  {C.B}Easy Git{C.R}"
    if subtitle:
        title += f"  {C.GRAY}·{C.R}  {C.GRAY}{subtitle}{C.R}"
    print(f"  {title}")
    print(f"  {C.GRAY}{'━' * (w - 4)}{C.R}")
    print()


def footer(hint=""):
    """하단 키 힌트"""
    w = term_width()
    print()
    print(f"  {C.GRAY}{'━' * (w - 4)}{C.R}")
    if hint:
        print(f"  {C.GRAY}{hint}{C.R}")
    print()


# ─────── 섹션 ───────
def section(label):
    """카테고리 헤더 (회색 대문자)"""
    print(f"  {C.GRAY}{label}{C.R}")
    print()


def divider():
    w = term_width()
    print(f"  {C.GRAY}{'╶' * (w - 4)}{C.R}")


# ─────── 상태 라인 ───────
def status_line(label, value, dot_color=C.GREEN):
    print(f"  {dot_color}●{C.R}  {C.B}{label:<10}{C.R} {value}")


# ─────── 메시지 ───────
def info(msg):
    print(f"  {C.BLUE}ℹ{C.R}  {msg}")


def success(msg):
    print(f"  {C.GREEN}✓{C.R}  {msg}")


def warn(msg):
    print(f"  {C.YELLOW}⚠{C.R}  {msg}")


def error(msg):
    print(f"  {C.RED}✗{C.R}  {msg}")


def step_done(label, detail=""):
    print(f"  {C.GREEN}✓{C.R}   {C.B}{label:<10}{C.R} {C.GRAY}{detail}{C.R}")


def step_now(label, detail=""):
    print(f"  {C.YELLOW}⠙{C.R}   {C.B}{label:<10}{C.R} {C.GRAY}{detail}{C.R}")


def pause(msg="↵  메뉴로 돌아가기"):
    print()
    print(f"  {C.GRAY}{msg}{C.R}")
    try:
        read_key()
    except KeyboardInterrupt:
        pass


# ─────── 헬퍼 ───────
def shorten(s, mx):
    if dwidth(s) <= mx:
        return s
    return "…" + s[-(mx - 1):]


# ─────── 메뉴 (단일 선택) ───────
def select_menu(subtitle, items, prompt=None):
    """
    화살표 키 선택 메뉴.
    items: [
        {"icon": "🚀", "label": "업로드", "desc": "...", "value": "upload"},
        None,  # 구분선
        {"category": "WORKFLOW"},  # 카테고리 헤더
        ...
    ]
    """
    selectable = [i for i, it in enumerate(items)
                  if it and "value" in it]
    if not selectable:
        raise GoBack()
    idx = selectable[0]

    hide_cursor()
    try:
        while True:
            _draw_menu(subtitle, items, idx, prompt)
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


def _draw_menu(subtitle, items, idx, prompt):
    header(subtitle)
    if prompt:
        print(f"  {prompt}")
        print()

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

    footer("↑↓  이동      ↵  선택      1-9  단축      q  뒤로")


# ─────── 체크리스트 (다중 선택) ───────
def checklist(subtitle, items, prompt=None):
    """
    items: [{"label": "...", "value": "...", "meta": "추가표시"}]
    """
    idx = 0
    checked = set()

    hide_cursor()
    try:
        while True:
            _draw_checklist(subtitle, items, idx, checked, prompt)
            k = read_key()
            if k == kmod.UP:
                idx = (idx - 1) % len(items)
            elif k == kmod.DOWN:
                idx = (idx + 1) % len(items)
            elif k == kmod.SPACE:
                if idx in checked:
                    checked.remove(idx)
                else:
                    checked.add(idx)
            elif isinstance(k, str) and k.lower() == "a":
                if len(checked) == len(items):
                    checked.clear()
                else:
                    checked = set(range(len(items)))
            elif k == kmod.ENTER:
                return [items[i]["value"] for i in sorted(checked)]
            elif k in (kmod.QUIT, kmod.ESC):
                raise GoBack()
    finally:
        show_cursor()


def _draw_checklist(subtitle, items, idx, checked, prompt):
    header(subtitle)
    if prompt:
        print(f"  {prompt}")
        print()

    for i, it in enumerate(items):
        is_sel = i == idx
        is_chk = i in checked
        box = f"{C.GREEN}●{C.R}" if is_chk else f"{C.GRAY}○{C.R}"
        arrow = f"{C.CYAN}→{C.R}" if is_sel else " "
        meta = it.get("meta", "")

        if is_sel:
            label_color = C.B + C.CYAN
        elif is_chk:
            label_color = C.WHITE
        else:
            label_color = C.GRAY

        print(f"  {arrow}  {box}   {label_color}{it['label']:<35}{C.R} {meta}")

    print()
    print(f"  {C.GRAY}{len(checked)} / {len(items)}  selected{C.R}")
    footer("space  토글     a  전체     ↵  다음     q  뒤로")


# ─────── 확인 다이얼로그 ───────
def confirm(prompt, default_yes=True):
    items = [
        {"label": "진행", "value": True},
        {"label": "취소", "value": False},
    ]
    idx = 0 if default_yes else 1

    hide_cursor()
    try:
        while True:
            _draw_confirm(prompt, items, idx)
            k = read_key()
            if k in (kmod.LEFT, kmod.UP):
                idx = (idx - 1) % 2
            elif k in (kmod.RIGHT, kmod.DOWN, kmod.TAB):
                idx = (idx + 1) % 2
            elif k == kmod.ENTER:
                return items[idx]["value"]
            elif k in (kmod.QUIT, kmod.ESC):
                raise GoBack()
            elif isinstance(k, str) and k.lower() == "y":
                return True
            elif isinstance(k, str) and k.lower() == "n":
                return False
    finally:
        show_cursor()


def _draw_confirm(prompt, items, idx):
    header("Confirm")
    print(f"  {prompt}")
    print()
    print()

    line = "      "
    for i, it in enumerate(items):
        if i == idx:
            btn = f"{C.CYAN}┌─────────────┐{C.R}\n      {C.CYAN}│{C.R}  {C.B}↵  {it['label']}{C.R}     {C.CYAN}│{C.R}\n      {C.CYAN}└─────────────┘{C.R}"
            print(btn)
        else:
            print(f"      {C.GRAY}    {it['label']}{C.R}")

    footer("← →  이동      ↵  선택      y / n")


# ─────── 텍스트 입력 ───────
def text_input(prompt, default=""):
    show_cursor()
    hint = f" {C.GRAY}[{default}]{C.R}" if default else ""
    try:
        val = input(f"  {C.CYAN}>{C.R}  {prompt}{hint}  {C.GRAY}(q=뒤로){C.R}: ").strip()
    except (EOFError, KeyboardInterrupt):
        raise GoBack()
    if val.lower() == "q":
        raise GoBack()
    return val if val else default


# ─────── 종료 ───────
def goodbye():
    w = term_width()
    print()
    print(f"  {C.GRAY}{'━' * (w - 4)}{C.R}")
    print()
    print(f"  {C.CYAN}✦{C.R}  {C.B}수고하셨습니다{C.R}")
    print(f"  {C.GRAY}Easy Git 을 사용해주셔서 감사합니다{C.R}")
    print()
    print(f"  {C.GRAY}{'━' * (w - 4)}{C.R}")
    print()
    show_cursor()
