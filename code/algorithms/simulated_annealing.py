from code.visualisation import visualisation
from code.classes import district
from code.algorithms import mutation_functions as mutation
import math
import copy
import random

def simulated_annealing_algorithm(district, plot = "n", move_batteries = False, input_temperature = 500, cooling_rate = 0.99, random_selection = 20):
    '''
    Input:
    - valid starting district (made by random)
    - move batteries (False or True)
    - plot (static, live, or battery)
    - temperature (number above 1)
    - cooling rate (number between 0 and 1)
    - random selection (number for the selection amount of the mutation swapping batteries)

    Returns:
    - new district with lowest cost

    Pseudo code:
    - Begin with random start state
    - Loops twice (first focussing on connections, then routes)
        - While temperature > 1:
            - Induce small change to the state (either swap houses or make new routes)
            - If random number > probability(new_cost, old_cost, temperature):
                - Disregard the change
            - Lower the temperature
    '''

    if plot == "y":
        fig, ax1, ax2 = visualisation.setup_plot(district)
        iterations = []
        cost_list = []
        iteration = 1

    # Perform algorithm twice
    for i in range(2):
        temperature = input_temperature

        while temperature > 1:

            # Makes a copy of the district to work with
            new_district = copy.deepcopy(district)

            if i == 0:
                # Mutate the district
                mutation.swapping_connections(new_district.connections, random_selection)

                # Change battery locations if ADVANCED option is chosen
                if move_batteries:
                    mutation.change_battery_location(new_district.connections)

                # First focus on own cost (routes are not yet optimalised)
                cost_type = 'own'

            else:
                # Optimalise the routes
                mutation.new_route(new_district.connections)

                # Now focussing on shared costs
                cost_type = 'shared'

            # Calculate costs
            new_cost = new_district.calculate_cost(cost_type)
            old_cost = district.calculate_cost(cost_type)

            # Calculate the probability of accepting this new district
            probability = math.exp(-(new_cost - old_cost) / temperature)

            # if random falls in probabilty range, new district is accepted
            if random.random() > probability:
                # Return to the previous state
                new_district = district

            else:
                # Keep the new state
                district = new_district

                print(new_cost)

            # Lower the temperature
            temperature *= cooling_rate

            # Plot
            if plot == "y":
                cost_list.append(old_cost)
                iterations.append(iteration)
                iteration += 1
                visualisation.draw_district(district, fig, ax1, ax2, cost_list, iterations)

    return district
