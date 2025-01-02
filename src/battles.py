#!/usr/bin/python3
"""This module runs each battle in the game."""
from console import console
from text_display_tools import attack_sleep_print, clear_screen
from villain import Villain, random_beast, random_human, random_non_beast, main_villain


def beast_battle() -> None:
    """Starts the beast battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    console.print(f"Suddenly a {random_beast.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_beast)
    attack_sleep_print()
    console.print()
    Villain.beast_attack_hero(random_beast)
    console.print()


def human_battle() -> None:
    """Starts the human battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    console.print(f"Suddenly a {random_human.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_human)
    attack_sleep_print()
    console.print()
    Villain.human_attack_hero(random_human)
    console.print()


def non_beast_battle() -> None:
    """Starts the non-beast battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    console.print(f"Suddenly a {random_non_beast.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_non_beast)
    attack_sleep_print()
    console.print()
    Villain.non_beast_attack_hero(random_non_beast)
    console.print()


def villain_battle() -> None:
    """Starts the Main Villain battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    console.print(f"The {main_villain.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(main_villain)
    attack_sleep_print()
    console.print()
    Villain.main_villain_attack_hero(main_villain)
    console.print()
