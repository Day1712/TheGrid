class Cable:
    def __init__(self, battery, house, color):
        self.battery = battery
        self.house = house
        self.color = color

    def lay_cable(self):
        start_x = self.house.house_x
        start_y = self.house.house_y
        end_x = self.battery.battery_x
        end_y = self.battery.battery_y

        self.cable_xs = []
        self.cable_ys = []
        self.cable_xs.append(start_x)
        self.cable_ys.append(start_y)

        current_x = start_x
        current_y = start_y

        while current_x != end_x or current_y != end_y:
            if current_x != end_x:
                current_x += 1 if end_x > start_x else -1
                self.cable_xs.append(current_x)
                self.cable_ys.append(current_y)
                
            if current_y != end_y:
                current_y += 1 if end_y > start_y else -1
                self.cable_xs.append(current_x)
                self.cable_ys.append(current_y)

        return self.cable_xs, self.cable_ys
