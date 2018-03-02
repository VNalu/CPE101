import unittest
from fold import *

class TestCases(unittest.TestCase):
	def test_1(self):
		# Add code here.
		self.assertEqual(sum([1, 2, 3]), 6)
		self.assertEqual(sum([1, 2, 3, 9, -10]), 5)
		self.assertEqual(index_of_smallest([10, 5, 3, 0, 55]), 3)
		self.assertEqual(index_of_smallest([10, -5, 3, 0, 55, -22]), 5)


# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

