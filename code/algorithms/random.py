from code.classes import cable
from code.functions import load_entities


import random

def random_cables(houses, batteries):
    """This function connects each house to a random battery
    and creates a cable instance for each, not taking
    into account maximum battery capacity"""
    cables = []
    for house in houses:
        current_cable = cable.Cable(random.choice(batteries), house)
        cables.append(current_cable)

    load_entities.load_cables(cables)
    return cables
