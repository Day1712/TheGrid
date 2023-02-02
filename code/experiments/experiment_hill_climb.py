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

    # Parameters
    random_selection_options = [10, 50, 150]


    for i in range(number_of_runs):
        # Load the district (1, 2, or 3)
        the_district = district.District(district_number)

        # Create starting state with random solution
        random.create_all_routes(the_district)

        # Parameters
        selection_index = i // (number_of_runs // 3)
        random_selection = random_selection_options[min(selection_index, len(random_selection_options) - 1)]

        # Keep track of time
        start_time = time.time()

        # Run the algorithm
        the_district = hill_climber.hill_climber_algorithm(the_district, random_selection = random_selection)

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

        print(f'Loop {i+1} of hill climber experiment is completed')

    # Save results as csv
    df = pd.DataFrame(data)
    df.to_csv(f'code/experiments/results/hill_climber/experiment_hill_climb{district_number}.csv', header=True)
