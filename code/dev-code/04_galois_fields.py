# Author: Dev Mody
# Date: December 4th, 2024
# Description: Implements Galois Extension Fields

import numpy as np

class GaloisField:
    def __init__(self, field_size, irreducible_poly):
        self.field_size = 2 ^ field_size
        self.irreducible_poly = irreducible_poly

        #self.inverses = self.precompute_inverses()

    def precompute_inverses(self):
        inverses = {}
        for i in range(1, self.field_size):
            inverses[i] = self.multiplicative_inverse(i)
        return inverses

    def add(self, a, b):
        return a ^ b

    def subtract(self, a, b):
        return a ^ b

    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1:  # If the lowest bit of b is set, add a to result
                result ^= a
            b >>= 1  # Shift b right
            a <<= 1  # Shift a left
            if a & self.field_size:  # Check if a exceeds the field size
                a ^= self.irreducible_poly  # Reduce modulo the irreducible polynomial
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not defined in GF(2^n)")
        inv_b = self.multiplicative_inverse(b)
        return self.multiply(a, inv_b)

    def multiplicative_inverse(self, b):
        r0, r1 = self.irreducible_poly, b
        t0, t1 = 0, 1

        while r1 != 0:
            # Now compute the quotient by reducing r0 with r1
            # This part mimics the division in finite field with XOR
            quotient = r0 ^ r1
            r0, r1 = r1, r0 ^ self.multiply(quotient, r1)
            t0, t1 = t1, t0 ^ self.multiply(quotient, t1)

        if r0 != 1:
            raise ValueError(f"{b} has no multiplicative inverse in GF(2^n)")
        return t0

    def vector_to_int(self, vector):
        """Converts binary vector to regular integer."""
        return int(''.join(map(str, vector)), 2)
    
    def int_to_vector(self, value):
        """Converts integer to binary vector."""
        return list(map(int, bin(value)[2:].zfill(self.degree)))


# Test with smaller values
def test_galois_field():
    gf = GaloisField(field_size=4, irreducible_poly = 19)

    print("Addition (1 ^ 2):", bin(gf.add(13, 6))) 
    print("Subtraction (1 ^ 2):", bin(gf.subtract(13, 6)))  

    # Test multiplication
    print("Multiplication (2 * 3):", bin(gf.multiply(13, 6))) 

    # Test division (multiplying by inverse)
    #print("Division (2 / 3):", gf.divide(2, 3))  # Expected: 2

    # Test multiplicative inverse
   #print("Multiplicative Inverse of 2:", gf.multiplicative_inverse(2))  # Expected: 3

    # Test division by zero
    # try:
    #     print("Division by zero (2 / 0):", gf.divide(2, 0))
    # except ValueError as e:
    #     print("Division by zero:", e)

    # Test field size validation (only power of 2 is allowed)
    # try:
    #     gf_invalid = GaloisField(field_size=5, irreducible_poly=0x3)  # Should raise ValueError
    # except ValueError as e:
    #     print("Invalid field size:", e)

test_galois_field()
