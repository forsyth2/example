import calculator as c
import unittest

class CalculatorTest(unittest.TestCase):
    def test_sum1(self):
        n = 10
        value1 = 0
        for i in range(1, n + 1):
            value1 = c.add(value1, i)
        self.assertEqual(value1, 55)
        value2 = c.divide(c.multiply(n, c.add(n, 1)), 2)
        self.assertEquals(value2, 55)

if __name__ == "__main__":
    unittest.main()
