from math import gcd

PX = "px"
PY = "py"
PZ = "pz"
VX = "vx"
VY = "vy"
VZ = "vz"

X = [PX, VX]
Y = [PY, VY]
Z = [PZ, VZ]


###############################################################################
def run_a(input_data):
    moons = build_moons(input_data)

    energy = simulate(1000, moons)
    print(energy)
    return [energy]


def run_b(input_data):
    moons = build_moons(input_data)

    x_repeat_rate = simulate_axis(moons, X)
    y_repeat_rate = simulate_axis(moons, Y)
    z_repeat_rate = simulate_axis(moons, Z)
    xy = int(lcm(x_repeat_rate, y_repeat_rate))
    yz = int(lcm(z_repeat_rate, y_repeat_rate))
    xyz = int(lcm(xy, yz))

    print(xyz)

    return [xyz]


def simulate_axis(moons, axis):
    initial_state = get_axis_state(moons, axis)
    state_found = False
    steps = 0

    while not state_found:
        steps += 1
        for i in range(0, len(moons) - 1):
            moon = moons[i]
            for j in range(i + 1, len(moons)):
                next_moon = moons[j]

                change_velocity(moon, next_moon, axis)

        for moon in moons:
            move(moon, axis)

        state_found = is_state_equal(initial_state, get_axis_state(moons, axis))

    return steps


def get_axis_state(moons, axis):
    state = []
    for moon in moons:
        state.append(moon[axis[0]])
        state.append(moon[axis[1]])

    return state


def is_state_equal(state, other_state):
    for i in range(len(state)):
        if not state[i] == other_state[i]:
            return False

    return True


def simulate(steps, moons):
    for step in range(steps):
        apply_gravity(moons)
        apply_velocity(moons)

    energy = calculate_energy(moons)
    return energy


def calculate_energy(moons):
    energy = 0

    for moon in moons:
        energy += calculate_moon_energy(moon)

    return energy


def calculate_moon_energy(moon):
    pot = abs(moon[PX]) + abs(moon[PY]) + abs(moon[PZ])
    kin = abs(moon[VX]) + abs(moon[VY]) + abs(moon[VZ])

    return pot * kin


def apply_velocity(moons):
    for moon in moons:
        move(moon, X)
        move(moon, Y)
        move(moon, Z)


def move(moon, axis):
    position_axis = axis[0]
    velocity_axis = axis[1]
    moon[position_axis] += moon[velocity_axis]


def apply_gravity(moons):
    for i in range(0, len(moons) - 1):
        moon = moons[i]
        for j in range(i + 1, len(moons)):
            next_moon = moons[j]

            change_velocity(moon, next_moon, X)
            change_velocity(moon, next_moon, Y)
            change_velocity(moon, next_moon, Z)


def change_velocity(moon, next_moon, axis):
    position_axis = axis[0]
    velocity_axis = axis[1]
    if moon[position_axis] > next_moon[position_axis]:
        moon[velocity_axis] -= 1
        next_moon[velocity_axis] += 1

    if moon[position_axis] < next_moon[position_axis]:
        moon[velocity_axis] += 1
        next_moon[velocity_axis] -= 1


def build_moons(data):
    moons = []

    for line in data:
        parms = line.split(",")
        x = int(parms[0].split("=")[-1])
        y = int(parms[1].split("=")[-1])
        z = int(parms[2].split("=")[-1][:-1])
        moon = {PX: x, PY: y, PZ: z, VX: 0, VY: 0, VZ: 0}
        moons.append(moon)

    return moons


def lcm(a, b):
    return a * b / gcd(a, b)
