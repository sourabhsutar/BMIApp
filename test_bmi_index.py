from bmi_index import *
import unittest

class TestCuboid(unittest.TestCase):
    def test_calculateBMI(self):
        self.assertAlmostEqual(calculateBMI(96,171),32.83)
        self.assertAlmostEqual(calculateBMI(85,0),0)
        self.assertAlmostEqual(calculateBMI(0,161),0)

    def test_BMICatgHealthRisk(self):
        self.assertAlmostEqual(BMICatgHealthRisk(32.83),['Moderately obese','Medium risk'])