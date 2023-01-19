from code.algorithms import rhode_algo
from code.functions import load_entities

def experiment(district_number, number_of_runs):
    all_costs = []
    for i in range(number_of_runs):
        houses = load_entities.load_houses(f"data/Huizen_Batterijen/district_{district_number}/district-{district_number}_houses.csv")
        batteries = load_entities.load_batteries(f"data/Huizen_Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
        current_cost = rhode_algo.random_shortest_route(houses, batteries)
        all_costs.append(current_cost)

    print(f'The average own cost over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')
