from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import invalid_shortest_route, valid_shortest_route
from code.experiments import experiment1


# -------------------------------- Input ----------------------------------
district_number = 4
experiment_runs = 100

# --------------------------- Shortest route -------------------------------
'''
Make cable routes WITH taking capacity and output levels into account. The order
of creating routes for each house is random, so each run produces different
results
'''
district = district.District(district_number)
valid_shortest_route.random_shortest_route(district)

# --------------------------- Visualisation --------------------------------
visualisation.visualise(district)

# ------------------------------ Output ------------------------------------
output.generate_json(district)

# ----------------------------- Experiment ---------------------------------
'''
Calculates the average cost of a number of runs
'''
experiment1.experiment(district_number, experiment_runs)
