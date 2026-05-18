# -*- coding: utf-8 -*-
"""키보드 입력 (macOS 터미널)"""
import sys
import tty
import termios

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
ENTER = "ENTER"
SPACE = "SPACE"
ESC = "ESC"
TAB = "TAB"
BACKSPACE = "BACKSPACE"
QUIT = "QUIT"


def read_key():
    """단일 키 입력 받기"""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)

        if ch == "\x1b":
            try:
                ch2 = sys.stdin.read(1)
                if ch2 == "[":
                    ch3 = sys.stdin.read(1)
                    return {
                        "A": UP, "B": DOWN, "C": RIGHT, "D": LEFT,
                    }.get(ch3, ESC)
                return ESC
            except Exception:
                return ESC

        if ch in ("\r", "\n"):
            return ENTER
        if ch == " ":
            return SPACE
        if ch == "\t":
            return TAB
        if ch in ("\x7f", "\b"):
            return BACKSPACE
        if ch == "\x03":
            raise KeyboardInterrupt
        if ch.lower() == "q":
            return QUIT

        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
