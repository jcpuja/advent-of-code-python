from day10.circular_list import CircularList


class KnotHashV1:
    def __init__(self, lengths, list_size=256, initial_position=0, initial_skip_size=0):
        self.position = initial_position
        self.skip_size = initial_skip_size
        self.list = CircularList(list_size)

        for length in lengths:
            self.list.reverse(self.position, length)
            self.position = self.list.get_actual_position(self.position + length + self.skip_size)
            self.skip_size += 1

    def get_current_position(self):
        return self.position

    def get_list(self):
        return self.list.get_list()

    def get_skip_size(self):
        return self.skip_size

    def compute_checksum(self):
        current_list = self.get_list()
        return current_list[0] * current_list[1]
