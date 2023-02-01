from code.visualisation import visualisation
from code.classes import district
from code.algorithms import mutation_functions as mutation
import copy

def simulated_annealing_algorithm(district, mutation_function, cost_type, move_batteries = False, temperature = 5000, cooling_rate = 0.99, random_selection = 20):
    '''
    Input:
    - valid starting district (made by random)
    - mutation functions (swapping connections or new route)
    - move batteries (False or True)
    - cost type (shared or own)
    - temperature (number above 1)
    - cooling rate (number between 0 and 1)
    - random selection (number for the selection amount of the mutation swapping batteries)

    Returns:
    - new district with lowest cost

    Pseudo code:
    - While temperature > 1:
        - Begin with random start state
        - Induce small change to the state (either swap houses or make new routes)
        - If random number > probability(new_cost, old_cost, temperature):
            - Disregard the change
        - Lower the temperature
    '''
    while temperature > 1:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Mutate the district
        if mutation_function == 'swapping_connections':
            mutation.swapping_connections(new_district.connections, random_selection)

            if move_batteries:
                mutation.change_battery_location(new_district.connections)

        elif mutation_function == 'new_route':
            mutation.new_route(new_district.connections)

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

            # Uncomment if you want to see the costs go down:
            print(district.calculate_shared_cost())

        # Lower the temperature
        temperature *= cooling_rate

    return district
