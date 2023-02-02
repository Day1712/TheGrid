import pandas as pd
import numpy as np
import os
import re

def num_there(s):
    return any(i.isdigit() for i in s)

directory = "hill_climber"
hill_df = pd.DataFrame(columns=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path) and num_there(path) == True:
        current_df = pd.read_csv(path, header=0, names=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])
        hill_df = pd.concat([hill_df, current_df], ignore_index=True)

new = hill_df["parameter"].str.split("of ", n = 1, expand = True)
hill_df["parameter"] = new[1]
hill_df = hill_df.drop(columns=["iteration", "algorithm"])
hill_df = hill_df.astype({"district": "int64", "parameter": "int64", "shared": "int64", "own": "int64"})

print(hill_df)

sim_df = pd.read_csv("simulated_annealing/experiment_sim_ann.csv", header=0, names=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])

new = sim_df["parameter"].str.split(" and", n = 1, expand = True)
new1 = new[0].str.split("of ", n = 1, expand = True)
new2 = new[1].str.split("of ", n = 1, expand = True)

sim_df.insert(4, "temp", new1[1])
sim_df.insert(5, "random_selection", new2[1])
sim_df = sim_df.drop(columns=["iteration", "algorithm", "parameter"])
sim_df = sim_df.astype({"district": "int64", "temp": "int64", "random_selection": "int64", "shared": "int64", "own": "int64"})
print(sim_df)






#
