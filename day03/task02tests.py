import unittest
import numpy as np

from day03.task02 import get_spiral_memory_steps, SpiralMemory, get_max_index_overflow


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

    def testMappedMatrix_initialization(self):
        sample_spiral = SpiralMemory(23)
        expected_matrix = np.array([
            [147, 142, 133, 122, 59],
            [304, 5, 4, 2, 57],
            [330, 10, 1, 1, 54],
            [351, 11, 23, 25, 26],
            [362, 747, 806, 0, 0]
        ])

        self.assertEqual(expected_matrix[4, 2], sample_spiral.mapped_matrix[4, 2])
        self.assertEqual(expected_matrix[1, 4], sample_spiral.mapped_matrix[1, 4])
        # print(sample_spiral.mapped_matrix)

    def testMappedMatrix_maxIndexOverflow(self):
        self.assertEqual(25, get_max_index_overflow(23))
