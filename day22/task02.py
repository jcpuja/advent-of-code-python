def task01(file_name):
    states = {}
    up, right, down, left = 0, 1, 2, 3
    clean, weakened, infected, flagged = '.', 'W', '#', 'F'

    x, y = 0, 0
    with open(file_name) as f:
        for y, l in enumerate(f):
            for x, c in enumerate(l.strip()):
                if c == '#':
                    states[(x, y)] = infected

    position = (int(x / 2), int(y / 2))
    heading = up

    infections = 0

    for n in range(10_000_000):
        # Turn and change state
        current_state = states[position] if position in states else clean

        if current_state == clean:
            heading = heading - 1
            states[position] = weakened

        elif current_state == weakened:
            states[position] = infected
            infections += 1

        elif current_state == infected:
            heading = heading + 1
            states[position] = flagged

        elif current_state == flagged:
            heading = heading + 2
            states[position] = clean

        heading = heading % 4

        # Move
        if heading == up:
            position = position[0], position[1] - 1

        elif heading == right:
            position = position[0] + 1, position[1]

        elif heading == down:
            position = position[0], position[1] + 1

        elif heading == left:
            position = position[0] - 1, position[1]

    print(infections)


# task01('example_input.txt')
task01('input.txt')
