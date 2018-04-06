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

    # should give the discount multiple times if required
    def test_4_Bs(self):
        self.assertEqual(checkout('BBBB'), 90)

    def test_5_As(self):
        self.assertEqual(checkout('AAAAA'), 200)

    def test_6_As(self):
        self.assertEqual(checkout('AAAAAA'), 250)

    def test_8_As(self):
        self.assertEqual(checkout('AAAAAAAA'), 330)

    def test_9_As(self):
        self.assertEqual(checkout('AAAAAAAAA'), 380)

    def test_loads_of_ABs(self):
        self.assertEqual(checkout('ABCDCBAABCABBAAA'), 495)

    def test_2_Es_B_is_free(self):
        self.assertEqual(checkout('EEB'), 80)

    def test_2_Es_B_is_free(self):
        self.assertEqual(checkout('EEBB'), 95)

    def test_ABCDE(self):
        self.assertEquals(checkout('ABCDE'), 155)

    def test_EEEEBB(self):
        self.assertEquals(checkout('EEEEBB'), 160)

    def test_BEBEEE(self):
        self.assertEquals(checkout('BEBEEE'), 160)


if __name__ == '__main__':
    unittest.main()
