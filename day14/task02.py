from day10.knot_hash import KnotHash

# puzzle_input = 'flqrgnkx'
puzzle_input = 'amgozmfv'
matrix_size = 128

key_rows = [f"{puzzle_input}-{i}" for i in range(matrix_size)]

hash_rows = [KnotHash(key).get_hash() for key in key_rows]

hash_bits = list([
                     int(bit) for bit in
                     ''.join([
                         format(int(char, 16), '04b') for char in row
                     ])
                 ] for row in hash_rows)

found_elements = set()
number_of_connected_components = 0


def search_connected_elements(source):
    targets = []
    source_x, source_y = source

    if source_x > 0:
        targets.append((source_x - 1, source_y))

    if source_x < matrix_size - 1:
        targets.append((source_x + 1, source_y))

    if source_y > 0:
        targets.append((source_x, source_y - 1))

    if source_y < matrix_size - 1:
        targets.append((source_x, source_y + 1))

    for target in targets:
        target_x, target_y = target
        if target not in found_elements and hash_bits[target_y][target_x] == 1:
            found_elements.add(target)
            search_connected_elements(target)


for y, row in enumerate(hash_bits):
    for x, bit in enumerate(row):
        if bit == 1 and (x, y) not in found_elements:
            search_connected_elements((x, y))
            number_of_connected_components += 1

print(number_of_connected_components)
