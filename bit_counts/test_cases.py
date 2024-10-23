import unittest
from bit_counter import count_bits


class TestBitCounter(unittest.TestCase):

    def test_fixed_cases(self):
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(3), 2)
        self.assertEqual(count_bits(27), 4)
        self.assertEqual(count_bits(1532), 8)

if __name__ == "__main__":
    unittest.main()