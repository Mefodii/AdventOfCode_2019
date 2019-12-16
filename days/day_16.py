PATTERN = [0, 1, 0, -1]


###############################################################################
def run_a(input_data):
    data = input_data[0] * 2

    result = phase(data, 100)
    print(result)
    return [result[0:8]]


def run_b(input_data):
    data = input_data[0] * 10000
    offset = input_data[0][0:7]
    result = phase(data, 100)
    print(result[offset:offset + 8])
    return [result]


def phase(data, times):
    result = data

    for i in range(times):
        print(result)
        result = apply_phase(result)

    return result


def apply_phase(data):
    result = ""

    for i in range(len(data)):
        pattern = get_pattern_for_position(i)
        check_sum = apply_fft(data, pattern)

        result += str(check_sum)[-1]

    return result


def apply_fft(data, pattern):
    pattern_index = 1
    check_sum = 0

    for element in data:
        check_sum += int(element) * pattern[pattern_index]

        pattern_index += 1
        pattern_index = pattern_index % len(pattern)

    return check_sum


def get_pattern_for_position(position):
    pattern = []

    for element in PATTERN:
        for i in range(position + 1):
            pattern.append(element)

    return pattern
