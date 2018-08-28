# GrowingList and Tape implementations courtesy of https://stackoverflow.com/a/43110523


class GrowingList(list):
    def __init__(self, default_value):
        super().__init__()
        self.default_value = default_value

    def __getitem__(self, i):
        return list.__getitem__(self, i) if i < len(self) else self.default_value

    def __setitem__(self, i, v):
        if i >= len(self):
            self.extend([self.default_value] * (i + 1 - len(self)))
        list.__setitem__(self, i, v)


class Tape:
    def __init__(self):
        self.pos_range = GrowingList(0)
        self.neg_range = GrowingList(0)

    def __getitem__(self, i):
        if i >= 0:
            return self.pos_range[i]
        else:
            return self.neg_range[-i - 1]

    def __setitem__(self, i, v):
        if i >= 0:
            self.pos_range[i] = v
        else:
            self.neg_range[-i - 1] = v

    def __repr__(self):
        start = -len(self.neg_range)
        end = len(self.pos_range)
        data = list(reversed(self.neg_range)) + self.pos_range
        return "Tape(range=[{}, {}), data={})".format(start, end, data)

    def checksum(self):
        return sum(self.pos_range) + sum(self.neg_range)


def task01():
    # rule := initial state, steps before checksum, state actions
    # state actions := for each state, a 2-element array, where:
    #   - index 0: state action if the value is 0
    #   - index 1: state action if the value is 1
    # state action := value to write, direction of cursor move (-1 = left, 1 = right), next state
    example_rules = ('A', 6, {
        'A': [(1, 1, 'B'), (0, -1, 'B')],
        'B': [(1, -1, 'A'), (1, 1, 'A')]
    })

    prod_rules = ('A', 12399302, {
        'A': [(1, 1, 'B'), (0, 1, 'C')],
        'B': [(0, -1, 'A'), (0, 1, 'D')],
        'C': [(1, 1, 'D'), (1, 1, 'A')],
        'D': [(1, -1, 'E'), (0, -1, 'D')],
        'E': [(1, 1, 'F'), (1, -1, 'B')],
        'F': [(1, 1, 'A'), (1, 1, 'E')],
    })

    rules = prod_rules

    state, steps_before_checksum, state_actions = rules

    cursor = 0
    tape = Tape()

    for step in range(steps_before_checksum):
        to_write, move, next_state = state_actions[state][tape[cursor]]

        tape[cursor] = to_write
        cursor += move
        state = next_state

    return tape.checksum()


print(task01())
