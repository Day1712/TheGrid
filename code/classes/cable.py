from code.classes import house, battery
from code.functions import simple_functions
import random

class Cable:
    def __init__(self, xs, ys, battery, house):
        self.cable_xs = xs
        self.cable_ys = ys
        self.battery = battery
        self.house = house

    def lay_cable(self):
        """This method determines the way the cable is laid down and stores
        corresponding coordinates"""
        # setting start and end points equal to house and battery
        start_x = self.house.house_x
        start_y = self.house.house_y
        end_x = self.battery.battery_x
        end_y = self.battery.battery_y

        # keeping track of cable coordinates
        self.cable_xs = []
        self.cable_ys = []
        self.cable_xs.append(start_x)
        self.cable_ys.append(start_y)
        current_x = start_x
        current_y = start_y

        # the expressions below introduce randomness in laying the cables
        first_direction_options = ["horizontal", "vertical"]
        first_direction = random.choice(first_direction_options)

        # depending on start and end point the cable is made
        if first_direction == "horizontal":
            if end_x < start_x:
                while current_x > end_x:
                    current_x -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_x < end_x:
                    current_x += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

            if end_y < start_y:
                while current_y > end_y:
                    current_y -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_y < end_y:
                    current_y += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
        else:
            if end_y < start_y:
                while current_y > end_y:
                    current_y -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_y < end_y:
                    current_y += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

            if end_x < start_x:
                while current_x > end_x:
                    current_x -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_x < end_x:
                    current_x += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

        # getting one list containing all coordinates
        self.coordinates = []
        for index in range(len(self.cable_xs)):
            self.coordinates.append(simple_functions.get_coordinate(self.cable_xs[index],
                                                   self.cable_ys[index]))

        return self.cable_xs, self.cable_ys

    def compute_cable_length(self):
        """This method calculates complete cable length"""
        self.cable_length = simple_functions.manhattan_distance(max(self.cable_xs),
                                               max(self.cable_ys),
                                               min(self.cable_xs),
                                               min(self.cable_ys))
        return self.cable_length

    def compute_cable_cost(self, cost_per_segment):
        """This method calculates cable costs only,
        so excluding battery cost"""
        self.cable_cost = self.cable_length * cost_per_segment
        return self.cable_cost
