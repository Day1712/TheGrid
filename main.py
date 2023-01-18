from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import invalid_shortest_route, valid_shortest_route
from code.experiments import experiment1


# -------------------------------- Input ----------------------------------
district_number = 1
district = district.District(district_number)


# --------------------------- Shortest route -------------------------------
'''
Make cable routes WITH taking capacity and output levels into account. The order
of creating routes for each house is random, so each run produces different
results
'''
valid_shortest_route.random_shortest_route(district)

# --------------------------- Visualisation --------------------------------
visualisation.visualise(district)

# ------------------------------ Output ------------------------------------
output.generate_json(district)

# ----------------------------- Experiment ---------------------------------
experiment1.experiment(district)
