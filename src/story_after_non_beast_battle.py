#!/usr/bin/python3
from human_battle import human_battle
from improve_loadout import improve_loadout
from regain_health import regain_health
from sleep_print import sleep_print


def after_non_beast_battle_story() -> None:
    """
    This function displays the game's storyline after the hero defeats the non-beast.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print("After the battle the other non-beasts melt into puddles.".center(55))
    print()
    sleep_print()
    print("The puddles bubble as if they were boiling.".center(55))
    print()
    sleep_print()
    print("A little later the puddles evaporate.".center(55))
    print()
    sleep_print()
    print("Eventually the land is free of the non-beasts.".center(55))
    print()
    sleep_print()
    print("The hero walks around looking around at the changes.".center(55))
    print()
    sleep_print()
    print("A portion of the land separates and a river forms.".center(55))
    print()
    sleep_print()
    print("Plateaus and hills rise from the ground around the river.".center(55))
    print()
    sleep_print()
    print("Bushes sprout from the ground with little tufts of green grass.".center(55))
    regain_health()
    improve_loadout()
    print()
    print("A sinister groan travels through the land.".center(55))
    print()
    sleep_print()
    print("The hero and the residents look around in confusion.".center(55))
    print()
    sleep_print()
    print("The malevolent voice returns:".center(55))
    print()
    sleep_print()
    print("\"You defeated my non-beast with a quickness.\"".center(55))
    print()
    sleep_print()
    print("\"How? Where did you get your power?\"".center(55))
    print()
    sleep_print()
    print("\"I thought you were one of those pitiful humans, but you aren't.\"".center(55))
    print()
    sleep_print()
    print("\"Why don't you respond to my questions?\"".center(55))
    print()
    sleep_print()
    print("\"Do you not understand what I am? Who I am?\"".center(55))
    print()
    sleep_print()
    print("\"Fine. Stay silent. One of MY humans will make you talk!\"".center(55))
    print()
    sleep_print()
    print("The malevolent voice ceases.".center(55))
    print()
    sleep_print()
    print(f"{hero.name} nods to the residents and departs for the infected land.".center(55))
    print()
    sleep_print()
    print("The hero readies their sword and shield ready to fight!".center(55))
    print()
    sleep_print()
    print(f"All types of evil humans stand on the land staring at the hero.".center(55))
    print()
    sleep_print()
    print("A lumberjack with a crazed look holds a bloody axe.".center(55))
    print()
    sleep_print()
    print("A mage holds a rotating ball of fire in one of his hands.".center(55))
    print()
    sleep_print()
    print("A rouge twirls his knives in his hands over and over.".center(55))
    print()
    sleep_print()
    print("A spearman points their spear at the hero.".center(55))
    print()
    sleep_print()
    print("Finally, a cultist kneels on the ground praying in an unknown language.".center(55))
    human_battle()