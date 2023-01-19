import heapq

import csv
from code.classes import house, battery

#TODO calculate overal cost of the cables

#Class: District?

        # Function to calculate the estimated cost from the current node to the goal
        def heuristic_cost(current, goal):
            # Example implementation: Manhattan distance
            return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

        def a_star(graph, start, goal):
            # Create open and closed lists
            open_list = []
            closed_list = set()

            # Add the starting node to the open list
            heapq.heappush(open_list, (0, start))

            # Create a dictionary to store the cameFrom information
            cameFrom = dict()

            # Create a dictionary to store the cost from the start node to the current node
            cost_so_far = dict()
            cost_so_far[start] = 0

            while open_list:
                # Get the node with the lowest cost from the open list
                current = heapq.heappop(open_list)[1]

                # If we have reached the goal, return the path
                if current == goal:
                    path = [goal]
                    while current in cameFrom:
                        current = cameFrom[current]
                        path.append(current)
                    return path[::-1]

                # Add the current node to the closed list
                closed_list.add(current)

                # Check the neighbors of the current node
                for neighbor in graph[current]:
                    if neighbor in closed_list:
                        continue

                    # Calculate the cost to reach the neighbor
                    cost = cost_so_far[current] + graph[current][neighbor]

                    # Check if the neighbor is on the open list
                    if neighbor not in cost_so_far or cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = cost
                        priority = cost + heuristic_cost(neighbor, goal)
                        heapq.heappush(open_list, (priority, neighbor))
                        cameFrom[neighbor] = current

            # If the goal was not reached, return "no path found"
            return "no path found"
