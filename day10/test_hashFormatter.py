from unittest import TestCase

from day10.hash_formatter import HashFormatter


class TestHashFormatter(TestCase):

    def test_hex_function(self):
        self.assertEqual('01', hex(1)[2:].zfill(2))
        self.assertEqual('ff', hex(255)[2:].zfill(2))

    def testHashFormatter_shouldReturnConcatenatedStringRepresentationsOfHexValuesOfInput(self):
        dummy_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual('000102030405060708090a0b0c0d0e0f', HashFormatter.format(dummy_input))
