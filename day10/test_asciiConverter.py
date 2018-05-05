from unittest import TestCase

from day10.ascii_converter import AsciiConverter


class TestAsciiConverter(TestCase):

    def test_toAsciiCodes_whenInputIsEmptyString_shouldReturnSuffixOnly(self):
        self.assertEqual([17, 31, 73, 47, 23], AsciiConverter.to_ascii_codes(''))

    def test_toAsciiCodes_whenInputIsLikeExample_shouldReturnExampleResult(self):
        self.assertEqual([49, 44, 50, 44, 51, 17, 31, 73, 47, 23], AsciiConverter.to_ascii_codes('1,2,3'))
