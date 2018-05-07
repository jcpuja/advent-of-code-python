from day10.ascii_converter import AsciiConverter
from day10.dense_hash_processor import DenseHashProcessor
from day10.hash_formatter import HashFormatter
from day10.knot_hash_round import KnotHashRound


class KnotHash:
    def __init__(self, message):
        self.message = message

        lengths = AsciiConverter.to_ascii_codes(message)

        current_round = None
        initial_position = 0
        initial_skip_size = 0
        for i in range(64):
            current_round = KnotHashRound(lengths,
                                          initial_position=initial_position,
                                          initial_skip_size=initial_skip_size)
            initial_position = current_round.get_current_position()
            initial_skip_size = current_round.get_skip_size()

        sparse_hash = current_round.get_list()
        dense_hash = DenseHashProcessor(sparse_hash).get_hash()
        self.string_hash = HashFormatter.format(dense_hash)

    def get_hash(self):
        return self.string_hash
