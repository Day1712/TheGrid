from code.classes import cable

class House():
    '''
    This class defines the house properties
    '''
    def __init__(self, pos_x, pos_y, output):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.location = f'{pos_x}, {pos_y}'
        self.output = float(output)
        self.colour = None
        self.cables = cable.Cable()
