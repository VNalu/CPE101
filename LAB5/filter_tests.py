import unittest
from filter import *

class TestCases(unittest.TestCase):
	def test_1(self):
		self.assertEqual(are_positive([-1, 4, 0, -4, 2, 4]), [4, 2, 4])
		self.assertEqual(are_positive([0, -4, -333, 6, 5]), [6, 5])
	def test_2(self):
		self.assertEqual(are_greater_than_n([6, 5, 4, 3, 2], 2), [6, 5, 4, 3])
		self.assertEqual(are_greater_than_n([6, 5, 4], 5), [6])
	def test_3(self):
		self.assertEqual(listDiv([9, 8, 7, 6, 5, 4, 3, 2], 3), [9, 6, 3])
		self.assertEqual(listDiv([4, 3, 2, 9], 2), [4, 2])

# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

