from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, a_star_route, hill_climber, simulated_annealing
from code.experiments import experiment_random, experiment_sim_ann, experiment_hill_climb

# -------------------------------- Input ----------------------------------
district_number = 1
experiment_runs = 54

# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Routes ------------------------------
random.create_all_routes(district)


# ------------------------------ Hill Climber  ----------------------------
district = hill_climber.hill_climber_algorithm(district, mutation_function = 'swapping_connections', cost_type = 'own')
district = hill_climber.hill_climber_algorithm(district, mutation_function = 'new_route', cost_type = 'shared')


# -------------------------- Simulated Annealing --------------------------
#district = simulated_annealing.simulated_annealing_algorithm(district, mutation_function = 'swapping_connections', cost_type = 'own')
#district = simulated_annealing.simulated_annealing_algorithm(district, mutation_function = 'new_route', cost_type = 'shared')


# ----------------------- District Visualisation ---------------------------
visualisation.colour_visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment_random.experiment_random(district_number, experiment_runs)
#experiment_hill_climb.experiment_hill_climb(district_number, experiment_runs)
#experiment_sim_ann.experiment_sim_ann(district_number, experiment_runs)
