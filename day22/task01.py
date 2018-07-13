def task01(file_name):
    infected = set()
    up, right, down, left = 0, 1, 2, 3

    x, y = 0, 0
    with open(file_name) as f:
        for y, l in enumerate(f):
            for x, c in enumerate(l.strip()):
                if c == '#':
                    infected.add((x, y))

    position = (int(x / 2), int(y / 2))
    heading = up

    infections = 0

    for n in range(10_000):
        # Turn
        current_is_infected = position in infected
        heading = (heading + 1 if current_is_infected else heading - 1) % 4

        # Clean or infect
        if current_is_infected:
            infected.remove(position)
        else:
            infected.add(position)
            infections += 1

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
