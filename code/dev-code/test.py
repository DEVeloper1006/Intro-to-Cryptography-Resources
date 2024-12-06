import random
from sympy import isprime

def miller_rabin(n, k=10):
    """Perform Miller-Rabin primality test."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(lower_bound, upper_bound):
    """Generate a large prime number in the specified range."""
    while True:
        candidate = random.randint(lower_bound, upper_bound)
        if miller_rabin(candidate):
            return candidate

def generate_dsa_primes():
    """Generate primes p and q for DSA."""
    lower_bound_q = 2**223
    upper_bound_q = 2**224 - 1
    lower_bound_p = 2**2047
    upper_bound_p = 2**2048 - 1

    for _ in range(4096):
        # Step 1: Find a 224-bit prime q
        q = generate_large_prime(lower_bound_q, upper_bound_q)

        # Step 2: Find a 2048-bit prime p such that p - 1 is a multiple of q
        for _ in range(1000):  # Limit attempts to find p
            m = random.randint(lower_bound_p, upper_bound_p)
            p = m - (m % (2 * q)) + 1  # Adjust m so that p-1 is a multiple of q
            if p > lower_bound_p and p < upper_bound_p and isprime(p):
                return p, q

    raise ValueError("Failed to find suitable primes p and q within 4096 iterations.")

# Example usage
try:
    p, q = generate_dsa_primes()
    print(f"Generated primes:\np = {p}\nq = {q}")
except ValueError as e:
    print(e)
