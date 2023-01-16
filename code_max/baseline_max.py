import pandas as pd
import matplotlib.pyplot as plt
import random
import math

class House:
    def __init__(self, house_x, house_y, max_output):
        self.house_x = house_x
        self.house_y = house_y
        self.max_output = max_output
        self.is_connected = False

class Battery:
    def __init__(self, battery_x, battery_y, max_capacity, battery_cost=5000):
        self.battery_x = battery_x
        self.battery_y = battery_y
        self.max_capacity = max_capacity
        self.battery_cost = battery_cost
        self.capacity_used = 0
        self.selected = False
        self.color = None

class Cable:
    def __init__(self, battery, house, color):
        self.battery = battery
        self.house = house
        self.color = color

    def lay_cable(self):
        start_x = self.house.house_x
        start_y = self.house.house_y
        end_x = self.battery.battery_x
        end_y = self.battery.battery_y

        self.cable_xs = []
        self.cable_ys = []
        self.cable_xs.append(start_x)
        self.cable_ys.append(start_y)

        current_x = start_x
        current_y = start_y

        first_direction_options = ["horizontal", "vertical"]
        first_direction = random.choice(first_direction_options)

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

        return self.cable_xs, self.cable_ys

    def cable_length(self):
        x_length = max(self.cable_xs) - min(self.cable_xs)
        y_length = max(self.cable_ys) - min(self.cable_ys)
        self.cable_length = x_length + y_length
        return self.cable_length

    def cable_cost(self, cost_per_segment):
        self.cable_cost = self.cable_length * cost_per_segment
        return self.cable_cost

def load_houses(csv_file_path):
    "This function turns a csv file to a list of house instances"
    house_df = pd.read_csv(csv_file_path)
    houses = []
    for house_index, house_data in house_df.iterrows():
        house = House(*tuple(map(float, house_data)))
        houses.append(house)
    return houses

def load_batteries(csv_file_path):
    "This function turns a csv file to a list of battery instances"
    battery_colors = ["g", "b", "m", "y", "c"]
    battery_df_crude = pd.read_csv(csv_file_path)
    battery_df = pd.concat([battery_df_crude["positie"].str.split(',', expand=True), battery_df_crude["capaciteit"]], axis=1)
    batteries = []
    for battery_index, battery_data in battery_df.iterrows():
        battery = Battery(*tuple(map(float, battery_data)))
        battery.color = battery_colors[battery_index]
        batteries.append(battery)
    return batteries

def random_cables(houses, batteries):
    cables = []
    for house in houses:
        cable = Cable(random.choice(batteries), house)
        cables.append(cable)
    return cables

def manhattan_distance(house_x, house_y, battery_x, battery_y):
    distance = abs(house_x - battery_x) + abs(house_y - battery_y)
    return distance

def closest_cables(houses, batteries):
    cables = []
    for house in houses:
        house_x = house.house_x
        house_y = house.house_y
        closest_battery = None
        lowest_distance = math.inf
        battery_count = 0

        for battery in batteries:
            battery_count += 1
            # print(battery_count)
            battery_x = battery.battery_x
            battery_y = battery.battery_y
            distance = manhattan_distance(house_x, house_y, battery_x, battery_y)
            # print(distance)
            if distance < lowest_distance:
                lowest_distance = distance
                # print(lowest_distance)
                closest_battery = battery
                # print(closest_battery)
        cable = Cable(closest_battery, house)
        cables.append(cable)
    print(len(cables))
    return cables

def optimal_cables(houses, batteries):
    cables = []
    # available_houses = set(houses)
    # connected_houses = set()

    while len(cables) < len(houses):
        # available_houses = available_houses - connected_houses

        lowest_distance = math.inf
        lowest_distance_house = None
        lowest_distance_battery = None

        for battery in batteries:
            battery_x = battery.battery_x
            battery_y = battery.battery_y

            for house in houses:
                house_x = house.house_x
                house_y = house.house_y

                distance = manhattan_distance(house_x, house_y, battery_x, battery_y)
                if distance < lowest_distance and (battery.capacity_used + house.max_output) < battery.max_capacity and house.is_connected == False:
                    print("HIT")
                    lowest_distance = distance
                    lowest_distance_house = house
                    lowest_distance_battery = battery

        for house in houses:
            for battery in batteries:
                if house.house_x == lowest_distance_house.house_x and house.house_y == lowest_distance_house.house_y and \
                battery.battery_x == lowest_distance_battery.battery_x and battery.battery_y == lowest_distance_battery.battery_y:

                    house.is_connected = True
                    print(house.is_connected)
                    battery.capacity_used += lowest_distance_house.max_output
                    cable = Cable(battery, house, battery.color)
                    cables.append(cable)
                    # print(house.is_connected)
                    # connected_houses.add(house)
        """
        for battery in batteries:
            if battery == lowest_distance_battery:
                battery.capacity_used += lowest_distance_house.max_output
                cable = Cable(battery, lowest_distance_house, battery.color)
                cables.append(cable)
        """

    print(len(cables))
    return cables

def compute_total_cable_length(cables):
    total_length = 0
    for cable in cables:
        total_length += cable.cable_length()
    print(f"Total cable length: {total_length}")

def compute_total_cable_cost(cables):
    total_cost = 0
    for cable in cables:
        total_cost += cable.cable_cost(9)
    print(f"Total cable cost: {total_cost}")

def plot(houses, batteries, cables):
    "This function plots houses and batteries together in one plot"
    house_xs = []
    house_ys = []
    for house in houses:
        house_xs.append(house.house_x)
        house_ys.append(house.house_y)

    for battery in batteries:
        marker = battery.color + "s"
        plt.plot(battery.battery_x, battery.battery_y, marker)

    for cable in cables:
        cable_xs, cable_ys = cable.lay_cable()
        marker = cable.color + "-"
        plt.plot(cable_xs, cable_ys, marker)

    # test_cable = Cable(batteries[0], houses[0])
    # test_cable.lay_cable()
    # plt.plot(test_cable.cable_xs, test_cable.cable_ys, 'b-')

    plt.plot(house_xs, house_ys, "ro")

    plt.grid()
    plt.show()

def create_json_output(district_number, houses, batteries, cables):
    python_output = []
    info_dict = {}
    info_dict["district"] = district_number
    info_dict["costs-own"] = compute_total_cable_cost(cables)
    python_output.append(info_dict)
    for battery in batteries:
        battery_dict = {}
        battery_dict["location"] = battery.coordinate
        battery_dict["capacity"] = battery.max_capacity
        connected_houses = []
        for cable in cables:
            if cable.battery == battery:
                house_dict = {}
                house_dict["location"] = cable.house.coordinate
                house_dict["output"] = cable.house.max_output
                house_dict["cables"] = cable.coordinates
                connected_houses.append(house_dict)
        battery_dict["houses"] = connected_houses
        python_output.append(battery_dict)
    json_output = json.dumps(python_output, indent=2)
    with open('output.json', 'w') as file:
        file.write(json_output)
    return json_output

houses_1 = load_houses("Huizen&Batterijen/district_1/district-1_houses.csv")
batteries_1 = load_batteries("Huizen&Batterijen/district_1/district-1_batteries.csv")
# cables_1 = random_cables(houses_1, batteries_1)
# cables_1 = closest_cables(houses_1, batteries_1)
cables_1 = optimal_cables(houses_1, batteries_1)


plot(houses_1, batteries_1, cables_1)
total_cable_length(cables_1)
total_cable_cost(cables_1)

houses_2 = load_houses("Huizen&Batterijen/district_2/district-2_houses.csv")
batteries_2 = load_batteries("Huizen&Batterijen/district_2/district-2_batteries.csv")
# cables_2 = random_cables(houses_2, batteries_2)
# cables_2 = closest_cables(houses_2, batteries_2)
cables_2 = optimal_cables(houses_2, batteries_2)
plot(houses_2, batteries_2, cables_2)
total_cable_length(cables_2)
total_cable_cost(cables_2)

houses_3 = load_houses("Huizen&Batterijen/district_3/district-3_houses.csv")
batteries_3 = load_batteries("Huizen&Batterijen/district_3/district-3_batteries.csv")
# cables_3 = random_cables(houses_3, batteries_3)
# cables_3 = closest_cables(houses_3, batteries_3)
cables_3 = optimal_cables(houses_3, batteries_3)
plot(houses_3, batteries_3, cables_3)
total_cable_length(cables_3)
total_cable_cost(cables_3)




#
