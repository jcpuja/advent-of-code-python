class HashFormatter:
    @staticmethod
    def format(dense_hash):
        strings = [hex(x)[2:].zfill(2) for x in dense_hash]
        return ''.join(strings)
