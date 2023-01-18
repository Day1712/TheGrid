from code.classes import district
import numpy as np

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def nearest_battery(house, battery_list):
    distances = []

    # Calculate the distance of a house to every battery in the list
    for i in range(len(battery_list)):
        distances.append(manhattan_distance(house.pos_x, house.pos_y, battery_list[i].pos_x, battery_list[i].pos_y))

    # Find the battery with the lowest distance
    min_distance_index = np.argmin(distances)
    return battery_list[min_distance_index]

def create_route_list(house, battery):
    # TODO improve this code

    x = house.pos_x
    y = house.pos_y

    # If the cable is left from the battery, the route goes right
    while x < battery.pos_x:
        x += 1
        house.cables.append((x, y))
        if x == battery.pos_x:
            break
    # If the cable is right from the battery, the route goes left
    while x > battery.pos_x:
        x -= 1
        house.cables.append((x, y))
        if x == battery.pos_x:
            break

    # If the cable is under from the battery, the route goes up
    while y < battery.pos_y:
        y += 1
        house.cables.append((x, y))
        if y == battery.pos_y:
            break

    # If the cable is above from the battery, the route goes down
    while y > battery.pos_y:
        y -= 1
        house.cables.append((x, y))
        if y == battery.pos_y:
            break

def shortest_route(district):
    '''
    Calculates the shortest route from a house to the nearest battery with
    overlapping cables and ignoring all outputs and battery capacity.
    '''
    for house in district.houses:
        closest_battery = nearest_battery(house, district.batteries)
        create_route_list(house, closest_battery)

    # Calculate the cost
    district.calculate_own_cost()
