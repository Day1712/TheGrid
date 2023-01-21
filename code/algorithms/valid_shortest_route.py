from code.classes import district
import numpy as np
import random


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def update_battery_capacity(house, battery):
    battery.current_capacity += house.output

def nearest_available_battery(house, battery_list):
    distances = []

    # Calculate the distance of a house to every battery in the list
    for i in range(len(battery_list)):

        # Only look for batteries that still have room for the house output
        if battery_list[i].current_capacity + house.output < battery_list[i].max_capacity:
            distances.append(manhattan_distance(house.pos_x, house.pos_y, battery_list[i].pos_x, battery_list[i].pos_y))

    # Find the battery with the lowest distance
    best_battery_index = np.argmin(distances)

    # Update battery max_capacity
    update_battery_capacity(house, battery_list[best_battery_index])

    return battery_list[best_battery_index]

def create_route_list(house, battery):
    # TODO improve this code

    x = house.pos_x
    y = house.pos_y

    # If the cable is left from the battery, the route goes right
    while x < battery.pos_x:
        x += 1
        house.cables.add_cable_segment((x - 1, y), (x, y))
        if x == battery.pos_x:
            break
    # If the cable is right from the battery, the route goes left
    while x > battery.pos_x:
        x -= 1
        house.cables.add_cable_segment((x + 1, y), (x, y))
        if x == battery.pos_x:
            break

    # If the cable is under from the battery, the route goes up
    while y < battery.pos_y:
        y += 1
        house.cables.add_cable_segment((x, y - 1), (x, y))
        if y == battery.pos_y:
            break

    # If the cable is above from the battery, the route goes down
    while y > battery.pos_y:
        y -= 1
        house.cables.add_cable_segment((x, y + 1), (x, y))
        if y == battery.pos_y:
            break

def random_shortest_route(district):
    '''
    Calculates the shortest route from a house to the nearest available battery.
    The order of houses is random, so each run the routes will be different.
    '''
    # Randomize the order of houses
    shuffled_houses = district.houses[:]
    random.shuffle(shuffled_houses)

    # Create route from house to battery for each house in the grid
    for house in shuffled_houses:
        closest_battery = nearest_available_battery(house, district.batteries)
        create_route_list(house, closest_battery)

    # Calculate the cost
    district.calculate_own_cost()
    district.calculate_shared_cost()
