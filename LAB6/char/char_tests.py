import unittest
from char import *

class TestChar(unittest.TestCase):
	def test_lower(self):
		self.assertEqual(is_lower_101("s"), True)
		self.assertEqual(is_lower_101("Y"), False)
	def test_char_rot(self):
		self.assertEqual(char_rot_13("s"), "f")
		self.assertEqual(char_rot_13("Y"), "L")


if __name__ == '__main__':
	unittest.main()

