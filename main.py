from code.functions import load_entities
from code.algorithms import closest, random
from code.output import output_creator
from code.visualization import plot

# load, plot and save json for test district max
test_houses = load_entities.load_houses("data/Huizen_Batterijen/district_max/houses_max.csv")
test_batteries = load_entities.load_batteries("data/Huizen_Batterijen/district_max/batteries_max.csv")
test_cables = closest.closest_cables(test_houses, test_batteries)

plot.plot(test_houses, test_batteries, test_cables)
# output_creator.compute_total_cable_length(cables_1)
# output_creator.compute_total_cable_cost(cables_1)
# print(output_creator.create_json_output(1, houses_1, batteries_1, cables_1))
