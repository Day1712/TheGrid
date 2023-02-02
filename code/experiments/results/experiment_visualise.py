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








#
