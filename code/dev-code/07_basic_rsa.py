# Author: Dev Mody
# Date: December 4th, 2024
# Description: Implements Simple RSA + Runs some tests

import random
import sympy
from math import gcd

class ModularInverse:
    
    def __init__(self, a, m):
        self.a = a
        self.m = m
    
    def euler_mod_inverse (self):
        if sympy.isprime(self.m):
            phi_m = self.m - 1 #assuming m is prime
            inverse_b = pow(self.a, phi_m - 1, self.m)
            return inverse_b
        return self.eea_mod_inverse()
    
    def eea_mod_inverse (self):
        s0, s1 = 1, 0
        t0, t1 = 0, 1
        r0, r1 = self.a, self.m
        
        while r1 != 0:
            q = r0 // r1  
            r0, r1 = r1, r0 - q * r1
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1
        
        if r0 != 1:
            return None  
        else:
            return s0 % self.m

class BasicRSA:
    
    def __init__(self, n):
        self.n = n
        self.phi_n = n - 1
        self._generate_keys()
        
    def _generate_keys (self):
        e = random.randint(1, self.phi_n - 1)
        while gcd(e, self.phi_n) != 1:
            e = random.randint(1, self.phi_n - 1)
        d = ModularInverse(e, self.phi_n).euler_mod_inverse()
        self.public_key = (e, self.n)
        self.private_key = (d)
        
    def _square_and_multiply (self, x, h):
        
        def number_to_binary (number):
            return [int(b) for b in bin(number)[2:]]
            
        if h == 0: return 1
        if h == 1: return x
        binary_h = number_to_binary(h)
        t = len(binary_h)
        result = 1
        for i in range(t):
            result = (result * result) % self.n
            if binary_h[i] == 1:
                result = (result * x) % self.n
        return result
    
    def encrypt (self, x):
        e, _ = self.public_key
        return self._square_and_multiply(x, e)
    
    def decrypt (self, y):
        d = self.private_key
        return self._square_and_multiply(y, d)
    
def assignment_3_test ():
    n = 508281196310201376192554864656699346831575429768465482788715190735760361687281737746563113895010157
    e = 7
    y = 4066488477440339689911514138508998613662966982287543919056006242924596335364286584668317646217011
    assert y < n
    x = round(pow(y, (1/e)))
    print("x:", x)
    assert x ** e == y
    
n = 61  # A prime number n
rsa = BasicRSA(n)

# Public and private keys
print("Public Key:", rsa.public_key)
print("Private Key:", rsa.private_key)

# Message to encrypt
message = 42
print(message)

# Encrypt the message
encrypted_message = rsa.encrypt(message)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = rsa.decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
        
assignment_3_test()