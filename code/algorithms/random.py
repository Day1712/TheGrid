from code.classes import district
import numpy as np
import random

'''
Probleem:
Met deze code komt er geen geldige oplossing uit wanneer je huizen met random
batterijen connect, behalve misschien als je het een dag (jaar?) laat runnen.

More info:
- Het gaat goed totdat er een route gemaakt moet worden voor de laatste huizen
    (bijv. huis 148, 149, of 150). Er is dan geen batterij meer over die nog
    genoeg capaciteit heeft voor die laatste huizen met route. Helaas mag de
    laatste output(s) niet onderverdelen over de batterijen, dan zou het wel
    lukken.

- Ik dacht misschien helpt het als we eerst de huizen met hoogste outputs met
    een batterij linken en daarna de huizen met lagere outputs. This did not
    help... Komt waarschijnlijk omdat alle House outputs rond het gemiddelde
    van 50 liggen dus echt hoge/lage zijn er niet.

- Misschien is het beter om minder streng te zijn en ook invalide oplossingen
    toe te staan en dat met de 'slimmere' algoritmes te verbeteren... Minder
    leuk though
'''

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

            # Returns a battery that has enough capacity
            return battery_list[i]

    # Only returns false when there are no batteries available
    return False

def create_route(house, battery):
    '''
    First goes right or left in the direction of the battery. Then goes up or down.
    '''
    x = house.pos_x
    y = house.pos_y

    # If the cable is left from the battery, the route goes right
    while x < battery.pos_x:
        x += 1
        house.cables.add_cable_segment((x - 1, y), (x, y))
        if x == battery.pos_x:
            break
    # If the cable is right from the battery, the route goes left
    while x > battery.pos_x:
        x -= 1
        house.cables.add_cable_segment((x + 1, y), (x, y))
        if x == battery.pos_x:
            break

    # If the cable is under from the battery, the route goes up
    while y < battery.pos_y:
        y += 1
        house.cables.add_cable_segment((x, y - 1), (x, y))
        if y == battery.pos_y:
            break

    # If the cable is above from the battery, the route goes down
    while y > battery.pos_y:
        y -= 1
        house.cables.add_cable_segment((x, y + 1), (x, y))
        if y == battery.pos_y:
            break

def random_routes(district):
    '''
    Creates routes for each house to an available battery.
    The order of batteries is random, so each run the routes will be different.
    '''

    # Keep track of houses that are connected with a battery
    all_connected = False
    connected_houses_count = 0

    # Keeps trying until it creates routes for all houses
    while not all_connected:

        # Short houses on output (highest first)
        district.houses.sort(key=lambda x: x.output, reverse=True) # (This is in the hope it will find a valid solution quicker)

        # For each house, find a random available battery
        for house in district.houses:
            chosen_battery = random_available_battery(house, district.batteries)

            # If there is no available battery, the chosen battery is False
            if not chosen_battery:

                # Clear all cable segments
                for house in district.houses:
                    house.cables.cable_segments = []

                # Start the for-loop again
                break

            # If battery is found, the house is conncected!
            if chosen_battery != False:
                connected_houses_count += 1

            # It will create a route between house and battery
            create_route(house, chosen_battery)

            # Check if all houses are connected to break the while-loop
            if connected_houses_count == len(district.houses):
                all_connected = True

    # Calculate the cost
    district.calculate_own_cost()
    district.calculate_shared_cost()
