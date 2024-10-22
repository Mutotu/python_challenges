import unittest
from is_valid_walk import is_valid_walk

class TestWalks(unittest.TestCase):

    def test_fixed_tests(self):
        self.assertEqual(is_valid_walk(['s']), False)
        self.assertEqual(
            is_valid_walk(['s', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n']), True
        )
        self.assertEqual(
            is_valid_walk(['n', 'n', 'n', 's', 's', 's', 'w', 'w', 'e', 'e']), True
        )
        self.assertEqual(
            is_valid_walk(['s', 's', 's', 's', 'y', 'n', 'n', 'n', 'x', 'n']), False
        )
        self.assertEqual(
            is_valid_walk(['a', 'a', 's', 's', 'y', 'n', 'n', 'n', 'x', 'n']), False
        )


if __name__ == "__main__":
    unittest.main()