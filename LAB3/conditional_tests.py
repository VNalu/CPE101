import unittest
from conditionals import *

class TestCases(unittest.TestCase):
	def test_case_1(self):
		# testing the max of two numbers
		self.assertEqual(max_101(1, 2), 2)
		self.assertEqual(max_101(10, 5), 10)
		pass
	def test_case_2(self):
		# testing the max of three numbers
		self.assertEqual(max_of_three(1, 2, 3), 3)
		self.assertEqual(max_of_three(5, 9, 2), 9)
		self.assertEqual(max_of_three(10, 9, 8), 10)
		pass
	def test_case_3(self):
		# testing the return on the fee by days late
		self.assertEqual(rental_late_fee(3), 5)
		self.assertEqual(rental_late_fee(10), 7)
		self.assertEqual(rental_late_fee(24), 19)
		pass


# Run the unit tests.
if __name__ == '__main__':
	unittest.main()


