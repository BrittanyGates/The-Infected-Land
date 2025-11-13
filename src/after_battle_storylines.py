#!/usr/bin/python3
"""This module provides the storyline after each battle."""
from improve_loadout import improve_loadout
from regain_health import regain_health
from text_display_tools import storyline_formatter
from villain import random_human, random_non_beast, main_villain


def after_beast_battle_story(hero) -> None:
    """Displays the game's storyline after the hero defeats the beast.
    :return: None
    """
    lines: list = [
        "After the battle the other beasts start to disintegrate.",
        "The wind picks up and blows away the remnants.",
        "Eventually the land is free of the beasts.",
        "The hero walks around looking around at the changes.",
        "Green grass appears and spreads out.",
        "All types of flowers bloom within the lush blades.",
        "Trees shoot up from the ground and extend their branches."
    ]
    storyline_formatter(lines)
    regain_health(hero)
    improve_loadout(hero)

    lines: list = [
        "An evil scream reverberates through the land.",
        "The hero and the residents look around in confusion.",
        "Then the malevolent voice returns:",
        "\"You defeated my beast?\"",
        "\"I underestimated you.\"",
        "\"Well, one of my non-beasts will destroy you.\"",
        "The malevolent voice ceases.",
        f"{hero.name} nods to the residents and departs for the infected land.",
        "The hero readies their sword and shield ready to fight!",
        f"All types of evil non-beasts plod toward the hero.",
        "Towering skeletons beat the earth with a bone.",
        "Decaying ghouls moan as pus oozes from their bodies.",
        "A mummy walks around with their arms extended.",
        "A lich practices their evil magic.",
        "Banshees howl as they soar around."
    ]
    storyline_formatter(lines)
    from battles import non_beast_battle
    non_beast_battle(hero, random_non_beast)


def after_human_battle_story(hero) -> None:
    """Displays the game's storyline after the hero defeats the human.
    :return: None
    """
    lines: list = [
        "After the battle the other humans fade away.",
        "However, the land doesn't heal as before.",
        f"{hero.name} appears puzzled."
    ]
    storyline_formatter(lines)
    regain_health(hero)
    improve_loadout(hero)

    lines = [
        "A tall column of flames appears in the middle of the land.",
        "The hero retakes their battle stance, ready to fight again.",
        "The flames disappear and a man wearing deep red tunic appears.",
        f"\"Hello, {hero.name}. Oh yes, I know your name.\"",
        f"\"I also know who you are, and what you are.\"",
        f"\"You are...special. I think you already know that.\"",
        f"\"That's why you were able to defeat all my creations.\"",
        f"\"But you aren't as special as me.\"",
        f"\"I will show the person who sent you here that now!\""
    ]
    storyline_formatter(lines)
    from battles import villain_battle
    villain_battle(hero, main_villain)


def after_non_beast_battle_story(hero) -> None:
    """Displays the game's storyline after the hero defeats the non-beast.
    :return: None
    """
    lines: list = [
        "After the battle the other non-beasts melt into puddles.",
        "The puddles bubble as if they were boiling.",
        "A little later the puddles evaporate.",
        "Eventually the land is free of the non-beasts.",
        "The hero walks around looking around at the changes.",
        "A portion of the land separates and a river forms.",
        "Plateaus and hills rise from the ground around the river.",
        "Bushes sprout from the ground with little tufts of green grass."
    ]
    storyline_formatter(lines)
    regain_health(hero)
    improve_loadout(hero)

    lines = [
        "A sinister groan travels through the land.",
        "The hero and the residents look around in confusion.",
        "The malevolent voice returns:",
        "\"You defeated my non-beast with a quickness.\"",
        "\"How? Where did you get your power?\"",
        "\"I thought you were one of those pitiful humans, but you aren't.\"",
        "\"Why don't you respond to my questions?\"",
        "\"Do you not understand what I am? Who I am?\"",
        "\"Fine. Stay silent. One of MY humans will make you talk!\"",
        "The malevolent voice ceases.",
        f"{hero.name} nods to the residents and departs for the infected land.",
        "The hero readies their sword and shield ready to fight!",
        f"All types of evil humans stand on the land staring at the hero.",
        "A lumberjack with a crazed look holds a bloody axe.",
        "A mage holds a rotating ball of fire in one of his hands.",
        "A rouge twirls his knives in his hands over and over.",
        "A spearman points their spear at the hero.",
        "Finally, a cultist kneels on the ground praying in an unknown language."
    ]
    storyline_formatter(lines)
    from battles import human_battle
    human_battle(hero, random_human)
