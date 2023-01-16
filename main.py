from code.functions import load_entities
from code.algorithms import closest, random
from code.output import output_creator
from code.visualization import plot

# load, plot and save json for district 1
houses_1 = load_entities.load_houses("data/Huizen&Batterijen/district_1/district-1_houses.csv")
batteries_1 = load_entities.load_batteries("data/Huizen&Batterijen/district_1/district-1_batteries.csv")
cables_1 = closest.closest_cables(houses_1, batteries_1)

plot.plot(houses_1, batteries_1, cables_1)
output_creator.compute_total_cable_length(cables_1)
output_creator.compute_total_cable_cost(cables_1)
print(output_creator.create_json_output(1, houses_1, batteries_1, cables_1))
