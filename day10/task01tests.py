import unittest

from day10.task01 import KnotHash, CircularList


class TestKnotHash(unittest.TestCase):

    @unittest.skip("Acceptance test, will not pass until implementation is complete")
    def testExampleScenario(self):
        sut = KnotHash([3, 4, 1, 5], list_size=5)
        self.assertEqual(4, sut.get_skip_size())
        self.assertEqual(4, sut.get_current_position())
        self.assertEqual([3, 4, 2, 1, 0], sut.get_list())
        self.assertEqual(12, sut.compute_checksum())


class TestCircularList(unittest.TestCase):

    def testInitialization(self):
        sut = CircularList(list_size=5)
        self.assertEqual([0, 1, 2, 3, 4], sut.get_list())

    def testReverse_whenPositionPlusLengthEqualsListLength_shouldReverseFromPositionToListEnd(self):
        sut = CircularList(5)
        sut.reverse(1, 4)
        self.assertEqual([0, 4, 3, 2, 1], sut.get_list())

    def testReverse_whenPositionPlusLengthLTListLength_shouldReverseNoWrap(self):
        sut = CircularList(5)
        sut.reverse(1, 3)
        self.assertEqual([0, 3, 2, 1, 4], sut.get_list())

    def testReverse_whenPositionPlusLengthGTListLength_shouldReverseWithWrap(self):
        sut = CircularList(5)
        sut.reverse(4, 2)
        self.assertEqual([4, 1, 2, 3, 0], sut.get_list())

    def testReverse_whenLengthEquals1_shouldNotChangeList(self):
        sut = CircularList(5)
        sut.reverse(position=0, length=1)
        self.assertEqual([0, 1, 2, 3, 4], sut.get_list())

    def testReverse_whenPositionGTEListLength_shouldRaise(self):
        sut = CircularList(5)
        self.assertRaises(Exception, sut.reverse, 5, 1)

    def testReverse_whenPositionLT0_shouldRaise(self):
        sut = CircularList(5)
        self.assertRaises(Exception, sut.reverse, -1, 1)

    def testReverse_whenLengthGTListLength_shouldRaise(self):
        sut = CircularList(5)
        self.assertRaises(Exception, sut.reverse, 0, 6)

    def testReverse_whenLengthLT1_shouldRaise(self):
        sut = CircularList(5)
        self.assertRaises(Exception, sut.reverse, 0, 0)
