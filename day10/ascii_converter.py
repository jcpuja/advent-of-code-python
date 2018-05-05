class AsciiConverter:

    @staticmethod
    def to_ascii_codes(input_string):
        standard_suffix = [17, 31, 73, 47, 23]

        char_codes = [ord(c) for c in input_string]

        return char_codes + standard_suffix
