import unittest


class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(9 / 4, 2)  # Python 2.7
        self.assertEqual(9 / 4.0, 2.25)
