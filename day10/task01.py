class KnotHash:
    def __init__(self, lengths, list_size=256):
        self.current_position = 0
        self.skip_size = 0
        self.lengths = lengths
        self.list = list(range(list_size))

    def get_current_position(self):
        return self.current_position

    def get_list(self):
        return self.list

    def get_skip_size(self):
        return self.skip_size

    def compute_checksum(self):
        current_list = self.get_list()
        return current_list[0] * current_list[1]

