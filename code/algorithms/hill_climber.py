from code.algorithms import a_star_route, random as rando
from code.visualisation import visualisation
from code.classes import district
import numpy as np
import random
import copy

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def new_route(connections_dict):
    # Pick house with longest route
    #house = max(connections_dict, key=lambda x: len(x.cables.segments))

    # Pick random house
    house = random.choice(list(connections_dict.keys()))

    # Corresponding battery
    battery = connections_dict[house]

    # List of all houses connected to the battery
    same_battery_houses = [k for k, v in connections_dict.items() if v == battery and k != house]

    # List of all the cable points that another cable can connect to
    cable_coordinates = set()
    for house in same_battery_houses:
        for coordinate in house.cables.coordinates:
            cable_coordinates.add(coordinate)


    # Calculate manhattan distances
    distances = []
    for coordinate in list(cable_coordinates):
        if coordinate != None:
            distances.append(manhattan_distance(house.coordinate, coordinate))

    # Find the nearest
    nearest_index = np.argmin(distances)

    # Delete previous
    house.cables.clear_route()

    # Create route to the nearest point
    house.cables.create_route(house.coordinate, list(cable_coordinates)[nearest_index])

    # Add the route from the point to the battery (so it stays connected to the battery)
    house.cables.create_route(list(cable_coordinates)[nearest_index], battery.coordinate)


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
                connections_dict[house_1] = battery_1
                connections_dict[house_2] = battery_2

                # Stop the loop
                continue_loop = False

def hill_climber_algorithm(district, convergence_treshold = 20):
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

        # Swapping a house-battery connnection
        swapping_connections(new_district.connections)

        # Making a new route
        #new_route(new_district.connections)

        # Calculate costs
        new_cost = new_district.calculate_shared_cost()
        old_cost = district.calculate_shared_cost()

        #print(new_cost)

        new_district.valid_solution()

        # Undo if solution is costs went up (or district is not valid)
        if new_cost > old_cost or not new_district.valid:
            new_district = district

        else:
            # Continue with the new_district if costs go down
            district = new_district

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0

            # Comment out if you don't want to see the costs go down:
            print(new_cost)

        # PLOT PART BELOW
        #visualisation.draw(district)

    return district


'''
HERE IS THE CODE THAT STARTS WITH RANDOM BUT CREATES NEW ROUTES WITH A*.
TAKES A FEW MINUTES.

Results are worse than ^ where routes are created horizontally and then
vertically towards the battery. That's why this is commented out for now. Will
clean it up soon.





def swapping_connections(connections_dict, cable_coordinates):
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
                house_1.cables.cable_segments = []
                house_2.cables.cable_segments = []

                # Create new cable routes
                a_star_route.create_route(house_1, battery_2, cable_coordinates)
                a_star_route.create_route(house_2, battery_1, cable_coordinates)

                # Updating the connections_dict with new connections
                connections_dict[house_1] = battery_1
                connections_dict[house_2] = battery_2

                # Stop the loop
                continue_loop = False

def hill_climber_algorithm(district, convergence_treshold = 75):
    no_improvements = 0

    while no_improvements < convergence_treshold:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Updates cable coordinates
        new_district.update_cable_coordinates()

        # Swapping a house-battery connnection
        swapping_connections(new_district.connections, new_district.cable_coordinates)

        # Calculate costs
        new_cost = new_district.calculate_shared_cost()
        old_cost = district.calculate_shared_cost()

        # Undo if solution is costs went up (or district is not valid)
        if new_cost > old_cost:
            new_district = district

        else:
            # Continue with the new_district if costs go down
            district = new_district

            # Uncomment if you want to see the costs go down:
            print(district.calculate_shared_cost())

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0

    return district
'''
