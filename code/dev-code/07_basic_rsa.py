import random
import sympy
from math import gcd
from hashlib import sha256

# Uses the ModularInverse class
class ModularInverse:
    
    def __init__(self, a, m):
        self.a = a
        self.m = m
    
    def euler_mod_inverse(self):
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

# Basic RSA implementation
class BasicRSA:
    
    def __init__(self, bit_length=2048):
        self.bit_length = bit_length
        self._generate_keys() # Generates a key
        
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
        
    # Fast Exponentiation using SAM
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
    
    # Encrypt
    def encrypt(self, x):
        e, _ = self.public_key
        # RSA Encryption: c = m^e mod n
        return self._square_and_multiply(x, e)
    
    # Decrypt
    def decrypt(self, y):
        d, _ = self.private_key
        # RSA Decryption: m = c^d mod n
        return self._square_and_multiply(y, d)

# Example usage:
rsa = BasicRSA(bit_length=512)

# Message to encrypt
message = 42

# Encrypt the message
ciphertext = rsa.encrypt(message)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_message = rsa.decrypt(ciphertext)
print(f"Decrypted Message: {decrypted_message}")
