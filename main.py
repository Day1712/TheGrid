from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import shortest_route


district_number = 3
district = district.District(district_number)

# -------------------- Shortest route (with overlap)------------------------
# Make cable routes without checking for capacity and output levels
shortest_route.shortest_route(district)

# --------------------------- Visualisation --------------------------------
# Plot the district
visualisation.visualise(district)

# ------------------------------ Output ------------------------------------
# Save output as json file
output.generate_json(district)
