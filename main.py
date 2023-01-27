from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, random_a_star, hill_climber
from code.experiments import experiment1

# -------------------------------- Input ----------------------------------
district_number = 3
experiment_runs = 500


# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Route ------------------------------
random.create_all_routes(district)


# --------------------------- Random A* Route ------------------------------
#random_a_star.create_all_routes(district)

# ----------------------- Hill Climber with Random  -----------------------
district = hill_climber.hill_climber_algorithm(district)


# ----------------------- District Visualisation ---------------------------
visualisation.visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment1.experiment(district_number, experiment_runs)
