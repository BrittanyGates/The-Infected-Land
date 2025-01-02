#!/usr/bin/python3
"""This module runs the ending for the game."""
from console import console, notification
from text_display_tools import clear_screen, sleep_print
from villain import main_villain
import sys


def the_ending_choice() -> None:
    """Starts the hero's final decision during the ending
    :return: None
    """
    console.print()
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    console.print(f"{hero.name}, choose your action: (S) Stay or (L) Leave.", justify="center")
    try:
        user_input = input("Enter your choice here: ").capitalize()
    except ValueError:
        console.print()
        console.print("!! Please enter either S or L !!", justify="center")
        console.print()
        sleep_print()
        clear_screen()
        the_ending_choice()
    else:
        if user_input == "S":
            console.print()
            sleep_print()
            console.print("\"I will stay here to protect all of you.\"", justify="center")
            console.print()
            sleep_print()
            console.print("\"What if you turn evil?\"", justify="center")
            console.print()
            sleep_print()
            console.print("\"I won't. I'm strong enough to fight it from overtaking me.\"", justify="center")
            console.print()
            sleep_print()
            console.print("\"We shall see.\"", justify="center")
            sleep_print()
            console.print()
            console.print("-- THE END --", justify="center")
            console.print()
            sys.exit()
        elif user_input == "L":
            console.print()
            sleep_print()
            console.print("\"I will leave. I don't want to turn evil.\"", justify="center")
            console.print()
            sleep_print()
            console.print("\"Do you think that will happen?\"", justify="center")
            console.print()
            sleep_print()
            console.print("\"It could. I rather not take that risk.\"", justify="center")
            console.print()
            sleep_print()
            console.print("The residents nod.", justify="center")
            console.print()
            sleep_print()
            console.print(f"{hero.name} disappears in a flash of lightning and a clap of thunder.", justify="center")
            sleep_print()
            console.print("-- THE END --", justify="center")
            console.print()
            sys.exit()
        else:
            console.print()
            console.print("!! Incorrect input !!", style=notification, justify="center")
            sleep_print()
            clear_screen()
            the_ending_choice()


def the_ending() -> None:
    """Displays the ending of the game.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    console.print()
    sleep_print()
    console.print(f"{main_villain.name} collapses onto the ground and blood gushes out of his body.", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name} stands over the {main_villain.name}.", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"Go ahead and kill me.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"Who are you?\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I forgot my name. It's been so long since anyone used it.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I was sent by The Great Power long ago.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I was good. I was pure.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"What happened? Why did you become evil?\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"Corruption.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"I don't understand.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I don't either. I started having bad thoughts.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I thought about killing the people.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"I thought about destroying the land.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"Eventually, I succumbed to my thoughts.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"It will happen to you if you stay here.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"I won't. I'm strong.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"So was I. Leave here. Go back to The Great Power.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"These residents need me!\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"They will survive without you. They did without me.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"I'm not like you.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name}: \"You will become like me. Learn from my mistake.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{hero.name}: \"You're trying to manipulate me. It won't work.\"", justify="center")
    console.print()
    sleep_print()
    console.print(f"{main_villain.name} sighs and closes his eyes.", justify="center")
    console.print()
    sleep_print()
    console.print("His body erupts into flames. The fire burns fast.", justify="center")
    console.print()
    sleep_print()
    console.print("Smoke rises from the scattered ashes.", justify="center")
    console.print()
    sleep_print()
    console.print(f"The residents walk over to {hero.name}. One of them steps forward.", justify="center")
    console.print()
    sleep_print()
    console.print("\"So will you stay with us, or will you leave?\"", justify="center")
    the_ending_choice()
