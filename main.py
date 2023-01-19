from code.functions import load_entities
from code.algorithms import closest, random
from code.output import output_creator
from code.visualization import plot
from code.output import output_creator
from code.experiments import rhode_experiment
import matplotlib.pyplot as plt
import numpy as np


"""
# load, plot and save json for test district max
test_houses = load_entities.load_houses("data/Huizen_Batterijen/district_max/houses_max.csv")
test_batteries = load_entities.load_batteries("data/Huizen_Batterijen/district_max/batteries_max.csv")
test_cables = random.random_cables(test_houses, test_batteries)

plot.plot(test_houses, test_batteries, test_cables)
# output_creator.compute_total_cable_length(cables_1)
# output_creator.compute_total_cable_cost(cables_1)
# print(output_creator.create_json_output(1, houses_1, batteries_1, cables_1))
"""

# load, plot and save json for given district
district = 1
number_of_runs = 1000
rhode_experiment.experiment(district, number_of_runs)
"""

houses = load_entities.load_houses(f"data/Huizen_Batterijen/district_{district}/district-{district}_houses.csv")
batteries = load_entities.load_batteries(f"data/Huizen_Batterijen/district_{district}/district-{district}_batteries.csv")


cables = closest.closest_cables(houses, batteries)
plot.plot(houses, batteries, cables)
output_creator.compute_total_cable_length(cables)
output_creator.compute_total_cable_cost(cables)
print(output_creator.create_json_output(1, houses, batteries, cables))


iterations = 1000
lowest_cost = None

iteration_list = []
costs_list = []

iteration = 1
for i in range(iterations):
    cables = random.random_cables(houses, batteries)
    output_creator.compute_total_cable_length(cables)
    cost = output_creator.compute_total_cable_cost(cables)
    iteration_list.append(iteration)
    costs_list.append(cost)
    iteration += 1

lowest_cost = np.argmin(costs_list)
plt.plot(iteration_list, costs_list, 'b.')
plt.show()
"""
# plot.plot(houses, batteries, cables)
# output_creator.compute_total_cable_length(cables_1)
# output_creator.compute_total_cable_cost(cables_1)
# print(output_creator.create_json_output(district, houses_1, batteries_1, cables_1))
