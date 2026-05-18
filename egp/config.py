# -*- coding: utf-8 -*-
"""설정 파일 관리"""
import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".easy_git_config.json"


def load():
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save(cfg):
    try:
        CONFIG_PATH.write_text(
            json.dumps(cfg, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except Exception:
        pass


def add_recent_repo(path):
    cfg = load()
    recent = cfg.get("recent_repos", [])
    if path in recent:
        recent.remove(path)
    recent.insert(0, path)
    cfg["recent_repos"] = recent[:8]
    save(cfg)


def get_recent_repos():
    return load().get("recent_repos", [])
