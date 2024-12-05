# Author: Dev Mody
# Date: December 4th, 2024
# Description: Performs Fermat and Miller-Rabin Primality Test

import sympy
import random

def fermat_primality_test(candidate, security):
    if candidate < 2:
        return False
    for _ in range(1, security + 1):
        a = random.randint(2, candidate - 2)
        if pow(a, candidate - 1, candidate) != 1:
            return False
    return True

def is_carmichael (candidate, security):
    return fermat_primality_test(candidate, security) and not sympy.isprime(candidate)

def miller_rabin_primality_test (candidate, security):
    if candidate < 2:
        return False
    r = candidate - 1
    u = 0
    while r % 2 == 0:
        r //= 2
        u += 1
    for _ in range(1, security + 1):
        a = random.randint(2, candidate - 2)
        z = pow(a, r, candidate)
        if z != 1 and z != candidate - 1:
            j = 1
            while j <= u - 1 and z != candidate - 1:
                z = pow(z, 2, candidate)
                if z == 1:
                    return False
                j += 1
            if z != candidate - 1:
                return False
    return True
n = 561  # Prime number example
result = fermat_primality_test(n, 5)
print(f"Is {n} prime? {result}")

# Test a prime candidate
candidate = 17
print(miller_rabin_primality_test(candidate, 40))  # Should return True (17 is prime)

# Test a composite candidate
candidate = 18
print(miller_rabin_primality_test(candidate, 40))  # Should return False (18 is composite)

