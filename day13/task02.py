
layers = []

# with open('example_input.txt') as f:
with open('input.txt') as f:
    for line in [line.rstrip() for line in f]:
        layers.append(tuple([int(part) for part in line.split(': ')]))

    caught = True
    delay = 0
    while caught:
        caught = False
        for layer_index, layer_size in layers:
            if (layer_index + delay) % (2 * layer_size - 2) == 0:
                caught = True
                delay += 1
                break
        if not caught:
            print(delay)
            break
