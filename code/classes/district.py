import csv
from code.classes import house, battery, cable

class District():
    '''
    This class ...
    '''
    def __init__(self, district_number):
        self.district_number = district_number
        self.batteries = []
        self.houses = []

        # Houses and batteries in one list (only used for plot, maybe not so smart)
        self.grid_inputs = []

        # Dictionary of house-battery combinations (key: house, value: battery)
        self.connections = {}

        # Costs
        self.own_cost = 0
        self.shared_cost = 0

        # Valid solution or not
        self.valid = False

        # Adding battery and house objects into the lists
        self.load_houses(f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv')
        self.load_batteries(f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv')

    def load_batteries(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:

                # Extract the x, y, and capacity from this specific battery file
                location = [int(x) for x in row['positie'].split(',')]
                x = location[0]
                y = location[1]
                capacity = row['capaciteit']

                # Add the battery to the list
                self.grid_inputs.append(battery.Battery(x, y, capacity))
                self.batteries.append(battery.Battery(x, y, capacity))

    def load_houses(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)

            # Skip the header row
            next(reader)
            for row in reader:

                # Loading the house with the x, y, and max output from the file
                self.grid_inputs.append(house.House(row[0], row[1], row[2]))
                self.houses.append(house.House(row[0], row[1], row[2]))

    # We won't really have to use the own cost anymore but I left it in for now
    def calculate_own_cost(self):
        '''
        Calculate the cost of the cables and batteries. All shared segments are
        counted without taking overlapping ones into account (thus this is own
        cost and not shared)
        '''

        for house in self.houses:
            self.own_cost += house.cables.price * len(house.cables.cable_segments)

        # Add cost for each battery
        for battery in self.batteries:
            self.own_cost += battery.price

        return self.own_cost

    def calculate_shared_cost(self):
        '''
        Calculate the cost of the cables and batteries. Taking into account
        overlap.
        '''

        # Create a set of the union all house cable segments in the grid
        unique_segments = set()
        for house in self.houses:
            for segment in house.cables.cable_segments:
                unique_segments.add(segment)

        # Multiply the cost of the first house cable price (because all cables
        # have the same cost)
        self.shared_cost = self.houses[0].cables.price * len(unique_segments)

        # Add cost for each battery
        for battery in self.batteries:
            self.shared_cost += battery.price

        return self.shared_cost

    def reset_grid(self):
        # Clear connections (house-battery)
        self.connections = {}

        # Clear all cable segments
        for house in self.houses:
            house.cables.clear_segments()

        # Batteries back to current_capacity 0
        for battery in self.batteries:
            battery.current_capacity = 0

    def valid_solution(self):
        self.valid = True

        for battery in self.batteries:
            if battery.current_capacity > battery.max_capacity:
                print(f'Capacity of battery ({battery.pos_x}, {battery.pos_y}) is exceeded with {battery.current_capacity - battery.max_capacity}')
                self.valid = False

        if len(self.connections) != len(self.houses):
            #print('Not all houses are connected')
            self.valid = False
