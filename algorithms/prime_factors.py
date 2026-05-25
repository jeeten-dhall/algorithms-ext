import math

from primes_sieve import generate_primes


def get_factor_map(a: int) -> dict[int, int]:
    """Return prime factorization map of a positive integer."""

    if a <= 0:
        raise ValueError("Input must be a positive integer.")

    factor_map: dict[int, int] = {}

    primes = generate_primes(math.isqrt(a))
    for factor in primes:
        if a == 1:
            break

        while a % factor == 0:
            a //= factor
            factor_map[factor] = factor_map.get(factor, 0) + 1

    if a > 1:
        factor_map[a] = 1

    return factor_map

def main():
    print(get_factor_map(48))
    print(get_factor_map(77))
    print(get_factor_map(1))

if __name__ == "__main__":
    main()
