from day10.circular_list import CircularList


class KnotHashRound:
    def __init__(self, lengths, list_size=256):
        self.current_position = 0
        self.skip_size = 0
        self.list = CircularList(list_size)

        for length in lengths:
            self.list.reverse(self.current_position, length)
            self.current_position = self.list.get_actual_position(self.current_position + length + self.skip_size)
            self.skip_size += 1

    def get_current_position(self):
        return self.current_position

    def get_list(self):
        return self.list.get_list()

    def get_skip_size(self):
        return self.skip_size

    def compute_checksum(self):
        current_list = self.get_list()
        return current_list[0] * current_list[1]
