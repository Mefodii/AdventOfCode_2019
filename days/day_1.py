import paths
from constants import RUN_A, RUN_B, RUN_SAMPLE_A, RUN_SAMPLE_B
from utils.File import read_file, write_file

# CHANGE THE DAY
DAY = 1
################

INPUT_FILE = paths.get_file_for_day(paths.INPUT_TYPE, DAY)
INPUT_SAMPLE_FILE = paths.get_file_for_day(paths.INPUT_SAMPLE_TYPE, DAY)
OUTPUT_A_FILE = paths.get_file_for_day(paths.OUTPUT_TYPE_A, DAY)
OUTPUT_B_FILE = paths.get_file_for_day(paths.OUTPUT_TYPE_B, DAY)
OUTPUT_SAMPLE_FILE = paths.get_file_for_day(paths.OUTPUT_SAMPLE_TYPE, DAY)


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


def run(run_type=""):
    output_data = None
    output_file = None

    if run_type == RUN_SAMPLE_A:
        output_data = run_a(read_file(INPUT_SAMPLE_FILE))
        output_file = OUTPUT_SAMPLE_FILE
    elif run_type == RUN_A:
        output_data = run_a(read_file(INPUT_FILE))
        output_file = OUTPUT_A_FILE
    elif run_type == RUN_SAMPLE_B:
        output_data = run_b(read_file(INPUT_SAMPLE_FILE))
        output_file = OUTPUT_SAMPLE_FILE
    elif run_type == RUN_B:
        output_data = run_b(read_file(INPUT_FILE))
        output_file = OUTPUT_B_FILE

    write_file(output_file, output_data)


