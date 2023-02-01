from code.visualisation import visualisation
from code.classes import district
from code.algorithms import mutation_functions as mutation
import copy

def simulated_annealing_algorithm(district, mutation_function, cost_type, move_batteries = False, temperature = 5000, cooling_rate = 0.99, random_selection = 20):
    '''
<<<<<<< HEAD
    Input:
    - valid starting district (made by random)
    - mutation functions (swapping connections or new route)
    - move batteries (False or True)
    - cost type (shared or own)
    - temperature (number above 1)
    - cooling rate (number between 0 and 1)
    - random selection (number for the selection amount of the mutation swapping batteries)
=======
    Given a starting point and a list of coordinates,
    returns the index of the nearest coordinate of the list
    '''
    distances = []
    for coordinate in coordinate_list:
        distances.append(manhattan_distance(start, coordinate))

    return np.argmin(distances)

def middle_point(list_coordinates):
    x_values = [point[0] for point in list_coordinates]
    y_values = [point[1] for point in list_coordinates]
    x_mid = round(sum(x_values) / len(list_coordinates))
    y_mid = round(sum(y_values) / len(list_coordinates))

    return (x_mid, y_mid)

def change_battery_location(connections_dict):
    for battery in connections_dict.values():

        # List of coordinates connected to one battery
        cluster_coordinates = []
        for house in connections_dict:
            if connections_dict[house] == battery:
                cluster_coordinates.append(house.coordinate)

        # Find middle point of the cluster
        new_location = middle_point(cluster_coordinates)

        # Update battery to that location
        battery.change_location(new_location)

        for house in connections_dict:
            if connections_dict[house] == battery:
                # Delete previous route
                house.cables.clear_route()
                # Create route to the nearest point
                house.cables.create_route(house.coordinate, battery.coordinate)



def swapping_connections(connections_dict, random_selection):
    '''
    Input: dictionary of all house-battery connections (key: house, value: battery)

    - Randomly picks a house within the top of longest routes
    - Finds nearest battery and the houses currently connected to that battery
    - In random order, checks if there is a switch possible with one of the
        potential houses.
        - If solutions remains valid, the two houses switch from battery.
        - New routes are created, connections are updated
        - Loop ends
    '''
    while True:
        # Sort houses by segments length (longest route)
        houses_by_segments = sorted(list(connections_dict.keys()), key=lambda x: len(x.cables.segments), reverse=True)

        # Randomly pick a house with the top-10 longest segments
        house_1 = random.choice(houses_by_segments[0:random_selection])
        battery_1 = connections_dict[house_1]

        # Find nearest battery
        all_batteries = [battery.coordinate for battery in connections_dict.values()]
        nearest_index = find_nearest_index(house_1.coordinate, all_batteries)
        battery_2 = list(connections_dict.values())[nearest_index]

        # Find houses connected to the nearest battery
        potential_houses = [house for house, battery in connections_dict.items() if battery == battery_2]

        # Shuffle the potential houses
        random.shuffle(potential_houses)

         # Check each potential house
        for house_2 in potential_houses:
            # Check if swapping results in a valid solution
            if (battery_1.current_capacity - house_1.output + house_2.output <= battery_1.max_capacity) and \
               (battery_2.current_capacity - house_2.output + house_1.output <= battery_2.max_capacity):

                # Update battery capacities
                battery_1.current_capacity -= house_1.output - house_2.output
                battery_2.current_capacity -= house_2.output - house_1.output

                # Remove previous cable segments
                house_1.cables.clear_route()
                house_2.cables.clear_route()

                # Update colours
                house_1.colour = battery_2.colour
                house_2.colour = battery_1.colour

                # Create new cable routes
                house_1.cables.create_route(house_1.coordinate, battery_2.coordinate)
                house_2.cables.create_route(house_2.coordinate, battery_1.coordinate)

                # Updating the connections_dict with new connections
                connections_dict[house_1] = battery_2
                connections_dict[house_2] = battery_1

                # Stop the loop
                return

def new_route(connections_dict):
    '''
    Input: dictionary of all house-battery connections (key: house, value: battery)

    Out of a random selection, the house with the longest cable is chosen. Then,
    it will find if there is a cable nearby that goes towards the same battery.
    If so, it will recreate a route to go the that nearest point.
    '''
    # Pick random house
    house = random.choice(list(connections_dict.keys()))
    battery = connections_dict[house]

    # List of all the cable points that another cable can connect to
    cable_coordinates = set()
    for h in connections_dict:
        if h != house:
            for coordinate in h.cables.coordinates:
                cable_coordinates.add(coordinate)
    cable_coordinates = list(cable_coordinates)

    # Calculate manhattan distances and find nearest point
    nearest_index = find_nearest_index(house.coordinate, cable_coordinates)

    # Only change route if the nearest point is not the same location
    if house.coordinate != cable_coordinates[nearest_index]:
        # Delete previous route
        house.cables.clear_route()
        # Create route to the nearest point
        house.cables.create_route(house.coordinate, cable_coordinates[nearest_index])
        # Add the route from the point to the battery (so it stays connected to the battery)
        house.cables.create_route(cable_coordinates[nearest_index], battery.coordinate)

def simulated_annealing_algorithm(district, mutation_function, cost_type = 'shared', plot = "y", temperature = 5000, cooling_rate = 0.99, random_selection = 20):
    '''
    Input: starting district, temperature, cooling rate
    returns: new district with lowest cost
>>>>>>> 12a7b7569476d72bb78183c1114457f50889fbc6

    Returns:
    - new district with lowest cost

    Pseudo code:
    - While temperature > 1:
        - Begin with random start state
        - Induce small change to the state (either swap houses or make new routes)
        - If random number > probability(new_cost, old_cost, temperature):
            - Disregard the change
        - Lower the temperature
    '''

    if plot == "y":
        fig, ax1, ax2 = visualisation.setup_plot(district)
        iterations = []
        cost_list = []
        iteration = 1

    while temperature > 1:
        # Makes a copy of the district to work with
        new_district = copy.deepcopy(district)

        # Mutate the district
        if mutation_function == 'swapping_connections':
<<<<<<< HEAD
            mutation.swapping_connections(new_district.connections, random_selection)

            if move_batteries:
                mutation.change_battery_location(new_district.connections)

=======
            swapping_connections(new_district.connections, random_selection)
            # change_battery_location(new_district.connections)
>>>>>>> 12a7b7569476d72bb78183c1114457f50889fbc6
        elif mutation_function == 'new_route':
            mutation.new_route(new_district.connections)

        # Calculate costs
        new_cost = new_district.calculate_cost(cost_type)
        old_cost = district.calculate_cost(cost_type)

        # Calculate the probability of accepting this new district
        probability = math.exp(-(new_cost - old_cost) / temperature)

        # if random falls in probabilty range, new district is accepted
        if random.random() > probability:
            # Return to the previous state
            new_district = district
            if plot == "y":
                cost_list.append(new_cost)

        else:
            # Keep the new state
            district = new_district
            if plot == "y":
                cost_list.append(old_cost)

            # Uncomment if you want to see the costs go down:
            print(district.calculate_shared_cost())

        # Lower the temperature
        temperature *= cooling_rate

<<<<<<< HEAD
=======
        if plot == "y":
            iterations.append(iteration)
            iteration += 1
        if plot == "y":
            visualisation.draw_district(district, fig, ax1, ax2, cost_list, iterations)


>>>>>>> 12a7b7569476d72bb78183c1114457f50889fbc6
    return district
