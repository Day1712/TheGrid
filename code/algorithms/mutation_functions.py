import numpy as np
import random


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def find_nearest_index(start, coordinate_list):
    '''
    Given a starting point and a list of coordinates,
    returns the index of the nearest coordinate of the list
    '''
    distances = []
    for coordinate in coordinate_list:
        distances.append(manhattan_distance(start, coordinate))

    return np.argmin(distances)

def middle_point(list_coordinates):
    '''
    For a list with coordinates, returns the middle point as a coordinate.
    '''
    # Lists of x and y's
    x_values = [point[0] for point in list_coordinates]
    y_values = [point[1] for point in list_coordinates]

    # Average
    x_mid = round(sum(x_values) / len(list_coordinates))
    y_mid = round(sum(y_values) / len(list_coordinates))

    # New coordinate
    return (x_mid, y_mid)

def change_battery_location(connections_dict):
    '''
    All batteries find the middle point of their assigned houses and moves
    to that location. All routes are then redrawn.
    '''
    for battery in connections_dict.values():

        # List of coordinates connected to one battery
        cluster_coordinates = []
        for house in connections_dict:
            if connections_dict[house] == battery:
                cluster_coordinates.append(house.coordinate)

        # Find middle point of the cluster
        new_location = middle_point(cluster_coordinates)

        # Update battery to that location
        battery.change_location(new_location)

        # Redraw the routes to the new battery location.
        for house in connections_dict:
            if connections_dict[house] == battery:
                # Delete previous route
                house.cables.clear_route()
                # Create route to the nearest point
                house.cables.create_route(house.coordinate, battery.coordinate)

def swapping_connections(connections_dict, random_selection):
    '''
    Input:
    - Dictionary of all house-battery connections (key: house, value: battery)
    - Random selection (number)

    Pseudo code:
    - Randomly picks a house within a selection of top of longest routes
    - Finds nearest battery and the houses currently connected to that battery
    - For every house in the potential houses list (in random order):
        - Checks if there is a switch possible. If solutions remains valid:
            - The two houses switch from battery.
            - Loop ends
    '''
    while True:
        # Sort houses by segments length (longest route)
        houses_by_segments = sorted(list(connections_dict.keys()), key=lambda x: len(x.cables.segments), reverse=True)

        # Randomly pick a house with the top-10 longest segments
        house_1 = random.choice(houses_by_segments[0:random_selection])
        battery_1 = connections_dict[house_1]

        # Find nearest battery
        all_batteries = [battery.coordinate for battery in connections_dict.values()]
        nearest_index = find_nearest_index(house_1.coordinate, all_batteries)
        battery_2 = list(connections_dict.values())[nearest_index]

        # Find houses connected to the nearest battery
        potential_houses = [house for house, battery in connections_dict.items() if battery == battery_2]

        # Shuffle the potential houses
        random.shuffle(potential_houses)

         # Check each potential house
        for house_2 in potential_houses:
            # Check if swapping results in a valid solution
            if (battery_1.current_capacity - house_1.output + house_2.output <= battery_1.max_capacity) and \
               (battery_2.current_capacity - house_2.output + house_1.output <= battery_2.max_capacity):

                # Updating the connections_dict with new connections
                connections_dict[house_1] = battery_2
                connections_dict[house_2] = battery_1

                # Update battery capacities
                battery_1.current_capacity -= house_1.output - house_2.output
                battery_2.current_capacity -= house_2.output - house_1.output

                # Remove previous cable segments
                house_1.cables.clear_route()
                house_2.cables.clear_route()

                # Update colours
                house_1.colour = battery_2.colour
                house_2.colour = battery_1.colour

                # Create new cable routes
                house_1.cables.create_route(house_1.coordinate, battery_2.coordinate)
                house_2.cables.create_route(house_2.coordinate, battery_1.coordinate)

                # Stop the loop
                return

def new_route(connections_dict):
    '''
    Input:
    - dictionary of all house-battery connections (key: house, value: battery)

    Pseudo code:
    - For a random house, it will look if there is a route nearby.
    - If so, it will recreate a route to go the that nearest point.
    '''
    # Randomly pick a house
    house = random.choice(list(connections_dict.keys()))
    battery = connections_dict[house]

    # List of all the cable points that another cable can connect to
    cable_coordinates = set()
    for h in connections_dict:
        if h != house:
            for coordinate in h.cables.coordinates:
                cable_coordinates.add(coordinate)
    cable_coordinates = list(cable_coordinates)

    # Calculate manhattan distances and find nearest point
    nearest_index = find_nearest_index(house.coordinate, cable_coordinates)

    # Only change route if the nearest point is not the same location
    if house.coordinate != cable_coordinates[nearest_index]:
        # Delete previous route
        house.cables.clear_route()
        # Create route to the nearest point
        house.cables.create_route(house.coordinate, cable_coordinates[nearest_index])
        # Add the route from the point to the battery (so it stays connected to the battery)
        house.cables.create_route(cable_coordinates[nearest_index], battery.coordinate)
