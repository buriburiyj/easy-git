# -*- coding: utf-8 -*-
"""📜 커밋 기록"""
from ... import ui, git_core
from ..ui import C


def run(repo):
    ui.header("History")
    r = git_core.run(
        ["log", "--oneline", "--graph", "--decorate", "--all", "-30", "--color=always"],
        repo,
    )
    for line in r.stdout.splitlines():
        print(f"  {line}")
    ui.pause()
