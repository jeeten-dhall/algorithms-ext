import pytest

from gcd_euclid import gcd, validate_input

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(48, 18, 6, id="common_case_1"),
        pytest.param(17, 13, 1, id="coprime"),
        pytest.param(7, 7, 7, id="same_number"),
        pytest.param(18, 0, 18, id="with_zero"),
        pytest.param(100, 10, 10, id="common_case_2"),
        pytest.param(72, 24, 24, id="school_method_use_case"),
        pytest.param(55, 34, 1, id="fibonacci_worst_case")
    ]
)
def test_gcd(a, b, expected):
    result = gcd(a, b)
    assert result == expected


def test_gcd_symmetry():
    assert gcd(48, 18) == gcd(18, 48)


def test_gcd_zero_symmetry():
    assert gcd(0, 18) == gcd(18, 0)


def test_gcd_divides_inputs():
    result = gcd(48, 18)

    assert 48 % result == 0
    assert 18 % result == 0


def test_validate_negative_numbers():
    is_valid, error_message = validate_input(-1, 5)

    assert is_valid is False
    assert error_message == "GCD cannot be computed for negative numbers."


def test_validate_both_zero():
    is_valid, error_message = validate_input(0, 0)

    assert is_valid is False
    assert error_message == "GCD is undefined for (0, 0)."


def test_validate_valid_input():
    is_valid, error_message = validate_input(40, 12)

    assert is_valid is True
    assert error_message == ""
