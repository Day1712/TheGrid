from code.algorithms import random
from code.classes import district

def experiment(district_number, number_of_runs):
    all_costs = []
    for i in range(number_of_runs):
        new_district = district.District(district_number)
        random_route.random_routes(new_district)
        all_costs.append(new_district.shared_cost)

    print(f'The average shared costs over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')

    return
