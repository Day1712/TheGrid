class Cable:
    def __init__(self):
        # Dictionary to store cable segments, where key is the start point and value is the end point
        self.cable_segments = {}
        self.price = 9

    def add_cable_segment(self, start, end):
        """
        A segment consists out of two adjacent points in the grid (start and end)
        Add a new cable segment to the cable_segments dictionary

        Parameters:
        start (tuple): start point of the segment
        end (tuple): end point of the segment
        """
        self.cable_segments[start] = end

    def get_route_list(self):
        """
        Gets a list of coordinates from the cable routes for the plot
        """
        # Adding the first coordinate from the segment for every segment in the dictionary
        cable_plot_list = [start for start in self.cable_segments.keys()]
        # adds last segment (the battery location)
        cable_plot_list.append(self.cable_segments[cable_plot_list[-1]])
        return cable_plot_list

    def get_route_list_string(self):
        """
        Get a list of the coordinates of the cable routes for the json output
        """
        new_list = []
        for start, end in self.cable_segments.items():
            new_list.append(f"{start[0]},{start[1]}")
        new_list.append(f"{end[0]},{end[1]}")
        return new_list
