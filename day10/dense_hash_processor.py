from functools import reduce


class DenseHashProcessor:

    @staticmethod
    def process_block(block_of_numbers):
        input_size = len(block_of_numbers)
        if input_size != 16:
            raise Exception('Cannot process a block that is not of size 16. Actual size: ' + str(input_size))

        return reduce(lambda x, y: x ^ y, block_of_numbers)

    def __init__(self, sparse_hash):
        input_size = len(sparse_hash)
        if input_size != 256:
            raise Exception('Cannot process a sparse hash that is not of size 256. Actual size: ' + str(input_size))

        self.hash = []
        start_index = 0
        end_index = 16
        while end_index <= 256:
            self.hash.append(DenseHashProcessor.process_block(sparse_hash[start_index:end_index]))
            start_index += 16
            end_index += 16

    def get_hash(self):
        return self.hash
