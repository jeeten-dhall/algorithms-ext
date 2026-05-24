def gcd(a: int, b: int) -> int:
    """Compute GCD using consecutive integer checking."""
    if a == 0:
        return b
    if b == 0:
        return a

    c = min(a, b)
    while c > 0:
        if a % c == 0 and b % c == 0:
            break
        c -= 1

    return c

if __name__ == "__main__":
    a, b = 48, 18
    result = gcd(a, b)
    print(f"GCD of {a} and {b} is: {result}")