from functools import reduce

from day10.knot_hash import KnotHash

puzzle_input = 'amgozmfv'

key_rows = [f"{puzzle_input}-{i}" for i in range(128)]

hash_rows = [KnotHash(key).get_hash() for key in key_rows]

hash_bits = list([
                     int(bit) for bit in
                     ''.join([
                         format(int(char, 16), '04b') for char in row
                     ])
                 ] for row in hash_rows)

bit_sum = reduce((lambda x, y: x + y), [sum(row) for row in hash_bits])

print(bit_sum)
