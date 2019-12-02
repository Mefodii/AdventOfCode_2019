from paths import INPUT_FILES_PATH, OUTPUT_FILES_PATH
from constants import PART_ONE, PART_TWO, FILE_TEMPLATES, DAY_TAG
from constants import INPUT_TYPE, INPUT_SAMPLE_TYPE, OUTPUT_A_TYPE, OUTPUT_B_TYPE, OUTPUT_SAMPLE_TYPE
from utils.File import read_file, write_file
from days import day_1, day_2

DAYS = {
    1: day_1,
    2: day_2,
}


def get_io_files(day, part, sample):
    if sample:
        input_file = FILE_TEMPLATES[INPUT_SAMPLE_TYPE].replace(DAY_TAG, str(day))
        output_file = FILE_TEMPLATES[OUTPUT_SAMPLE_TYPE].replace(DAY_TAG, str(day))
    else:
        input_file = FILE_TEMPLATES[INPUT_TYPE].replace(DAY_TAG, str(day))
        if part == PART_ONE:
            output_file = FILE_TEMPLATES[OUTPUT_A_TYPE].replace(DAY_TAG, str(day))
        else:
            output_file = FILE_TEMPLATES[OUTPUT_B_TYPE].replace(DAY_TAG, str(day))

    input_file_path = "\\".join([INPUT_FILES_PATH, input_file])
    output_file_path = "\\".join([OUTPUT_FILES_PATH, output_file])
    return [input_file_path, output_file_path]


def run(day, part, sample=False):
    input_file, output_file = get_io_files(day, part, sample)

    output_data = ["None"]
    if part == PART_ONE:
        output_data = DAYS[day].run_a(read_file(input_file))
    elif part == PART_TWO:
        output_data = DAYS[day].run_b(read_file(input_file))

    write_file(output_file, output_data)
