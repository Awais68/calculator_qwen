import pytest
from src.calculator import calculate


class TestCalculator:
    """Test suite for the Python Calculator."""
    
    # Basic arithmetic operations
    def test_addition(self):
        assert calculate("5 + 3") == 8.0
        assert calculate("10 + 20") == 30.0
        assert calculate("0 + 5") == 5.0
        assert calculate("-5 + 3") == -2.0

    def test_subtraction(self):
        assert calculate("10 - 4") == 6.0
        assert calculate("5 - 10") == -5.0
        assert calculate("0 - 5") == -5.0
        assert calculate("-5 - 3") == -8.0

    def test_multiplication(self):
        assert calculate("6 * 7") == 42.0
        assert calculate("0 * 5") == 0.0
        assert calculate("-3 * 4") == -12.0
        assert calculate("-3 * -4") == 12.0

    def test_division(self):
        assert calculate("15 / 3") == 5.0
        assert calculate("10 / 4") == 2.5
        assert calculate("0 / 5") == 0.0
        assert calculate("-10 / 2") == -5.0

    def test_division_by_zero_raises_error(self):
        with pytest.raises(ValueError):
            calculate("10 / 0")
        with pytest.raises(ValueError):
            calculate("0 / 0")
        with pytest.raises(ValueError):
            calculate("5 / (3 - 3)")

    # Advanced operations
    def test_exponentiation(self):
        assert calculate("2 ^ 3") == 8.0
        assert calculate("5 ^ 2") == 25.0
        assert calculate("2 ^ 0") == 1.0
        assert calculate("10 ^ 1") == 10.0

    def test_right_associative_exponentiation(self):
        # 2 ^ 3 ^ 2 should be 2 ^ (3 ^ 2) = 2 ^ 9 = 512, not (2 ^ 3) ^ 2 = 8 ^ 2 = 64
        assert calculate("2 ^ 3 ^ 2") == 512.0

    def test_square_root(self):
        assert calculate("sqrt(16)") == 4.0
        assert calculate("sqrt(25)") == 5.0
        assert calculate("sqrt(0)") == 0.0
        assert calculate("sqrt(1)") == 1.0
        assert calculate("sqrt(2)") == pytest.approx(1.4142135623730951)

    def test_negative_square_root_raises_error(self):
        with pytest.raises(ValueError):
            calculate("sqrt(-4)")
        with pytest.raises(ValueError):
            calculate("sqrt(-1)")

    # Operator precedence
    def test_multiplication_before_addition(self):
        assert calculate("2 + 3 * 4") == 14.0  # Not 20
        assert calculate("10 - 2 * 3") == 4.0  # Not 24

    def test_division_before_addition(self):
        assert calculate("10 + 6 / 2") == 13.0  # Not 8
        assert calculate("20 - 8 / 4") == 18.0  # Not 3

    def test_exponentiation_before_multiplication(self):
        assert calculate("2 * 3 ^ 2") == 18.0  # 2 * (3^2), not (2*3)^2
        assert calculate("sqrt(16) * 2 ^ 3") == 32.0  # 4 * (2^3)

    def test_function_precedence(self):
        assert calculate("sqrt(16) * 2") == 8.0
        assert calculate("sqrt(25) + 3") == 8.0

    # Parentheses
    def test_parentheses_override_precedence(self):
        assert calculate("(2 + 3) * 4") == 20.0  # Not 14
        assert calculate("10 / (5 - 3)") == 5.0  # Not 7
        assert calculate("(10 - 5) * (3 + 2)") == 25.0

    def test_nested_parentheses(self):
        assert calculate("((2 + 3) * 4) + 1") == 21.0
        assert calculate("(10 - (5 - 2)) * 2") == 14.0

    # Whitespace handling
    def test_whitespace_ignored(self):
        assert calculate(" 10 + 5 ") == 15.0
        assert calculate("10  +  5") == 15.0
        assert calculate("\t10\n+\r5") == 15.0

    # Edge cases and complex expressions
    def test_decimal_numbers(self):
        assert calculate("0.5 + 0.5") == 1.0
        assert calculate("3.14 * 2") == 6.28
        assert calculate("10 / 0.5") == 20.0

    def test_complex_expression(self):
        assert calculate("sqrt(16) + 2 * (5 - 3)") == 8.0  # sqrt(16) + 2 * (5 - 3) = 4 + 2 * 2 = 4 + 4 = 8
        assert calculate("(10 + 5) * 2 - 4 / 2") == 28.0

    def test_large_numbers(self):
        assert calculate("1000000 + 1") == 1000001.0
        assert calculate("10 ^ 6") == 1000000.0

    # Error cases
    def test_invalid_expression_raises_error(self):
        with pytest.raises(ValueError):
            calculate("10 +")  # Incomplete expression
        # Note: "+ 10" is valid (unary plus) and should return 10.0
        assert calculate("+ 10") == 10.0
        with pytest.raises(ValueError):
            calculate("()")  # Empty parentheses
        with pytest.raises(ValueError):
            calculate("(10 + 5")  # Unbalanced parentheses
        with pytest.raises(ValueError):
            calculate("10 + * 5")  # Invalid operator sequence
        with pytest.raises(ValueError):
            calculate("")  # Empty expression
        with pytest.raises(ValueError):
            calculate("abc")  # Invalid characters
        with pytest.raises(ValueError):
            calculate("10 @ 5")  # Invalid operator

    def test_single_number(self):
        assert calculate("5") == 5.0
        assert calculate("0") == 0.0
        assert calculate("-5") == -5.0

    def test_precision_tolerance(self):
        # Test that calculations are accurate within 1e-9 tolerance
        result = calculate("1 / 3 * 3")
        assert abs(result - 1.0) < 1e-9