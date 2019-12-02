from constants import RUN_A, RUN_B


def calculate_fuel(mass):
    return (mass // 3) - 2


###############################################################################
def run_a(input_data):
    total_fuel_req = 0
    for line in input_data:
        total_fuel_req += calculate_fuel(int(line))
    return [total_fuel_req]


def run_b(input_data):
    total_fuel_req = 0
    for line in input_data:
        mass = int(line)
        while mass > 0:
            mass = calculate_fuel(mass)
            if mass > 0:
                total_fuel_req += mass
    return [total_fuel_req]


def run(data, run_type=""):
    if run_type == RUN_A:
        return run_a(data)
    elif run_type == RUN_B:
        return run_b(data)



