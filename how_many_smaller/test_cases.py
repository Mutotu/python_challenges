import unittest
from smaller import smaller


# Unit test class
class TestSmallerFunction(unittest.TestCase):

    def test_fixed_tests(self):
        self.assertEqual(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
        self.assertEqual(smaller([1, 2, 3]), [0, 0, 0])
        self.assertEqual(smaller([1, 2, 0]), [1, 1, 0])
        self.assertEqual(smaller([1, 2, 1]), [0, 1, 0])
        self.assertEqual(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
        self.assertEqual(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()