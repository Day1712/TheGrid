from code.visualisation import visualisation
from code.classes import district
from code.algorithms import mutation_functions as mutation
import copy

def hill_climber_algorithm(district, plot = "n", move_batteries = False, convergence_threshold = 50, random_selection = 50):
    '''
    Input:
    - valid starting district (made by random)
    - plot (static, live, or battery)
    - move batteries (True or False)
    - convergence threshold (number > 1)
    - random selection (number for the selection amount of the mutation 'swapping batteries')

    returns:
    - new district with lowest cost

    Pseudo code:
    - Begin with random start state
    - Loops twice (first focussing on connections, then routes)
        - While not converged:
            - Induce small change to the state
            - If the cost goes up:
                - Disregard the change
                - Keep track of convergence
    '''
    # Set up plot
    if plot == "y":
        fig, ax1, ax2 = visualisation.setup_plot(district)
        iterations = []
        cost_list = []
        iteration = 1

    # Makes a copy of the district to work with
    new_district = copy.deepcopy(district)

    # Perform algorithm twice
    for i in range(2):
        no_improvements = 0

        # Loop until the same cost is found more than {threshold} times
        while no_improvements < convergence_threshold:

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

            # Undo if solution is costs went up
            if new_cost > old_cost:
                new_district = district

            else:
                # Continue with the new_district
                district = new_district

                # Check if local minimum is found
                if new_cost == old_cost:
                    no_improvements += 1
                else:
                    no_improvements = 0

                # PLOT
                if plot == "y":
                    cost_list.append(new_cost)
                    iterations.append(iteration)
                    iteration += 1
                    visualisation.draw_district(district, fig, ax1, ax2, cost_list, iterations)

    return district
