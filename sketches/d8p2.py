WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT

BLACK = 0
WHITE = 1
TRANSPARENT = 2

def split_into_layers(in_list):
    l = len(in_list)
    layer_count = int(l / LAYER_SIZE)

    slice_tuples = (((LAYER_SIZE * i), (LAYER_SIZE * (i + 1)))
                    for i in range(0, layer_count))
    slices = (slice(*s) for s in slice_tuples)

    layers = [in_list[s] for s in slices]

    res = []
    for layer in layers:
        rows = [layer[(i * WIDTH):((i + 1) * WIDTH)]
                for i in range(HEIGHT)]
        res.append(rows)

    return res

def split_into_layers_new(in_list):
    print(len(in_list))
    layers = []
    working_layer = []
    for i, v in enumerate(in_list):
        working_layer.append(v)
        if i % LAYER_SIZE == 0 and i != 0:
            layers.append(working_layer)
            working_layer = []

    if working_layer:
        print('HERE', len(working_layer))
        layers.append(working_layer)

    res = []
    for layer in layers:
        rows = [layer[(i * WIDTH):((i + 1) * WIDTH)]
                for i in range(HEIGHT)]
        res.append(rows)

    return res

def get_rendered_value(layer_values):
    for value in layer_values:
        if value == TRANSPARENT:
            continue
        return value

def get_values_at_coord_old(layers, r, c):
    res = []
    for layer in layers:
        res.append(layer[r][c])
    return res

def get_values_at_coord(layers, r, c):
    return (layer[r][c] for layer in layers)

def print_rendered_layers(layer):
    val_map = {
        BLACK: ' ',
        WHITE: '#',
    }
    for row in layer:
        print(''.join(val_map[i] for i in row))
 
if __name__ == '__main__':
    # Get the input as a list
    with open('d8p1_input.txt', 'r') as f:
        input_list = f.read().strip()
    input_list = [int(c) for c in input_list]
    layers = split_into_layers(input_list)

    rendered_layers = [[None for i in range(WIDTH)] for j in range(HEIGHT)]

    for r in range(HEIGHT):
        for c in range(WIDTH):
            layer_values = get_values_at_coord(layers, r, c)
            rendered_layers[r][c] = get_rendered_value(layer_values)

    print_rendered_layers(rendered_layers)
