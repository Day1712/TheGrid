from code.classes import district
import numpy as np
import random
import heapq

'''
Bij het schrijven van deze code kwam ik erachter dat onze eerste 'random' het
dus niet goed deed (batterijen gingen over hun max heen). Daarna heb ik hier
niet meer aan verder gewerkt.
'''


def nearest_manhattan_distance(current_location, location_goals):
    distances = []

    # Calculate the distance of the location to every possible location goal
    for goal in location_goals.keys():
        distances.append(abs(goal[0] - current_location[0]) + abs(goal[1] - current_location[1]))

    # Return the nearest distance of the list
    return min(distances)

def update_battery_capacity(house, battery):
    battery.current_capacity += house.output

def a_star_route(house, battery_list, district):
    start = (house.pos_x, house.pos_y)
    potential_goals = {}

    for battery in battery_list:
        if battery.current_capacity + house.output < battery.max_capacity:
            potential_goals[(battery.pos_x, battery.pos_y)] = battery
        else:
            print(f'No available batteries for the house with the coordinates {start}')
            return a_star_routes(district)


    # Create a priority queue list and evaluated nodes set
    queue = []
    evaluated = set()

    # Add the starting node to the queue
    heapq.heappush(queue, (0, start))

    # Create a dictionary to store the parent of each node
    came_from = {start: None}

    # Create a dictionary to store the cost of each node
    costs_so_far = {start: 0}

    while queue:
        current = heapq.heappop(queue)[1]

        # If we have reached the goal, return the path
        if current in potential_goals:
            path = []
            path.append(current)

            # Update battery max_capacity
            update_battery_capacity(house, potential_goals[current])

            while current != start:
                current = came_from[current]
                path.append(current)

            path.append(start)
            return path

        evaluated.add(current)

        # Generate the neighbours of the current node
        neighbours = []

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbour = (x + dx, y + dy)

            if neighbour not in evaluated:
                neighbours.append(neighbour)

        # Update the costs and parents of the neighbours
        for neighbour in neighbours:
            cost = costs_so_far[current] + 1

            if neighbour not in costs_so_far or cost < costs_so_far[neighbour]:
                costs_so_far[neighbour] = cost
                priority = cost + nearest_manhattan_distance(neighbour, potential_goals)
                heapq.heappush(queue, (priority, neighbour))
                came_from[neighbour] = current

    # If the goal was not reached, return "no path found"
    return print("no path found")


def a_star_routes(district):
    '''
    Calculates the shortest route from a house to an available battery.
    '''
    # Randomize the order of houses
    shuffled_houses = district.houses[:]
    random.shuffle(shuffled_houses)

    # Create route from house to battery for each house in the grid
    for house in shuffled_houses:
        route = a_star_route(house, district.batteries, district)

        for i in range(len(route)-1):
            house.cables.add_cable_segment(route[i], route[i+1])

    # Calculate the cost
    district.calculate_own_cost()
    district.calculate_shared_cost()
