from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import random, a_star
from code.experiments import experiment1

'''
Voor nu heb ik een paar stappen eruit gecomment aangezien we nog aan het testen zijn
'''

# -------------------------------- Input ----------------------------------
district_number = 3
experiment_runs = 1000


# --------------------------- Create district -----------------------------
district = district.District(district_number)


# ----------------------------- Random Route ------------------------------
random.random_routes(district)


# ------------------------------ A* Route ---------------------------------
#a_star.a_star_routes(district)


# ----------------------- District Visualisation ---------------------------
visualisation.visualise(district)


# ------------------------------ Output ------------------------------------
#output.generate_json(district)


# ----------------------------- Experiment ---------------------------------
#experiment1.experiment(district_number, experiment_runs)
