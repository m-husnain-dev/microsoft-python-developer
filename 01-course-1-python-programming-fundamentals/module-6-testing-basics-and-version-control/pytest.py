import pytest 
def calculate_discount(price, percentage):
  return price - (price * percentage / 100)
 
class TestDiscountCalculation:
  def test_ten_percent_discount(self):
    result = calculate_discount(100, 10)
    assert result == 90  # Assertion
 
  def test_invalid_input(self):
    with pytest.raises(TypeError):
      calculate_discount("100", 10)   # Test for incorrect input type