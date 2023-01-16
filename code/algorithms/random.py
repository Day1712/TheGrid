from code.classes import cable
import random

def random_cables(houses, batteries):
    """This function connects each house to a random battery
    and creates a cable instance for each, not taking
    into account maximum battery capacity"""
    cables = []
    for house in houses:
        cable = cable.Cable(random.choice(batteries), house)
        cables.append(cable)
    return cables
