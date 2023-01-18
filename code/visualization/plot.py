from code.classes import cable, house, battery
import matplotlib.pyplot as plt

def plot(houses, batteries, cables):
    """This function plots houses, batteries and cables
    all together in one plot"""
    # lay each cable and plot it
    for cable in cables:
        plt.plot(cable.cable_xs, cable.cable_ys, "b-")


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
