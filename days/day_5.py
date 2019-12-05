ADD = "01"
MULTIPLY = "02"
INPUT = "03"
OUTPUT = "04"
JIT = "05"
JIF = "06"
LT = "07"
EQ = "08"
END = "99"

POSITION_MODE = "0"
IMMEDIATE_MODE = "1"


###############################################################################
def run_a(input_data):
    split_data = input_data[0].split(",")

    return [calculate("1", split_data)]


def run_b(input_data):
    split_data = input_data[0].split(",")

    return [calculate("5", split_data)]


def build_command(command_line):
    while len(command_line) < 4:
        command_line.append(-1)

    op = command_line[0].rjust(5, "0")
    commands = [op[3:],
                op[2],
                op[1],
                int(command_line[1]),
                int(command_line[2]),
                int(command_line[3]),
                ]
    return commands


def calculate(input_value, data):
    i = 0
    end = False
    results = []
    while not end:
        operation, in_1_mode, in_2_mode, in_1, in_2, out = build_command(data[i:i+4])

        if operation in [ADD, MULTIPLY, JIF, JIT, LT, EQ]:
            op_1 = in_1
            if in_1_mode == POSITION_MODE:
                op_1 = int(data[in_1])

            op_2 = in_2
            if in_2_mode == POSITION_MODE:
                op_2 = int(data[in_2])

        if operation == ADD:
            result = op_1 + op_2
            data[out] = str(result)
            i += 4
        elif operation == MULTIPLY:
            result = op_1 * op_2
            data[out] = str(result)
            i += 4
        elif operation == INPUT:
            data[in_1] = input_value
            i += 2
        elif operation == JIT:
            i += 3
            if not op_1 == 0:
                i = op_2
        elif operation == JIF:
            i += 3
            if op_1 == 0:
                i = op_2
        elif operation == LT:
            if op_1 < op_2:
                data[out] = 1
            else:
                data[out] = 0
            i += 4
        elif operation == EQ:
            if op_1 == op_2:
                data[out] = 1
            else:
                data[out] = 0
            i += 4
        elif operation == OUTPUT:
            results.append(data[in_1])
            i += 2
        elif operation == END:
            end = True
        else:
            print("Oups")
            end = True

    return results[-1]
