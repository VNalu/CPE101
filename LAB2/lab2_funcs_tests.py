#Name: Veronica Pollock
#Section: CPE-101
import unittest
from funcs import *

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here.
      math_func1(10, 3)
      self.assertTrue(math_func1(10, 3), 368)
      self.assertTrue(math_func1(10, 3), 501)
      pass


   def test_f_2(self):
      # Add code here.
      math_func2(1, 6, 9)
      self.assertTrue(math_func2(1, 6, 9), -3.0)
      self.assertTrue(math_func2(1, 10, 20), -2.0)
      pass

   def test_f_3(self):
      # Add code here.
      math_d(5, 5, 0, 0)
      self.assertTrue(math_d(5, 5, 0, 0), 7.0710678118)
      self.assertEqual(math_d(0, 0, 0, 10), 10)
      pass

   def test_f_4(self):
      # Add code here.
      self.assertFalse(is_negative(2), True)
      self.assertTrue(is_negative(-2), True)
      pass   

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
