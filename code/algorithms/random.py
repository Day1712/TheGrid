from code.classes import district
import random

def update_battery_capacity(house, battery):
    battery.current_capacity += house.output

def random_available_battery(house, battery_list):
    # Randomize order of battery list
    random.shuffle(battery_list)

    # Loop over every battery in the list
    for i in range(len(battery_list)):

        # Check if battery has capacity left for the house output
        if battery_list[i].current_capacity + house.output < battery_list[i].max_capacity:

            # Update battery max_capacity
            update_battery_capacity(house, battery_list[i])

            # Returns the battery index that has enough capacity
            return i

    # Only returns -1 when there are no batteries available
    return -1

def create_all_routes(district):
    '''
    Finds a valid solution based on random house-battery connections.
    '''
    while not district.valid:

        # Reset for every dead end
        district.reset_grid()

        # For each house, find a random available battery
        for house in district.houses:
            chosen_battery_index = random_available_battery(house, district.batteries)

            # If battery index is -1 no battery was found, start the loop again!
            if chosen_battery_index == -1:
                #print('trying again')
                break

            # If loop is not broken, there is a house-battery connection!
            district.connections[house] = district.batteries[chosen_battery_index]

            # End the while-loop if it can
            district.valid_solution()

    # It will create a route between house and battery
    for house in district.connections:
        house.cables.create_route(house.coordinate, district.connections[house].coordinate)

        # Match the house colour to the battery
        house.colour = district.connections[house].colour

    # Update costs
    district.calculate_cost('own')
    district.calculate_cost('shared')
