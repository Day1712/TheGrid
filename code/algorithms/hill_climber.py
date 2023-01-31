from code.visualisation import visualisation
from code.classes import district
import numpy as np
import random
import copy

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
    x_values = [point[0] for point in list_coordinates]
    y_values = [point[1] for point in list_coordinates]
    x_mid = round(sum(x_values) / len(list_coordinates))
    y_mid = round(sum(y_values) / len(list_coordinates))

    return (x_mid, y_mid)

def change_battery_location(connections_dict):
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

        for house in connections_dict:
            if connections_dict[house] == battery:
                # Delete previous route
                house.cables.clear_route()
                # Create route to the nearest point
                house.cables.create_route(house.coordinate, battery.coordinate)

def swapping_connections(connections_dict, random_selection):
    '''
    Input: dictionary of all house-battery connections (key: house, value: battery)

    - Randomly picks a house within the top of longest routes
    - Finds nearest battery and the houses currently connected to that battery
    - In random order, checks if there is a switch possible with one of the
        potential houses.
        - If solutions remains valid, the two houses switch from battery.
        - New routes are created, connections are updated
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

                # Updating the connections_dict with new connections
                connections_dict[house_1] = battery_2
                connections_dict[house_2] = battery_1

                # Stop the loop
                return


def new_route(connections_dict):
    '''
    Input: dictionary of all house-battery connections (key: house, value: battery)

    Out of a random selection, the house with the longest cable is chosen. Then,
    it will find if there is a cable nearby that goes towards the same battery.
    If so, it will recreate a route to go the that nearest point.
    '''
    # Randomly pick a house
    house = random.choice(list(connections_dict.keys()))
    battery = connections_dict[house]

    # List of all the cable points that another cable can connect to
    cable_coordinates = set()
    for h in connections_dict:
        if connections_dict[h] == battery and h != house:
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


def hill_climber_algorithm(district, mutation_function, cost_type = 'shared', convergence_treshold = 50, random_selection = 20):
    '''
    Input: starting district, convergence treshold
    returns: new district with lowest cost

    - While not converged:
        - Begin with random start state
        - Induce small change to the state
        - If the cost goes up:
            - Disregard the change
            - Keep track of convergence
    '''
    no_improvements = 0

    # house_x, house_y, house_colour, battery_x, battery_y, battery_colour = visualisation.setup_plot(district)

    while no_improvements < convergence_treshold:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Mutate the district by swapping connection and/or changing the routes
        if mutation_function == 'swapping_connections':
            swapping_connections(new_district.connections, random_selection)
            #change_battery_location(new_district.connections)
        elif mutation_function == 'new_route':
            new_route(new_district.connections)

        # Calculate costs
        if cost_type == 'own':
            new_cost = new_district.calculate_own_cost()
            old_cost = district.calculate_own_cost()
        else:
            new_cost = new_district.calculate_shared_cost()
            old_cost = district.calculate_shared_cost()

        # Undo if solution is costs went up
        if new_cost > old_cost:
            new_district = district

        else:
            # Continue with the new_district if costs go down
            district = new_district

            # Comment out if you don't want to see the costs go down:
            #print(new_cost)

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0

        # PLOT PART BELOW
        #visualisation.draw(district)

    return district
