from unittest import TestCase

from day16.task01 import spin, exchange, partner


class TestDanceMoves(TestCase):

    def test_spin(self):
        self.assertEqual('cdeab', spin('abcde', 3))
        self.assertEqual('eabcd', spin('abcde', 1))

    def test_exchange(self):
        self.assertEqual('aecdb', exchange('abcde', 1, 4))
        self.assertEqual('eabdc', exchange('eabcd', 3, 4))

    def test_partner(self):
        self.assertEqual('baedc', partner('eabdc', 'e', 'b'))
