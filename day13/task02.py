class FirewallLayout:

    def __init__(self, filename):
        self.layer_sizes = {}
        self.layer_sizes_flat = {}
        self.last_layer = 0

        with open(filename) as f:
            for line in [line.rstrip() for line in f]:
                layer_index, layer_size = tuple([int(part) for part in line.split(': ')])
                # Instead of simulating the back and forth travel direction of scanners, we extend the size of the layer
                #  by the return travel distance and reset a scanner position to zero when they reach the end.
                # [0][1][...][n-1][n] both ways = [0][1][...][n-1][n][n-1][...][1] one-way
                self.layer_sizes_flat[layer_index] = layer_size + max(0, layer_size - 2)
                # Still need to keep a reference to the original size to compute the severity
                self.layer_sizes[layer_index] = layer_size
                self.last_layer = max(layer_index, self.last_layer)

    def compute_severity(self, _delay):
        # init
        severity = 0
        scanner_positions = {}
        for layer_index in self.layer_sizes.keys():
            scanner_positions[layer_index] = 0

        for tick in range(self.last_layer + 1 + _delay):
            # wait for delay
            if tick >= _delay:

                # collision detection
                packet_position = tick - _delay
                if packet_position in scanner_positions and scanner_positions[packet_position] == 0:
                    severity += packet_position * self.layer_sizes[packet_position]

            # scanner move
            for layer_index, layer_size in self.layer_sizes_flat.items():
                scanner_positions[layer_index] = (scanner_positions[layer_index] + 1) % layer_size

        return severity


layout = FirewallLayout('example_input.txt')
delay = 0
while layout.compute_severity(delay) > 0:
    delay += 1

print(delay)
