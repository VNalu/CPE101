import unittest
from string_101 import *

class TestString(unittest.TestCase):
	def test_lower(self):
		self.assertEqual(str_rot_13("hello"), "uryyb")
		self.assertEqual(str_rot_13("helloworld"), "uryybjbeyq")
	def test_translate(self):
		self.assertEqual(str_translate_101("asdfasdfasdf", "a", "w"), "wsdfwsdfwsdf")
		self.assertEqual(str_translate_101("banana", "n", "b"), "bababa")


if __name__ == '__main__':
	unittest.main()

