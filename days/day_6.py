###############################################################################
def run_a(input_data):
    system = build_system(input_data)
    direct, total = calculate_system_orbits(system)
    return [total]


def run_b(input_data):
    system = build_system(input_data)
    distance = calculate_distance_to_santa(system)
    return [distance]


def build_system(data):
    system = {}
    for orbit in data:
        obj_1, obj_2 = orbit.split(")")
        system[obj_1] = system.get(obj_1, []) + [obj_2]

    return system


COM = "COM"
MY_LOCATION = "YOU"
SANTA_LOCATION = "SAN"


def calculate_system_orbits(system):
    direct, total = calculate_orbits(0, COM, system)
    return [direct, total]


def calculate_distance_to_santa(system):
    path_to_me = set(calculate_path_to_obj([], COM, MY_LOCATION, system))
    path_to_santa = set(calculate_path_to_obj([], COM, SANTA_LOCATION, system))

    distance = len(path_to_me - path_to_santa) + len(path_to_santa - path_to_me) - 2
    return distance


def calculate_path_to_obj(path, obj, target_obj, system):
    current_path = path + [obj]
    if obj == target_obj:
        return current_path
    else:
        for sat in system.get(obj, []):
            result = calculate_path_to_obj(current_path, sat, target_obj, system)
            if target_obj in result:
                return result

    return current_path


def calculate_orbits(path, obj, system):
    direct, total = len(system.get(obj, [])), path
    path += 1
    for sat in system.get(obj, []):
        result = calculate_orbits(path, sat, system)
        direct += result[0]
        total += result[1]

    return [direct, total]