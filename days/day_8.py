###############################################################################
def run_a(input_data):
    width = 25
    height = 6
    picture_layers = build_layers(width, height, input_data[0])

    result = corruption_check(picture_layers)
    return [result]


def run_b(input_data):
    width = 25
    height = 6
    picture_layers = build_layers(width, height, input_data[0])

    composed = compose_picture(picture_layers)
    [print(row.replace("0", " ")) for row in composed]
    return composed


def compose_picture(picture_layers):
    composed_layer = []
    for row in range(len(picture_layers[0])):
        composed_row = ""
        for pixel in range(len(picture_layers[0][0])):
            composed_pixel = "2"
            for layer in picture_layers:
                layer_pixel = layer[row][pixel]
                if not layer_pixel == composed_pixel:
                    composed_pixel = layer_pixel
                    break

            composed_row += composed_pixel

        composed_layer.append(composed_row)

    return composed_layer


def build_layers(width, height, data):
    rows = [data[i:i+width] for i in range(0, len(data), width)]
    layers = [rows[i:i+height] for i in range(0, len(rows), height)]

    return layers


def corruption_check(picture_layers):
    min_zeroes = 999999999999999
    zero_layer = None

    for layer in picture_layers:
        zero_count = 0
        for row in layer:
            zero_count += row.count("0")

        if zero_count < min_zeroes:
            min_zeroes = zero_count
            zero_layer = layer

    return decode(zero_layer)


def decode(layer):
    ones = 0
    twos = 0
    for row in layer:
        ones += row.count("1")
        twos += row.count("2")

    return ones * twos
