#!/usr/bin/env python3
"""The Infected Land
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: A text-based RPG game featuring a HERO sent to an infected land controlled by the VILLAIN featuring evil beasts,
non-beasts, and humans.
"""
from console import console, notification
from story_introduction import story_intro
from text_display_tools import clear_screen, sleep_print
import sys


def game_menu() -> None:
    """Displays the game menu.
    :return: None
    """
    while True:
        clear_screen()
        console.print()
        console.print("THE INFECTED LAND", justify="center")
        console.print()
        console.print("0 - Quit Game", justify="center")
        console.print("1 - New Game", justify="center")
        try:
            menu_choice: int = int(input("\nEnter your choice here: "))
        except ValueError:
            console.print()
            console.print("!! This menu only accepts numbers !!", style=notification, justify="center")
            console.print()
            sleep_print()
            continue
        except (EOFError, KeyboardInterrupt):
            console.print()
            console.print(" -- Interrupt signal received --", style=notification)
            console.print()
            sys.exit()
        else:
            if menu_choice == 0:
                console.print()
                console.print("!! You quit the game !!", style=notification, justify="center")
                console.print()
                sys.exit()
            elif menu_choice == 1:
                story_intro()
                break
            else:
                console.print()
                console.print("!! Enter either 0 or 1 !!", style=notification, justify="center")
                console.print()
                sleep_print()


if __name__ == "__main__":
    game_menu()
