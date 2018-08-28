import numpy as np
import unittest
from unittest import TestCase

from day21.task02 import enhance, build_rules


class GridUnitTests(TestCase):

    # Acceptance tests

    @unittest.skip('Acceptance test')
    def test_enhance_example_step1(self):
        rules = build_rules(example=True)
        self.assertEqual('1001000000001001', enhance('010001111', rules))

    @unittest.skip('Acceptance test')
    def test_enhance_example_step2(self):
        rules = build_rules(example=True)
        self.assertEqual('110110100100000000110110100100000000', enhance('1001000000001001', rules))

    # Unit tests

    def test_build_rules(self):
        rules2, rules3 = build_rules(example=True)

        self.assertEqual(4, len(rules2))
        example_post = np.array([int(i) for i in list('110100000')]).reshape(3, 3)
        self.assertTrue(np.array_equal(example_post, rules2['0001']))
        self.assertTrue(np.array_equal(example_post, rules2['0100']))
        self.assertTrue(np.array_equal(example_post, rules2['0010']))
        self.assertTrue(np.array_equal(example_post, rules2['0010']))

        self.assertEqual(8, len(rules3))
