import unittest


def camelize(s):
    # Replace all non-alphanumeric characters with spaces, split into words
    words = s.replace('-', ' ').replace('_', ' ').split()

    # Return empty string if no words
    if not words:
        return ''

    # First word remains lowercase, others are capitalized
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


class TestCamelize(unittest.TestCase):

    def test_fixed_tests(self):
        self.assertEqual(camelize(''), '')
        self.assertEqual(camelize('----'), '')
        self.assertEqual(camelize('--_-_- _ --'), '')
        self.assertEqual(camelize('come_on_already'), 'comeOnAlready')
        self.assertEqual(camelize('come-on-already'), 'comeOnAlready')
        self.assertEqual(camelize('come-__-_-_-on-_-already'), 'comeOnAlready')


if __name__ == '__main__':
    unittest.main()