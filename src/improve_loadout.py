#!/usr/bin/python3
from clear_screen import clear_screen
from sleep_print import sleep_print


def improve_loadout() -> None:
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print("Another resident steps forward to speak:".center(55))
    print()
    sleep_print()
    print("\"I brought you a sword I had in my house.\"".center(55))
    print()
    sleep_print()
    print("\"It's quite flexible with a super sharp edge.\"".center(55))
    print()
    sleep_print()
    print("A different resident steps forward to speak:".center(55))
    print()
    sleep_print()
    print("\"I brought you some armor I found long ago.\"".center(55))
    print()
    sleep_print()
    print("\"It's resistant to impact, but won't weigh you down.\"".center(55))
    print()
    print("*" * 60)
    print(f"{hero.name}, choose either the (S) Sword or the (A) Armor.".center(55))
    print("*" * 60)
    print()
    user_input = input("Enter your choice here: ").capitalize()
    try:
        if user_input == "S":
            print()
            print(f"{hero.name} takes the sword from the resident.".center(55))
            print()
            sleep_print()
            print("Immediately their old sword disappears from its scabbard!".center(55))
            print()
            sleep_print()
            print(f"{hero.name} inserts the new sword into the scabbard.".center(55))
            print()
            sleep_print()
            if hero.weapon_type == "Long Sword":
                hero.weapon_type = "Great Sword"
                hero.weapon_damage += 5
                print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==".center(55))
                sleep_print()
                clear_screen()
            elif hero.weapon_type == "Great Sword":
                hero.weapon_type = "Mighty Sword"
                hero.weapon_damage += 5
                print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==".center(55))
                sleep_print()
                clear_screen()
            else:
                hero.weapon_type = "Long Sword"
                hero.weapon_damage += 5
                print(f"== {hero.weapon_type} deals {hero.weapon_damage} points of damage per swing ==".center(55))
                sleep_print()
                clear_screen()
        elif user_input == "A":
            print()
            print(f"{hero.name} takes the armor from the resident.".center(55))
            print()
            sleep_print()
            print("Suddenly, the armor fuses onto the hero's body!".center(55))
            print()
            sleep_print()
            if hero.armor_type == "Upgraded Armor":
                hero.armor_type = "Improved Armor"
                hero.armor_defense += 5
                print(f"== {hero.armor_type} adds 5 additional points of defense ==".center(55))
                print()
                print(f"The total armor defense points is now {hero.armor_defense}.".center(55))
                sleep_print()
                clear_screen()
            elif hero.armor_type == "Improved Armor":
                hero.armor_type = "Enhanced Armor"
                hero.armor_defense += 5
                print(f"== {hero.armor_type} adds 5 additional points of defense ==".center(55))
                print()
                print(f"The total armor defense points is now {hero.armor_defense}.".center(55))
                sleep_print()
                clear_screen()
            else:
                hero.armor_type = "Upgraded Armor"
                hero.armor_defense += 5
                print(f"== {hero.armor_type} adds 10 additional points of defense ==".center(55))
                print()
                print(f"The total armor defense points is now {hero.armor_defense}.".center(55))
                sleep_print()
                clear_screen()
        else:
            print()
            print("*" * 60)
            print("!! Incorrect input !!".center(55))
            print("*" * 60)
            sleep_print()
            clear_screen()
            improve_loadout()
    except ValueError:
        print()
        print("*" * 60)
        print("!! The name can only contain letters !!".center(55))
        print("*" * 60)
        print()
        sleep_print()
        clear_screen()
        improve_loadout()
