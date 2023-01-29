from code.algorithms import a_star_route, random as rando
from code.classes import district
import random
import copy
import random
import math

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


def simulated_annealing_algorithm(district, temperature = 1000, cooling_rate = 0.99):
    '''
    Input: starting district, temperature, cooling rate
    returns: new district with lowest cost


    Pseudo code:
    While temperature > 1:
        Begin with random start state
        Induce small change to the state (randomly swap the battery connections of two houses)
        If random number > probability(new_cost, old_cost, temperature):
            Disregard the change
        Lower the temperature
    '''
    while temperature > 1:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Swapping a house-battery connnection
        swapping_connections(new_district.connections)

        # Calculate costs
        new_cost = new_district.calculate_shared_cost()
        old_cost = district.calculate_shared_cost()

        # Calculate the probability of accepting this new district
        delta = new_cost - old_cost
        probability = math.exp(-delta / temperature)

        # if random falls in probabilty range, new district is accepted
        if random.random() > probability:

            # Return to the previous state
            new_district = district

        else:
            # Keep the new state
            district = new_district

            # Comment out if you don't want to see the costs go down:
            print(district.calculate_shared_cost())

        # Lower the temperature
        temperature *= cooling_rate


    return district
