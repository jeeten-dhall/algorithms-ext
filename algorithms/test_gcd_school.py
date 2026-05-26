import pytest

from gcd_school import gcd

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(48, 18, 6, id="common_case_1"),
        pytest.param(17, 13, 1, id="coprime"),
        pytest.param(7, 7, 7, id="same_number"),
        pytest.param(18, 0, 18, id="with_zero"),
        pytest.param(100, 10, 10, id="common_case_2"),
        pytest.param(55, 34, 1, id="fibonacci_worst_case"),
        pytest.param(72, 24, 24, id="multiplier_vs_exponent_bugfix")
    ]
)
def test_gcd(a, b, expected):
    result = gcd(a, b)
    assert result == expected


def test_negative_input():
    with pytest.raises(ValueError,
                       match = "GCD requires non-negative integers."):
        gcd(12, -1)

def test_gcd_both_zero():
    with pytest.raises(ValueError,
                       match = "GCD is undefined for \\(0, 0\\)."):
        gcd(0, 0)

def test_gcd_symmetry():
    assert gcd(48, 18) == gcd(18, 48)


def test_gcd_divides_inputs():
    result = gcd(72, 24)

    assert 72 % result == 0
    assert 24 % result == 0