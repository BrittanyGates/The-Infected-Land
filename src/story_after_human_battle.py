#!/usr/bin/python3
from improve_loadout import improve_loadout
from regain_health import regain_health
from sleep_print import sleep_print
from villain_battle import villain_battle


def after_human_battle_story() -> None:
    """
    This function displays the game's storyline after the hero defeats the human.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print("After the battle the other humans fade away.".center(55))
    print()
    sleep_print()
    print("However, the land doesn't heal as before.".center(55))
    print()
    sleep_print()
    print(f"{hero.name} appears puzzled.".center(55))
    regain_health()
    improve_loadout()
    print()
    sleep_print()
    print("A tall column of flames appears in the middle of the land.".center(55))
    print()
    sleep_print()
    print("The hero retakes their battle stance, ready to fight again.".center(55))
    print()
    sleep_print()
    print("The flames disappear and a man wearing deep red tunic appears.".center(55))
    print()
    sleep_print()
    print(f"\"Hello, {hero.name}. Oh yes, I know your name.\"".center(55))
    print()
    sleep_print()
    print(f"\"I also know who you are, and what you are.\"".center(55))
    print()
    sleep_print()
    print(f"\"You are...special. I think you already know that.\"".center(55))
    print()
    sleep_print()
    print(f"\"That's why you were able to defeat all my creations.\"".center(55))
    print()
    sleep_print()
    print(f"\"But you aren't as special as me.\"".center(55))
    print()
    sleep_print()
    print(f"\"I will show the person who sent you here that now!\"".center(55))
    villain_battle()
