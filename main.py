from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, a_star_route, hill_climber, simulated_annealing
from code.experiments import experiment_random, experiment_sim_ann, experiment_hill_climb

# -------------------------------- Input ----------------------------------
district_number = 3
live_plot = "y"
# experiment_runs = 18

# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Routes ------------------------------
random.create_all_routes(district)


# ------------------------------ Hill Climber  ----------------------------
# district = hill_climber.hill_climber_algorithm(district, mutation_function = 'swapping_connections', cost_type = 'own', plot = live_plot)
district = hill_climber.hill_climber_algorithm(district, mutation_function = 'new_route', cost_type = 'shared', plot = live_plot)


# -------------------------- Simulated Annealing --------------------------
#district = simulated_annealing.simulated_annealing_algorithm(district, mutation_function = 'swapping_connections', cost_type = 'own')
#district = simulated_annealing.simulated_annealing_algorithm(district, mutation_function = 'new_route', cost_type = 'shared')


# ----------------------- District Visualisation ---------------------------
visualisation.basic_static_visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment_random.experiment_random(district_number, experiment_runs)
#experiment_hill_climb1.experiment_hill_climb(district_number, experiment_runs)
#experiment_sim_ann.experiment_sim_ann(district_number, experiment_runs)
