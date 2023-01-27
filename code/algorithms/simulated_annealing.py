from code.algorithms import a_star_route, random as rando
from code.classes import district
import random
import copy
import random
import math


'''
NOT WORKING PROPERLY YET. NEED TO DEBUG.


Simulated Annealing,
pseudo code of the lecture example:

Herhaal:
    Kies een random start state
    Kies start temperatuur
    Herhaal N iteraties:
        Doe een kleine random aanpassing
        Als random( ) > kans(oud, nieuw, temperatuur):
            Maak de aanpassing ongedaan
        Verlaag temperatuur

'''
def swapping_connections(connections_dict):
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


def simulated_annealing_algorithm(district, temperature = 100, cooling_rate = 0.99, convergence_treshold = 100):
    no_improvements = 0

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
        if random.random() < probability:

            district = new_district
            no_improvements = 0

            # Comment out if you don't want to see the costs go down:
            print(district.calculate_shared_cost())

        else:
            new_district = district
            no_improvements += 1

        temperature *= cooling_rate

        # check for convergence
        if no_improvements >= convergence_treshold:
            break

    return district
