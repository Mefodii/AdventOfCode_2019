ADD = 1
MULTIPLY = 2
END = 99


def build_command(command_line):
    commands = [int(command_line[0]), None, None, None]
    if len(command_line) >= 2:
        commands[1] = int(command_line[1])
    if len(command_line) >= 3:
        commands[2] = int(command_line[2])
    if len(command_line) == 4:
        commands[3] = int(command_line[3])

    return commands


def calculate(data):
    for i in range(0, len(data), 4):
        operation, in_1, in_2, out = build_command(data[i:i+4])

        if operation == ADD:
            result = int(data[in_1]) + int(data[in_2])
            data[out] = str(result)
        elif operation == MULTIPLY:
            result = int(data[in_1]) * int(data[in_2])
            data[out] = str(result)
        elif operation == END:
            return data[0]


###############################################################################
def run_a(input_data):
    split_data = input_data[0].split(",")
    noun = "12"
    verb = "2"
    split_data[1] = noun
    split_data[2] = verb

    return [calculate(split_data)]


def run_b(input_data):
    desired_output = 19690720
    noun, verb = 0, 0
    for noun in range(100):
        for verb in range(100):
            split_data = input_data[0].split(",")
            split_data[1] = str(noun)
            split_data[2] = str(verb)

            result = calculate(split_data)
            if int(result) == desired_output:
                return [100 * noun + verb]
