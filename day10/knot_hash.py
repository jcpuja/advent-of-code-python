from day10.ascii_converter import AsciiConverter
from day10.circular_list import CircularList
from day10.dense_hash_processor import DenseHashProcessor
from day10.hash_formatter import HashFormatter


class KnotHash:
    def __init__(self, message):
        self.message = message

        lengths = AsciiConverter.to_ascii_codes(message)

        position = 0
        skip_size = 0
        nums = CircularList(256)
        for _ in range(64):
            for length in lengths:
                nums.reverse(position, length)
                position = nums.get_actual_position(position + length + skip_size)
                skip_size += 1

        sparse_hash = nums.get_list()
        dense_hash = DenseHashProcessor(sparse_hash).get_hash()
        self.string_hash = HashFormatter.format(dense_hash)

    def get_hash(self):
        return self.string_hash
