# https://www.reddit.com/r/adventofcode/comments/7l78eb/2017_day_21_solutions/drk4o3k

import numpy as np

with open("input.txt") as f:
    LINES = [l.strip() for l in f]

replacements = {}

for l in LINES:
    src, repl = l.split(' => ')

    src = np.array([[c == '#' for c in b] for b in src.split('/')])
    repl = np.array([[c == '#' for c in b] for b in repl.split('/')])

    flip = np.fliplr(src)

    for i in range(4):
        replacements[src.tobytes()] = repl
        replacements[flip.tobytes()] = repl
        src, flip = np.rot90(src), np.rot90(flip)

pat = np.array([
    [False, True, False],
    [False, False, True],
    [True, True, True],
])

size = 3

# or 5 for part 1
for k in range(5):
    if size % 2 == 0:
        newsize = size // 2 * 3
        newpattern = np.empty((newsize, newsize), dtype=bool)
        for i in range(0, size, 2):
            for j in range(0, size, 2):
                newpattern[i // 2 * 3:i // 2 * 3 + 3, j // 2 * 3:j // 2 * 3 + 3] = replacements[
                    pat[i:i + 2, j:j + 2].tobytes()]
    else:
        newsize = size // 3 * 4
        newpattern = np.empty((newsize, newsize), dtype=bool)
        for i in range(0, size, 3):
            for j in range(0, size, 3):
                newpattern[i // 3 * 4:i // 3 * 4 + 4, j // 3 * 4:j // 3 * 4 + 4] = replacements[
                    pat[i:i + 3, j:j + 3].tobytes()]
    pat = newpattern
    size = newsize

print('result:', sum(sum(pat)))
