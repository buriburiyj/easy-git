# -*- coding: utf-8 -*-
"""Git 명령 래퍼"""
import os
import subprocess


def run(args, cwd, capture=True):
    if capture:
        return subprocess.run(
            ["git"] + args, cwd=cwd, capture_output=True,
            text=True, encoding="utf-8", errors="replace",
        )
    return subprocess.run(["git"] + args, cwd=cwd)


def is_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))


def branch(repo):
    r = run(["branch", "--show-current"], repo)
    return r.stdout.strip() or "(detached)"


def remote_url(repo):
    r = run(["remote", "get-url", "origin"], repo)
    return r.stdout.strip() if r.returncode == 0 else None


STATUS_MAP = {
    "M": ("M", "수정", "\033[93m"),
    "A": ("A", "추가", "\033[92m"),
    "D": ("D", "삭제", "\033[91m"),
    "R": ("R", "이름변경", "\033[94m"),
    "C": ("C", "복사", "\033[94m"),
    "U": ("U", "충돌", "\033[91m"),
    "??": ("?", "새파일", "\033[95m"),
}


def changed_files(repo):
    r = run(["status", "--porcelain"], repo)
    if r.returncode != 0:
        return []
    files = []
    for line in r.stdout.splitlines():
        if len(line) < 3:
            continue
        st = line[:2].strip()
        name = line[3:].strip().strip('"')
        if " -> " in name:
            name = name.split(" -> ")[1]
        code, label, color = STATUS_MAP.get(st, ("?", "변경", "\033[90m"))
        size = ""
        full = os.path.join(repo, name)
        if os.path.isfile(full):
            try:
                size = fmt_size(os.path.getsize(full))
            except Exception:
                pass
        files.append({
            "status": st, "code": code, "label": label,
            "color": color, "name": name, "size": size,
        })
    return files


def fmt_size(n):
    for u in ("B", "K", "M", "G"):
        if n < 1024:
            return f"{n:.0f}{u}" if u == "B" else f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.1f}T"


def unpushed_count(repo):
    r = run(["log", "@{u}..HEAD", "--oneline"], repo)
    if r.returncode != 0:
        return 0
    return len([l for l in r.stdout.splitlines() if l.strip()])


def has_upstream(repo):
    r = run(["rev-parse", "--abbrev-ref", "@{u}"], repo)
    return r.returncode == 0
