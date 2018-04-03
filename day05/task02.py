with open('input.txt') as f:
    inputs = [int(s) for s in list(f)]

    current_index = 0
    steps = 0

    while 0 <= current_index < len(inputs):
        steps += 1
        this_offset = inputs[current_index]
        inputs[current_index] = this_offset + 1 if this_offset < 3 else this_offset - 1
        current_index += this_offset

    print(steps)
