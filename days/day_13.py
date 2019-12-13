ADD = "01"
MULTIPLY = "02"
INPUT = "03"
OUTPUT = "04"
JIT = "05"
JIF = "06"
LT = "07"
EQ = "08"
ADJUST_RELATIVE_BASE = "09"
END = "99"

POSITION_MODE = "0"
IMMEDIATE_MODE = "1"
RELATIVE_MODE = "2"

SCORE = -1
BLOCK = 2
PADDLE = 3
BALL = 4


###############################################################################
def run_a(input_data):
    split_data = input_data[0].split(",")
    extended_memory = ["0" for i in range(1000)]

    result = calculate([], split_data + extended_memory, 0)
    block_tiles = count_block_tiles(result)
    print(block_tiles)
    return [block_tiles]


def run_b(input_data):
    split_data = input_data[0].split(",")
    extended_memory = ["0" for i in range(10000)]

    score = simulate(split_data + extended_memory)
    return [score]


def simulate(data):
    entities = map_entities(calculate([], data, 0)["OUTPUT"])

    data[0] = "2"
    while entities[SCORE] == 0:
        move = 0
        if entities[PADDLE][0] > entities[BALL][0]:
            move = -1
        if entities[PADDLE][0] > entities[BALL][0]:
            move = 1

        result = calculate([move], data, 0)
        entities = map_entities(result["OUTPUT"])
        print(entities)

    return entities[SCORE]


def map_entities(data):
    entities = {}
    for i in range(0, len(data), 3):
        line = data[i:i+3]
        if line[0] == -1 and line[1] == 0:
            entities[SCORE] = line[2]
        elif line[2] == PADDLE:
            entities[PADDLE] = [line[0], line[1]]
        elif line[2] == BALL:
            entities[BALL] = [line[0], line[1]]
        elif line[2] == BLOCK:
            entities[BLOCK] = entities.get(BLOCK, 0) + 1

    entities[BLOCK] = entities.get(BLOCK, 0)
    entities[SCORE] = entities.get(SCORE, 0)
    return entities


def count_block_tiles(intcode_result):
    block_tiles = 0
    for i in range(0, len(intcode_result["OUTPUT"]), 3):
        print(intcode_result["OUTPUT"][i:i+3])
        if intcode_result["OUTPUT"][i+2] == 2:
            block_tiles += 1

    return block_tiles


def build_command(command_line):
    while len(command_line) < 4:
        command_line.append(-1)

    op = command_line[0].rjust(5, "0")
    commands = [op[3:],
                op[2],
                op[1],
                op[0],
                int(command_line[1]),
                int(command_line[2]),
                int(command_line[3]),
                ]
    return commands


def calculate(inputs, data, start_index, base=0):
    i = start_index
    relative_base = base
    end = False
    results = {"OUTPUT": [],
               "END": end}

    input_index = 0

    while not end:
        operation, in_1_mode, in_2_mode, out_mode, in_1, in_2, out = build_command(data[i:i+4])

        # print(data[i:i+4], operation, in_1_mode, in_2_mode, out_mode, in_1, in_2, out, relative_base)

        if operation in [ADD, MULTIPLY, JIF, JIT, LT, EQ, ADJUST_RELATIVE_BASE, OUTPUT, INPUT]:
            op_1 = in_1
            if in_1_mode == POSITION_MODE:
                op_1 = int(data[in_1])
            elif in_1_mode == RELATIVE_MODE:
                op_1 = int(data[relative_base + in_1])

        if operation in [ADD, MULTIPLY, JIF, JIT, LT, EQ]:
            op_2 = in_2
            if in_2_mode == POSITION_MODE:
                op_2 = int(data[in_2])
            elif in_2_mode == RELATIVE_MODE:
                op_2 = int(data[relative_base + in_2])

        if out_mode == RELATIVE_MODE:
            out += relative_base

        if operation == ADD:
            result = op_1 + op_2
            data[out] = str(result)
            i += 4
        elif operation == MULTIPLY:
            result = op_1 * op_2
            data[out] = str(result)
            i += 4
        elif operation == INPUT:
            if in_1_mode == RELATIVE_MODE:
                data[in_1 + relative_base] = inputs[input_index]
            else:
                data[in_1] = inputs[input_index]
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
            results["OUTPUT"].append(op_1)
            i += 2

            # if len(results["OUTPUT"]) >= 2:
            #     results["INDEX"] = i
            #     results["BASE"] = relative_base
            #     return results
        elif operation == ADJUST_RELATIVE_BASE:
            relative_base += op_1
            i += 2
        elif operation == END:
            end = True
        else:
            print("Oups", operation)
            end = True

    results["END"] = True
    return results
