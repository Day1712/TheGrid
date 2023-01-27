from code.algorithms import random as rando
from code.classes import district
import random
import copy

'''
DUURT ONGEVEER EEN MINUUT


Pseudo code:

Genereer een random start state
Herhaal tot de kosten na N-keer niet meer verbeteren:
    Doe een kleine random aanpassing: ruil de batterijen om van 2 huizen
    Als de kost is omlaag gaat:
        terug naar vorige staat
'''

def swapping_connections(connections_dict):
    continue_loop = True

    while continue_loop:
        # Randomly picking two houses
        house_1, house_2 = random.sample(list(connections_dict), 2)
        battery_1, battery_2 = connections_dict[house_1], connections_dict[house_2]

        # Only swap if solution stays valid
        # (TODO change this long if statement into something readable)
        if ((battery_1.current_capacity - house_1.output) + house_2.output) <= battery_1.max_capacity and ((battery_2.current_capacity - house_2.output) + house_1.output) <= battery_2.max_capacity:

            # Update battery capacities
            battery_1.current_capacity += -house_1.output + house_2.output
            battery_2.current_capacity += -house_2.output + house_1.output

            # Remove previous cable segments
            house_1.cables.cable_segments = []
            house_2.cables.cable_segments = []

            # Create new cable routes
            rando.create_route(house_1, battery_2)
            rando.create_route(house_2, battery_1)

            # Updating the connections_dict with new connections
            connections_dict[house_1] = battery_1
            connections_dict[house_2] = battery_2

            # Stop the loop
            continue_loop = False

def hill_climber_algorithm(district, convergence_treshold = 10):
    no_improvements = 0

    while no_improvements < convergence_treshold:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Swapping a house-battery connnection
        swapping_connections(new_district.connections)

        # Calculate costs
        new_cost = new_district.calculate_shared_cost()
        old_cost = district.calculate_shared_cost()

        # Undo if solution is costs went up (or district is not valid)
        if new_cost > old_cost:
            new_district = district

        # Continue with the new_district if costs go down
        else:
            district = new_district

            # Uncomment if you want to see the costs go down:
            print(district.calculate_shared_cost())

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0

    return district
