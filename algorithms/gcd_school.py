from prime_factors import get_factor_map


def gcd(a: int, b: int) -> int:
    """Compute GCD using school method."""
    if a < 0 or b < 0:
        raise ValueError("GCD requires non-negative integers.")

    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for (0, 0).")

    if a == 0:
        return b
    if b == 0:
        return a

    result = 1

    a_factors: dict[int, int] = get_factor_map(a)
    b_factors: dict[int, int] = get_factor_map(b)

    for factor, a_count in a_factors.items():
        if factor in b_factors:
            b_count = b_factors[factor]
            result *= factor ** min(a_count, b_count)

    return result

if __name__ == "__main__":
    a, b = 48, 18
    result = gcd(a, b)
    print(f"GCD of {a} and {b} is: {result}")

    a, b = 72, 24
    result = gcd(a, b)
    print(f"GCD of {a} and {b} is: {result}")