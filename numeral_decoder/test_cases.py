import unittest
from numeral_decoder import deromanize  # Adjust this import based on your actual Python file structure

class TestRomanNumeralEncoder(unittest.TestCase):
    def test_no_more_than_four_digits_for_numbers_under_4000(self):
        self.assertEqual(deromanize('MMMCMXCIX'), 3999)

    def test_numbers_over_4000(self):
        self.assertEqual(deromanize('MMMMCMXCIX'), 4999)
        self.assertEqual(deromanize('MMMMMMMMMCMXCIX'), 9999)

    def test_basic_numbers(self):
        self.assertEqual(deromanize('XXVII'), 27)
        self.assertEqual(deromanize('MDCLXVI'), 1666)

if __name__ == '__main__':
    unittest.main()
