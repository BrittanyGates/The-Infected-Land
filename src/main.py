#!/usr/bin/env python3
"""The Infected Land
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://www.linkedin.com/in/brittanycgates) | (https://brittbot.com/)
About: A text-based RPG game featuring a HERO sent to an infected land controlled by the VILLAIN featuring evil beasts, non-beasts, and humans.
"""
from story_introduction import story_intro
from text_display_tools import *
import sys


def game_menu() -> None:
    """Displays the game menu.
    :return: None
    """
    print(center_text("-" * 80))
    print(center_text("THE INFECTED LAND"))
    print(center_text("-" * 80))
    print(center_text("0 - Quit Game"))
    print(center_text("1 - New Game"))

    try:
        menu_choice: int = int(input("\nEnter your choice here: "))
        if menu_choice == 0:
            print()
            print(center_text("*" * 80))
            print(center_text("!! You quit the game !!"))
            print(center_text("*" * 80))
            print()
            sys.exit()
        elif menu_choice == 1:
            story_intro()
        else:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Enter either 0 or 1 !!"))
            print()
            print(center_text(" -- The game menu will reappear in a few seconds -- "))
            print(center_text("*" * 80))
            sleep_print()
            clear_screen()
            game_menu()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! This menu only accepts numbers !!"))
        print()
        print(center_text("-- The game menu will reappear in a few seconds --"))
        print(center_text("*" * 80))
        sleep_print()
        clear_screen()
        game_menu()
    except (EOFError, KeyboardInterrupt):
        print()
        print()
        print(center_text("*" * 80))
        print(center_text(" -- Interrupt signal received --"))
        print(center_text("*" * 80))
        print()


if __name__ == "__main__":
    game_menu()
