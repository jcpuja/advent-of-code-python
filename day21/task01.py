import numpy as np


# THIS IS NOT FINISHED OR EVEN WORKING PROPERLY


def enhance(flat_in, rules):
    pass


def combinations(in_arr):
    combs = set()
    for k in range(4):
        combs.add(grid_as_string(np.rot90(in_arr, k)))
        combs.add(grid_as_string(np.fliplr(np.rot90(in_arr, k))))
        combs.add(grid_as_string(np.flipud(np.rot90(in_arr, k))))

    return combs


def grid_as_string(arr):
    return ''.join([str(c) for c in arr.flatten()])


def build_rules(example):
    file_name = 'example_input.txt' if example else 'input.txt'
    rules2 = {}
    rules3 = {}
    with open(file_name) as f:
        for l in f:
            src, tgt = l.strip().split(' => ')
            src = src.replace('/', '')
            tgt = tgt.replace('/', '')
            src = np.array([1 if c == '#' else 0 for c in src])
            tgt = np.array([1 if c == '#' else 0 for c in tgt])

            if len(src) == 4:
                for src_combination in combinations(src.reshape(2, 2)):
                    rules2[src_combination] = tgt.reshape(3, 3)
            elif len(src) == 9:
                for src_combination in combinations(src.reshape(3, 3)):
                    rules3[src_combination] = tgt.reshape(4, 4)

            else:
                assert False

    return rules2, rules3
