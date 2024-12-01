#!/usr/bin/python3
import os


def clear_screen() -> None:
    """
    This function clears the terminal screen using the operating system-specific command.
    :return: None
    """
    os.system("cls" if os.name == "nt" else "clear")
