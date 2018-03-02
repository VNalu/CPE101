# Project 1 
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

import unittest
from funcs import *

class TestCases(unittest.TestCase):
    
    # This is testing the object's velocity
    def testObjectVel(self):
        self.assertAlmostEqual(getVelocityObject(500), 49.49747468305833)
        self.assertAlmostEqual(getVelocityObject(50), 15.652475842498529)
        pass
    
    # This is testing the skater's velocity
    def testGetVelSkater(self):
        self.assertAlmostEqual(getVelocitySkater(9, 5.3, 1300), 0.0366923076923076)
        self.assertAlmostEqual(getVelocitySkater(10, 0.1, 1300), 0.0007692307692307692)
        pass

    # This is testing the pounds to kilograms
    def testLbToKg(self):
        self.assertAlmostEqual(poundsToKG(10), 4.53592)
        self.assertAlmostEqual(poundsToKG(3), 1.360776)
        pass

    # This is testing the object's mass with the item chosen
    def testObjMass(self):
        self.assertAlmostEqual(getMassObject("t"), 0.1)
        self.assertAlmostEqual(getMassObject("g"), 5.3)
        pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main() 

