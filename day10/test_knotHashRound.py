import unittest

from day10.knot_hash_v1 import KnotHashV1


class TestKnotHashRound(unittest.TestCase):

    def testExampleScenario(self):
        sut = KnotHashV1([3, 4, 1, 5], list_size=5)
        self.assertEqual(4, sut.get_skip_size())
        self.assertEqual(4, sut.get_current_position())
        self.assertEqual([3, 4, 2, 1, 0], sut.get_list())
        self.assertEqual(12, sut.compute_checksum())

    def testTask01Scenario(self):
        sut = KnotHashV1([157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30])
        self.assertEqual(62238, sut.compute_checksum())
