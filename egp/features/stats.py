# -*- coding: utf-8 -*-
"""📊 통계"""
from ... import ui, git_core
from ..ui import C


def run(repo):
    r = git_core.run(["rev-list", "--count", "HEAD"], repo)
    total = r.stdout.strip() or "0"

    r = git_core.run(["shortlog", "-sn", "--all"], repo)
    contributors = []
    for line in r.stdout.strip().splitlines():
        parts = line.strip().split("\t", 1)
        if len(parts) == 2:
            contributors.append((int(parts[0]), parts[1]))

    r = git_core.run(["ls-files"], repo)
    file_count = len(r.stdout.strip().splitlines())

    ui.header("Stats")
    print()
    print(f"       {C.B}{C.CYAN}{total:>5}{C.R}             {C.B}{C.GREEN}{file_count:>5}{C.R}             {C.B}{C.PURPLE}{len(contributors):>5}{C.R}")
    print(f"       {C.GRAY}commits{C.R}             {C.GRAY}files{C.R}             {C.GRAY}authors{C.R}")
    print()
    print()

    print(f"  {C.GRAY}CONTRIBUTORS{C.R}")
    print()
    if contributors:
        max_cnt = max(c[0] for c in contributors)
        for cnt, name in contributors[:10]:
            bar_len = int((cnt / max_cnt) * 25)
            bar = "█" * bar_len
            print(f"  {C.B}{name:<12}{C.R} {C.CYAN}{bar}{C.R}{' ' * (28 - bar_len)} {C.GRAY}{cnt}{C.R}")
    print()
    print()

    # 최근 30일 활동
    r = git_core.run(
        ["log", "--pretty=format:%cd", "--date=short", "--since=30.days.ago"],
        repo
    )
    days = r.stdout.strip().splitlines()
    if days:
        from collections import Counter
        counts = Counter(days)
        max_c = max(counts.values()) if counts else 1
        blocks = " ▁▂▃▄▅▆▇█"

        print(f"  {C.GRAY}ACTIVITY     last 30 days{C.R}")
        print()
        # 날짜 정렬해서 sparkline
        sorted_dates = sorted(counts.keys())[-30:]
        spark = ""
        for d in sorted_dates:
            level = min(int((counts[d] / max_c) * 8), 8)
            spark += blocks[level]
        print(f"  {C.CYAN}{spark}{C.R}")
        print()

    ui.pause()
