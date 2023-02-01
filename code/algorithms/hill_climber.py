from code.visualisation import visualisation
from code.classes import district
from code.algorithms import mutation_functions as mutation
import copy

def hill_climber_algorithm(district, mutation_function, move_batteries = False, cost_type = 'shared', convergence_treshold = 50, random_selection = 50):
    '''
    Input:
    - valid starting district (made by random)
    - mutation functions (swapping connections or new route)
    - move batteries (True or False)
    - cost type (shared or own)
    - temperature (number above 1)
    - cooling rate (number between 0 and 1)
    - random selection (number for the selection amount of the mutation 'swapping batteries')

    returns:
    - new district with lowest cost

    Pseudo code:
    - While not converged:
        - Begin with random start state
        - Induce small change to the state
        - If the cost goes up:
            - Disregard the change
            - Keep track of convergence
    '''
    no_improvements = 0

    if plot == "y":
        fig, ax1, ax2 = visualisation.setup_plot(district)
        iterations = []
        cost_list = []
        iteration = 1

    while no_improvements < convergence_treshold:
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

        # Undo if solution is costs went up
        if new_cost > old_cost:
            new_district = district
            if plot == "y":
                cost_list.append(old_cost)

        else:
            # Continue with the new_district if costs go down
            district = new_district

            # Uncomment if you want to see the costs go down:
            print(new_cost)

            # Check if local minimum is found
            if new_cost == old_cost:
                no_improvements += 1
            else:
                no_improvements = 0
            if plot == "y":
                cost_list.append(new_cost)

        if plot == "y":
            iterations.append(iteration)
            iteration += 1

        # PLOT PART BELOW
        if plot == "y":
            visualisation.draw_district(district, fig, ax1, ax2, cost_list, iterations)

    return district
