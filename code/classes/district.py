import csv
import pandas as pd
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

        # Set of cable segments
        self.cable_segments = set()

        # Costs
        self.own_cost = 0
        self.shared_cost = 0

        # Valid solution or not
        self.valid = False

        # Adding battery and house objects into the lists
        self.load_houses(f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv')
        self.load_batteries(f'data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv')

    def load_batteries(self, file_path):
        """This function turns a csv file to a list of battery instances"""
        battery_colours = ['red', 'green', 'blue', 'magenta', 'darkkhaki']
        battery_df_crude = pd.read_csv(file_path)

        # Split coordinate column in two seperate columns
        battery_df = pd.concat(
                    [battery_df_crude["positie"].str.split(',', expand=True),
                     battery_df_crude["capaciteit"]], axis=1)

        for battery_index, battery_data in battery_df.iterrows():
            pos_x, pos_y, capacity = tuple(map(float, battery_data))
            current_battery = battery.Battery(pos_x, pos_y, capacity, battery_colours[battery_index])
            self.grid_inputs.append(current_battery)
            self.batteries.append(current_battery)


    def load_houses(self, file_path):
        """This function turns a csv file into a list of house instances"""
        house_df = pd.read_csv(file_path)

        for house_index, house_data in house_df.iterrows():
            current_house = house.House(*tuple(map(float, house_data)))
            self.grid_inputs.append(current_house)
            self.houses.append(current_house)

    # We won't really have to use the own cost anymore but I left it in for now
    def calculate_own_cost(self):
        '''
        Calculate the cost of the cables and batteries. All shared segments are
        counted without taking overlapping ones into account (thus this is own
        cost and not shared)
        '''
        for house in self.houses:
            self.own_cost += house.cables.price * len(house.cables.segments)

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
        self.all_cable_segments()

        # Multiply the cost of the first house cable price (because all cables
        # have the same cost)
        self.shared_cost = self.houses[0].cables.price * len(self.cable_segments)

        # Add cost for each battery
        for battery in self.batteries:
            self.shared_cost += battery.price

        return self.shared_cost

    def reset_grid(self):
        # Clear connections (house-battery)
        self.connections = {}

        # Clear all cable segments
        for house in self.houses:
            house.cables.clear_route()

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
            print('Not all houses are connected')
            self.valid = False

    def all_cable_segments(self):
        self.cable_segments = set()

        for house in self.houses:
            house.cables.create_cable_segments()

            for segment in house.cables.segments:
                self.cable_segments.add(segment)
