#!/usr/bin/python3
"""This module runs the ending for the game."""
from console import console, notification
from text_display_tools import clear_screen, sleep_print, storyline_formatter
import sys


def the_ending_choice(hero) -> None:
    """Starts the hero's final decision during the ending
    :return: None
    """
    while True:
        console.print()
        console.print()
        console.print(f"{hero.name}, choose your action: (S) Stay or (L) Leave.", justify="center")

        user_input = input("Enter your choice here: ").upper()

        if user_input == "S":
            lines: list = [
                '"I will stay here to protect all of you."',
                '"What if you turn evil?"',
                '"I won\'t. I\'m strong enough to fight it from overtaking me."',
                '"We shall see."',
                "-- THE END --"
            ]
            storyline_formatter(lines)
            sys.exit()
        elif user_input == "L":
            lines: list = [
                '"I will leave. I don\'t want to turn evil."',
                '"Do you think that will happen?"',
                '"It could. I rather not take that risk."',
                "The residents nod.",
                f"{hero.name} disappears in a flash of lightning and a clap of thunder.",
                "-- THE END --"
            ]
            storyline_formatter(lines)
            sys.exit()
        else:
            console.print()
            console.print("!! Incorrect input. Please enter S or L. !!", style=notification, justify="center")
            sleep_print()
            clear_screen()
            continue


def the_ending(hero, villain) -> None:
    """Displays the ending of the game.
    :return: None
    """
    lines: list = [
        f"{villain.name} collapses onto the ground and blood gushes out of his body.",
        f"{hero.name} stands over the {villain.name}.",
        f'{villain.name}: "Go ahead and kill me."',
        f'{hero.name}: "Who are you?"',
        f'{villain.name}: "I forgot my name. It\'s been so long since anyone used it."',
        f'{villain.name}: "I was sent by The Great Power long ago."',
        f'{villain.name}: "I was good. I was pure."',
        f'{hero.name}: "What happened? Why did you become evil?"',
        f'{villain.name}: "Corruption."',
        f'{hero.name}: "I don\'t understand."',
        f'{villain.name}: "I don\'t either. I started having bad thoughts."',
        f'{villain.name}: "I thought about killing the people."',
        f'{villain.name}: "I thought about destroying the land."',
        f'{villain.name}: "Eventually, I succumbed to my thoughts."',
        f'{villain.name}: "It will happen to you if you stay here."',
        f'{hero.name}: "I won\'t. I\'m strong."',
        f'{villain.name}: "So was I. Leave here. Go back to The Great Power."',
        f'{hero.name}: "These residents need me!"',
        f'{villain.name}: "They will survive without you. They did without me."',
        f'{hero.name}: "I\'m not like you."',
        f'{villain.name}: "You will become like me. Learn from my mistake."',
        f'{hero.name}: "You\'re trying to manipulate me. It won\'t work."',
        f"{villain.name} sighs and closes his eyes.",
        "His body erupts into flames. The fire burns fast.",
        "Smoke rises from the scattered ashes.",
        f"The residents walk over to {hero.name}. One of them steps forward.",
        '"So will you stay with us, or will you leave?"'
    ]
    storyline_formatter(lines)
    the_ending_choice(hero)
