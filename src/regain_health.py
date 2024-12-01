#!/usr/bin/python3
from clear_screen import clear_screen
from sleep_print import sleep_print
import random


def regain_health() -> int:
    """
    This function allows the player to choose a health potion to regain a range of health points (10 to 30).
    The total health points cannot exceed 100.
    :return: The function returns an int that's added to the hero's health points.
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print(f"{hero.name} sees the residents leave their homes.".center(55))
    print()
    sleep_print()
    print("They walk over to the hero carrying items.".center(55))
    print()
    sleep_print()
    print("\"Thank you for saving us.\"".center(55))
    print()
    sleep_print()
    print("\"We brought you an elixir to regain your health.\"".center(55))
    print()
    sleep_print()
    if hero.health == 100:
        print(f"{hero.name} rejects the elixir due to already being at max health.".center(55))
    else:
        print(f"{hero.name} takes the bottle, opens it, and drinks the liquid.".center(55))
        print()
        sleep_print()
        print("It is pleasantly warm, and is sweet like honey.".center(55))
        health_points_list: list = [10, 20, 30]
        randomly_chosen_health_points: int = random.choice(health_points_list)
        if hero.health + randomly_chosen_health_points > 100:
            hero.health = 100
            print()
            sleep_print()
            print(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!".center(55))
            print()
            sleep_print()
            print(f"== The hero is at max (100) health points ==".center(55))
            return hero.health
        else:
            hero.health += randomly_chosen_health_points
            print()
            sleep_print()
            print(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!".center(55))
            print()
            sleep_print()
            print(f"== The hero now has {hero.health} health points ==".center(55))
            return hero.health
