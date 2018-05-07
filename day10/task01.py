from day10.knot_hash_v1 import KnotHashV1

input_lengths = [157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30]

knot_hash = KnotHashV1(input_lengths)

print(knot_hash.compute_checksum())
