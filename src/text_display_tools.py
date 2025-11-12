#!/usr/bin/python3
"""This module modifies the way the text displays in the program."""
from console import console
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


def storyline_formatter(storyline: list[str]) -> None:
    """Formats the game's storyline.
    :return: None
    """
    for line in storyline:
        console.print()
        sleep_print()
        console.print(line, justify="center")