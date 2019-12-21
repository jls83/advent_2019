from collections import Counter

WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT

def split_into_layers_old(in_list):
    l = len(in_list)
    layer_count = int(l / LAYER_SIZE)

    slice_tuples = (((LAYER_SIZE * i), ((LAYER_SIZE * (i + 1)) - 1))
                    for i in range(0, layer_count + 1))
    slices = (slice(*s) for s in slice_tuples)

    return [in_list[s] for s in slices]

def split_into_layers(in_list):
    res = []
    inner = []
    for i, v in enumerate(in_list):
        inner.append(v)
        if i % LAYER_SIZE == 0 and i != 0:
            res.append(inner)
            inner = []

    if inner:
        res.append(inner)

    return res
 
def get_count_from_layers(layers):
    return [Counter(layer) for layer in layers]

if __name__ == '__main__':
    # Get the input as a list
    with open('d8p1_input.txt', 'r') as f:
        input_list = f.read().strip()
    input_list = [int(c) for c in input_list]
    layers = split_into_layers(input_list)
    layer_counts = get_count_from_layers(layers)
    
    current_zero_min = float('inf')
    current_mult_val = 0
    for layer_count in layer_counts:
        if layer_count[0] < current_zero_min:
            current_zero_min = layer_count[0]
            current_mult_val = layer_count[1] * layer_count[2]

    print(current_mult_val)

