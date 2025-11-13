#!/usr/bin/python3
"""This module runs each battle in the game."""
from after_battle_storylines import after_beast_battle_story, after_human_battle_story, after_non_beast_battle_story
from console import console
from text_display_tools import attack_sleep_print, clear_screen
from the_ending import the_ending


def beast_battle(hero, beast) -> None:
    """Starts the beast battle.
    :return: None
    """
    console.print()
    console.print(f"Suddenly a {beast.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()

    while hero.health > 0 and beast.health > 0:
        attack_sleep_print()
        hero.display_hero_vitals()
        beast.display_villain_vitals()
        attack_sleep_print()
        console.print()
        beast.attack_hero(hero)
        console.print()
        hero.attack_villain(beast)
        if beast.health <= 0:
            after_beast_battle_story(hero)
            break


def human_battle(hero, human) -> None:
    """Starts the human battle.
    :return: None
    """
    console.print()
    console.print(f"Suddenly a {human.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()

    while hero.health > 0 and human.health > 0:
        attack_sleep_print()
        hero.display_hero_vitals()
        human.display_villain_vitals()
        attack_sleep_print()
        console.print()
        human.attack_hero(hero)
        console.print()
        hero.attack_villain(human)
        if human.health <= 0:
            after_human_battle_story(hero)
            break


def non_beast_battle(hero, non_beast) -> None:
    """Starts the non-beast battle.
    :return: None
    """
    console.print()
    console.print(f"Suddenly a {non_beast.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()

    while hero.health > 0 and non_beast.health > 0:
        attack_sleep_print()
        hero.display_hero_vitals()
        non_beast.display_villain_vitals()
        attack_sleep_print()
        console.print()
        non_beast.attack_hero(hero)
        console.print()
        hero.attack_villain(non_beast)
        if non_beast.health <= 0:
            after_non_beast_battle_story(hero)
            break


def villain_battle(hero, final_villain) -> None:
    """Starts the Main Villain battle.
    :return: None
    """
    console.print()
    console.print(f"The {final_villain.name} attacks {hero.name}!", justify="center")
    attack_sleep_print()
    clear_screen()
    console.print()
    console.print("!! THE BATTLE BEGINS !!", justify="center")
    console.print()

    while hero.health > 0 and final_villain.health > 0:
        attack_sleep_print()
        hero.display_hero_vitals()
        final_villain.display_villain_vitals()
        attack_sleep_print()
        console.print()
        final_villain.attack_hero(hero)
        console.print()
        hero.attack_villain(final_villain)
        if final_villain.health <= 0:
            the_ending(hero, final_villain)
            break
