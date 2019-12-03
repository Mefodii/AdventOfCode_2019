WIRE_ID = "ID"
WIRE_DISTANCE = "DIST"

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

VALUE = "VALUE"
WIRE = "WIRE"
CROSS = "X"
CENTRAL = "O"

START_X, START_Y = 0, 0


def plot_cell(cell, wire):
    wire[WIRE_DISTANCE] += 1
    wire_id = wire[WIRE_ID]
    wire_distance = wire[WIRE_DISTANCE]
    cell_result = {
        VALUE: str(wire_id),
        wire_id: wire_distance
    }

    if cell:
        cell_result = cell

        value = cell[VALUE]
        if value == CROSS or value == CENTRAL or value == str(wire_id):
            pass
        else:
            cell_result[VALUE] = CROSS
            cell_result[wire_id] = wire_distance

    return cell_result


DIRECTIONS = {
    UP: [0, 1],
    DOWN: [0, -1],
    LEFT: [-1, 0],
    RIGHT: [1, 0],
}


def plot_direction(grid, direction, distance, x, y, wire):
    for i in range(distance):
        x += DIRECTIONS[direction][0]
        y += DIRECTIONS[direction][1]
        coords = f"{x},{y}"
        grid[coords] = plot_cell(grid.get(coords, None), wire)

    return [grid, x, y]


def calculate_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def closest_cross(grid):
    closest = 9999999
    for key, value in grid.items():
        x, y = key.split(",")
        if value[VALUE] == CROSS:
            distance = calculate_distance(START_X, START_Y, int(x), int(y))
            closest = min(distance, closest)

    return closest


def shortest_cross(grid):
    shortest = 9999999
    for key, value in grid.items():
        x, y = key.split(",")
        if value[VALUE] == CROSS:
            wires_length = 0
            for key2, wire_len in value.items():
                if not key2 == VALUE:
                    wires_length += wire_len
            shortest = min(wires_length, shortest)

    return shortest


def plot_wire(grid, commands, wire):
    grid_x = START_X
    grid_y = START_Y
    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        grid, grid_x, grid_y = plot_direction(grid, direction, distance, grid_x, grid_y, wire)


def plot_grid(input_data):
    grid = {
        f"{START_X},{START_Y}": {
            VALUE: CENTRAL
        }
    }

    wire_id = 0
    for wire_path in input_data:
        wire_id += 1
        wire = {
            WIRE_ID: wire_id,
            WIRE_DISTANCE: 0
        }
        plot_wire(grid, wire_path.split(","), wire)

    return grid


###############################################################################
def run_a(input_data):
    grid = plot_grid(input_data)
    return [closest_cross(grid)]


def run_b(input_data):
    grid = plot_grid(input_data)
    return [shortest_cross(grid)]
