import sympy

class ModularInverse:
    def __init__(self, a, m):
        self.a = a
        self.m = m
    
    def euler_mod_inverse(self):
        if sympy.isprime(self.m):
            phi_m = self.m - 1  # assuming m is prime
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
            return None  # no modular inverse if gcd(a, m) != 1
        else:
            return s0 % self.m

# ElGamal Encryption
p = 467  # prime number
alpha = 2  # base
d = 105  # Bob's private key
i = 213  # Alice's private key

# Public keys
K_b = pow(alpha, d, p)  # Bob's public key
print(f"Bob's public key (K_b): {K_b}")

K_a = pow(alpha, i, p)  # Alice's public key
print(f"Alice's public key (K_a): {K_a}")

# Shared secret key K_ab
K_ab = pow(K_b, i, p)  # Alice computes K_ab = K_b^i mod p
print(f"Shared key (K_ab) computed by Alice: {K_ab}")

# Message to be encrypted
x = 33  # Example plaintext message

# Encryption
encrypt = (K_ab * x) % p
print(f"Encrypted message: {encrypt}")

# Decryption
K_ab_inv = ModularInverse(K_ab, p).euler_mod_inverse()  # Compute modular inverse of K_ab
decrypt = (K_ab_inv * encrypt) % p  # Decrypt the message
print(f"Decrypted message: {decrypt}")

