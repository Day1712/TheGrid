class Battery():
    '''
    This class defines battery properties.
    '''
    def __init__(self, pos_x, pos_y, max_capacity, colour):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.coordinate = (self.pos_x, self.pos_y)
        self.location = f'{self.pos_x}, {self.pos_y}'
        self.max_capacity = float(max_capacity)
        self.current_capacity = 0.0
        self.colour = colour
        self.price = 5000

    def change_location(self, new_location):
        self.pos_x = new_location[0]
        self.pos_y = new_location[1]
        self.coordinate = new_location
