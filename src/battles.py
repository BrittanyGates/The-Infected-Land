#!/usr/bin/python3
from text_display_tools import *
from villain import *


def beast_battle() -> None:
    """Starts the beast battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    print(center_text(f"Suddenly a {random_beast.name} attacks {hero.name}!"))
    attack_sleep_print()
    clear_screen()
    print()
    print(center_text("!! THE BATTLE BEGINS !!"))
    print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_beast)
    attack_sleep_print()
    print()
    Villain.beast_attack_hero(random_beast)
    print()


def human_battle() -> None:
    """Starts the human battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    print(center_text(f"Suddenly a {random_human.name} attacks {hero.name}!"))
    attack_sleep_print()
    clear_screen()
    print()
    print(center_text("!! THE BATTLE BEGINS !!"))
    print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_human)
    attack_sleep_print()
    print()
    Villain.human_attack_hero(random_human)
    print()


def non_beast_battle() -> None:
    """Starts the non-beast battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    print(center_text(f"Suddenly a {random_non_beast.name} attacks {hero.name}!"))
    attack_sleep_print()
    clear_screen()
    print()
    print(center_text("!! THE BATTLE BEGINS !!"))
    print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(random_non_beast)
    attack_sleep_print()
    print()
    Villain.non_beast_attack_hero(random_non_beast)
    print()


def villain_battle() -> None:
    """Starts the Main Villain battle.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    print(center_text(f"The {main_villain.name} attacks {hero.name}!"))
    attack_sleep_print()
    clear_screen()
    print()
    print(center_text("!! THE BATTLE BEGINS !!"))
    print()
    attack_sleep_print()
    hero.display_hero_vitals()
    Villain.display_villain_vitals(main_villain)
    attack_sleep_print()
    print()
    Villain.main_villain_attack_hero(main_villain)
    print()
