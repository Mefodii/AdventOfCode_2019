import copy

ASTEROID = "ASTEROID"
FOV = "FOV"
BLOCKED = "BLOCKED"
COUNT = "COUNT"


###############################################################################
def run_a(input_data):
    the_map = build_map(input_data)
    max_x = len(input_data[0])
    max_y = len(input_data)
    y, x, max_count = check_fov(the_map, max_x, max_y)
    print(max_count)
    return [max_count]


def run_b(input_data):
    the_map = build_map(input_data)
    max_x = len(input_data[0])
    max_y = len(input_data)
    y, x, max_count = check_fov(the_map, max_x, max_y)

    y1, x1 = pulse_asteroids(y, x, the_map, 200, max_x, max_y)

    return [max_count]


def pulse_asteroids(y, x, the_map, count, max_x, max_y):
    asteroid = update_asteroid_fov(y, x, copy.deepcopy(the_map), max_x, max_y)
    print(asteroid)
    return [0, 0]


def check_fov(the_map, max_x, max_y):
    max_count = 0
    y1, x1 = -1, -1
    y = 0
    row = the_map.get(y, None)
    while row is not None:
        x = 0
        cell = row.get(x, None)
        while cell is not None:
            if cell[ASTEROID]:
                cell = update_asteroid_fov(y, x, copy.deepcopy(the_map), max_x, max_y)
                if cell[COUNT] > max_count:
                    y1, x1 = y, x
                    max_count = cell[COUNT]
            x += 1
            cell = row.get(x, None)
        y += 1
        row = the_map.get(y, None)

    return [y1, x1, max_count]


def update_asteroid_fov(y, x, asteroids_map, max_x, max_y):
    def parse_fov(step_y, step_x):
        asteroid_in_fov = False

        yy = y + step_y
        xx = x + step_x
        val = asteroids_map.get(yy, {}).get(xx, None)
        if val[ASTEROID]:
            asteroid_in_fov = True

        yy += step_y
        xx += step_x
        val = asteroids_map.get(yy, {}).get(xx, None)

        while val:
            if val[ASTEROID]:
                asteroid_in_fov = True
            val[BLOCKED] = True
            yy += step_y
            xx += step_x
            val = asteroids_map.get(yy, {}).get(xx, None)

        return asteroid_in_fov

    def build_coords(distance):
        width = distance * 2 + 1
        top = [[y - distance, x1] for x1 in range(x - (width // 2), x + (width // 2) + 1)]
        bottom = [[y + distance, x1] for x1 in range(x - (width // 2), x + (width // 2) + 1)]
        left = [[y1, x - distance] for y1 in range(y - ((width - 2) // 2), y + ((width - 2) // 2) + 1)]
        right = [[y1, x + distance] for y1 in range(y - ((width - 2) // 2), y + ((width - 2) // 2) + 1)]

        return top + bottom + left + right

    def in_range(distance):
        return not (x + distance >= max_x and x - distance < 0 and y + distance >= max_y and y - distance < 0)

    dist = 1
    asteroid = asteroids_map[y][x]
    while in_range(dist):
        coords = build_coords(dist)
        for y1, x1 in coords:
            cell = asteroids_map.get(y1, {}).get(x1, None)
            if cell and (not cell[BLOCKED]):
                if parse_fov(y1 - y, x1 - x):
                    asteroid[COUNT] += 1
                    asteroid[FOV][y1] = asteroid[FOV].get(y1, {})
                    asteroid[FOV][y1][x1] = cell
                # mark_blocked(y1 - y, x1 - x)
        dist += 1

    return asteroid


def build_map(data):
    asteroids = {}
    for row in range(0, len(data)):
        for column in range(0, len(data[0])):
            asteroid_belt = asteroids.get(row, {})
            asteroid_belt[column] = {FOV: {},
                                     ASTEROID: data[row][column] == "#",
                                     BLOCKED: False,
                                     COUNT: 0}
            asteroids[row] = asteroid_belt

    return asteroids
