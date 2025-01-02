#!/usr/bin/python3
"""This module upgrades the Hero's sword or armor."""
from console import console, notification
from text_display_tools import clear_screen, sleep_print


def improve_loadout() -> None:
    """Allows the player to choose either a stronger sword or better armor.    
    :return: None 
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    sleep_print()
    console.print("Another resident steps forward to speak:", justify="center")
    console.print()
    sleep_print()
    console.print("\"I brought you a sword I had in my house.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"It's quite flexible with a super sharp edge.\"", justify="center")
    console.print()
    sleep_print()
    console.print("A different resident steps forward to speak:", justify="center")
    console.print()
    sleep_print()
    console.print("\"I brought you some armor I found long ago.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"It's resistant to impact, but won't weigh you down.\"", justify="center")
    console.print()
    console.print(f"{hero.name}, choose either the (S) Sword or the (A) Armor.", justify="center")
    console.print()
    try:
        user_input = input("Enter your choice here: ").capitalize()
    except ValueError:
        console.print()
        console.print("!! The name can only contain letters !!", style=notification, justify="center")
        console.print()
        sleep_print()
        clear_screen()
        improve_loadout()
    else:
        if user_input == "S":
            console.print()
            console.print(f"{hero.name} takes the sword from the resident.", justify="center")
            console.print()
            sleep_print()
            console.print("Immediately their old sword disappears from its scabbard!", justify="center")
            console.print()
            sleep_print()
            console.print(f"{hero.name} inserts the new sword into the scabbard.", justify="center")
            console.print()
            sleep_print()
            if hero.weapon_type == "Long Sword":
                hero.weapon_type = "Great Sword"
                hero.weapon_damage += 5
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
            elif hero.weapon_type == "Great Sword":
                hero.weapon_type = "Mighty Sword"
                hero.weapon_damage += 5
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
            else:
                hero.weapon_type = "Long Sword"
                hero.weapon_damage += 5
                console.print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==", justify="center")
                sleep_print()
                clear_screen()
        elif user_input == "A":
            console.print()
            console.print(f"{hero.name} takes the armor from the resident.", justify="center")
            console.print()
            sleep_print()
            console.print("Suddenly, the armor fuses onto the hero's body!", justify="center")
            console.print()
            sleep_print()
            if hero.armor_type == "Upgraded Armor":
                hero.armor_type = "Improved Armor"
                hero.armor_defense += 5
                console.print(f"== {hero.armor_type} adds 5 additional points of defense ==", justify="center")
                console.print()
                console.print(f"The total armor defense points is now {hero.armor_defense}.", justify="center")
                sleep_print()
                clear_screen()
            elif hero.armor_type == "Improved Armor":
                hero.armor_type = "Enhanced Armor"
                hero.armor_defense += 5
                console.print(f"== {hero.armor_type} adds 5 additional points of defense ==", justify="center")
                console.print()
                console.print(f"The total armor defense points is now {hero.armor_defense}.", justify="center")
                sleep_print()
                clear_screen()
            else:
                hero.armor_type = "Upgraded Armor"
                hero.armor_defense += 5
                console.print(f"== {hero.armor_type} adds 10 additional points of defense ==", justify="center")
                console.print()
                console.print(f"The total armor defense points is now {hero.armor_defense}.", justify="center")
                sleep_print()
                clear_screen()
        else:
            console.print()
            console.print("!! Incorrect input !!", style=notification, justify="center")
            sleep_print()
            clear_screen()
            improve_loadout()
