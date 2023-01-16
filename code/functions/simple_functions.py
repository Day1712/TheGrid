
# simple functions for later use
def get_coordinate(x, y):
    coordinate = str(int(x)) + "," + str(int(y))
    return coordinate

def manhattan_distance(house_x, house_y, battery_x, battery_y):
    distance = abs(house_x - battery_x) + abs(house_y - battery_y)
    return distance
