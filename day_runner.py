import paths
from constants import PART_ONE, PART_TWO
from utils.File import read_file, write_file
from days import day_1, day_2

DAYS = {
    1: day_1,
    2: day_2,
}


def get_io_files(day, part, sample):
    input_a_file = paths.get_file_for_day(paths.INPUT_TYPE, day)
    input_sample_file = paths.get_file_for_day(paths.INPUT_SAMPLE_TYPE, day)
    output_a_file = paths.get_file_for_day(paths.OUTPUT_TYPE_A, day)
    output_b_file = paths.get_file_for_day(paths.OUTPUT_TYPE_B, day)
    output_sample_file = paths.get_file_for_day(paths.OUTPUT_SAMPLE_TYPE, day)

    input_file = input_sample_file
    output_file = output_sample_file

    if not sample:
        input_file = input_a_file
        if part == PART_ONE:
            output_file = output_a_file
        elif part == PART_TWO:
            output_file = output_b_file

    return [input_file, output_file]


def run(day, part, sample=False):
    input_file, output_file = get_io_files(day, part, sample)

    if part == PART_ONE:
        output_data = DAYS[day].run_a(read_file(input_file))
    elif part == PART_TWO:
        output_data = DAYS[day].run_b(read_file(input_file))

    write_file(output_file, output_data)


