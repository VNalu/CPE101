import unittest
from poly import *

class TestPoly(unittest.TestCase):
	#do not delete this part use this to comapre two list
	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)



	# Add tests here
	def testAdd2(self):
		self.assertEqual(poly_add2([2, 6, 9], [1, 1, 1]), [3, 7, 10])
		self.assertEqual(poly_add2([43, 49, 29], [27, 5, 32]), [70, 54, 61])
	def testMult2(self):
		self.assertEqual(poly_mult2([7, 17, 3], [3, 2, 6]), [21, 65, 34, 108, 18])
		self.assertEqual(poly_mult2([1, 2, 3], [40, 8, 1]), [40, 88, 16, 26, 3])

if __name__ == '__main__':
	unittest.main()
