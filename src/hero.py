#!/usr/bin/python3
"""This module contains the Hero class and its methods."""
from console import attack_or_block_successful, attack_or_block_unsuccessful, console, notification, hero_or_villain_defeated
from text_display_tools import attack_sleep_print, clear_screen
import random


class Hero:
    def __init__(self, name: str, class_type: str, race_type: str, weapon_type: str, weapon_damage: int,
                 armor_type: str, armor_defense: int, health: int):
        """Information about the Hero class.
        :param name: The hero's name.
        :param class_type: The hero's class type (ex. Warrior or Rouge).
        :param race_type: The hero's race type (ex. Human or Elf).
        :param weapon_type: The hero's weapon type (ex. Sword or Bow).
        :param weapon_damage: The weapon damage for the chosen weapon type.
        :param armor_type: The hero's armor type (ex. Plate or Leather).
        :param armor_defense: The armor defense for the chosen armor type.
        :param health: The hero's health amount.
        """
        self.name = name
        self.class_type = class_type
        self.race_type = race_type
        self.weapon_type = weapon_type
        self.weapon_damage = weapon_damage
        self.armor_type = armor_type
        self.armor_defense = armor_defense
        self.health = health

    def display_hero_vitals(self) -> None:
        """Displays the vitals of the HERO.
        :return: None
        """
        console.print(f"== {self.name} has {self.health} points of health ==", justify="center")
        console.print(f"== {self.name} wears {self.armor_type} with {self.armor_defense} points of defense ==", justify="center")

    def attack_villain(self, villain) -> None:
        """Takes input from the player to attack the beast Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        while True:
            console.print()
            console.print(f"{hero.name}, choose your action: (A) Attack or (B) Block.", justify="center")
            console.print()
            user_input = input("Enter your choice here: ").capitalize()

            if user_input == "A":
                if random_num == 0:
                    console.print()
                    console.print(f"!! {hero.name} slashes at the {villain.name} with their sword !!", style=attack_or_block_successful, justify="center")
                    attack_sleep_print()
                    console.print()
                    console.print(f"-- {villain.name} fails to dodge the attack --", style=attack_or_block_unsuccessful, justify="center")
                    attack_sleep_print()
                    console.print()
                    console.print(f"!! {self.weapon_type} does {self.weapon_damage - villain.armor_defense} points of damage !!", justify="center")
                    villain.health -= (self.weapon_damage - villain.armor_defense)
                    console.print()
                    if villain.health <= 0:
                        attack_sleep_print()
                        console.print(f"!! {hero.name} defeats the {villain.name} !!", style=hero_or_villain_defeated, justify="center")
                        attack_sleep_print()
                        console.print()
                        console.print(f"== After the battle {hero.name} has {hero.health} health points ==", justify="center")
                        attack_sleep_print()
                        clear_screen()
                    else:
                        attack_sleep_print()
                        clear_screen()
                else:
                    console.print()
                    console.print(f"!! {hero.name} swings their sword at the {villain.name}, but misses !!", style=attack_or_block_unsuccessful, justify="center")
                    console.print()
                    attack_sleep_print()
                    clear_screen()
                break
            elif user_input == "B":
                if random_num == 0:
                    console.print()
                    console.print(f"-- {hero.name} readies to block the attack with their shield --", justify="center")
                    attack_sleep_print()
                    console.print()
                    console.print(f"!! The block is successful !!", style=attack_or_block_successful, justify="center")
                    console.print()
                    attack_sleep_print()
                    console.print(f"-- The block stuns {villain.name} allowing {hero.name} to attack again --", justify="center")
                    attack_sleep_print()
                    clear_screen()
                else:
                    console.print()
                    console.print(f"-- {hero.name} readies to block the attack with their shield --", justify="center")
                    console.print()
                    attack_sleep_print()
                    console.print(f"!! The block is unsuccessful !!", style=attack_or_block_unsuccessful, justify="center")
                    console.print()
                    attack_sleep_print()
                    clear_screen()
                break
            else:
                console.print()
                console.print("!! Incorrect input !!", style=notification, justify="center")
                attack_sleep_print()
                clear_screen()
                continue


# Create the Hero instance
hero = Hero("", "Warrior", "Human", "Sword", 10, "Regular Armor", 5, 100)
