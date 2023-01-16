import pandas as pd
import matplotlib.pyplot as plt

# Load the house data
houses = pd.read_csv("district_1/district-1_houses.csv")

# Load the battery data and process the 'positive' column to separate x and y coordinates
batteries = pd.read_csv("district_1/district-1_batteries.csv")
batteries[['x', 'y']] = batteries['positie'].str.split(',', expand=True)

import pandas as pd
from scipy.optimize import minimize

# Import dataframe containing houses
houses_df = houses
# Import dataframe containing batteries
batteries_df = batteries

# Set the cost of batteries
battery_cost = 5000

# Set the cost of cables
cable_cost = 9

# Create a function to calculate the total cost of the SmartGrid
def total_cost(assignment):
    # Initialize the total cost
    total_cost = 0

    # Add the cost of the batteries
    total_cost += len(batteries_df) * battery_cost

    # Calculate the total cable cost
    cable_cost = 0
    for i, house in enumerate(houses_df.itertuples()):
        battery_id = int(assignment[i])
        cable_cost += abs(house.x_coord - batteries_df.loc[battery_id, 'x_coord']) + abs(house.y_coord - batteries_df.loc[battery_id, 'y_coord'])
    total_cost += cable_cost * 9
    return total_cost

# Create a function to check the constraints
def constraints(assignment):
    # Initialize the total capacity for each battery
    total_capacity = [0 for _ in range(len(batteries_df))]

    # Assign the house to the battery and check the capacity constraints
    for i, house in enumerate(houses_df.itertuples()):
        battery_id = int(assignment[i])
        total_capacity[battery_id] += house.max_output

        if total_capacity[battery_id] > batteries_df.loc[battery_id, 'capacity']:
            return False
    return True

# Create the bounds for the decision variables
bounds = [(0, len(batteries_df) - 1) for _ in range(len(houses_df))]

# Create the initial solution
initial_solution = [0 for _ in range(len(houses_df))]

# Call the optimization algorithm
result = minimize(total_cost, initial_solution, bounds=bounds, constraints=constraints)

# Extract the optimal assignment
assignment = result.x

# Assign the houses to the batteries
for i, house in enumerate(houses_df.itertuples()):
    battery_id = int(assignment[i])
    house.battery_id = battery_id
