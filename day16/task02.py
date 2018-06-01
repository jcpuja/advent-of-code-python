# This is a naive/brute-force solution with an added cache, runs in about 5m on a laptop
# A "proper" solution would be to find cycles

def spin(_positions, x):
    return _positions[-x:] + _positions[:-x]


def exchange(_positions, ia, ib):
    new_positions = [c for c in _positions]
    new_positions[ia] = _positions[ib]
    new_positions[ib] = _positions[ia]
    return ''.join(new_positions)


def partner(_positions, a, b):
    ia = _positions.index(a)
    ib = _positions.index(b)
    return exchange(_positions, ia, ib)


def perform_dance(_positions, _moves):
    for move in _moves:
        if move.startswith('s'):
            _positions = spin(_positions, int(str(move[1:])))

        if move.startswith('x'):
            ia, ib = str(move[1:]).split('/')
            _positions = exchange(_positions, int(ia), int(ib))

        if move.startswith('p'):
            a, b = str(move[1:]).split('/')
            _positions = partner(_positions, a, b)

    return _positions


run_example = False
positions = 'abcde' if run_example else 'abcdefghijklmnop'
file_name = 'example_input.txt' if run_example else 'input.txt'
n = 2 if run_example else 1_000_000_000

with open(file_name) as f:
    moves = f.readline().rstrip().split(',')

cache = {}

for _ in range(n):
    if positions in cache:
        new_positions = cache[positions]
    else:
        new_positions = perform_dance(positions, moves)
    cache[positions] = new_positions
    positions = new_positions

print(positions)
