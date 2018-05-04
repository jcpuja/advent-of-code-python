import unittest

from day10.task01 import KnotHash


class TestKnotHash(unittest.TestCase):

    @unittest.skip("Acceptance test, will not pass until implementation is complete")
    def testExampleScenario(self):
        sut = KnotHash([3, 4, 1, 5], list_size=5)
        self.assertEqual(4, sut.get_skip_size())
        self.assertEqual(4, sut.get_current_position())
        self.assertEqual([3, 4, 2, 1, 0], sut.get_list())
        self.assertEqual(12, sut.compute_checksum())


