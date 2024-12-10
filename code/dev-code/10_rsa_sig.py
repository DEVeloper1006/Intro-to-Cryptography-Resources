# Author: Dev Mody
# Date: December 5th 2024
# Description: Implements RSA Signature Scheme

import random
import sympy
from math import gcd

# Uses Modular Inverse
class ModularInverse:
    
    def __init__(self, a, m):
        self.a = a
        self.m = m
    
    def euler_mod_inverse(self):
        # If m is prime, we can use Fermat's little theorem to find the inverse.
        if sympy.isprime(self.m):
            phi_m = self.m - 1  # Assuming m is prime
            inverse_b = pow(self.a, phi_m - 1, self.m)
            return inverse_b
        return self.eea_mod_inverse()

    def eea_mod_inverse(self):
        s0, s1 = 1, 0
        t0, t1 = 0, 1
        r0, r1 = self.a, self.m
        
        while r1 != 0:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1
        
        if r0 != 1:
            return None  # No inverse exists
        else:
            return s0 % self.m

# RSA Signature Scheme based on the textbook
class RSASigScheme:
    
    def __init__(self, bit_length=2048):
        self.bit_length = bit_length
        self._generate_keys()
        
    def _generate_keys(self):
        # Generate two distinct primes p and q
        p = sympy.randprime(2**(self.bit_length // 2), 2**(self.bit_length // 2 + 1))
        q = sympy.randprime(2**(self.bit_length // 2), 2**(self.bit_length // 2 + 1))
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)
        
        # Choose e such that gcd(e, phi_n) = 1
        e = random.randint(2, self.phi_n - 1)
        while gcd(e, self.phi_n) != 1:
            e = random.randint(2, self.phi_n - 1)
        
        # Compute d, the modular inverse of e modulo phi_n
        d = ModularInverse(e, self.phi_n).eea_mod_inverse()
        self.public_key = (e, self.n)
        self.private_key = (d, self.n)
        
    # Fast Modular Exponentiation
    def _square_and_multiply(self, x, h):
        def number_to_binary(number):
            return [int(b) for b in bin(number)[2:]]
            
        if h == 0:
            return 1
        if h == 1:
            return x
        binary_h = number_to_binary(h)
        t = len(binary_h)
        result = 1
        for i in range(t):
            result = (result * result) % self.n
            if binary_h[i] == 1:
                result = (result * x) % self.n
        return result
    
    def sign(self, message):
        d, _ = self.private_key
        # Sign the message: s = m^d mod n
        return pow(message, d, self.n)

    
    def verify(self, message, signature):
        e, n = self.public_key
        # Verify the signature: m = s^e mod n
        return pow(signature, e, n) == message
    
# Example usage:
rsa = RSASigScheme(bit_length=512)

# Message to sign
message = 42

# Sign the message
signature = rsa.sign(message)
print(f"Signature: {signature}")

# Verify the signature
is_valid = rsa.verify(message, signature)
print(f"Signature valid: {is_valid}")