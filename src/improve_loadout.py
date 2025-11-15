#!/usr/bin/python3
"""This module upgrades the Hero's sword or armor."""
from console import console, notification
from game_constants import *
from text_display_tools import clear_screen, sleep_print, storyline_formatter


def improve_loadout(hero) -> None:
    """Allows the player to choose either a stronger sword or better armor.    
    :return: None 
    """
    lines: list = [
        "Another resident steps forward to speak:",
        "\"I brought you a sword I had in my house.\"",
        "\"It's quite flexible with a super sharp edge.\"",
        "A different resident steps forward to speak:",
        "\"I brought you some armor I found long ago.\"",
        "\"It's resistant to impact, but won't weigh you down.\"",
        f"{hero.name}, choose either the (S) Sword or the (A) Armor.",
    ]

    storyline_formatter(lines)

    while True:
        user_input = input("Enter your choice here: ").capitalize()
        sword_lines: list = [
            f"{hero.name} takes the sword from the resident.",
            "Immediately their old sword disappears from its scabbard!",
            f"{hero.name} inserts the new sword into the scabbard.",
        ]
        armor_lines: list = [
            f"{hero.name} takes the armor from the resident.",
            "Suddenly, the armor fuses onto the hero's body!",
        ]
        armor_upgrade_lines: list = [
            f"== {hero.armor_type} adds 5 additional points of defense ==",
            f"The total armor defense points is now {hero.armor_defense}.",
        ]

        if user_input == "S":
            storyline_formatter(sword_lines)
            if hero.weapon_type == "Long Sword":
                hero.weapon_type = "Great Sword"
                hero.weapon_damage = GREAT_SWORD
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
            elif hero.weapon_type == "Great Sword":
                hero.weapon_type = "Mighty Sword"
                hero.weapon_damage = MIGHTY_SWORD
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
            else:
                hero.weapon_type = "Long Sword"
                hero.weapon_damage = LONG_SWORD
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
            break
        elif user_input == "A":
            storyline_formatter(armor_lines)
            if hero.armor_type == "Upgraded Armor":
                hero.armor_type = "Improved Armor"
                hero.armor_defense = IMPROVED_ARMOR
                storyline_formatter(armor_upgrade_lines)
                clear_screen()
            elif hero.armor_type == "Improved Armor":
                hero.armor_type = "Enhanced Armor"
                hero.armor_defense = ENHANCED_ARMOR
                storyline_formatter(armor_upgrade_lines)
                clear_screen()
            else:
                hero.armor_type = "Upgraded Armor"
                hero.armor_defense = UPGRADED_ARMOR
                storyline_formatter(armor_upgrade_lines)
                clear_screen()
            break
        else:
            console.print()
            console.print("!! Incorrect input !!", style=notification, justify="center")
            sleep_print()
            clear_screen()
            continue
