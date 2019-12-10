import copy
from math import gcd, atan2, degrees

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

    return [str(x1 * 100 + y1)]


def angle(x1, y1, x2, y2):
    value = degrees(atan2(y2-y1, x2-x1))
    if value < 0:
        value = 360 + value
    value += 90
    if value >= 360:
        value -= 360

    return value


def pulse_asteroids(y, x, the_map, count, max_x, max_y):
    asteroid = None

    current_scan_count = 0
    while current_scan_count < count:
        asteroid = update_asteroid_fov(y, x, copy.deepcopy(the_map), max_x, max_y)

        for row, value in asteroid[FOV].items():
            for column, fov in value.items():
                current_scan_count += 1

        if current_scan_count < count:
            pulse(asteroid, the_map)

    angles = []
    data = {}

    for row, value in asteroid[FOV].items():
        for column, fow in value.items():
            ang = angle(x, y, column, row)
            data[str(ang)] = [row, column]
            angles.append(ang)

    list.sort(angles)
    print(current_scan_count, len(angles), angles[count])
    return data[str(angles[count-1])]


def pulse(asteroid, the_map):
    for row, value in asteroid[FOV].items():
        for column, fow in value.items():
            the_map[row][column][ASTEROID] = False


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
        asteroid_in_fov = None

        yy = y + step_y
        xx = x + step_x
        val = asteroids_map.get(yy, {}).get(xx, None)
        if val[ASTEROID] and not val[BLOCKED]:
            asteroid_in_fov = [yy, xx]

        yy += step_y
        xx += step_x
        val = asteroids_map.get(yy, {}).get(xx, None)

        while val:
            if val[ASTEROID] and not val[BLOCKED] and not asteroid_in_fov:
                asteroid_in_fov = [yy, xx]
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
                result = parse_fov(y1 - y, x1 - x)
                if result:
                    asteroid[COUNT] += 1
                    asteroid[FOV][result[0]] = asteroid[FOV].get(result[0], {})
                    asteroid[FOV][result[0]][result[1]] = result
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
