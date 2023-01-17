from code.classes import district
from code.visualisation import visualisation, output
from code.algorithms import shortest_route


district_number = 3
district = district.District(f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv',
                            f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv')

# -------------------- Shortest route (with overlap)------------------------
# Without checking for capacity and output levels
shortest_route.shortest_route(district)


# --------------------------- Visualisation --------------------------------
visualisation.visualise(district, district_number)


# ------------------------------ Output ------------------------------------
# save output as json file
# visualisation.name_function()
