#!/usr/bin/python3
from clear_screen import clear_screen
from sleep_print import sleep_print
from villain import *


def non_beast_battle() -> None:
    """
    This function starts the non-beast battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    # Randomly pick the beast for the battle
    print(f"Suddenly a {random_non_beast.name} attacks {hero.name}!".center(55))
    attack_sleep_print()
    clear_screen()
    print("!! THE BATTLE BEGINS !!".center(55))
    print()
    attack_sleep_print()
    # Display the vitals at the start of the battle.
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_non_beast)
    attack_sleep_print()
    print()
    # The non-beast attacks first
    Villain.non_beast_attack_hero(random_non_beast)
    print()
