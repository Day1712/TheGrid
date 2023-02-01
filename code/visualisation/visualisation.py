import matplotlib.pyplot as plt
from code.classes import district
from matplotlib import collections

def basic_static_visualise(district):
    # Set up the plot
    fig, ax1 = plt.subplots()

    # Create lists for plotting the houses and batteries
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each house/battery to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)

    # Create district plot
    ax1.grid(which = 'both')
    ax1.scatter(house_x, house_y, c = house_colour, marker = 'o', zorder = 3)
    ax1.scatter(battery_x, battery_y, c = battery_colour, marker = 's', zorder = 3)
    ax1.set_title(f"Optimalised district {district.district_number}")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    # Add the plot of the cables
    cables_list = []
    colors_list = []

    # Add cable coordinates and their respectice colours
    for house in district.connections:
        cable_points = []
        for segment in house.cables.segments:
            point1, point2 = segment
            cable_points.extend([point1, point2])
        cables_list.append(cable_points)
        colors_list.append(house.colour)

    # Plot the cables in the district
    lc = collections.LineCollection(cables_list, colors=colors_list)
    ax1.add_collection(lc)

    plt.show()

def draw_district(district, fig, ax1, ax2, cost_list, iterations):

    # Create cable lists
    # segment_count = 0
    cables_list = []
    colors_list = []

    # Add cable coordinates and their respectice colours
    for house in district.connections:
        cable_points = []
        for segment in house.cables.segments:
            # segment_count += 1
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

    # Plot the cables in the district
    lc = collections.LineCollection(cables_list, colors=colors_list)
    ax1.add_collection(lc)
    #ax1.autoscale()
    #ax1.margins(0.1)

    # Create lists for plotting the houses and batteries
    house_x = []
    house_y = []
    house_colour = []
    battery_x = []
    battery_y = []
    battery_colour = []

    # Add the location and colour of each house/battery to the lists
    for house in district.connections:
        house_x.append(house.pos_x)
        house_y.append(house.pos_y)
        house_colour.append(house.colour)
        battery_x.append(district.connections[house].pos_x)
        battery_y.append(district.connections[house].pos_y)
        battery_colour.append(district.connections[house].colour)

    # Create district plot
    ax1.grid(which = 'both')
    ax1.scatter(house_x, house_y, c = house_colour, marker = 'o', zorder = 3)
    ax1.scatter(battery_x, battery_y, c = battery_colour, marker = 's', zorder = 3)
    #ax1.set_xticks(range(min(house_x + battery_x), max(house_x + battery_x) + 1), fontsize = 7)
    #ax1.set_yticks(range(min(house_y + battery_y), max(house_y + battery_y) + 1), fontsize = 7)
    ax1.set_title(f"District {district.district_number} (with shared cost of {district.shared_cost})")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    # Create cost plot
    ax2.plot(iterations, cost_list)
    ax2.set_title("Cost graph")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Total cost")

    # Drawing and removing the plot each iteration
    plt.draw()
    plt.pause(0.0001)
    ax1.cla()
    ax2.cla()


def setup_plot(district):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7), gridspec_kw={'width_ratios': [3, 2]})
    return fig, ax1, ax2

def plot_per_battery(district):
    # Iterate over battery colours
    for current_colour in district.battery_colours:

        # Create lists for plotting the houses and battery
        house_x = []
        house_y = []
        battery_x = []
        battery_y = []

        # Change the figure size
        plt.figure(figsize=(8,8))

        # Add the location and colour of each input to the lists
        for house in district.connections:
            if house.colour == current_colour:
                house_x.append(house.pos_x)
                house_y.append(house.pos_y)

                # Only connect battery one time
                if len(battery_x) == 0:
                    battery_x.append(district.connections[house].pos_x)
                    battery_y.append(district.connections[house].pos_y)

                # Plot cable segments
                for segment in house.cables.segments:
                    x = [point[0] for point in segment]
                    y = [point[1] for point in segment]
                    plt.plot(x, y, c = current_colour)

        # Plot the batteries and houses in a grid
        plt.grid(which = 'both')
        plt.scatter(house_x, house_y, c = current_colour, marker = 'o', zorder = 3)
        plt.scatter(battery_x, battery_y, c = current_colour, marker = 's', zorder = 3)

        plt.show()
