#!/usr/bin/python3
"""This module modifies the way the text displays in the game."""
from time import sleep
import os


def attack_sleep_print() -> None:
    """Introduces a three-second pause in between printing battle result information.
    :return: None
    """
    sleep(3)


def clear_screen() -> None:
    """Clears the terminal screen using the operating system-specific command.
    :return: None
    """
    os.system("cls" if os.name == "nt" else "clear")


def sleep_print() -> None:
    """introduces a four-second pause in between printing story lines.
    :return: None
    """
    sleep(4)
