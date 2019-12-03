from utils.File import write_file

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

CROSS = "X"
CENTRAL = "O"
EMPTY = "."

GRID_X, GRID_Y = 40000, 5000
START_X, START_Y = GRID_X / 2, GRID_Y / 2


def print_grid(grid):
    lines = []
    for column in range(len(grid[0]) - 1, -1, -1):
        print_row = []
        for row in range(len(grid)):
            print_row.append(str(grid[row][column]))

        lines.append("".join(print_row))

    return lines


def generate_grid(x, y):
    grid = [[EMPTY for j in range(x)] for i in range(y)]
    grid[START_X][START_Y] = CENTRAL
    return grid


def plot_cell(cell_value, wire_id):
    if cell_value == CROSS or cell_value == CENTRAL or cell_value == str(wire_id):
        pass
    elif not cell_value == EMPTY:
        return CROSS
    else:
        return str(wire_id)


def plot_up(grid, distance, x, y, wire_id):
    for i in range(distance):
        y += 1
        grid[x][y] = plot_cell(grid[x][y], wire_id)

    return [grid, x, y]


def plot_down(grid, distance, x, y, wire_id):
    for i in range(distance):
        y -= 1
        grid[x][y] = plot_cell(grid[x][y], wire_id)

    return [grid, x, y]


def plot_left(grid, distance, x, y, wire_id):
    for i in range(distance):
        x -= 1
        grid[x][y] = plot_cell(grid[x][y], wire_id)

    return [grid, x, y]


def plot_right(grid, distance, x, y, wire_id):
    for i in range(distance):
        x += 1
        grid[x][y] = plot_cell(grid[x][y], wire_id)

    return [grid, x, y]


PLOTS = {
    UP: plot_up,
    DOWN: plot_down,
    LEFT: plot_left,
    RIGHT: plot_right,
}


def calculate_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def closest_cross(grid):
    closest = len(grid) + len(grid[0])
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == CROSS:
                distance = calculate_distance(START_X, START_Y, x, y)
                if distance < closest:
                    closest = distance

    return closest


def plot_wire(grid, commands, wire_id):
    grid_x = START_X
    grid_y = START_Y
    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        grid, grid_x, grid_y = PLOTS[direction](grid, distance, grid_x, grid_y, wire_id)


def calculate_grid_limits(commands):
    l_x, h_x, l_y, h_y = 0, 0, 0, 0
    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        if direction == UP:
            h_x += distance
        if direction == DOWN:
            l_x += distance
        if direction == LEFT:
            l_y += distance
        if direction == RIGHT:
            h_y += distance

    return [l_x, h_x, l_y, h_y]



###############################################################################
def run_a(input_data):
    # grid = generate_grid(30000, 30000)

    wire_id = 0
    for wire in input_data:
        print(calculate_grid_limits(wire.split(",")))
        wire_id += 1
        # plot_wire(grid, wire.split(","), wire_id)

    # write_file("debug.txt", print_grid(grid))
    # return [closest_cross(grid)]


def run_b(input_data):
    return ""
