#!/usr/bin/python3
from text_display_tools import *
import random


def regain_health() -> int:
    """The player regains a range of health points (10 to 30) after each battle.
    :return: An int added to the hero's health points.
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print(center_text(f"{hero.name} sees the residents leave their homes."))
    print()
    sleep_print()
    print(center_text("They walk over to the hero carrying items."))
    print()
    sleep_print()
    print(center_text("\"Thank you for saving us.\""))
    print()
    sleep_print()
    print(center_text("\"We brought you an elixir to regain your health.\""))
    print()
    sleep_print()
    if hero.health == 100:
        print(center_text(f"{hero.name} rejects the elixir due to already being at max health."))
    else:
        print(center_text(f"{hero.name} takes the bottle, opens it, and drinks the liquid."))
        print()
        sleep_print()
        print(center_text("It is pleasantly warm, and is sweet like honey."))
        health_points_list: list = [10, 20, 30]
        randomly_chosen_health_points: int = random.choice(health_points_list)
        if hero.health + randomly_chosen_health_points > 100:
            hero.health = 100
            print()
            sleep_print()
            print(center_text(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!"))
            print()
            sleep_print()
            print(center_text(f"== The hero is at max (100) health points =="))
            return hero.health
        else:
            hero.health += randomly_chosen_health_points
            print()
            sleep_print()
            print(center_text(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!"))
            print()
            sleep_print()
            print(center_text(f"== The hero now has {hero.health} health points =="))
            return hero.health
