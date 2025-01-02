#!/usr/bin/python3
"""This module introduces the game's storyline."""
from battles import beast_battle
from console import console, notification
from hero import hero
from text_display_tools import clear_screen, sleep_print


def get_the_hero_name() -> str:
    """ Gets the hero's name from the player.    
    :return: A string of the hero's name.
    """
    console.print()
    console.print("What is your name, hero?", justify="center")
    console.print()
    try:
        hero.name = input("Enter your name here: ").capitalize()
        if len(hero.name) >= 20:
            console.print()
            console.print("I cannot remember that long of a name. Please enter a shorter one.", justify="center")
            sleep_print()
            get_the_hero_name()
        elif hero.name == "":
            console.print()
            console.print("Are you sure you don't have a name? Everyone has a name.", justify="center")
            sleep_print()
            console.print()
            hero.name = input("Enter your name here: ").capitalize()
            if hero.name == "":
                console.print()
                console.print("Well, I'll just call you Hero.", justify="center")
                sleep_print()
                hero.name = "Hero"  # Default name for the hero if the player doesn't provide one
        return hero.name
    except ValueError:
        console.print()
        console.print("!! The name can only contain letters !!", style=notification, justify="center")
        console.print()
        sleep_print()
        get_the_hero_name()
        console.print()


def story_intro() -> None:
    """
    This function displays the game's storyline.
    :return: None
    """
    clear_screen()
    console.print()
    console.print("The storyline of THE INFECTED LAND", justify="center")
    console.print()
    sleep_print()
    console.print("Infection ruins the land.", justify="center")
    console.print()
    sleep_print()
    console.print("Residents huddle in their homes.", justify="center")
    console.print()
    sleep_print()
    console.print("Evil beasts, non-beasts, and humans roam the land.", justify="center")
    console.print()
    sleep_print()
    console.print("The residents pray for help.", justify="center")
    console.print()
    sleep_print()
    console.print("It arrives in a flash of lightning and a clap of thunder.", justify="center")
    console.print()
    sleep_print()
    console.print("A hero stands at the entrance to the infected land.", justify="center")
    console.print()
    sleep_print()
    get_the_hero_name()
    console.print()
    console.print(f"{hero.name} holds a sword and a shield.", justify="center")
    console.print()
    sleep_print()
    console.print("The sun reflects off the hero's metal armor.", justify="center")
    console.print()
    sleep_print()
    console.print("Suddenly, a malevolent voice fills the air:", justify="center")
    console.print()
    sleep_print()
    console.print("\"You come to save the people and the land.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"Go ahead and try. You will fail.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"I called one of my beasts to destroy you.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"Then I called one of my non-beasts.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"Oh, and I called one of my humans.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"I await your defeat.\"", justify="center")
    console.print()
    sleep_print()
    console.print("\"It's been too long since I had a good laugh.\"", justify="center")
    console.print()
    sleep_print()
    console.print("The malevolent voice ceases.", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name} walks into the infected land ready to fight!", justify="center")
    console.print()
    sleep_print()
    console.print(f"All types of evil beasts surround the hero.", justify="center")
    console.print()
    sleep_print()
    console.print("Bats glide through the sky.", justify="center")
    console.print()
    sleep_print()
    console.print("Wolves travel in packs.", justify="center")
    console.print()
    sleep_print()
    console.print("A massive black bear lumbers around.", justify="center")
    console.print()
    sleep_print()
    console.print("Wild boars root around.", justify="center")
    console.print()
    sleep_print()
    console.print("Feral dogs sniff the air and growl.", justify="center")
    console.print()
    sleep_print()
    clear_screen()
    beast_battle()
