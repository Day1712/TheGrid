from code.functions import simple_functions

class House:
    def __init__(self, house_x, house_y, max_output):
        self.house_x = house_x
        self.house_y = house_y
        self.coordinate = simple_functions.get_coordinate(self.house_x, self.house_y)
        self.max_output = max_output