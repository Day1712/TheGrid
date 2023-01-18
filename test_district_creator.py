import pandas as pd

x_houses = [1, 7, 3, 4, 4, 3, 1, 7, 4, 9]
y_houses = [3, 8, 8, 1, 9, 5, 6, 2, 7, 3]
maxoutput = [51.81241388, 54.14676516, 47.72196575, 49.07862835, 51.95373609, 48.01846294, 53.85924912, 49.85021052, 50.14676516, 47.72196575]

test_houses = pd.DataFrame(list(zip(x_houses, y_houses, maxoutput)), columns=["x", "y", "maxoutput"])
print(test_houses)

test_houses.to_csv("data/Huizen_Batterijen/district_max/houses_max.csv", index=False)

positions = ["2,5", "6,3"]
capacity = [260, 260]

test_batteries = pd.DataFrame(list(zip(positions, capacity)), columns=["positie", "capaciteit"])
print(test_batteries)

test_batteries.to_csv("data/Huizen_Batterijen/district_max/batteries_max.csv", index=False)
