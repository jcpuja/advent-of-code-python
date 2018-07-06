from numpy import matrix, rot90, flip, ndarray, concatenate


def flatten(m: ndarray):
    rows = [''.join(list(row.flat)) for row in m]
    return '/'.join(rows)


class Grid:

    def __init__(self, mat):
        self.m = mat
        self.matching_patterns = set()
        for i in range(4):
            # Axis 0 = horizontal axis
            # Axis 1 = vertical axis
            # rot90 with default paramters = CCW rotation
            self.matching_patterns.add(flatten(rot90(mat, i)))
            self.matching_patterns.add(flatten(flip(rot90(mat, i), 0)))
            self.matching_patterns.add(flatten(flip(rot90(mat, i), 1)))

    def __str__(self):
        return str(self.m)

    __repr__ = __str__

    @staticmethod
    def initial():
        return Grid.from_pattern('.#./..#/###')

    @staticmethod
    def from_pattern(pattern):
        arr2d = [list(row) for row in (pattern.split('/'))]
        return Grid(matrix(arr2d))

    def split(self):
        size = len(self.m)
        out = []
        step = 2 if size % 2 == 0 else 3

        for i in range(0, size, step):
            out.append([])
            for j in range(0, size, step):
                out[-1].append(Grid(self.m[i:i + step, j:j + step].copy()))

        return out

    def to_pattern(self):
        return flatten(self.m)

    def concat(self, other_grid, axis):
        return Grid(concatenate((self.m.copy(), other_grid.m.copy()), axis))

    def count_active(self):
        cnt = 0
        for c in self.m.flat:
            if c == '#':
                cnt += 1

        return cnt

    def debug(self):
        print(self.m)
