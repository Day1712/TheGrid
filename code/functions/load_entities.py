from code.classes import house, battery
import pandas as pd

def load_houses(csv_file_path):
    """This function turns a csv file into a list of house instances"""
    house_df = pd.read_csv(csv_file_path)
    houses = []

    for house_index, house_data in house_df.iterrows():
        current_house = house.House(*tuple(map(float, house_data)))
        houses.append(current_house)

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
        current_battery = battery.Battery(*tuple(map(float, battery_data)))
        batteries.append(current_battery)

    return batteries

def load_cables(cables):
    for cable in cables:
        cable.lay_cable()
