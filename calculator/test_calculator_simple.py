import calculator as c
import unittest

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(c.add(4,5), 9)

    def test_subtract(self):
        self.assertEquals(c.subtract(5,2), 3)

    def test_multiply(self):
        self.assertEquals(c.multiply(2,3), 6)

    def test_divide(self):
        self.assertEquals(c.divide(4, 2), 2)

    def test_divide_exception(self):
        self.assertRaises(Exception, c.divide, 3, 0)

if __name__ == "__main__":
    unittest.main()
