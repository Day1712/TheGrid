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
    temperature_options = [100, 500, 1000]
    random_selection_options = [10, 50, 150]

    for i in range(number_of_runs):
        # Load the district (1, 2, or 3)
        the_district = district.District(district_number)

        # Create starting state with random solution
        random.create_all_routes(the_district)

        # Change the parameters depending on iteration
        temperature_index = i // (number_of_runs // 3)
        random_selection_index = (i % (number_of_runs // 3)) // (number_of_runs // 9)

        temperature = temperature_options[min(temperature_index, len(temperature_options) - 1)]
        random_selection = random_selection_options[min(random_selection_index, len(random_selection_options) - 1)]

        # Keep track of time
        start_time = time.time()

        # Run the algorithm
        the_district = simulated_annealing.simulated_annealing_algorithm(the_district)

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
    df.to_csv(f'code/experiments/results/simulated_annealing/experiment_sim_ann{district_number}.csv', header=True)
