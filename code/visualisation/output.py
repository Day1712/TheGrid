from code.classes import district
import json

def tuple_to_string(list_of_tuples):
    new_list = []
    for tuble in list_of_tuples:
        new_list.append(",".join(map(str, tuble)))
    return new_list

def generate_json(district):
    data = []
    data.append({"district": district.district_number, "costs-shared": district.shared_cost})

    for battery in district.batteries:
        data.append({"location": battery.location, "capacity": battery.max_capacity, "houses": []})

        for house in district.houses:

            # Only adding houses to the list if they lead to that battery
            if house.cables[-1] == (battery.pos_x, battery.pos_y):
                data[-1]["houses"].append({"location": house.location, "output": house.output, "cables": tuple_to_string(house.cables)})

    json_output = json.dumps(data, indent = 2)
    with open("output.json", "w") as file:
        file.write(json_output)

    return json_output
