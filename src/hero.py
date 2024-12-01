#!/usr/bin/python3
from sleep_print import attack_sleep_print
from story_after_beast_battle import after_beast_battle_story
from story_after_human_battle import after_human_battle_story
from story_after_non_beast_battle import after_non_beast_battle_story
from the_ending import the_ending
from villain import *
import random


class Hero:
    def __init__(self, name: str, class_type: str, race_type: str, weapon_type: str, weapon_damage: int,
                 armor_type: str, armor_defense: int, health: int):
        """ Additional information about the Hero class.
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
        """
        This function displays the vitals of the HERO.
        :return: None
        """
        print(f"== {self.name} has {self.health} points of health ==".center(55))
        print(f"== {self.name} wears {self.armor_type} with {self.armor_defense} points of defense ==".center(55))

    def hero_attack_beast(self) -> None:
        """
        This function takes input from the player to attack the beast Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print("*" * 60)
        print(f"{hero.name}, choose your action: (A) Attack or (B) Block.".center(55))
        print("*" * 60)
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(f"!! {hero.name} slashes at the {random_beast.name} with their sword !!".center(55))
                    attack_sleep_print()
                    print()
                    print(f"-- {random_beast.name} fails to dodge the attack --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! {self.weapon_type} does {self.weapon_damage - random_beast.armor_defense} points of damage !!".center(55))
                    random_beast.health -= (self.weapon_damage - random_beast.armor_defense)
                    print()
                    if random_beast.health <= 0:
                        attack_sleep_print()
                        print("*" * 60)
                        print(f"!! {hero.name} defeats the {random_beast.name} !!".center(55))
                        print("*" * 60)
                        attack_sleep_print()
                        print()
                        print(f"== After the battle {hero.name} has {hero.health} health points ==".center(55))
                        attack_sleep_print()
                        clear_screen()
                        after_beast_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.beast_attack_hero(random_beast)
                else:
                    print()
                    print(f"!! {hero.name} swings their sword at the {random_beast.name}, but misses !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.beast_attack_hero(random_beast)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! The block is successful !!".center(55))
                    print()
                    attack_sleep_print()
                    print(f"-- The block stuns {random_beast.name} allowing {hero.name} to attack again --".center(55))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_beast(self)
                else:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    print()
                    attack_sleep_print()
                    print(f"!! The block is unsuccessful !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.beast_attack_hero(random_beast)
            else:
                print()
                print("*" * 60)
                print("!! Incorrect input !!".center(55))
                print("*" * 60)
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_beast(self)
        except ValueError:
            print()
            print("*" * 60)
            print("!! The name can only contain letters !!".center(55))
            print("*" * 60)
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_beast(self)

    def hero_attack_non_beast(self) -> None:
        """
        This function takes input from the player to attack the non-beast Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print("*" * 60)
        print(f"{hero.name}, choose your action: (A) Attack or (B) Block.".center(55))
        print("*" * 60)
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(f"!! {hero.name} slashes at the {random_non_beast.name} with their sword !!".center(55))
                    attack_sleep_print()
                    print()
                    print(f"-- {random_non_beast.name} fails to dodge the attack --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! {self.weapon_type} does {self.weapon_damage - random_non_beast.armor_defense} points of damage !!".center(55))
                    random_non_beast.health -= (self.weapon_damage - random_non_beast.armor_defense)
                    print()
                    if random_non_beast.health <= 0:
                        attack_sleep_print()
                        print("*" * 60)
                        print(f"!! {hero.name} defeats the {random_non_beast.name} !!".center(55))
                        print("*" * 60)
                        attack_sleep_print()
                        print()
                        print(f"== After the battle {hero.name} has {hero.health} health points ==".center(55))
                        attack_sleep_print()
                        clear_screen()
                        after_non_beast_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.non_beast_attack_hero(random_non_beast)
                else:
                    print()
                    print(f"!! {hero.name} swings their sword at the {random_non_beast.name}, but misses !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.non_beast_attack_hero(random_non_beast)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! The block is successful !!".center(55))
                    print()
                    attack_sleep_print()
                    print(f"-- The block stuns {random_non_beast.name} allowing {hero.name} to attack again --".center(55))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_non_beast(self)
                else:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    print()
                    attack_sleep_print()
                    print(f"!! The block is unsuccessful !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.non_beast_attack_hero(random_non_beast)
            else:
                print()
                print("*" * 60)
                print("!! Incorrect input !!".center(55))
                print("*" * 60)
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_non_beast(self)
        except ValueError:
            print()
            print("*" * 60)
            print("!! Please enter either A or B !!".center(55))
            print("*" * 60)
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_non_beast(self)

    def hero_attack_human(self) -> None:
        """
        This function takes input from the player to attack the human Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print("*" * 60)
        print(f"{hero.name}, choose your action: (A) Attack or (B) Block.".center(55))
        print("*" * 60)
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(f"!! {hero.name} slashes at the {random_human.name} with their sword !!".center(55))
                    attack_sleep_print()
                    print()
                    print(f"-- {random_human.name} fails to dodge the attack --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! {self.weapon_type} does {self.weapon_damage - random_human.armor_defense} points of damage !!".center(55))
                    random_human.health -= (self.weapon_damage - random_human.armor_defense)
                    print()
                    if random_human.health <= 0:
                        attack_sleep_print()
                        print("*" * 60)
                        print(f"!! {hero.name} defeats the {random_human.name} !!".center(55))
                        print("*" * 60)
                        attack_sleep_print()
                        print()
                        print(f"== After the battle {hero.name} has {hero.health} health points ==".center(55))
                        attack_sleep_print()
                        clear_screen()
                        after_human_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.human_attack_hero(random_human)
                else:
                    print()
                    print(f"!! {hero.name} swings their sword at the {random_human.name}, but misses !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.human_attack_hero(random_human)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! The block is successful !!".center(55))
                    print()
                    attack_sleep_print()
                    print(f"-- The block stuns {random_human.name} allowing {hero.name} to attack again --".center(55))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_human(self)
                else:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    print()
                    attack_sleep_print()
                    print(f"!! The block is unsuccessful !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.human_attack_hero(random_human)
            else:
                print()
                print("*" * 60)
                print("!! Incorrect input !!".center(55))
                print("*" * 60)
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_human(self)
        except ValueError:
            print()
            print("*" * 60)
            print("!! Please enter either A or B !!".center(55))
            print("*" * 60)
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_human(self)

    def hero_attack_main_villain(self) -> None:
        """
        This function takes input from the player to attack the Main Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print("*" * 60)
        print(f"{hero.name}, choose your action: (A) Attack or (B) Block.".center(55))
        print("*" * 60)
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(f"!! {hero.name} slashes at the {main_villain.name} with their sword !!".center(55))
                    attack_sleep_print()
                    print()
                    print(f"-- {main_villain.name} fails to dodge the attack --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! {self.weapon_type} does {self.weapon_damage - main_villain.armor_defense} points of damage !!".center(55))
                    main_villain.health -= (self.weapon_damage - main_villain.armor_defense)
                    print()
                    if main_villain.health <= 0:
                        attack_sleep_print()
                        print("*" * 60)
                        print(f"!! {hero.name} defeats the {main_villain.name} !!".center(55))
                        print("*" * 60)
                        attack_sleep_print()
                        print()
                        print(f"== After the battle {hero.name} has {hero.health} health points ==".center(55))
                        attack_sleep_print()
                        clear_screen()
                        the_ending()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.main_villain_attack_hero(main_villain)
                else:
                    print()
                    print(f"!! {hero.name} swings their sword at the {main_villain.name}, but misses !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.main_villain_attack_hero(main_villain)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    attack_sleep_print()
                    print()
                    print(f"!! The block is successful !!".center(55))
                    print()
                    attack_sleep_print()
                    print(f"-- The block stuns {main_villain.name} allowing {hero.name} to attack again --".center(55))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_main_villain(self)
                else:
                    print()
                    print(f"-- {hero.name} readies to block the attack with their shield --".center(55))
                    print()
                    attack_sleep_print()
                    print(f"!! The block is unsuccessful !!".center(55))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.main_villain_attack_hero(main_villain)
            else:
                print()
                print("*" * 60)
                print("!! Incorrect input !!".center(55))
                print("*" * 60)
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_main_villain(self)
        except ValueError:
            print()
            print("*" * 60)
            print("!! Please enter either A or B !!".center(55))
            print("*" * 60)
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_main_villain(self)


# Create the Hero instance
hero = Hero("", "Warrior", "Human", "Sword", 10, "Regular Armor", 5, 100)
