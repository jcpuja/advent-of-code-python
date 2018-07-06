from day21.grid import Grid

rules = {}

filename = 'example_input.txt'
with open(filename) as f:
    for line in [l.rstrip() for l in f]:
        src, tgt = line.split(' => ')
        rules[src] = tgt

g = Grid.initial()

for i in range(2):
    sub_grids = g.split()  # 2-d array of grids
    new_grids = [[None] * len(sub_grids)] * len(sub_grids)  # Empty 2-d array of the same size
    for y, row in enumerate(sub_grids):
        for x, sg in enumerate(row):
            for pattern in sg.matching_patterns:
                if pattern in rules:
                    new_grids[y][x] = Grid.from_pattern(rules[pattern])
                    break

    merged_grid = None
    for y, row in enumerate(new_grids):
        merged_row = None
        for x, grid_part in enumerate(row):
            if not merged_row:
                merged_row = grid_part
            else:
                merged_row = merged_row.concat(grid_part, 0)

        if not merged_grid:
            merged_grid = merged_row
        else:
            merged_grid = merged_grid.concat(merged_row, 1)

    g = merged_grid

# print(m)
print(g.m)
# print(rot90(m, 0))


# Axis 0 = horizontal axis
# Axis 1 = vertical axis
# rot90 with default paramters = CCW rotation
