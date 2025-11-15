#!/usr/bin/python3
"""This module contains the Villain class and its methods."""
from console import attack_or_block_successful, attack_or_block_unsuccessful, console, hero_or_villain_defeated
from game_constants import *
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
            console.print(f"== {self.name} wears {self.armor_type} with {self.armor_defense} points of defense ==",
                          justify="center")

    def attack_hero(self, hero) -> None:
        """Attacks the Hero with a random beast.
        :return: None
        """
        random_num = random.randint(0, 1)
        console.print(f"!! {self.name} attacks {hero.name} with its {self.weapon_type} !!",
                      style=attack_or_block_successful, justify="center")
        attack_sleep_print()
        if random_num == 0:
            console.print()
            console.print(f"-- {hero.name} fails to block the attack with their shield --",
                          style=attack_or_block_unsuccessful, justify="center")
            attack_sleep_print()
            console.print()
            console.print(f"!! {self.weapon_type} does {self.weapon_damage - hero.armor_defense} points of damage !!",
                          justify="center")
            hero.health -= (self.weapon_damage - hero.armor_defense)
            if hero.health <= 0:
                console.print(f"{self.name} defeats {hero.name} during battle. Game over.",
                              style=hero_or_villain_defeated, justify="center")
                console.print()
                sys.exit()
            else:
                console.print()
                attack_sleep_print()
                clear_screen()
        else:
            console.print()
            console.print(f"{self.name} misses with {self.weapon_type} as {hero.name} blocks it.",
                          style=attack_or_block_unsuccessful, justify="center")
            attack_sleep_print()
            clear_screen()


# Main Villain instance
main_villain = Villain("VILLAIN", MAIN_VILLAIN_CLASS_TYPE, MAIN_VILLAIN_RACE_TYPE, "N/A", "Destruction",
                       MAIN_VILLAIN_WEAPON_DAMAGE, MAIN_VILLAIN_ARMOR_TYPE, MAIN_VILLAIN_ARMOR_DEFENSE,
                       MAIN_VILLAIN_HEALTH)

# Beasts instances
megabat = Villain("Megabat", BEAST_CLASS_TYPE, BEAST_RACE_TYPE, "Bat", "Bite", BEAST_WEAPON_DAMAGE, BEAST_ARMOR_TYPE,
                  BEAST_ARMOR_DEFENSE, BEAST_HEALTH)
gray_wolf = Villain("Gray Wolf", BEAST_CLASS_TYPE, BEAST_RACE_TYPE, "Wolf", "Bite", BEAST_WEAPON_DAMAGE,
                    BEAST_ARMOR_TYPE, BEAST_ARMOR_DEFENSE, BEAST_HEALTH)
black_bear = Villain("Black Bear", BEAST_CLASS_TYPE, BEAST_RACE_TYPE, "Bear", "Claws", BEAST_WEAPON_DAMAGE,
                     BEAST_ARMOR_TYPE, BEAST_ARMOR_DEFENSE, BEAST_HEALTH)
wild_boar = Villain("Wild Boar", BEAST_CLASS_TYPE, BEAST_RACE_TYPE, "Boar", "Tusk", BEAST_WEAPON_DAMAGE,
                    BEAST_ARMOR_TYPE, BEAST_ARMOR_DEFENSE, BEAST_HEALTH)
feral_dog = Villain("Feral Dog", BEAST_CLASS_TYPE, BEAST_RACE_TYPE, "Dog", "Bite", BEAST_WEAPON_DAMAGE,
                    BEAST_ARMOR_TYPE, BEAST_ARMOR_DEFENSE, BEAST_HEALTH)

# Humans instances
crazed_lumberjack = Villain("Crazed Lumberjack", HUMAN_CLASS_TYPE, "Human", "N/A", "Axe", HUMAN_WEAPON_DAMAGE,
                            HUMAN_ARMOR_TYPE, HUMAN_ARMOR_DEFENSE, HUMAN_HEALTH)
fire_mage = Villain("Fire Mage", HUMAN_CLASS_TYPE, "Mage", "N/A", "Fireball", HUMAN_WEAPON_DAMAGE, HUMAN_ARMOR_TYPE,
                    HUMAN_ARMOR_DEFENSE, HUMAN_HEALTH)
nimble_rouge = Villain("Nimble Rouge", HUMAN_CLASS_TYPE, "Rouge", "N/A", "Knife Strike", HUMAN_WEAPON_DAMAGE,
                       HUMAN_ARMOR_TYPE, HUMAN_ARMOR_DEFENSE, HUMAN_HEALTH)
hearty_spearman = Villain("Hearty Spearman", HUMAN_CLASS_TYPE, "Soldier", "N/A", "Spear Thrust", HUMAN_WEAPON_DAMAGE,
                          HUMAN_ARMOR_TYPE, HUMAN_ARMOR_DEFENSE, HUMAN_HEALTH)
unwavering_cultist = Villain("Unwavering Cultist", HUMAN_CLASS_TYPE, "Cultist", "N/A", "Spiked Mace",
                             HUMAN_WEAPON_DAMAGE, HUMAN_ARMOR_TYPE, HUMAN_ARMOR_DEFENSE, HUMAN_HEALTH)

# Non-beasts instances
towering_skeleton = Villain("Towering Skeleton", NON_BEAST_CLASS_TYPE, NON_BEAST_RACE_TYPE, "N/A", "Bone Throw",
                            NON_BEAST_WEAPON_DAMAGE, NON_BEAST_ARMOR_TYPE, NON_BEAST_ARMOR_DEFENSE, NON_BEAST_HEALTH)
decaying_ghoul = Villain("Decaying Ghoul", NON_BEAST_CLASS_TYPE, NON_BEAST_RACE_TYPE, "N/A", "Punch",
                         NON_BEAST_WEAPON_DAMAGE, NON_BEAST_ARMOR_TYPE, NON_BEAST_ARMOR_DEFENSE, NON_BEAST_HEALTH)
powerful_mummy = Villain("Powerful Mummy", NON_BEAST_CLASS_TYPE, NON_BEAST_RACE_TYPE, "N/A", "Head Butt",
                         NON_BEAST_WEAPON_DAMAGE, NON_BEAST_ARMOR_TYPE, NON_BEAST_ARMOR_DEFENSE, NON_BEAST_HEALTH)
corrupt_lich = Villain("Corrupt Lich", NON_BEAST_CLASS_TYPE, NON_BEAST_RACE_TYPE, "N/A", "Drain Life",
                       NON_BEAST_WEAPON_DAMAGE, NON_BEAST_ARMOR_TYPE, NON_BEAST_ARMOR_DEFENSE, NON_BEAST_HEALTH)
howling_banshee = Villain("Howling Banshee", NON_BEAST_CLASS_TYPE, NON_BEAST_RACE_TYPE, "N/A", "Scream",
                          NON_BEAST_WEAPON_DAMAGE, NON_BEAST_ARMOR_TYPE, NON_BEAST_ARMOR_DEFENSE, NON_BEAST_HEALTH)

beasts = [megabat, gray_wolf, black_bear, wild_boar, feral_dog]
humans = [crazed_lumberjack, fire_mage, nimble_rouge, hearty_spearman, unwavering_cultist]
non_beasts = [towering_skeleton, decaying_ghoul, powerful_mummy, corrupt_lich, howling_banshee]

# Get the random beast, non-beast, and human from the Villain class for the battle.
# Added the random variables here so it's available for use by the Hero class
random_beast = random.choice(beasts)
random_non_beast = random.choice(non_beasts)
random_human = random.choice(humans)
