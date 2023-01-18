from code.algorithms import valid_shortest_route
from code.classes import district

def experiment(district_number, number_of_runs):
    all_costs = []
    for i in range(number_of_runs):
        new_district = district.District(district_number)
        valid_shortest_route.random_shortest_route(new_district)
        all_costs.append(new_district.own_cost)

    print(f'The average own cost over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')

    return
