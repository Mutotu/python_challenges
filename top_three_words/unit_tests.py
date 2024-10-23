import unittest
from top_three_words import top_three_words_extractor

# Unit test cases
class TestTopThreeWords(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(top_three_words_extractor('a a a  b  c c  d d d d  e e e e e'), ['e', 'd', 'a'])
        self.assertEqual(top_three_words_extractor('a a c b b'), ['a', 'b', 'c'])

    def test_strips_unknown_characters(self):
        self.assertEqual(top_three_words_extractor('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e'), ['e', 'ddd', 'aa'])
        self.assertEqual(top_three_words_extractor('  , e   .. '), ['e'])
        self.assertEqual(top_three_words_extractor('  ...  '), [])
        self.assertEqual(top_three_words_extractor("  '  "), [])

    def test_dont_strip_apostrophes(self):
        self.assertEqual(top_three_words_extractor("  //wont won't won't "), ["won't", 'wont'])

    def test_real_use_case(self):
        text = '''In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.'''
        self.assertEqual(top_three_words_extractor(text), ['a', 'of', 'on'])

if __name__ == "__main__":
    unittest.main()
