import unittest

from lib.solutions.checkout import checkout


class TestHello(unittest.TestCase):
    def test_illegal_input(self):
        self.assertEqual(checkout('a'), -1)
        self.assertEqual(checkout('1'), -1)
        self.assertEqual(checkout(' '), -1)

    def test_empty_equals_zero(self):
        self.assertEqual(checkout(''), 0)

    def test_1_A(self):
        self.assertEqual(checkout('A'), 50)

    def test_1_B(self):
        self.assertEqual(checkout('B'), 30)

    def test_1_C(self):
        self.assertEqual(checkout('C'), 20)

    def test_1_D(self):
        self.assertEqual(checkout('D'), 15)

    def test_2_As(self):
        self.assertEqual(checkout('AA'), 100)

    def test_3_As(self):
        self.assertEqual(checkout('AAA'), 130)

    def test_2_Bs(self):
        self.assertEqual(checkout('BB'), 45)

    def test_3_As_and_2_Bs(self):
        self.assertEquals(checkout('AAABB'), 175)

    def test_4_Bs(self):
        self.assertEqual(checkout('BB'), 90)


if __name__ == '__main__':
    unittest.main()