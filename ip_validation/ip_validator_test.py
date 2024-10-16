import unittest
from ip_validator import ip_validator



class TestIpValidator(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertTrue(ip_validator('1.2.3.4'))
        self.assertTrue(ip_validator('0.0.0.0'))
        self.assertTrue(ip_validator('0.1.255.0'))

    def test_incorrect_length(self):
        self.assertFalse(ip_validator('1.2.3'))
        self.assertFalse(ip_validator('1.2.3.4.5'))

    def test_incorrect_range(self):
        self.assertFalse(ip_validator('1.2.3.456'))
        self.assertFalse(ip_validator('1.2.3.-1'))

    def test_leading_zeros(self):
        self.assertFalse(ip_validator('1.2.3.04'))
        self.assertFalse(ip_validator('0.0.0.00'))

if __name__ == '__main__':
    unittest.main()
