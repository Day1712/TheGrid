import pandas as pd
import numpy as np
import os
import re
import seaborn as sns
import matplotlib.pyplot as plt

# Hill Climber transformation
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
hill_df["shared"] = hill_df["shared"] - 25000
hill_df["own"] = hill_df["own"] - 25000
hill_df = hill_df.drop(columns=["iteration", "algorithm"])
hill_df = hill_df.astype({"district": "int64", "parameter": "int64", "shared": "int64", "own": "int64"})
#print(hill_df)

# Simulated Annealing transformation
directory = "simulated_annealing"
sim_df = pd.DataFrame(columns=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path) and num_there(path) == True:
        current_df = pd.read_csv(path, header=0, names=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])
        sim_df = pd.concat([sim_df, current_df], ignore_index=True)

new = sim_df["parameter"].str.split(" and", n = 1, expand = True)
new1 = new[0].str.split("of ", n = 1, expand = True)
new2 = new[1].str.split("of ", n = 1, expand = True)

sim_df.insert(4, "temp", new1[1])
sim_df.insert(5, "random_selection", new2[1])
sim_df["shared"] = sim_df["shared"] - 25000
sim_df["own"] = sim_df["own"] - 25000
sim_df = sim_df.drop(columns=["iteration", "algorithm", "parameter"])
sim_df = sim_df.astype({"district": "int64", "temp": "int64", "random_selection": "int64", "shared": "int64", "own": "int64"})
#print(sim_df)

# Random transformation
directory = "random"
random_df = pd.DataFrame(columns=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path) and num_there(path) == True:
        current_df = pd.read_csv(path, header=0, names=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])
        random_df = pd.concat([random_df, current_df], ignore_index=True)

random_df = random_df.drop(columns=["iteration", "algorithm", "parameter"])
random_df = random_df.astype({"district": "int64", "shared": "int64", "own": "int64"})
#print(random_df)

random_10000_df = pd.read_csv("random/10000runs_experiment_random3.csv", header=0, names=["iteration", "algorithm", "district", "parameter", "shared", "own", "time"])
random_10000_df = random_10000_df.drop(columns=["iteration", "algorithm", "parameter"])
random_10000_df = random_10000_df.astype({"district": "int64", "shared": "int64", "own": "int64"})
random_10000_df["shared"] = random_10000_df["shared"] - 25000
random_10000_df["own"] = random_10000_df["own"] - 25000

"""
# Barplot comparing random selection for Hill Climber
district3 = hill_df[hill_df["district"] == 3]
print(district3)
fig, ax = plt.subplots()
ax = sns.barplot(data=district3, x="parameter", y="shared", ci=None)
ax.set_title("Hill Climber: District 3")
ax.set_xlabel("Random Selection")
ax.set_ylabel("Shared Cost")
for i in ax.containers:
    ax.bar_label(i,)
plt.savefig("figures/hill_d3")
plt.show()
"""
"""
# Barplot comparing temperature and random selection for Simulated Annealing
district3 = sim_df[sim_df["district"] == 3]
fig, ax = plt.subplots(figsize=(10,7))
ax = sns.barplot(data=district3, x="random_selection", y="shared", hue="temp", ci=None)
ax.legend(title='Temperature')
sns.move_legend(ax, "lower right")
ax.set_title("Simulated Annealing: District 3")
ax.set_xlabel("Random Selection")
ax.set_ylabel("Shared Cost")
for i in ax.containers:
    ax.bar_label(i,)
plt.savefig("figures/sim_both_d3")
plt.show()


# Barplot comparing random selection for Simulated Annealing
district3 = sim_df[sim_df["district"] == 3]
fig, ax = plt.subplots(figsize=(10,7))
ax = sns.barplot(data=district3, x="temp", y="shared", ci=None)
ax.set_title("Simulated Annealing: District 3")
ax.set_xlabel("Temperature")
ax.set_ylabel("Shared Cost")
for i in ax.containers:
    ax.bar_label(i,)
plt.savefig("figures/sim_temp_d3")
plt.show()

# Barplot comparing temperature for Simulated Annealing
district3 = sim_df[sim_df["district"] == 3]
fig, ax = plt.subplots(figsize=(10,7))
ax = sns.barplot(data=district3, x="random_selection", y="shared", ci=None)
ax.set_title("Simulated Annealing: District 3")
ax.set_xlabel("Random Selection")
ax.set_ylabel("Shared Cost")
for i in ax.containers:
    ax.bar_label(i,)
plt.savefig("figures/sim_random_sel_d3")
plt.show()
"""

fig, ax = plt.subplots(figsize=(10,7))
ax = sns.histplot(data=random_10000_df, x="shared", bins=20)
ax.set_title("Random: District 3 (10000 iterations)")
ax.set_xlabel("Shared Cost")
ax.set_ylabel("Iteration count")
plt.savefig("figures/random_hist_d3")
plt.show()



















"""
# Compare algorithms per district

# Shared cost district 1
d1_hill_average_shared = hill_df[hill_df["district"] == 1]["shared"].mean() - 25000
print(f"d1_hill_average_shared: {d1_hill_average_shared}")

d1_sim_average_shared = sim_df[sim_df["district"] == 1]["shared"].mean() - 25000
print(f"d1_sim_average_shared: {d1_sim_average_shared}")

d1_random_average_shared = random_df[random_df["district"] == 1]["shared"].mean() - 25000
print(f"d1_random_average_shared: {d1_random_average_shared}")

# Own cost district 1
d1_hill_average_own = hill_df[hill_df["district"] == 1]["own"].mean() - 25000
print(f"d1_hill_average_own: {d1_hill_average_own}")

d1_sim_average_own = sim_df[sim_df["district"] == 1]["own"].mean() - 25000
print(f"d1_sim_average_own: {d1_sim_average_own}")

d1_random_average_own = random_df[random_df["district"] == 1]["own"].mean() - 25000
print(f"d1_random_average_own: {d1_random_average_own}")

# Time district 1
d1_hill_average_time = hill_df[hill_df["district"] == 1]["time"].mean()
print(f"d1_hill_average_time: {d1_hill_average_time}")

d1_sim_average_time = sim_df[sim_df["district"] == 1]["time"].mean()
print(f"d1_sim_average_time: {d1_sim_average_time}")

d1_random_average_time = random_df[random_df["district"] == 1]["time"].mean()
print(f"d1_random_average_time: {d1_random_average_time}")



# Shared cost district 2
d2_random_average_shared = random_df[random_df["district"] == 2]["shared"].mean() - 25000
print(f"d2_random_average_shared: {d2_random_average_shared}")

d2_hill_average_shared = hill_df[hill_df["district"] == 2]["shared"].mean() - 25000
print(f"d2_hill_average_shared: {d2_hill_average_shared}")

d2_sim_average_shared = sim_df[sim_df["district"] == 2]["shared"].mean() - 25000
print(f"d2_sim_average_shared: {d2_sim_average_shared}")
print()

# Own cost district 2
d2_random_average_own = random_df[random_df["district"] == 2]["own"].mean() - 25000
print(f"d2_random_average_own: {d2_random_average_own}")

d2_hill_average_own = hill_df[hill_df["district"] == 2]["own"].mean() - 25000
print(f"d2_hill_average_own: {d2_hill_average_own}")

d2_sim_average_own = sim_df[sim_df["district"] == 2]["own"].mean() - 25000
print(f"d2_sim_average_own: {d2_sim_average_own}")
print()

# Time district 2
d2_random_average_time = random_df[random_df["district"] == 2]["time"].mean()
print(f"d2_random_average_time: {d2_random_average_time}")

d2_hill_average_time = hill_df[hill_df["district"] == 2]["time"].mean()
print(f"d2_hill_average_time: {d2_hill_average_time}")

d2_sim_average_time = sim_df[sim_df["district"] == 2]["time"].mean()
print(f"d2_sim_average_time: {d2_sim_average_time}")

# Shared cost district 3
d3_random_average_shared = random_df[random_df["district"] == 3]["shared"].mean() - 25000
print(f"d3_random_average_shared: {d3_random_average_shared}")

d3_hill_average_shared = hill_df[hill_df["district"] == 3]["shared"].mean() - 25000
print(f"d3_hill_average_shared: {d3_hill_average_shared}")

d3_sim_average_shared = sim_df[sim_df["district"] == 3]["shared"].mean() - 25000
print(f"d3_sim_average_shared: {d3_sim_average_shared}")
print()

# Own cost district 3
d3_random_average_own = random_df[random_df["district"] == 3]["own"].mean() - 25000
print(f"d3_random_average_own: {d3_random_average_own}")

d3_hill_average_own = hill_df[hill_df["district"] == 3]["own"].mean() - 25000
print(f"d3_hill_average_own: {d3_hill_average_own}")

d3_sim_average_own = sim_df[sim_df["district"] == 3]["own"].mean() - 25000
print(f"d3_sim_average_own: {d3_sim_average_own}")
print()

# Time district 3
d3_random_average_time = random_df[random_df["district"] == 3]["time"].mean()
print(f"d3_random_average_time: {d3_random_average_time}")

d3_hill_average_time = hill_df[hill_df["district"] == 3]["time"].mean()
print(f"d3_hill_average_time: {d3_hill_average_time}")

d3_sim_average_time = sim_df[sim_df["district"] == 3]["time"].mean()
print(f"d3_sim_average_time: {d3_sim_average_time}")
"""
#
