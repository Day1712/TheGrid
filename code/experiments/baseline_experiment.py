from code.algorithms import baseline
from code.functions import load_entities
import numpy as np
import matplotlib.pyplot as plt


def experiment(district_number, number_of_runs):
    iterations = list(range(number_of_runs))
    all_costs = []
    for i in range(number_of_runs):

        houses = load_entities.load_houses(f"data/Huizen_Batterijen/district_{district_number}/district-{district_number}_houses.csv")
        batteries = load_entities.load_batteries(f"data/Huizen_Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
        current_cost, cables = baseline.random_shortest_route(houses, batteries)
        all_costs.append(current_cost)

    print(f'The average own cost over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')
    lowest_cost = min(all_costs)
    highest_cost = max(all_costs)
    print(f"Lowest cost found: {lowest_cost}")
    print(f"Highest cost found: {highest_cost}")

    return iterations, all_costs, houses, batteries, cables



def plot(iterations, all_costs):
    plt.plot(iterations, all_costs, 'b.')
    plt.show()
