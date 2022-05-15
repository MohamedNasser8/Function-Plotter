import unittest
import unittest
import test as valid

class testUnit(unittest.TestCase):

#-------------------------------------------------------------------------------------------------------------------------------------
    def testValidateExpresion(self):
        self.assertRaises(ValueError, valid.testmathexp, "")
        self.assertRaises(ValueError, valid.testmathexp, "x/")
        self.assertRaises(ValueError, valid.testmathexp, "a")
        self.assertRaises(ValueError, valid.testmathexp, "+")
        self.assertRaises(ValueError, valid.testmathexp, "-1+2/x^")
        self.assertEqual("1+2*x-3*x**2+4/x**3", valid.testmathexp("1+2*x-3*x^2+4/x^3"))
#-------------------------------------------------------------------------------------------------------------------------------------
    def testValidateInteger(self):
        self.assertRaises(ValueError, valid.testnumber, "")
        self.assertRaises(ValueError, valid.testnumber, "xassa")
        self.assertRaises(ValueError, valid.testnumber, "123x")
#-------------------------------------------------------------------------------------------------------------------------------------
    def testValidateMaxMinValues(self):
        self.assertRaises(ValueError, valid.testlimits,-10, -20)
        self.assertRaises(ValueError, valid.testlimits, 10, 0)
#-------------------------------------------------------------------------------------------------------------------------------------
    def testdivisionbyzero(self):
        self.assertAlmostEqual(False, valid.testDivisionByZero("1/x", -5, 10), "Should return False")

if __name__ == "__main__":
    testObject = testUnit()