import pytest

from prime_factors import get_factor_map

@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(1, {}, id="edge_case_for_one"),
        pytest.param(48, {2: 4, 3: 1}, id="composite_with_repeated_prime_factor"),
        pytest.param(77, {7: 1, 11: 1}, id="edge_case_for_factor_beyond_sqrt_a")
    ]
)
def test_get_factor_map(n, expected):
    result = get_factor_map(n)
    assert result == expected

def test_invalid_input():
    with pytest.raises(ValueError):
        get_factor_map(0)

def test_negative_input():
    with pytest.raises(ValueError):
        get_factor_map(-5)

def reconstruct(factor_map):
    result = 1

    for factor, exponent in factor_map.items():
        result *= factor ** exponent

    return result

def test_factorization_reconstruction():
    n = 48

    factor_map = get_factor_map(n)
    assert reconstruct(factor_map) == n