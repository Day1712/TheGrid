import csv
from code.classes import house, battery

#TODO calculate overal cost of the cables

class District():
    '''
    This class makes houses and batteries objects.
    '''
    def __init__(self, district_number):
        self.district_number = district_number
        self.grid_inputs = []
        self.batteries = []
        self.houses = []
        self.own_cost = 0
        self.shared_cost = None #TODO calculate cost without overlapping
        self.price_cable = 9
        self.price_battery = 5000
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

    def calculate_own_cost(self):
        '''
        Calculate the cost of the cables and batteries. All shared segments are
        counted without taking overlapping ones into account (thus this is own
        cost and not shared)
        '''
        segments = 0
        for house in self.houses:
            # Segments are the lines between the coordinates (therefore -1)
            segments += len(house.cables) - 1

        self.own_cost = self.price_cable * segments + self.price_battery * len(self.batteries)
