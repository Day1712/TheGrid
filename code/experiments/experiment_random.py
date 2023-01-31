from code.algorithms import random
from code.classes import district
import pandas as pd
import time

def experiment_random(district_number, number_of_runs):
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

        # Keep track of time
        start_time = time.time()

        # Connect the houses to batteries and plan the routes
        random.create_all_routes(the_district)

        # Stop the clock
        end_time = time.time() - start_time

        # Save the results
        data['algorithm'].append('random')
        data['district'].append(district_number)
        data['parameters'].append('N/A')
        data['shared cost'].append(the_district.shared_cost)
        data['own cost'].append(the_district.own_cost)
        data['time'].append(end_time)

        # Start clean next iteration
        the_district.reset_grid()

        print(f'We finished loop {i+1} of random experiment')

    # Save results as csv
    df = pd.DataFrame(data)
    df.to_csv('experiment_random.csv', header=True)
