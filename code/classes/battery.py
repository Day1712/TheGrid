class Battery():
    '''
    This class defines battery properties.
    '''
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.capacity = capacity
        self.colour = 'limegreen'
        # low priority TODO: instead of markers, find a way to use pictures in the plot
