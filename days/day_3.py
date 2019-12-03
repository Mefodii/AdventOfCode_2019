from utils.File import write_file

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

CROSS = "X"
CENTRAL = "O"
EMPTY = "."

START_X, START_Y = 0, 0


def plot_cell(cell_value, wire_id):
    if cell_value is None:
        return str(wire_id)
    elif cell_value == CROSS or cell_value == CENTRAL or cell_value == str(wire_id):
        pass
    elif not cell_value == EMPTY:
        return CROSS
    else:
        return str(wire_id)


def plot_up(grid, distance, x, y, wire_id):
    for i in range(distance):
        y += 1
        coords = f"{x},{y}"
        grid[coords] = plot_cell(grid.get(coords, None), wire_id)

    return [grid, x, y]


def plot_down(grid, distance, x, y, wire_id):
    for i in range(distance):
        y -= 1
        coords = f"{x},{y}"
        grid[coords] = plot_cell(grid.get(coords, None), wire_id)

    return [grid, x, y]


def plot_left(grid, distance, x, y, wire_id):
    for i in range(distance):
        x -= 1
        coords = f"{x},{y}"
        grid[coords] = plot_cell(grid.get(coords, None), wire_id)

    return [grid, x, y]


def plot_right(grid, distance, x, y, wire_id):
    for i in range(distance):
        x += 1
        coords = f"{x},{y}"
        grid[coords] = plot_cell(grid.get(coords, None), wire_id)

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
    closest = 9999999
    for key, value in grid.items():
        x, y = key.split(",")
        if value == CROSS:
            distance = calculate_distance(START_X, START_Y, int(x), int(y))
            closest = min(distance, closest)

    return closest


def plot_wire(grid, commands, wire_id):
    grid_x = START_X
    grid_y = START_Y
    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        grid, grid_x, grid_y = PLOTS[direction](grid, distance, grid_x, grid_y, wire_id)


###############################################################################
def run_a(input_data):
    grid = {
        f"{START_X},{START_Y}": CENTRAL
    }

    wire_id = 0
    for wire in input_data:
        wire_id += 1
        plot_wire(grid, wire.split(","), wire_id)

    return [closest_cross(grid)]


def run_b(input_data):
    return ""
