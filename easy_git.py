#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Easy Git - macOS 터미널용 Git 올인원 도구"""
import sys
from egp.menu import run_app
from egp.ui import goodbye, show_cursor

if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        show_cursor()
        goodbye()
        sys.exit(0)
    finally:
        show_cursor()
