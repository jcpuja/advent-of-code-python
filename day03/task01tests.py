import unittest

from day03.task01 import get_spiral_memory_steps, SpiralMemory


class TestSpiralMemory(unittest.TestCase):

    def testSteps(self):
        self.assertEqual(get_spiral_memory_steps(1), 0)
        self.assertEqual(get_spiral_memory_steps(12), 3)
        self.assertEqual(get_spiral_memory_steps(23), 2)
        self.assertEqual(get_spiral_memory_steps(1024), 31)

    def testCalculateEdgeSize(self):
        self.assertEqual(3, SpiralMemory.calculate_edge_size(2))
        self.assertEqual(3, SpiralMemory.calculate_edge_size(9))
        self.assertEqual(5, SpiralMemory.calculate_edge_size(10))

    def testMatrixInitialization_size(self):
        self.assertEqual((3, 3), SpiralMemory(2).get_matrix_shape())
        self.assertEqual((3, 3), SpiralMemory(9).get_matrix_shape())
        self.assertEqual((5, 5), SpiralMemory(10).get_matrix_shape())

    def testMatrixInitialization_contents(self):
        self.assertEqual(5, SpiralMemory(9).matrix[0, 0])
        self.assertEqual(9, SpiralMemory(9).matrix[2, 2])
        self.assertEqual(3, SpiralMemory(9).matrix[0, 2])
        self.assertEqual(7, SpiralMemory(9).matrix[2, 0])
        self.assertEqual(23, SpiralMemory(23).matrix[4, 2])
        self.assertEqual(17, SpiralMemory(23).matrix[0, 0])

    def testGetCoordinates(self):
        self.assertEqual((4, 2), SpiralMemory(23).get_coordinates(23))
        self.assertEqual((0, 0), SpiralMemory(23).get_coordinates(17))
