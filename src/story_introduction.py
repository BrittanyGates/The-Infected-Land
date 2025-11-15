#!/usr/bin/python3
"""This module introduces the game's storyline."""
from battles import beast_battle
from console import console, notification
from hero import hero
from text_display_tools import clear_screen, sleep_print, storyline_formatter
from villain import random_beast


def get_the_hero_name() -> str:
    """Gets the hero's name from the player.
    :return: A string of the hero's name.
    """
    console.print()
    console.print("What is your name, hero?", justify="center")
    console.print()

    while True:
        try:
            hero.name = input("Enter your name here: ").capitalize()
            if len(hero.name) >= 20:
                console.print()
                console.print(
                    "I cannot remember that long of a name. Please enter a shorter one.",
                    justify="center",
                )
                sleep_print()
                continue
            elif not hero.name:
                console.print()
                console.print(
                    "Are you sure you don't have a name? Everyone has a name.",
                    justify="center",
                )
                sleep_print()
                console.print()
                hero.name = input("Enter your name here: ").capitalize()
                if not hero.name:
                    console.print()
                    console.print("Well, I'll just call you Hero.", justify="center")
                    sleep_print()
                    hero.name = "Hero"
            return hero.name
        except ValueError:
            console.print()
            console.print(
                "!! The name can only contain letters !!",
                style=notification,
                justify="center",
            )
            console.print()
            sleep_print()
            continue  # Loop again


def story_intro() -> None:
    """
    This function displays the game's storyline.
    :return: None
    """
    clear_screen()

    lines: list = [
        "The storyline of THE INFECTED LAND",
        "Infection ruins the land.",
        "Residents huddle in their homes.",
        "Evil beasts, non-beasts, and humans roam the land.",
        "The residents pray for help.",
        "It arrives in a flash of lightning and a clap of thunder.",
        "A hero stands at the entrance to the infected land.",

    ]

    storyline_formatter(lines)
    get_the_hero_name()

    lines: list = [
        f"{hero.name} holds a sword and a shield.",
        "The sun reflects off the hero's metal armor.",
        "Suddenly, a malevolent voice fills the air:",
        "\"You come to save the people and the land.\"",
        "\"Go ahead and try. You will fail.\"",
        "\"I called one of my beasts to destroy you.\"",
        "\"Then I called one of my non-beasts.\"",
        "\"Oh, and I called one of my humans.\"",
        "\"I await your defeat.\"",
        "\"It's been too long since I had a good laugh.\"",
        "The malevolent voice ceases.",
        f"{hero.name} walks into the infected land ready to fight!",
        f"All types of evil beasts surround the hero.",
        "Bats glide through the sky.",
        "Wolves travel in packs.",
        "A massive black bear lumbers around.",
        "Wild boars root around.",
        "Feral dogs sniff the air and growl.",
    ]

    storyline_formatter(lines)
    beast_battle(hero, random_beast)
