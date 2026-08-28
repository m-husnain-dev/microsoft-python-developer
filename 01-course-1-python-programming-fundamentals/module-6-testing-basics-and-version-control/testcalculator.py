# test_calculator.py
import pytest
from calculator import Calculator

# 1. Setup a fixture to avoid repeating instantiation logic across tests
@pytest.fixture
def calc():
    return Calculator()

# 2. Basic assertions using the fixture
def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

# 3. Parametrized testing to evaluate multiple datasets efficiently
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (2.5, 2, 5.0)
    ]
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

# 4. Testing for expected exceptions (like dividing by zero)
def test_divide_by_zero(calc):
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)
    assert str(exc_info.value) == "Cannot divide by zero."
