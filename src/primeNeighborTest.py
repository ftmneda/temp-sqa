import unittest
import src.primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test010(self):
        actualResult = pn.primeNeighbor(upperBound=2)
        expectedResult = 2
        self.assertEqual(expectedResult, actualResult)




