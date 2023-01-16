import json


def compute_total_cable_length(cables):
    total_length = 0
    for cable in cables:
        total_length += cable.compute_cable_length()
    # print(f"Total cable length: {total_length}")

def compute_total_cable_cost(cables, cost_per_segment=9):
    """This method calculates total cable costs only,
    so excluding battery cost"""
    total_cost = 0
    for cable in cables:
        current_cable_cost = cable.compute_cable_cost(cost_per_segment)
        total_cost += current_cable_cost
    # print(f"Total cable cost: {total_cost}")
    return int(total_cost)


def create_json_output(district_number, houses, batteries, cables):
    python_output = []

    # create and add info dictionary to output
    info_dict = {}
    info_dict["district"] = district_number
    info_dict["costs-own"] = compute_total_cable_cost(cables)
    python_output.append(info_dict)

    # iterate over batteries and save location and capacity
    for battery in batteries:
        battery_dict = {}
        battery_dict["location"] = battery.coordinate
        battery_dict["capacity"] = battery.max_capacity
        connected_houses = []

        # store connected houses in the current battery dictionary
        for cable in cables:
            if cable.battery == battery:
                house_dict = {}
                house_dict["location"] = cable.house.coordinate
                house_dict["output"] = cable.house.max_output
                house_dict["cables"] = cable.coordinates
                connected_houses.append(house_dict)
        battery_dict["houses"] = connected_houses
        python_output.append(battery_dict)

    # transform output to json and save as file
    json_output = json.dumps(python_output, indent=2)
    with open('output.json', 'w') as file:
        file.write(json_output)

    return json_output
