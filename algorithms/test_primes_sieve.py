import pytest

from primes_sieve import generate_primes

@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(0, [], id="edge_case_for_zero"),
        pytest.param(1, [], id="edge_case_for_one"),
        pytest.param(2, [2], id="edge_case_for_two"),
        pytest.param(23, [2, 3, 5, 7, 11, 13, 17, 19, 23], id="edge_case_for_prime"),
        pytest.param(25, [2, 3, 5, 7, 11, 13, 17, 19, 23], id="composite_upper_bound")
    ]
)
def test_generate_primes(n, expected):
    result = generate_primes(n)
    assert result == expected

