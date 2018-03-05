matrix = []

with open('input.txt') as f:
    for line in f:
        matrix.append([int(x) for x in line.split()])

checksum = 0

for row in matrix:
    found = False
    for i in range(len(row)):
        for j in range(len(row)):
            if i != j and row[i] % row[j] == 0:
                found = True
                checksum += row[i] // row[j]
                break

        if found:
            break



print(checksum)