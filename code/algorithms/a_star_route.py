from code.classes import district
import random
import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def create_route(house, battery, previous_routes):
    start = (house.pos_x, house.pos_y)
    goal = (battery.pos_x, battery.pos_y)

    # Create a priority queue list and evaluated coordinates set
    queue = []
    evaluated = set()

    # Add the starting coordinate to the queue
    heapq.heappush(queue, (0, (start)))

    # Create a dictionary to store the previous location
    came_from = {start: None}

    # Create a dictionary to store the cost of the route
    costs_so_far = {start: 0}

    while queue:
        # Current location (coordinate)
        current = heapq.heappop(queue)[1]

        # Make sure to only check this coordinate once
        evaluated.add(current)

        # Generate the neighbours of the current coordinate
        neighbours = []

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbour = (x + dx, y + dy)

            # The road does not go back
            if neighbour not in evaluated:
                neighbours.append(neighbour)

        # Update the costs and parents of the neighbours
        for neighbour in neighbours:

            # Check whether the neighbour has not been visited before
            if neighbour not in costs_so_far:

                # Each adjencent step (i.e. towards a neighbour) costs 1
                costs_so_far[neighbour] = costs_so_far[current] + 1

                if current in previous_routes:
                    # Cost is less if already travelled by other route
                    bonus = -10
                else:
                    bonus = 0

                # The higher the score, the less favourable the step
                priority_score = costs_so_far[neighbour] + bonus + manhattan_distance(goal[0], neighbour[0], goal[1], neighbour[1])
                heapq.heappush(queue, (priority_score, neighbour))

                # Keeping track of the route
                came_from[neighbour] = current

        # If we have reached the goal, update the complete route
        if current == goal:
            route = []

            while current != start:
                route.append((current, came_from[current]))
                current = came_from[current]

            route.append((start, current))
            route.reverse()

            for segment in route:
                house.cables.add_cable_segment(segment[0], segment[1])

            return route
