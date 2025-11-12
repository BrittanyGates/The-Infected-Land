#!/usr/bin/python3
"""This module provides health regeneration to the Hero."""
from console import console
from text_display_tools import sleep_print, storyline_formatter
import random


def regain_health(hero) -> int:
    """The player regains a range of health points (10 to 30) after each battle.
    :return: An int added to the hero's health points.
    """
    lines: list = [
        f"{hero.name} sees the residents leave their homes.",
        "They walk over to the hero carrying items.",
        "\"Thank you for saving us.\"",
        "\"We brought you an elixir to regain your health.\"",

    ]
    storyline_formatter(lines)
    if hero.health == 100:
        return console.print(f"{hero.name} rejects the elixir due to already being at max health.", justify="center")
    else:
        lines: list = [
            f"{hero.name} takes the bottle, opens it, and drinks the liquid.",
            "It is pleasantly warm, and is sweet like honey.",
        ]
        storyline_formatter(lines)
        health_points_list: list = [10, 20, 30]
        randomly_chosen_health_points: int = random.choice(health_points_list)
        max_health_lines: list = [
            f"!! {hero.name} regains {randomly_chosen_health_points} health points !!",
            f"== The hero is at max (100) health points ==",
        ]
        health_regain_lines: list = [
            f"!! {hero.name} regains {randomly_chosen_health_points} health points !!",
            f"== The hero now has {hero.health} health points ==",
        ]
        if hero.health + randomly_chosen_health_points > 100:
            hero.health = 100
            storyline_formatter(max_health_lines)
            return hero.health
        else:
            hero.health += randomly_chosen_health_points
            storyline_formatter(health_regain_lines)
            return hero.health
