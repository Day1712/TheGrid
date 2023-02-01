from code.algorithms import random
from code.algorithms import simulated_annealing
from code.classes import district
import pandas as pd
import time

def experiment_sim_ann(district_number, number_of_runs):
    # Create data dictionary for the results
    data = {'algorithm': [],
            'district': [],
            'parameters': [],
            'shared cost': [],
            'own cost': [],
            'time': []}

    # Set changes to parameters
    num_param_changes = 6
    temperature_options = [250, 750]
    random_selection_options = [10, 50, 150]

    for i in range(number_of_runs):
        # Load the district (1, 2, or 3)
        the_district = district.District(district_number)

        # Create starting state with random solution
        random.create_all_routes(the_district)

        # Change parameters depending on iteration
        param_change = i % num_param_changes

        temperature_index = param_change // len(random_selection_options)
        random_selection_index = param_change % len(random_selection_options)
        temperature = temperature_options[temperature_index]
        random_selection = random_selection_options[random_selection_index]

        # Keep track of time
        start_time = time.time()

        # Run the algorithm
        the_district = simulated_annealing.simulated_annealing_algorithm(the_district, mutation_function = 'swapping_connections', cost_type = 'own', temperature = temperature, random_selection = random_selection)
        the_district = simulated_annealing.simulated_annealing_algorithm(the_district, mutation_function = 'new_route', cost_type = 'shared', temperature = temperature, random_selection = random_selection)

        # Stop the clock
        end_time = time.time() - start_time

        # Save the results
        data['algorithm'].append('simulated annealing')
        data['district'].append(district_number)
        data['parameters'].append(f'temperature of {temperature} and random selection of {random_selection}')
        data['shared cost'].append(the_district.shared_cost)
        data['own cost'].append(the_district.own_cost)
        data['time'].append(end_time)

        # Start clean next iteration
        the_district.reset_grid()

        print(f'Loop {i+1} of simulated annealing experiment is completed')

    # Save results as csv
    df = pd.DataFrame(data)
    df.to_csv('code/experiments/results/simulated_annealing/experiment_sim_ann.csv', header=True)
