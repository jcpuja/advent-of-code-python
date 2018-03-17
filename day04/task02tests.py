import unittest

from day04.task02 import passphrase_is_valid, count_valid_in_input


class TestPassphrase2(unittest.TestCase):
    def test_cases(self):
        # abcde fghij is a valid passphrase.
        self.assertTrue(passphrase_is_valid('abcde fghij'))
        # abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
        self.assertFalse(passphrase_is_valid('abcde xyz ecdab'))
        # a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
        self.assertTrue(passphrase_is_valid('a ab abc abd abf abj'))
        # iiii oiii ooii oooi oooo is valid.
        self.assertTrue(passphrase_is_valid('iiii oiii ooii oooi oooo'))
        # oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
        self.assertFalse(passphrase_is_valid('oiii ioii iioi iiio'))
