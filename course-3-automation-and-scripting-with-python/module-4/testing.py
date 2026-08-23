import unittest

def calculate_total(price, tax_rate):
    return price + (price * tax_rate)

class TestCalculateTotal(unittest.TestCase):
    def test_calculate_total(self):
        # Example unit test
        self.assertEqual(calculate_total(100, 0.05), 105)

    def test_calculate_total_no_tax(self):
        # Example unit test
        self.assertEqual(calculate_total(200, 0), 200)

unittest.main()