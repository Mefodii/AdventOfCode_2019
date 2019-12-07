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

    result = calculate_max_thrust(split_data)
    print(result)
    return [result]


def run_b(input_data):
    split_data = input_data[0].split(",")

    result = calculate_max_loop_thrust(split_data)
    print(result)
    return [result]


def calculate_max_thrust(data):
    max_phase = 4
    max_thrust = 0

    phase_seq = [0, 0, 0, 0, 0]

    while not phase_seq[0] == 5:
        all_thruster_data = [list(data) for i in range(5)]
        if len(set(phase_seq)) == 5:
            thrust_result = calculate_thrust(0, all_thruster_data, phase_seq)
            thrust = int(thrust_result.get("OUTPUT")[-1])
            max_thrust = max(thrust, max_thrust)

        phase_seq[-1] += 1
        for i in range(len(phase_seq) - 1, 0, -1):
            if phase_seq[i] > max_phase:
                phase_seq[i] = 0
                phase_seq[i - 1] += 1

    return max_thrust


def calculate_max_loop_thrust(data):
    max_phase = 9
    min_phase = 5
    max_thrust = 0

    phase_seq = [5 for i in range(5)]
    # phase_seq = [9,7,8,5,6]

    while not phase_seq[0] == 10:
        if len(set(phase_seq)) == 5:
            end_loop = False
            thrust = 0
            start_indexes = [0, 0, 0, 0, 0]
            all_thruster_data = [list(data) for i in range(5)]
            while not end_loop:
                thrust_result = calculate_thrust(thrust, all_thruster_data, phase_seq, start_indexes)
                end_loop = thrust_result["END"]
                start_indexes = thrust_result["INDEXES"]
                if not end_loop:
                    thrust = int(thrust_result.get("OUTPUT")[-1])

            max_thrust = max(thrust, max_thrust)

        phase_seq[-1] += 1
        for i in range(len(phase_seq) - 1, 0, -1):
            if phase_seq[i] > max_phase:
                phase_seq[i] = min_phase
                phase_seq[i - 1] += 1

        # phase_seq[0] = 10

    return max_thrust


def calculate_thrust(initial_thrust, all_thruster_data, phase_seq, start_indexes=None):
    if not start_indexes:
        start_indexes = [0, 0, 0, 0, 0]

    result = 0
    in_2 = initial_thrust
    i = 0
    for in_1 in phase_seq:
        result = calculate([in_1, in_2], all_thruster_data[i], start_indexes[i])
        start_indexes[i] = result["INDEX"]

        if not result["END"]:
            in_2 = int(result.get("OUTPUT")[-1])

        i += 1

    result["INDEXES"] = start_indexes
    return result


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


def calculate(inputs, data, start_index):
    i = start_index
    end = False
    results = {"OUTPUT": []}
    input_index = 0
    if i > 0:
        input_index = 1

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
            data[in_1] = inputs[input_index]
            input_index = 1
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
            results["OUTPUT"].append(data[in_1])
            # results["DATA"] = data
            results["END"] = False
            i += 2
            results["INDEX"] = i
            return results
        elif operation == END:
            end = True
        else:
            print("Oups")
            end = True

    # results["DATA"] = data
    results["END"] = True
    results["INDEX"] = 0
    return results
