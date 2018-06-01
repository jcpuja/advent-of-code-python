from unittest import TestCase

from day15.task01 import aoc_generator, low_16bit_match


class TestAocGenerator(TestCase):

    def test_shouldReturnExampleValues(self):
        self.assertEqual([1092455, 1181022009, 245556042, 1744312007, 1352636452], list(aoc_generator(65, 16807, 5)))
        self.assertEqual([430625591, 1233683848, 1431495498, 137874439, 285222916], list(aoc_generator(8921, 48271, 5)))

    def test_low_16bit_match_shouldWorkWithExampleValues(self):
        self.assertFalse(low_16bit_match(1092455, 430625591))
        self.assertFalse(low_16bit_match(1181022009, 1233683848))
        self.assertTrue(low_16bit_match(245556042, 1431495498))
        self.assertFalse(low_16bit_match(1744312007, 137874439))
        self.assertFalse(low_16bit_match(1352636452, 285222916))
