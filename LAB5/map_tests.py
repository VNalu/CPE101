import unittest
from map import *

class TestCases(unittest.TestCase):
	def test_1(self):
		self.assertEqual(square_all([2, 6, 9]), [4, 36, 81])
		self.assertEqual(square_all([1, 8, 4, 3]), [1, 64, 16, 9])
	def test_2(self):
		self.assertEqual(add_n_all([3, 4, 5], 100), [103, 104, 105])
		self.assertEqual(add_n_all([5, 1, 100], 10), [15, 11, 110])
	def test_3(self):
		self.assertEqual(even_or_odd_all([1, 2, 3, 4]), [False, True, False, True])
		self.assertEqual(even_or_odd_all([6, 5, 4, 3]), [True, False, True, False])


# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

