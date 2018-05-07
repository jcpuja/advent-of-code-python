import unittest
from unittest import TestCase

from day10.knot_hash import KnotHash


class TestKnotHash(TestCase):

    @unittest.skip('Implementation not done yet')
    def testKnotHash_ExampleScenario(self):
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', KnotHash('').get_hash())
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', KnotHash('AoC 2017').get_hash())
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', KnotHash('1,2,3').get_hash())
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', KnotHash('1,2,4').get_hash())
