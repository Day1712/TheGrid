from code.classes import cable
import numpy as np
import random
from code.output import output_creator

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def update_battery_capacity(house, battery):
    battery.current_capacity += house.max_output

def nearest_available_battery(house, battery_list):
    distances = []

    # Calculate the distance of a house to every battery in the list
    for i in range(len(battery_list)):

        # Only look for batteries that still have room for the house output
        if battery_list[i].current_capacity + house.max_output < battery_list[i].max_capacity:
            distances.append(manhattan_distance(house.house_x, house.house_y, battery_list[i].battery_x, battery_list[i].battery_y))

    # Find the battery with the lowest distance
    best_battery_index = np.argmin(distances)

    # Update battery max_capacity
    update_battery_capacity(house, battery_list[best_battery_index])

    return battery_list[best_battery_index]

def create_route_list(house, battery):
    # TODO improve this code

    x = house.house_x
    y = house.house_y

    cable_xs = [x]
    cable_ys = [y]

    # If the cable is left from the battery, the route goes right
    while x < battery.battery_x:
        x += 1
        cable_xs.append(x)
        cable_ys.append(y)
        if x == battery.battery_x:
            break
    # If the cable is right from the battery, the route goes left
    while x > battery.battery_x:
        x -= 1
        cable_xs.append(x)
        cable_ys.append(y)
        if x == battery.battery_x:
            break

    # If the cable is under from the battery, the route goes up
    while y < battery.battery_y:
        y += 1
        cable_xs.append(x)
        cable_ys.append(y)
        if y == battery.battery_y:
            break

    # If the cable is above from the battery, the route goes down
    while y > battery.battery_y:
        y -= 1
        cable_xs.append(x)
        cable_ys.append(y)
        if y == battery.battery_y:
            break

    new_cable = cable.Cable(cable_xs, cable_ys, house, battery)
    return new_cable

def random_shortest_route(houses, batteries):
    '''
    Calculates the shortest route from a house to the nearest available battery.
    The order of houses is random, so each run the routes will be different.
    '''
    # Randomize the order of houses
    shuffled_houses = houses[:]
    random.shuffle(shuffled_houses)
    cables = []

    # Create route from house to battery for each house in the grid
    for house in shuffled_houses:
        closest_battery = nearest_available_battery(house, batteries)
        current_cable = create_route_list(house, closest_battery)
        cables.append(current_cable)

    # Calculate the cost
    output_creator.compute_total_cable_length(cables)
    total_cost = output_creator.compute_total_cable_cost(cables)
    return total_cost
