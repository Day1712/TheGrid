from code.algorithms import random
from code.algorithms import hill_climber
from code.classes import district
import pandas as pd
import time

def experiment_hill_climb(district_number, number_of_runs):
    # Create data dictionary for the results
    data = {'algorithm': [],
            'district': [],
            'parameters': [],
            'shared cost': [],
            'own cost': [],
            'time': []}

    for i in range(number_of_runs):
        # Load the district (1, 2, or 3)
        the_district = district.District(district_number)

        # Create starting state with random solution
        random.create_all_routes(the_district)

        # Parameters
        if i <= 18:
            random_selection =  50
        elif i <= 36:
            random_selection =  50
        else:
            random_selection = 150

        # Keep track of time
        start_time = time.time()

        # Run the algorithm
        the_district = hill_climber.hill_climber_algorithm(the_district, mutation_function = 'swapping_connections', cost_type = 'own', random_selection = random_selection)
        the_district = hill_climber.hill_climber_algorithm(the_district, mutation_function = 'new_route', cost_type = 'shared', random_selection = random_selection)

        # Stop the clock
        end_time = time.time() - start_time

        # Save the results
        data['algorithm'].append('hill_climber')
        data['district'].append(district_number)
        data['parameters'].append(f'random selection of {random_selection}')
        data['shared cost'].append(the_district.shared_cost)
        data['own cost'].append(the_district.own_cost)
        data['time'].append(end_time)

        # Start clean next iteration
        the_district.reset_grid()

        print(f'We finished loop {i+1} of hill climber experiment')

    # Save results as csv
    df = pd.DataFrame(data)
    df.to_csv('experiment_hill_climb.csv', header=True)
