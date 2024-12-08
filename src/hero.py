#!/usr/bin/python3
from after_battle_storylines import *
from text_display_tools import *
from the_ending import the_ending
from villain import *
import random


class Hero:
    def __init__(self, name: str, class_type: str, race_type: str, weapon_type: str, weapon_damage: int,
                 armor_type: str, armor_defense: int, health: int):
        """ Information about the Hero class.
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
        print(center_text(f"== {self.name} has {self.health} points of health =="))
        print(center_text(f"== {self.name} wears {self.armor_type} with {self.armor_defense} points of defense =="))

    def hero_attack_beast(self) -> None:
        """Takes input from the player to attack the beast Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print(center_text("-" * 80))
        print(center_text(f"{hero.name}, choose your action: (A) Attack or (B) Block."))
        print(center_text("-" * 80))
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(center_text(f"!! {hero.name} slashes at the {random_beast.name} with their sword !!"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"-- {random_beast.name} fails to dodge the attack --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! {self.weapon_type} does {self.weapon_damage - random_beast.armor_defense} points of damage !!"))
                    random_beast.health -= (self.weapon_damage - random_beast.armor_defense)
                    print()
                    if random_beast.health <= 0:
                        attack_sleep_print()
                        print(center_text("*" * 80))
                        print(center_text(f"!! {hero.name} defeats the {random_beast.name} !!"))
                        print(center_text("*" * 80))
                        attack_sleep_print()
                        print()
                        print(center_text(f"== After the battle {hero.name} has {hero.health} health points =="))
                        attack_sleep_print()
                        clear_screen()
                        after_beast_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.beast_attack_hero(random_beast)
                else:
                    print()
                    print(center_text(f"!! {hero.name} swings their sword at the {random_beast.name}, but misses !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.beast_attack_hero(random_beast)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! The block is successful !!"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"-- The block stuns {random_beast.name} allowing {hero.name} to attack again --"))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_beast(self)
                else:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"!! The block is unsuccessful !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.beast_attack_hero(random_beast)
            else:
                print()
                print(center_text("*" * 80))
                print(center_text("!! Incorrect input !!"))
                print(center_text("*" * 80))
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_beast(self)
        except ValueError:
            print()
            print(center_text("*" * 80))
            print(center_text("!! The name can only contain letters !!"))
            print(center_text("*" * 80))
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_beast(self)

    def hero_attack_non_beast(self) -> None:
        """Takes input from the player to attack the non-beast Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print(center_text("*" * 80))
        print(center_text(f"{hero.name}, choose your action: (A) Attack or (B) Block."))
        print(center_text("*" * 80))
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(center_text(f"!! {hero.name} slashes at the {random_non_beast.name} with their sword !!"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"-- {random_non_beast.name} fails to dodge the attack --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! {self.weapon_type} does {self.weapon_damage - random_non_beast.armor_defense} points of damage !!"))
                    random_non_beast.health -= (self.weapon_damage - random_non_beast.armor_defense)
                    print()
                    if random_non_beast.health <= 0:
                        attack_sleep_print()
                        print(center_text("*" * 80))
                        print(center_text(f"!! {hero.name} defeats the {random_non_beast.name} !!"))
                        print(center_text("*" * 80))
                        attack_sleep_print()
                        print()
                        print(center_text(f"== After the battle {hero.name} has {hero.health} health points =="))
                        attack_sleep_print()
                        clear_screen()
                        after_non_beast_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.non_beast_attack_hero(random_non_beast)
                else:
                    print()
                    print(center_text(f"!! {hero.name} swings their sword at the {random_non_beast.name}, but misses !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.non_beast_attack_hero(random_non_beast)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! The block is successful !!"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"-- The block stuns {random_non_beast.name} allowing {hero.name} to attack again --"))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_non_beast(self)
                else:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"!! The block is unsuccessful !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.non_beast_attack_hero(random_non_beast)
            else:
                print()
                print(center_text("*" * 80))
                print(center_text("!! Incorrect input !!"))
                print(center_text("*" * 80))
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_non_beast(self)
        except ValueError:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Please enter either A or B !!"))
            print(center_text("*" * 80))
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_non_beast(self)

    def hero_attack_human(self) -> None:
        """Takes input from the player to attack the human Villain.
        :return: None
        """
        random_num = random.randint(0, 1)
        print()
        print(center_text("*" * 80))
        print(center_text(f"{hero.name}, choose your action: (A) Attack or (B) Block."))
        print(center_text("*" * 80))
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(center_text(f"!! {hero.name} slashes at the {random_human.name} with their sword !!"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"-- {random_human.name} fails to dodge the attack --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! {self.weapon_type} does {self.weapon_damage - random_human.armor_defense} points of damage !!"))
                    random_human.health -= (self.weapon_damage - random_human.armor_defense)
                    print()
                    if random_human.health <= 0:
                        attack_sleep_print()
                        print(center_text("*" * 80))
                        print(center_text(f"!! {hero.name} defeats the {random_human.name} !!"))
                        print(center_text("*" * 80))
                        attack_sleep_print()
                        print()
                        print(center_text(f"== After the battle {hero.name} has {hero.health} health points =="))
                        attack_sleep_print()
                        clear_screen()
                        after_human_battle_story()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.human_attack_hero(random_human)
                else:
                    print()
                    print(center_text(f"!! {hero.name} swings their sword at the {random_human.name}, but misses !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.human_attack_hero(random_human)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! The block is successful !!"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"-- The block stuns {random_human.name} allowing {hero.name} to attack again --"))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_human(self)
                else:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"!! The block is unsuccessful !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.human_attack_hero(random_human)
            else:
                print()
                print(center_text("*" * 80))
                print(center_text("!! Incorrect input !!"))
                print(center_text("*" * 80))
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_human(self)
        except ValueError:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Please enter either A or B !!"))
            print(center_text("*" * 80))
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
        print(center_text("*" * 80))
        print(center_text(f"{hero.name}, choose your action: (A) Attack or (B) Block."))
        print(center_text("*" * 80))
        print()
        user_input = input("Enter your choice here: ").capitalize()
        try:
            if user_input == "A":
                if random_num == 0:
                    print()
                    print(center_text(f"!! {hero.name} slashes at the {main_villain.name} with their sword !!"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"-- {main_villain.name} fails to dodge the attack --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! {self.weapon_type} does {self.weapon_damage - main_villain.armor_defense} points of damage !!"))
                    main_villain.health -= (self.weapon_damage - main_villain.armor_defense)
                    print()
                    if main_villain.health <= 0:
                        attack_sleep_print()
                        print(center_text("*" * 80))
                        print(center_text(f"!! {hero.name} defeats the {main_villain.name} !!"))
                        print(center_text("*" * 80))
                        attack_sleep_print()
                        print()
                        print(center_text(f"== After the battle {hero.name} has {hero.health} health points =="))
                        attack_sleep_print()
                        clear_screen()
                        the_ending()
                    else:
                        attack_sleep_print()
                        clear_screen()
                        Villain.main_villain_attack_hero(main_villain)
                else:
                    print()
                    print(center_text(f"!! {hero.name} swings their sword at the {main_villain.name}, but misses !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.main_villain_attack_hero(main_villain)
            elif user_input == "B":
                if random_num == 0:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    attack_sleep_print()
                    print()
                    print(center_text(f"!! The block is successful !!"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"-- The block stuns {main_villain.name} allowing {hero.name} to attack again --"))
                    attack_sleep_print()
                    clear_screen()
                    Hero.hero_attack_main_villain(self)
                else:
                    print()
                    print(center_text(f"-- {hero.name} readies to block the attack with their shield --"))
                    print()
                    attack_sleep_print()
                    print(center_text(f"!! The block is unsuccessful !!"))
                    print()
                    attack_sleep_print()
                    clear_screen()
                    Villain.main_villain_attack_hero(main_villain)
            else:
                print()
                print(center_text("*" * 80))
                print(center_text("!! Incorrect input !!"))
                print(center_text("*" * 80))
                attack_sleep_print()
                clear_screen()
                Hero.hero_attack_main_villain(self)
        except ValueError:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Please enter either A or B !!"))
            print(center_text("*" * 80))
            print()
            attack_sleep_print()
            clear_screen()
            Hero.hero_attack_main_villain(self)


# Create the Hero instance
hero = Hero("", "Warrior", "Human", "Sword", 10, "Regular Armor", 5, 100)
