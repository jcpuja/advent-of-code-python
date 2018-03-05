matrix = []

with open('input.txt') as f:
    for line in f:
        matrix.append([int(x) for x in line.split()])

checksum = 0

for row in matrix:
    checksum += max(row) - min(row)

print(checksum)