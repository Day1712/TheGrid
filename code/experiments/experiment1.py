from code.algorithms import valid_shortest_route
from code.classes import district

def experiment(district):
    number_of_runs = 200
    all_costs = []
    for i in range(number_of_runs):
        valid_shortest_route.random_shortest_route(district)
        all_costs.append(district.shared_cost)

    print(f'The average shared costs over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')

    return
