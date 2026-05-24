import pytest

from gcd_consecutive import gcd

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(48, 18, 6, id="common_case_1"),
        pytest.param(17, 13, 1, id="coprime"),
        pytest.param(7, 7, 7, id="same_number"),
        pytest.param(18, 0, 18, id="with_zero"),
        pytest.param(100, 10, 10, id="common_case_2"),
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
