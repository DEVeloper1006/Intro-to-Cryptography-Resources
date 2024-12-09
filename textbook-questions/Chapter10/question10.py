import sympy

class ModularInverse:
    def __init__(self, a, m):
        self.a = a
        self.m = m
    
    def euler_mod_inverse (self):
        if sympy.isprime(self.m):
            phi_m = self.m - 1 #assuming m is prime
            inverse_b = pow(a, phi_m - 1, self.m)
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

# Private key
d = 67
# Public parameters
p, alpha, beta = 97, 23, 15  # beta = alpha^d % p

# Message
x = 17
# Random ephemeral key
k_e = 31

# Signature generation
r = pow(alpha, k_e, p)  # Compute r = alpha^k_e mod p
print("r:", r)

k_e_inv = ModularInverse(k_e, p - 1).eea_mod_inverse()  # Modular inverse of k_e mod (p-1)
print("k_e_inv:", k_e_inv)

s = ((x - d * r) * k_e_inv) % (p - 1)  # Compute s
print("s:", s)

# Verification
lhs = (pow(beta, r, p) * pow(r, s, p)) % p  # Compute β^r * r^s mod p
rhs = pow(alpha, x, p)  # Compute α^x mod p
print(lhs, rhs)
print("Verification result:", lhs == rhs)
