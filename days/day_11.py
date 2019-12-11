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

BLACK = 0
WHITE = 1

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

RIGHT_TURN = {UP: RIGHT,
              RIGHT: DOWN,
              DOWN: LEFT,
              LEFT: UP}

LEFT_TURN = {UP: LEFT,
             LEFT: DOWN,
             DOWN: RIGHT,
             RIGHT: UP}

TURNS = [LEFT_TURN, RIGHT_TURN]


###############################################################################
def run_a(input_data):
    split_data = input_data[0].split(",")
    extended_memory = ["0" for i in range(1000)]

    result = count_unique_tiles(split_data + extended_memory)
    print(result)
    return [result]


def run_b(input_data):
    split_data = input_data[0].split(",")
    extended_memory = ["0" for i in range(10000)]

    result = calculate([2], list(split_data + extended_memory), 0)
    print(result)
    return [result["OUTPUT"][-1]]


def count_unique_tiles(data):
    panel = {}
    current_tile_color = BLACK
    x, y = 0, 0
    direction = UP
    index = 0

    result = calculate([current_tile_color], data, index)
    while not result["END"]:
        result_tile_color = result["OUTPUT"][0]
        turn = result["OUTPUT"][1]
        index = result["INDEX"]
        panel[y] = panel.get(y, {})
        panel[y][x] = result_tile_color

        direction = turn_robot(direction, int(turn))
        x, y = move(x, y, direction)
        current_tile_color = panel.get(y, {}).get(x, BLACK)

        print(result_tile_color, turn, direction, x, y)
        result = calculate([current_tile_color], data, index)

    panels = 0
    for key, row in panel.items():
        for column, value in row.items():
            panels += 1

    print(panels)
    return panels


def move(x, y, direction):
    if direction == UP:
        return [x, y - 1]
    if direction == DOWN:
        return [x, y + 1]
    if direction == LEFT:
        return [x - 1, y]
    if direction == RIGHT:
        return [x + 1, y]


def turn_robot(direction, turn):
    return TURNS[turn][direction]


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


def calculate(inputs, data, start_index):
    i = start_index
    relative_base = 0
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

            if len(results["OUTPUT"]) >= 2:
                results["INDEX"] = i
                return results
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
