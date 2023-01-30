class Cable():
    '''
    This class defines cables properties.
    '''
    def __init__(self):
        self.coordinates = []
        self.segments = [] # Example: [ ((1,1), (1,2)), ((1,2), (1,3)) ]
        self.price = 9
        # TODO net zoals bij huis en batterij hier ook een kleur toe te wijzen.
        # Tip van wouter was om batterijen verschillende kleuren te geven en de
        # kabels daarbij te matchen voor beter overzicht (begreep ik dat goed?)

    def create_route(self, start, end):
        x1, y1 = start
        x2, y2 = end

        self.coordinates.append(start)

        while (x1, y1) != (x2, y2):
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
            elif y1 < y2:
                y1 += 1
            else:
                y1 -= 1
            self.coordinates.append((x1, y1))

    # A segment consists out of two adjacent points in the route
    def create_cable_segments(self):
        for i in range(len(self.coordinates) - 1):
            self.segments.append((self.coordinates[i], self.coordinates[i + 1]))

    # Start clean
    def clear_route(self):
        self.coordinates = []
        self.segments = []

    # Get a list of the coordinates of the cable routes for the json output
    def get_route_list_string(self):
        new_list = []

        for segment in self.cable_segments:
            new_list.append(",".join(map(str, segment[0])))

        new_list.append(",".join(map(str, self.cable_segments[-1][-1])))
        return new_list
