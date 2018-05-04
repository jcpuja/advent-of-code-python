import unittest

from day10.task01 import KnotHash


class TestKnotHash(unittest.TestCase):

    def testExampleScenario(self):
        sut = KnotHash([3, 4, 1, 5], list_size=5)
        self.assertEqual(4, sut.skip_size)
        self.assertEqual(4, sut.current_position)
        self.assertEqual([3, 4, 2, 1, 0], sut.list)
