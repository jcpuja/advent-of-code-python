def spin(positions, x):
    return positions[-x:] + positions[:-x]


def exchange(positions, ia, ib):
    new_positions = [c for c in positions]
    new_positions[ia] = positions[ib]
    new_positions[ib] = positions[ia]
    return ''.join(new_positions)


def partner(positions, a, b):
    ia = positions.index(a)
    ib = positions.index(b)
    return exchange(positions, ia, ib)


def perform_dance(is_example):
    positions = 'abcde' if is_example else 'abcdefghijklmnop'
    file_name = 'example_input.txt' if is_example else 'input.txt'

    with open(file_name) as f:
        moves = f.readline().rstrip().split(',')

    for move in moves:
        if move.startswith('s'):
            positions = spin(positions, int(str(move[1:])))

        if move.startswith('x'):
            ia, ib = str(move[1:]).split('/')
            positions = exchange(positions, int(ia), int(ib))

        if move.startswith('p'):
            a, b = str(move[1:]).split('/')
            positions = partner(positions, a, b)

    print(positions)


perform_dance(False)
