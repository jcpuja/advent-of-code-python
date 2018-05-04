class KnotHash:
    def __init__(self, lengths, list_size=256):
        self.current_position = 0
        self.skip_size = 0
        self.lengths = lengths
        self.list = list(range(list_size))


