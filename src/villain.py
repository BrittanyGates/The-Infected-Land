#!/usr/bin/python3
"""This module contains the Villain class and its methods."""
from console import attack_or_block_successful, attack_or_block_unsuccessful, console, hero_or_villain_defeated
from text_display_tools import attack_sleep_print, clear_screen
import random
import sys


class Villain:
    def __init__(self, name: str, class_type: str, race_type: str, beast_type: str, weapon_type: str,
                 weapon_damage: int,
                 armor_type: str, armor_defense: int, health: int):
        """Additional information about the Villain class.
        :param name: The villain's name.
        :param class_type: The villain's class type (ex. Non-human or Human).
        :param race_type: The villain's race type (ex. Human or Elf).
        :param beast_type: The villain's beast type (ex. Bear or Vampire).
        :param weapon_type: The villain's weapon type (ex. Claws or Bite).
        :param weapon_damage: The weapon damage for the chosen weapon type.
        :param armor_type: The villain's armor type (ex. None or Armor).
        :param armor_defense: The armor defense for the chosen armor type.
        :param health: The villain's health amount.
        """
        self.name = name
        self.class_type = class_type
        self.race_type = race_type
        self.beast_type = beast_type
        self.weapon_type = weapon_type
        self.weapon_damage = weapon_damage
        self.armor_type = armor_type
        self.armor_defense = armor_defense
        self.health = health 

    def display_villain_vitals(self) -> None:
        """Displays the vitals of the VILLAIN.
        :return: None
        """
        if self.armor_type == "None":
            console.print(f"== {self.name} has {self.health} points of health and no armor ==", justify="center")
        else:
            console.print(f"== {self.name} has {self.health} points of health ==", justify="center")
            console.print(f"== {self.name} wears {self.armor_type} with {self.armor_defense} points of defense ==", justify="center")

    def attack_hero(self, hero) -> None:
        """Attacks the Hero with a random beast.
        :return: None
        """
        random_num = random.randint(0, 1)
        console.print(f"!! {self.name} attacks {hero.name} with its {self.weapon_type} !!", style=attack_or_block_successful, justify="center")
        attack_sleep_print()
        if random_num == 0:
            console.print()
            console.print(f"-- {hero.name} fails to block the attack with their shield --", style=attack_or_block_unsuccessful, justify="center")
            attack_sleep_print()
            console.print()
            console.print(f"!! {self.weapon_type} does {self.weapon_damage - hero.armor_defense} points of damage !!", justify="center")
            hero.health -= (self.weapon_damage - hero.armor_defense)
            if hero.health <= 0:
                console.print(f"{self.name} defeats {hero.name} during battle. Game over.", style=hero_or_villain_defeated, justify="center")
                console.print()
                sys.exit()
            else:
                console.print()
                attack_sleep_print()
                clear_screen()
        else:
            console.print()
            console.print(f"{self.name} misses with {self.weapon_type} as {hero.name} blocks it.", style=attack_or_block_unsuccessful, justify="center")
            attack_sleep_print()
            clear_screen()


# Main Villain instance
main_villain = Villain("VILLAIN", "?", "?", "N/A", "Destruction", 25, "Improved Armor", 8, 60)

# Beasts instances
megabat = Villain("Megabat", "Non-human", "N/A", "Bat", "Bite", 10, "None", 0, 20)
gray_wolf = Villain("Gray Wolf", "Non-human", "N/A", "Wolf", "Bite", 10, "None", 0, 20)
black_bear = Villain("Black Bear", "Non-human", "N/A", "Bear", "Claws", 10, "None", 0, 20)
wild_boar = Villain("Wild Boar", "Non-human", "N/A", "Boar", "Tusk", 10, "None", 0, 20)
feral_dog = Villain("Feral Dog", "Non-human", "N/A", "Dog", "Bite", 10, "None", 0, 20)

# Humans instances
crazed_lumberjack = Villain("Crazed Lumberjack", "Mercenary", "Human", "N/A", "Axe", 20, "Sturdy Armor", 5, 40)
fire_mage = Villain("Fire Mage", "Human", "Mage", "N/A", "Fireball", 20, "Sturdy Armor", 5, 40)
nimble_rouge = Villain("Nimble Rouge", "Human", "Rouge", "N/A", "Knife Strike", 20, "Sturdy Armor", 5, 40)
hearty_spearman = Villain("Hearty Spearman", "Human", "Soldier", "N/A", "Spear Thrust", 20, "Sturdy Armor", 5, 40)
unwavering_cultist = Villain("Unwavering Cultist", "Human", "Cultist", "N/A", "Spiked Mace", 20, "Sturdy Armor", 5, 40)

# Non-beasts instances
towering_skeleton = Villain("Towering Skeleton", "Non-human", "Undead", "N/A", "Bone Throw", 15, "None", 0, 30)
decaying_ghoul = Villain("Decaying Ghoul", "Non-human", "Undead", "N/A", "Punch", 15, "None", 0, 30)
powerful_mummy = Villain("Powerful Mummy", "Non-human", "Undead", "N/A", "Head Butt", 15, "None", 0, 30)
corrupt_lich = Villain("Corrupt Lich", "Non-human", "Undead", "N/A", "Drain Life", 15, "None", 0, 30)
howling_banshee = Villain("Howling Banshee", "Non-human", "Undead", "N/A", "Scream", 15, "None", 0, 30)

beasts = [megabat, gray_wolf, black_bear, wild_boar, feral_dog]
humans = [crazed_lumberjack, fire_mage, nimble_rouge, hearty_spearman, unwavering_cultist]
non_beasts = [towering_skeleton, decaying_ghoul, powerful_mummy, corrupt_lich, howling_banshee]

# Get the random beast, non-beast, and human from the Villain class for the battle.
# Added the random variables here so it's available for use by the Hero class
random_beast = random.choice(beasts)
random_non_beast = random.choice(non_beasts)
random_human = random.choice(humans)
