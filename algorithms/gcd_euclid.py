def gcd_iterative(a: int, b: int) -> int:
    """ITERATIVELY Compute the greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a # because gcd(a, 0) == a

def gcd(a: int, b: int) -> int:
    """RECURSIVELY Compute the greatest common divisor using Euclid's algorithm."""
    if b == 0:
        return a # because gcd(a, 0) == a

    return gcd(b, a % b)

def validate_input(a: int, b: int) -> tuple[bool, str]:
    if a < 0 or b < 0:
        return False, "GCD cannot be computed for negative numbers."
    if a == 0 and b == 0:
        return False, "GCD is undefined for (0, 0)."
    return True, ""

def main():
    while True:
        user_input = input(
            "Enter two non-negative integers separated by a space "
            "to calculate their GCD (Type x to exit): "
        )

        if user_input.strip().lower() == "x":
            print("Exiting...")
            break

        try:
            parts = user_input.split()
            if len(parts) != 2:
                raise ValueError

            a, b = map(int, parts)

            is_valid, error_message = validate_input(a, b)

            if not is_valid:
                print(error_message)
                continue

            result = gcd(a, b)
            print(f"GCD of {a} and {b} is: {result}")
        except ValueError:
            print("Please enter two valid integers separated by a space.")


if __name__ == "__main__":
    main()