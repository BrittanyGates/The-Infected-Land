#!/usr/bin/python3
"""
Title: The Infected Land
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (www.linkedin.com/in/brittanycgates)
About: A text-based RPG game featuring a HERO sent to an infected land controlled by the VILLAIN featuring evil beasts, non-beasts, and humans.
"""
import sys
from clear_screen import clear_screen
from sleep_print import sleep_print
from story_introduction import story_intro


def game_menu() -> None:
    """
    This function displays the game menu, and allows the player to either quit the game or start a new game.
    :return: None
    """
    print("-" * 60)
    print("THE INFECTED LAND".center(55))
    print("-" * 60)
    print("0 - Quit Game".center(55))
    print("1 - New Game".center(55))

    try:
        menu_choice: int = int(input("\nEnter your choice here: "))
        if menu_choice == 0:
            print()
            print("*" * 60)
            print("!! You quit the game !!".center(55))
            print("*" * 60)
            print()
            sys.exit()
        elif menu_choice == 1:
            story_intro()
        else:
            print()
            print("*" * 60)
            print("!! Enter either 0 or 1 !!".center(55))
            print()
            print(" -- The game menu will reappear in a few seconds -- ".center(55))
            print("*" * 60)
            sleep_print()
            clear_screen()
            game_menu()
    except ValueError:
        print()
        print("*" * 60)
        print("!! This menu only accepts numbers !!".center(55))
        print()
        print("-- The game menu will reappear in a few seconds --".center(55))
        print("*" * 60)
        sleep_print()
        clear_screen()
        game_menu()
    except (EOFError, KeyboardInterrupt):
        print()
        print()
        print("*" * 60)
        print(" -- Interrupt signal received --".center(55))
        print("*" * 60)
        print()


if __name__ == "__main__":
    game_menu()
