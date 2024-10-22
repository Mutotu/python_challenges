import unittest
from min_squares import min_squares


# Test Cases
class TestMinSquares(unittest.TestCase):

    def test_small_values(self):
        self.assertEqual(min_squares(1), 1)
        self.assertEqual(min_squares(2), 2)
        self.assertEqual(min_squares(3), 3)

    def test_basic_cases(self):
        self.assertEqual(min_squares(17), 2)  # 17 = 16 + 1
        self.assertEqual(min_squares(15), 4)  # 15 = 9 + 4 + 1 + 1


if __name__ == "__main__":
    unittest.main()