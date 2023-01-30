from code.visualisation import visualisation
from code.classes import district
import numpy as np
import random
import copy

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def new_route(connections_dict):
    # Pick random house
    house = random.choice(list(connections_dict.keys()))

    # Corresponding battery
    battery = connections_dict[house]

    # List of all the cable points that another cable can connect to
    cable_coordinates = set()

    for h in connections_dict:
        if connections_dict[h] == battery and h != house:
            for coordinate in h.cables.coordinates:
                cable_coordinates.add(coordinate)

    cable_coordinates = list(cable_coordinates)

    # Calculate manhattan distances
    distances = []
    for coordinate in cable_coordinates:
        distances.append(manhattan_distance(house.coordinate, coordinate))

    # Find the nearest point
    nearest_index = np.argmin(distances)

    # Only change route if the nearest point is not the same location
    if house.coordinate != cable_coordinates[nearest_index]:

        # Delete previous route
        house.cables.clear_route()

        # Create route to the nearest point
        house.cables.create_route(house.coordinate, cable_coordinates[nearest_index])

        # Add the route from the point to the battery (so it stays connected to the battery)
        house.cables.create_route(cable_coordinates[nearest_index], battery.coordinate)

def swapping_connections(connections_dict):
    '''
    Input: dictionary of all house-battery connections (key: house, value: battery)

    This function randomly chooses two houses. It switches the batteries only IF
    that results in a valid solution (i.e. battery capacities not exceeded). It
    updates the new house-battery routes and the dictionary.
    '''
    continue_loop = True

    while continue_loop:
        # Randomly picking two houses
        house_1, house_2 = random.sample(list(connections_dict), 2)
        battery_1, battery_2 = connections_dict[house_1], connections_dict[house_2]

        # Only swap if solution stays valid
        if (battery_1.current_capacity - house_1.output + house_2.output) <= battery_1.max_capacity and (battery_2.current_capacity - house_2.output + house_1.output) <= battery_2.max_capacity:

                # Update battery capacities
                battery_1.current_capacity += -house_1.output + house_2.output
                battery_2.current_capacity += -house_2.output + house_1.output

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
                continue_loop = False


def hill_climber_algorithm(district, mutation_function, cost_type = 'shared', convergence_treshold = 50):
    '''
    Input: starting district, convergence treshold
    returns: new district with lowest cost


    Pseudo code:
    While not converged:
        Begin with random start state
        Induce small change to the state (randomly swap the battery connections of two houses)
        If the cost goes up:
            Disregard the change
    '''
    no_improvements = 0

    # house_x, house_y, house_colour, battery_x, battery_y, battery_colour = visualisation.setup_plot(district)

    while no_improvements < convergence_treshold:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Mutate the district by swapping connection and/or changing the routes
        if mutation_function == 'swapping_connections':
            swapping_connections(new_district.connections)
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
            print(new_cost)

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0

        # PLOT PART BELOW
        #visualisation.draw(district)

    return district
