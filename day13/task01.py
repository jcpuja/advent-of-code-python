layer_sizes = {}
layer_sizes_flat = {}
scanner_positions = {}
last_layer = 0
severity = 0

# with open('example_input.txt') as f:
with open('input.txt') as f:
    for line in [line.rstrip() for line in f]:
        layer_index, layer_size = tuple([int(part) for part in line.split(': ')])
        # Instead of simulating the back and forth travel direction of scanners, we extend the size of the layer by the
        # return travel distance and reset a scanner position to zero when they reach the end.
        # [0][1][...][n-1][n] both ways = [0][1][...][n-1][n][n-1][...][1] one-way
        layer_sizes_flat[layer_index] = layer_size + max(0, layer_size - 2)
        # Still need to keep a reference to the original size to compute the severity
        layer_sizes[layer_index] = layer_size
        last_layer = max(layer_index, last_layer)
        scanner_positions[layer_index] = 0

for tick in range(last_layer + 1):
    # collision detection
    # tick is always equal to the index layer of the packet position
    if tick in scanner_positions and scanner_positions[tick] == 0:
        severity += tick * layer_sizes[tick]

    # scanner move
    for layer_index, layer_size in layer_sizes_flat.items():
        scanner_positions[layer_index] = (scanner_positions[layer_index] + 1) % layer_size

print(severity)
