#!/usr/bin/python3
from clear_screen import clear_screen
from sleep_print import sleep_print
from villain import *


def villain_battle() -> None:
    """
    This function starts the last battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    print(f"The {main_villain.name} attacks {hero.name}!".center(55))
    attack_sleep_print()
    clear_screen()
    print("!! THE BATTLE BEGINS !!".center(55))
    print()
    attack_sleep_print()
    # Display the vitals at the start of the battle.
    hero.display_hero_vitals()
    Villain.display_villain_vitals(main_villain)
    attack_sleep_print()
    print()
    # The main villain attacks first
    Villain.main_villain_attack_hero(main_villain)
    print()