###############################################################################
def run_a(input_data):
    start, end = get_ranges(input_data[0])

    return [len(get_valid_keys(int(start), int(end)))]


def run_b(input_data):
    start, end = get_ranges(input_data[0])

    keys = get_valid_keys(int(start), int(end))
    return [len(filter_adjacent(keys))]
###############################################################################


def get_ranges(data):
    return data.split("-")


def get_valid_keys(start, end):
    keys = []
    for i in range(start, end):
        if is_valid_key(i):
            keys.append(str(i))

    return keys


def filter_adjacent(keys):
    valid_keys = []
    for key in keys:
        adjacent_count = 0
        prev_digit = ""
        has_two_adjacent = False
        for digit in key:
            if digit == prev_digit:
                adjacent_count += 1
            else:
                if adjacent_count == 2:
                    has_two_adjacent = True
                prev_digit = digit
                adjacent_count = 1
        if adjacent_count == 2:
            has_two_adjacent = True

        if has_two_adjacent:
            valid_keys.append(key)

    return valid_keys


def is_valid_key(key):
    adjacent_digits = False
    str_key = str(key)
    for i in range(0, len(str_key) - 1):
        current_digit = str_key[i]
        next_digit = str_key[i+1]

        if current_digit > next_digit:
            return False

        if current_digit == next_digit:
            adjacent_digits = True

    return adjacent_digits
