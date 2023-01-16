import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import json

# simple functions for later use
def get_coordinate(x, y):
    coordinate = str(int(x)) + "," + str(int(y))
    return coordinate

def manhattan_distance(house_x, house_y, battery_x, battery_y):
    distance = abs(house_x - battery_x) + abs(house_y - battery_y)
    return distance

class House:
    def __init__(self, house_x, house_y, max_output):
        self.house_x = house_x
        self.house_y = house_y
        self.coordinate = get_coordinate(self.house_x, self.house_y)
        self.max_output = max_output

class Battery:
    def __init__(self, battery_x, battery_y, max_capacity, battery_cost=5000):
        self.battery_x = battery_x
        self.battery_y = battery_y
        self.coordinate = get_coordinate(self.battery_x, self.battery_y)
        self.max_capacity = max_capacity
        self.battery_cost = battery_cost

class Cable:
    def __init__(self, battery, house):
        self.battery = battery
        self.house = house

    def lay_cable(self):
        """This method determines the way the cable is laid down and stores
        corresponding coordinates"""
        # setting start and end points equal to house and battery
        start_x = self.house.house_x
        start_y = self.house.house_y
        end_x = self.battery.battery_x
        end_y = self.battery.battery_y

        # keeping track of cable coordinates
        self.cable_xs = []
        self.cable_ys = []
        self.cable_xs.append(start_x)
        self.cable_ys.append(start_y)
        current_x = start_x
        current_y = start_y

        # the expressions below introduce randomness in laying the cables
        first_direction_options = ["horizontal", "vertical"]
        first_direction = random.choice(first_direction_options)

        # depending on start and end point the cable is made
        if first_direction == "horizontal":
            if end_x < start_x:
                while current_x > end_x:
                    current_x -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_x < end_x:
                    current_x += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

            if end_y < start_y:
                while current_y > end_y:
                    current_y -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_y < end_y:
                    current_y += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
        else:
            if end_y < start_y:
                while current_y > end_y:
                    current_y -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_y < end_y:
                    current_y += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

            if end_x < start_x:
                while current_x > end_x:
                    current_x -= 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)
            else:
                while current_x < end_x:
                    current_x += 1
                    self.cable_xs.append(current_x)
                    self.cable_ys.append(current_y)

        # getting one list containing all coordinates
        self.coordinates = []
        for index in range(len(self.cable_xs)):
            self.coordinates.append(get_coordinate(self.cable_xs[index],
                                                   self.cable_ys[index]))

        return self.cable_xs, self.cable_ys

    def compute_cable_length(self):
        """This method calculates complete cable length"""
        self.cable_length = manhattan_distance(max(self.cable_xs),
                                               max(self.cable_ys),
                                               min(self.cable_xs),
                                               min(self.cable_ys))
        return self.cable_length

    def compute_cable_cost(self, cost_per_segment):
        """This method calculates cable costs only,
        so excluding battery cost"""
        self.cable_cost = self.cable_length * cost_per_segment
        return self.cable_cost


def load_houses(csv_file_path):
    """This function turns a csv file into a list of house instances"""
    house_df = pd.read_csv(csv_file_path)
    houses = []

    for house_index, house_data in house_df.iterrows():
        house = House(*tuple(map(float, house_data)))
        houses.append(house)

    return houses

def load_batteries(csv_file_path):
    """This function turns a csv file to a list of battery instances"""
    battery_df_crude = pd.read_csv(csv_file_path)

    # split coordinate column in two seperate columns
    battery_df = pd.concat(
                [battery_df_crude["positie"].str.split(',', expand=True),
                 battery_df_crude["capaciteit"]], axis=1)
    batteries = []

    for battery_index, battery_data in battery_df.iterrows():
        battery = Battery(*tuple(map(float, battery_data)))
        batteries.append(battery)

    return batteries








def random_cables(houses, batteries):
    """This function connects each house to a random battery
    and creates a cable instance for each, not taking
    into account maximum battery capacity"""
    cables = []
    for house in houses:
        cable = Cable(random.choice(batteries), house)
        cables.append(cable)
    return cables

def closest_cables(houses, batteries):
    """This function connects each house to the nearest battery,
    not taking into account maximum battery capacity"""
    cables = []

    # iterating over the houses
    for house in houses:
        house_x = house.house_x
        house_y = house.house_y
        closest_battery = None
        lowest_distance = math.inf

        for battery in batteries:
            # check which battery is the closest
            battery_x = battery.battery_x
            battery_y = battery.battery_y
            distance = manhattan_distance(house_x, house_y, battery_x, battery_y)
            if distance < lowest_distance:
                lowest_distance = distance
                closest_battery = battery

        # connect house to closest battery
        cable = Cable(closest_battery, house)
        cables.append(cable)

    return cables


def compute_total_cable_length(cables):
    total_length = 0
    for cable in cables:
        total_length += cable.compute_cable_length()
    # print(f"Total cable length: {total_length}")

def compute_total_cable_cost(cables, cost_per_segment=9):
    """This method calculates total cable costs only,
    so excluding battery cost"""
    total_cost = 0
    for cable in cables:
        current_cable_cost = cable.compute_cable_cost(cost_per_segment)
        total_cost += current_cable_cost
    # print(f"Total cable cost: {total_cost}")
    return int(total_cost)


def plot(houses, batteries, cables):
    """This function plots houses, batteries and cables
    all together in one plot"""
    # lay each cable and plot it
    for cable in cables:
        cable_xs, cable_ys = cable.lay_cable()
        plt.plot(cable_xs, cable_ys, "b-")


    # plot all houses in one run
    house_xs = []
    house_ys = []
    for house in houses:
        house_xs.append(house.house_x)
        house_ys.append(house.house_y)
    plt.plot(house_xs, house_ys, "ro")

    # plot all batteries in one run
    battery_xs = []
    battery_ys = []
    for battery in batteries:
        battery_xs.append(battery.battery_x)
        battery_ys.append(battery.battery_y)
    plt.plot(battery_xs, battery_ys, "gs")

    plt.grid()
    plt.show()


def create_json_output(district_number, houses, batteries, cables):
    python_output = []

    # create and add info dictionary to output
    info_dict = {}
    info_dict["district"] = district_number
    info_dict["costs-own"] = compute_total_cable_cost(cables)
    python_output.append(info_dict)

    # iterate over batteries and save location and capacity
    for battery in batteries:
        battery_dict = {}
        battery_dict["location"] = battery.coordinate
        battery_dict["capacity"] = battery.max_capacity
        connected_houses = []

        # store connected houses in the current battery dictionary
        for cable in cables:
            if cable.battery == battery:
                house_dict = {}
                house_dict["location"] = cable.house.coordinate
                house_dict["output"] = cable.house.max_output
                house_dict["cables"] = cable.coordinates
                connected_houses.append(house_dict)
        battery_dict["houses"] = connected_houses
        python_output.append(battery_dict)

    # transform output to json and save as file
    json_output = json.dumps(python_output, indent=2)
    with open('output.json', 'w') as file:
        file.write(json_output)

    return json_output

# load, plot and save json for district 1
houses_1 = load_houses("data/Huizen&Batterijen/district_1/district-1_houses.csv")
batteries_1 = load_batteries("data/Huizen&Batterijen/district_1/district-1_batteries.csv")
cables_1 = closest_cables(houses_1, batteries_1)

plot(houses_1, batteries_1, cables_1)
compute_total_cable_length(cables_1)
compute_total_cable_cost(cables_1)
print(create_json_output(1, houses_1, batteries_1, cables_1))

# load, plot and save json for district 2
houses_2 = load_houses("data/Huizen&Batterijen/district_2/district-2_houses.csv")
batteries_2 = load_batteries("data/Huizen&Batterijen/district_2/district-2_batteries.csv")
cables_2 = closest_cables(houses_2, batteries_2)

plot(houses_2, batteries_2, cables_2)
compute_total_cable_length(cables_2)
compute_total_cable_cost(cables_2)
create_json_output(2, houses_2, batteries_2, cables_2)

# load, plot and save json for district 3
houses_3 = load_houses("data/Huizen&Batterijen/district_3/district-3_houses.csv")
batteries_3 = load_batteries("data/Huizen&Batterijen/district_3/district-3_batteries.csv")
cables_3 = closest_cables(houses_3, batteries_3)

plot(houses_3, batteries_3, cables_3)
compute_total_cable_length(cables_3)
compute_total_cable_length(cables_3)
create_json_output(3, houses_3, batteries_3, cables_3)
