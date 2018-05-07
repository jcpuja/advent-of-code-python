# Very insightful explanation of Hexagon grids: https://www.redblobgames.com/grids/hexagons/

# We use a coordinate system with 3 axes:
# x-axis runs n-s
# y-axis runs nw-se
# z-axis runs sw-ne
#
# function cube_distance(a, b):
#     return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))

coord_deltas = {
    'n': (0, 1, -1),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
    's': (0, -1, 1),
    'se': (1, -1, 0),
    'ne': (1, 0, -1)
}


def compute_distance(input_string):
    position = 0, 0, 0
    x0, y0, z0 = position
    moves = input_string.split(',')
    for move in moves:
        x, y, z = position
        move_x, move_y, move_z = coord_deltas[move]
        position = [x + move_x, y + move_y, z + move_z]

    x, y, z = position
    return max(abs(x - x0), abs(y - y0), abs(z - z0))


def solve_task01():
    with open('input.txt') as f:
        text = f.readline().rstrip()
        print(compute_distance(text))

# solve_task01()