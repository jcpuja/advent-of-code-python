class CircularList:
    def __init__(self, list_size):
        self.list = list(range(list_size))

    def get_list(self):
        return self.list

    def reverse(self, position, length):

        list_length = len(self.list)

        if not 0 <= position < list_length:
            raise Exception('Start position for reverse is out of bounds: list_length='
                            + str(list_length) + ', position=' + str(position))

        if not 0 <= length <= list_length:
            raise Exception('Slice length for reverse is out of bounds: list_length='
                            + str(list_length) + ', length=' + str(length))

        if length <= 1:
            # short-circuit return
            return

        to_reverse = []
        for x in range(length):
            n = (position + x) % list_length
            to_reverse.append(self.list[n])
        to_reverse.reverse()
        for x in range(length):
            n = (position + x) % list_length
            self.list[n] = to_reverse[x]

    def get_actual_position(self, position):
        if position < 0:
            raise Exception('The given position to compute must be positive: position=' + str(position))

        return position % len(self.list)
