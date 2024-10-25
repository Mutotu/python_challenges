import unittest
from longest_palindrome import longest_palindrome

class TestLongestPalindrome(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(longest_palindrome(''), 0)
        self.assertEqual(longest_palindrome('a'), 1)
        self.assertEqual(longest_palindrome('zzbaabcd'), 4)
        self.assertEqual(longest_palindrome('HYTBCABADEFGHABCDEDCBAGHTFYW12345678987654321ZWETYGDE'), 17)
        self.assertEqual(longest_palindrome('test'), 0)

if __name__ == '__main__':
    unittest.main()
