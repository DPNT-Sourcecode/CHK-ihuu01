import unittest

from lib.solutions.hello import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('John'), 'Hello, John!')


if __name__ == '__main__':
    unittest.main()
