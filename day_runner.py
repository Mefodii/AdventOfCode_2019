import paths
from constants import RUN_A, RUN_B
from utils.File import read_file, write_file
from days import day_1, day_2

DAYS = {
    1: day_1.run,
    2: day_2.run
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
        if part == RUN_A:
            output_file = output_a_file
        elif part == RUN_B:
            output_file = output_b_file

    return [input_file, output_file]


def run(day, part, sample=False):
    input_file, output_file = get_io_files(day, part, sample)

    output_data = DAYS[day](read_file(input_file), part)

    write_file(output_file, output_data)


