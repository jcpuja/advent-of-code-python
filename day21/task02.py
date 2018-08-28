# https://www.reddit.com/r/adventofcode/comments/7l78eb/2017_day_21_solutions/drk8j2m

from collections import Counter

import numpy as np


def day21():
    def expand(pre, post):
        rules = []

        for k in [0, 1, 2, 3]:
            rot = np.rot90(pre, k=k)
            rules.append((rot.flatten(), post))
            rules.append((np.fliplr(rot).flatten(), post))
            rules.append((np.flipud(rot).flatten(), post))

        return rules

    def match(incell, rules):
        for pre, post in rules:
            if np.allclose(incell.flatten(), pre):
                return post
        assert False

    def iterate(grid):
        size = len(grid)
        if size % 2 == 0:
            steps = size // 2
            new_grid = np.zeros((3 * steps, 3 * steps))
            for row in range(steps):
                for col in range(steps):
                    incell = grid[2 * row:2 * row + 2, 2 * col:2 * col + 2].copy()
                    outcell = match(incell, rules2)
                    new_grid[3 * row:3 * row + 3, 3 * col:3 * col + 3] = outcell.copy()
        elif size % 3 == 0:
            steps = size // 3
            new_grid = np.zeros((4 * steps, 4 * steps))
            for row in range(steps):
                for col in range(steps):
                    incell = grid[3 * row:3 * row + 3, 3 * col:3 * col + 3].copy()
                    outcell = match(incell, rules3)
                    new_grid[4 * row:4 * row + 4, 4 * col:4 * col + 4] = outcell.copy()
        else:
            assert False
        return new_grid

    def calc_block_map_3_iters(block_string):
        block = np.array([int(c) for c in block_string]).reshape((3, 3))

        grid = iterate(block)
        grid = iterate(grid)
        grid = iterate(grid)

        counts = Counter()
        for row in range(3):
            for col in range(3):
                to_block = grid[3 * row:3 * row + 3, 3 * col:3 * col + 3]
                to_block = ''.join(str(int(x)) for x in to_block.flatten())
                counts[to_block] += 1

        return counts

    def fast_count(init_block, steps):
        if steps % 3 != 0:
            assert False
        steps //= 3

        block_counts = Counter()
        block_counts[init_block] += 1
        maps = {}

        for step in range(steps):
            new_block_counts = Counter()

            for block, count in block_counts.items():
                if block not in maps:
                    maps[block] = calc_block_map_3_iters(block)
                for to_block, to_count in maps[block].items():
                    new_block_counts[to_block] += count * to_count

            block_counts = new_block_counts

        total_ones = 0
        for block, count in block_counts.items():
            total_ones += block.count("1") * count

        return total_ones

    rules2 = []
    rules3 = []
    with open("input.txt") as f:
        for line in f.readlines():
            pre, post = line.strip().split(" => ")
            pre = pre.replace("/", "")
            post = post.replace("/", "")
            pre = np.array([1 if c == "#" else 0 for c in pre])
            post = np.array([1 if c == "#" else 0 for c in post])

            if len(pre) == 4:
                rules2 += expand(pre.reshape((2, 2)), post.reshape((3, 3)))
            elif len(pre) == 9:
                rules3 += expand(pre.reshape((3, 3)), post.reshape((4, 4)))
            else:
                assert False

    init_block = "010001111"
    print(fast_count(init_block, 18))


day21()
