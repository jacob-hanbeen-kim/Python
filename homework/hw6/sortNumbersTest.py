import unittest
from sortNumbers import *

class TestNotebook(unittest.TestCase):

    def test_sort_numbers_positives(self):
        self.assertEqual(sort_numbers(10,5,2), (2,5,10))
    def test_sort_numbers_decimals(self):
        self.assertEqual(sort_numbers(1.5, 0.2, 4), (0.2, 1.5, 4))
    def test_sort_numbers_negatives(self):
        self.assertEqual(sort_numbers(-1, -4, -10), (-10, -4, -1))


unittest.main(argv=[''], verbosity=2, exit=False)