#!/usr/bin/python3
"""This module provides health regeneration to the Hero."""
from console import console
from text_display_tools import sleep_print
import random


def regain_health(hero) -> int:
    """The player regains a range of health points (10 to 30) after each battle.
    :return: An int added to the hero's health points.
    """
    console.print()
    sleep_print()
    console.print(f"{hero.name} sees the residents leave their homes.", justify="center")
    console.print()
    sleep_print()
    console.print("They walk over to the hero carrying items.", justify="center")
    console.print()
    sleep_print()
    console.print("\"Thank you for saving us.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"We brought you an elixir to regain your health.\"", justify="center")
    console.print()
    sleep_print()
    if hero.health == 100:
        return console.print(f"{hero.name} rejects the elixir due to already being at max health.", justify="center")
    else:
        console.print(f"{hero.name} takes the bottle, opens it, and drinks the liquid.", justify="center")
        console.print()
        sleep_print()
        console.print("It is pleasantly warm, and is sweet like honey.", justify="center")
        health_points_list: list = [10, 20, 30]
        randomly_chosen_health_points: int = random.choice(health_points_list)
        if hero.health + randomly_chosen_health_points > 100:
            hero.health = 100
            console.print()
            sleep_print()
            console.print(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!", justify="center")
            console.print()
            sleep_print()
            console.print(f"== The hero is at max (100) health points ==", justify="center")
            return hero.health
        else:
            hero.health += randomly_chosen_health_points
            console.print()
            sleep_print()
            console.print(f"!! {hero.name} regains {randomly_chosen_health_points} health points !!", justify="center")
            console.print()
            sleep_print()
            console.print(f"== The hero now has {hero.health} health points ==", justify="center")
            return hero.health
