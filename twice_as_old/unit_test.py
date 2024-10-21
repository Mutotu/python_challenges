import unittest
from twice_as_old import twice_as_old


# Unit test cases
class TestTwiceAsOld(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(twice_as_old(36, 7), 22)

    def test_case_2(self):
        self.assertEqual(twice_as_old(55, 30), 5)

    def test_case_3(self):
        self.assertEqual(twice_as_old(42, 21), 0)

    def test_case_4(self):
        self.assertEqual(twice_as_old(22, 1), 20)

    def test_case_5(self):
        self.assertEqual(twice_as_old(29, 0), 29)


if __name__ == "__main__":
    unittest.main()
