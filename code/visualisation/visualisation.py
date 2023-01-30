import matplotlib.pyplot as plt
from code.classes import district


def visualise(district):
    # Lists for the plot
    list_x = []
    list_y = []
    list_colour = []

    # Add the location and color of each input to the lists
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

def draw(district):
    # Make scatter plot with grid
    # plt.figure(figsize=(9,9))
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and color of each input to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)

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

    plt.title(f'District {district.district_number} (with shared cost of {district.shared_cost})')
    plt.draw()

    # removing the plot each step before the next plot is drawn
    plt.pause(0.001)
    plt.cla()


def setup_plot(district):
    # Lists for the plot of houses
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and color of each input to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)


    return house_x, house_y, house_colour, battery_x, battery_y, battery_colour

def color_visualise(district):
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and color of each input to the lists
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
