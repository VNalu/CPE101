import unittest
from logic import *

class TestCases(unittest.TestCase):
	def test_case_1(self):
		self.assertFalse(is_even(3))
		self.assertTrue(is_even(6))
		pass
	def test_case_2(self):
		self.assertTrue(in_an_interval(2))
		self.assertFalse(in_an_interval(9))
		self.assertFalse(in_an_interval(45))
		self.assertFalse(in_an_interval(47))
		self.assertFalse(in_an_interval(12))
		self.assertTrue(in_an_interval(19))
		pass


# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

