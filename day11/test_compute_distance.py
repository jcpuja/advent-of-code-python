from unittest import TestCase

from day11.task01 import compute_distance


class TestComputeDistance(TestCase):

    def test_example_scenarios(self):
        self.assertEqual(3, compute_distance('ne,ne,ne'))
        self.assertEqual(0, compute_distance('ne,ne,sw,sw'))
        self.assertEqual(2, compute_distance('ne,ne,s,s'))
        self.assertEqual(3, compute_distance('se,sw,se,sw,sw'))

