import numpy as np
import pandas as pd
from heapq import heappop, heappush

# Read csv files with pandas
houses = pd.read_csv("district_1/district-1_houses.csv")
print(houses)

batteries = pd.read_csv("district_1/district-1_batteries.csv")
batteries[['x', 'y']] = batteries['positie'].str.split(',', expand=True)

print(batteries)

# Connect houses to batteries
connected_houses = []
for house in houses:
    closest_battery = None
    closest_distance = float("inf")

    for _,battery in batteries.iterrows():
        # Manhattan distance
        print(battery)
        distance = abs(house[x] - battery[x]) + abs(house[y] - battery[y])
        if distance < closest_distance and battery['capaciteit'] > house['maxoutput']:
            closest_battery = battery
            closest_distance = distance

    if closest_battery is not None:
        closest_battery[capacity] -= house[maxoutput] # Update remaining capacity of battery
        connected_houses.append((house[0], house[1], closest_battery[0], closest_battery[1]))

# Output list of connected houses
for house in connected_houses:
    print("House at (%d, %d) connected to battery at (%d, %d)" % (house[0], house[1], house[2], house[3]))
