PIPE = '|'
DASH = '-'
PLUS = '+'
EMPTY = ' '
N = 'north'
S = 'south'
E = 'east'
W = 'west'
dirs = [N, S, E, W]
letters = []

travel_deltas = {
    N: (0, -1),
    S: (0, 1),
    E: (1, 0),
    W: (-1, 0),
}

grid = []
start_x = None

# input_file = 'example_input.txt'
input_file = 'input.txt'
with open(input_file) as f:
    for yi, line in enumerate(f):
        grid.append([])
        for xi, char in enumerate(line.rstrip()):
            grid[yi].append(char)
            if not start_x and char == PIPE:
                start_x = xi

cursor = start_x, 0
travel_direction = S


def safe_get(x, y):
    try:
        c = grid[y][x]
    except IndexError:
        c = EMPTY
    return c


def travel(direction, c):
    x, y = c
    dx, dy = travel_deltas[direction]
    return x + dx, y + dy


def process(direction, cur):
    x, y = cur
    ch = safe_get(x, y)

    new_direction = direction

    if ch == PIPE or ch == DASH:
        pass
    elif ch == EMPTY:
        return True, None
    elif ch == PLUS:
        # Direction change, detect new direction
        to_check = [N, S] if direction in (E, W) else [E, W]
        for d in to_check:
            test_x, test_y = travel(d, cur)
            if safe_get(test_x, test_y) != EMPTY:
                new_direction = d

    else:
        letters.append(ch)

    return False, new_direction


# print(cursor)

while True:
    cursor = travel(travel_direction, cursor)
    # print(cursor)
    done, travel_direction = process(travel_direction, cursor)
    if done:
        break

print(''.join(letters))
