import math

def generate_primes(n: int) -> list[int]:
    """Generate all primes <= n using the Sieve of Eratosthenes."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)

    is_prime[0] = False
    is_prime[1] = False

    limit = math.isqrt(n)

    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]

if __name__ == "__main__":
    print(generate_primes(29))