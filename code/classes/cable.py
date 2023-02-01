class Cable():
    '''
    This class defines cables properties.
    '''
    def __init__(self):
        self.coordinates = []
        self.segments = [] # Example: [ ((1,1), (1,2)), ((1,2), (1,3)) ]
        self.price = 9

    def add_coordinates(self, start, end):
        x = start[0]
        y = start[1]

        # If the cable is left from the goal, the route goes right
        while x < end[0]:
            x += 1
            self.coordinates.append((x, y))
            if x == end[0]:
                break

        # If the cable is right from the goal, the route goes left
        while x > end[0]:
            x -= 1
            self.coordinates.append((x, y))
            if x == end[0]:
                break

        # If the cable is under from the goal, the route goes up
        while y < end[1]:
            y += 1
            self.coordinates.append((x, y))
            if y == end[1]:
                break

        # If the cable is above from goal the route goes down
        while y > end[1]:
            y -= 1
            self.coordinates.append((x, y))
            if y == end[1]:
                break

    def create_route(self, start, end, intermediate_point = None):
        self.coordinates.append(start)

        if intermediate_point:
            self.add_coordinates(start, intermediate_point)
            self.add_coordinates(intermediate_point, end)
        else:
            self.add_coordinates(start, end)

        # Create segment list
        self.create_cable_segments()

    # A segment consists out of two adjacent points in the route
    def create_cable_segments(self):
        #self.segments = []
        for i in range(len(self.coordinates) - 1):
            self.segments.append((self.coordinates[i], self.coordinates[i + 1]))

    # Start clean (but connections in district is remains the same)
    def clear_route(self):
        self.coordinates = []
        self.segments = []

    # Get a list of the coordinates of the cable routes for the json output
    def get_route_list_string(self):
        new_list = []

        for segment in self.segments:
            new_list.append(",".join(map(str, segment[0])))

        new_list.append(",".join(map(str, self.segments[-1][-1])))
        return new_list
