#!/usr/bin/python3
from text_display_tools import *


def improve_loadout() -> None:
    """Allows the player to choose either a stronger sword or better armor.    
    :return: None 
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print(center_text("Another resident steps forward to speak:"))
    print()
    sleep_print()
    print(center_text("\"I brought you a sword I had in my house.\""))
    print()
    sleep_print()
    print(center_text("\"It's quite flexible with a super sharp edge.\""))
    print()
    sleep_print()
    print(center_text("A different resident steps forward to speak:"))
    print()
    sleep_print()
    print(center_text("\"I brought you some armor I found long ago.\""))
    print()
    sleep_print()
    print(center_text("\"It's resistant to impact, but won't weigh you down.\""))
    print()
    print(center_text("*" * 80))
    print(center_text(f"{hero.name}, choose either the (S) Sword or the (A) Armor."))
    print(center_text("*" * 80))
    print()
    user_input = input("Enter your choice here: ").capitalize()
    try:
        if user_input == "S":
            print()
            print(center_text(f"{hero.name} takes the sword from the resident."))
            print()
            sleep_print()
            print(center_text("Immediately their old sword disappears from its scabbard!"))
            print()
            sleep_print()
            print(center_text(f"{hero.name} inserts the new sword into the scabbard."))
            print()
            sleep_print()
            if hero.weapon_type == "Long Sword":
                hero.weapon_type = "Great Sword"
                hero.weapon_damage += 5
                print(center_text(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing =="))
                sleep_print()
                clear_screen()
            elif hero.weapon_type == "Great Sword":
                hero.weapon_type = "Mighty Sword"
                hero.weapon_damage += 5
                print(center_text(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing =="))
                sleep_print()
                clear_screen()
            else:
                hero.weapon_type = "Long Sword"
                hero.weapon_damage += 5
                print(center_text(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing =="))
                sleep_print()
                clear_screen()
        elif user_input == "A":
            print()
            print(center_text(f"{hero.name} takes the armor from the resident."))
            print()
            sleep_print()
            print(center_text("Suddenly, the armor fuses onto the hero's body!"))
            print()
            sleep_print()
            if hero.armor_type == "Upgraded Armor":
                hero.armor_type = "Improved Armor"
                hero.armor_defense += 5
                print(center_text(f"== {hero.armor_type} adds 5 additional points of defense =="))
                print()
                print(center_text(f"The total armor defense points is now {hero.armor_defense}."))
                sleep_print()
                clear_screen()
            elif hero.armor_type == "Improved Armor":
                hero.armor_type = "Enhanced Armor"
                hero.armor_defense += 5
                print(center_text(f"== {hero.armor_type} adds 5 additional points of defense =="))
                print()
                print(center_text(f"The total armor defense points is now {hero.armor_defense}."))
                sleep_print()
                clear_screen()
            else:
                hero.armor_type = "Upgraded Armor"
                hero.armor_defense += 5
                print(center_text(f"== {hero.armor_type} adds 10 additional points of defense =="))
                print()
                print(center_text(f"The total armor defense points is now {hero.armor_defense}."))
                sleep_print()
                clear_screen()
        else:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Incorrect input !!"))
            print(center_text("*" * 80))
            sleep_print()
            clear_screen()
            improve_loadout()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! The name can only contain letters !!"))
        print(center_text("*" * 80))
        print()
        sleep_print()
        clear_screen()
        improve_loadout()
