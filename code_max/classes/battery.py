class Battery:
    def __init__(self, battery_x, battery_y, max_capacity, battery_cost=5000):
        self.battery_x = battery_x
        self.battery_y = battery_y
        self.coordinate = get_coordinate(self.battery_x, self.battery_y)
        self.max_capacity = max_capacity
        self.battery_cost = battery_cost
