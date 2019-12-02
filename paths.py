import os

PROJECT_PATH = "\\".join(os.getcwd().split("\\"))
FILES_PATH = PROJECT_PATH + "\\files"
INPUT_FILES_PATH = FILES_PATH + "\\input"
OUTPUT_FILES_PATH = FILES_PATH + "\\output"
DAYS = 25

ID_TAG = "<ID>"
INPUT_VAR = "INPUT_<ID>"
OUTPUT_VAR_A = "OUTPUT_<ID>_A"
OUTPUT_VAR_B = "OUTPUT_<ID>_B"
INPUT_SAMPLE_VAR = "INPUT_<ID>_S"
OUTPUT_SAMPLE_VAR = "OUTPUT_<ID>_S"

INPUT_TYPE = "I"
INPUT_SAMPLE_TYPE = "SI"
OUTPUT_TYPE_A = "OA"
OUTPUT_TYPE_B = "OB"
OUTPUT_SAMPLE_TYPE = "SO"


def build_files_dict():
    result = {}
    for i in range(1, DAYS + 1):
        input_file = f"{INPUT_FILES_PATH}\\i_day_{i}.txt"
        output_a_file = f"{OUTPUT_FILES_PATH}\\o_day_{i}_a.txt"
        output_b_file = f"{OUTPUT_FILES_PATH}\\o_day_{i}_b.txt"
        input_sample_file = f"{INPUT_FILES_PATH}\\i_day_{i}_sample.txt"
        output_sample_file = f"{OUTPUT_FILES_PATH}\\o_day_{i}_sample.txt"

        input_var = INPUT_VAR.replace(ID_TAG, str(i))
        output_a_var = OUTPUT_VAR_A.replace(ID_TAG, str(i))
        output_b_var = OUTPUT_VAR_B.replace(ID_TAG, str(i))
        input_sample_var = INPUT_SAMPLE_VAR.replace(ID_TAG, str(i))
        output_sample_var = OUTPUT_SAMPLE_VAR.replace(ID_TAG, str(i))

        result[input_var] = input_file
        result[output_a_var] = output_a_file
        result[output_b_var] = output_b_file
        result[input_sample_var] = input_sample_file
        result[output_sample_var] = output_sample_file

    return result


FILES_DICT = build_files_dict()


def get_file_for_day(file_type="", day=0):
    var = None
    if not 0 < day <= DAYS:
        raise Exception("Day not in range")
    if file_type == INPUT_TYPE:
        var = INPUT_VAR
    elif file_type == OUTPUT_TYPE_A:
        var = OUTPUT_VAR_A
    elif file_type == OUTPUT_TYPE_B:
        var = OUTPUT_VAR_B
    elif file_type == INPUT_SAMPLE_TYPE:
        var = INPUT_SAMPLE_VAR
    elif file_type == OUTPUT_SAMPLE_TYPE:
        var = OUTPUT_SAMPLE_VAR
    else:
        raise Exception("Type not valid")

    return FILES_DICT.get(var.replace(ID_TAG, str(day)))