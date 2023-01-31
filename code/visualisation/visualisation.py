import matplotlib.pyplot as plt
from code.classes import district
import pylab as pl
from matplotlib import collections

def visualise(district):
    # Lists for the plot
    list_x = []
    list_y = []
    list_colour = []

    # Add the location and colour of each input to the lists
    for input in district.grid_inputs:
        list_x.append(input.pos_x)
        list_y.append(input.pos_y)
        list_colour.append(input.colour)

    # Change the figure size
    plt.figure(figsize=(9,9))

    # Make scatter plot with grid
    plt.grid(which = 'both')
    plt.title(f'District {district.district_number} (with shared cost of {district.shared_cost})')
    plt.scatter(list_x, list_y, c = list_colour, zorder = 3)
    plt.xticks(range(min(list_x), max(list_x) + 1), fontsize = 7)
    plt.yticks(range(min(list_y), max(list_y) + 1), fontsize = 7)

    # Add the plot of the cables
    for house in district.connections:
        for segment in house.cables.segments:
            x = [point[0] for point in segment]
            y = [point[1] for point in segment]
            plt.plot(x, y, c = house.colour)

    plt.show()

def draw_district(district, fig, ax1, ax2, cost_list, iterations):

    # Add the plot of the cables
    segment_count = 0
    cables_list = []
    colors_list = []
    for house in district.connections:
        cable_points = []
        for segment in house.cables.segments:
            segment_count += 1
            point1, point2 = segment
            # if segment_count < 5:
                # print(segment)
                # print(point1)
                # print(point2)
            cable_points.extend([point1, point2])
            # x = [point[0] for point in segment]
            # y = [point[1] for point in segment]
            # plt.plot(x, y, c = house.colour)
        cables_list.append(cable_points)
        colors_list.append(house.colour)

        # if segment_count < 200:
            # print(cables_list)
            # print(colors_list)
    lc = collections.LineCollection(cables_list, colors=colors_list)

    ax1.add_collection(lc)
    ax1.autoscale()
    ax1.margins(0.1)

    # Make scatter plot with grid

    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each input to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)

    ax1.grid(which = 'both')
    ax1.scatter(house_x, house_y, c = house_colour, marker = 'o', zorder = 3)
    ax1.scatter(battery_x, battery_y, c = battery_colour, marker = 's', zorder = 3)
    ax1.set_xticks(range(min(house_x + battery_x), max(house_x + battery_x) + 1), fontsize = 7)
    ax1.set_yticks(range(min(house_y + battery_y), max(house_y + battery_y) + 1), fontsize = 7)

    ax2.plot(iterations, cost_list)


    # ax.title(f'District {district.district_number} (with shared cost of {district.shared_cost})')
    plt.draw()

    # removing the plot each step before the next plot is drawn
    plt.pause(0.1)
    ax1.cla()
    ax2.cla()


def setup_plot(district):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    """# Lists for the plot of houses
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each input to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)


    return house_x, house_y, house_colour, battery_x, battery_y, battery_colour
    """
    return fig, ax1, ax2

def colour_visualise(district):
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each input to the lists
    for house in district.houses:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)

    for battery in district.batteries:
        battery_x.append(battery.pos_x)
        battery_y.append(battery.pos_y)
        battery_colour.append(battery.colour)

    # Change the figure size
    plt.figure(figsize=(9,9))

    # Make scatter plot with grid
    plt.grid(which = 'both')
    plt.scatter(house_x, house_y, c = house_colour, marker = 'o', zorder = 3)
    plt.scatter(battery_x, battery_y, c = battery_colour, marker = 's', zorder = 3)
    plt.xticks(range(min(house_x + battery_x), max(house_x + battery_x) + 1), fontsize = 7)
    plt.yticks(range(min(house_y + battery_y), max(house_y + battery_y) + 1), fontsize = 7)

    # Add the plot of the cables
    for house in district.connections:
        for segment in house.cables.segments:
            x = [point[0] for point in segment]
            y = [point[1] for point in segment]
            plt.plot(x, y, c = house.colour)

    plt.show()

def updated_colour_visualise(district):
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each input to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)

    # Change the figure size
    plt.figure(figsize=(9,9))

    # Make scatter plot with grid
    plt.grid(which = 'both')
    plt.scatter(house_x, house_y, c = house_colour, marker = 'o', zorder = 3)
    plt.scatter(battery_x, battery_y, c = battery_colour, marker = 's', zorder = 3)
    plt.xticks(range(min(house_x + battery_x), max(house_x + battery_x) + 1), fontsize = 7)
    plt.yticks(range(min(house_y + battery_y), max(house_y + battery_y) + 1), fontsize = 7)

    # Add the plot of the cables
    for house in district.connections:
        for segment in house.cables.segments:
            x = [point[0] for point in segment]
            y = [point[1] for point in segment]
            plt.plot(x, y, c = house.colour)

    plt.show()

def plot_per_battery(district):
    for current_colour in district.battery_colours:
        house_x = []
        house_y = []
        battery_x = []
        battery_y = []


        # Change the figure size
        plt.figure(figsize=(9,9))

        # Add the location and colour of each input to the lists
        for house in district.connections:
            if house.colour == current_colour:
                house_x.append(house.pos_x)
                house_y.append(house.pos_y)
                if len(battery_x) == 0:
                    battery_x.append(district.connections[house].pos_x)
                    battery_y.append(district.connections[house].pos_y)
                for segment in house.cables.segments:
                    x = [point[0] for point in segment]
                    y = [point[1] for point in segment]
                    plt.plot(x, y, c = current_colour)

        # Make scatter plot with grid
        plt.grid(which = 'both')
        plt.scatter(house_x, house_y, c = current_colour, marker = 'o', zorder = 3)
        plt.scatter(battery_x, battery_y, c = current_colour, marker = 's', zorder = 3)
        plt.xticks(range(min(house_x + battery_x), max(house_x + battery_x) + 1), fontsize = 7)
        plt.yticks(range(min(house_y + battery_y), max(house_y + battery_y) + 1), fontsize = 7)



        plt.show()
