from code.classes import cable
import math
from code.functions import simple_functions

def closest_cables(houses, batteries):
    """This function connects each house to the nearest battery,
    not taking into account maximum battery capacity"""
    cables = []

    # iterating over the houses
    for house in houses:
        house_x = house.house_x
        house_y = house.house_y
        closest_battery = None
        lowest_distance = math.inf

        for battery in batteries:
            # check which battery is the closest
            battery_x = battery.battery_x
            battery_y = battery.battery_y
            distance = simple_functions.manhattan_distance(house_x, house_y, battery_x, battery_y)
            if distance < lowest_distance:
                lowest_distance = distance
                closest_battery = battery

        # connect house to closest battery
        current_cable = cable.Cable(closest_battery, house)
        cables.append(current_cable)

    return cables
