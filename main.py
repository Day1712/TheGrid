from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, a_star_route, hill_climber, simulated_annealing
from code.experiments import experiment1

# -------------------------------- Input ----------------------------------
district_number = 1
experiment_runs = 500


# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Routes ------------------------------
random.create_all_routes(district)


# ------------------------------ Hill Climber  ----------------------------
district = hill_climber.hill_climber_algorithm(district)
for battery in district.batteries:
    print(battery.current_capacity)

# -------------------------- Simulated Annealing --------------------------
# district = simulated_annealing.simulated_annealing_algorithm(district)


# ----------------------- District Visualisation ---------------------------
visualisation.color_visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment1.experiment(district_number, experiment_runs)
