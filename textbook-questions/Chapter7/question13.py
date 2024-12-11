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

ciphertexts = [2514, 1125, 333, 3696, 2514, 2929, 3368, 2514]
n, e = (3763, 11)

factors = list(sympy.factorint(n).keys())
print(factors)
phi_n = 1
for factor in factors:
    phi_n *= (factor - 1)
print(phi_n == sympy.totient(n))
d = ModularInverse(e, phi_n).eea_mod_inverse()

ord_values = []
for text in ciphertexts:
    ord_values.append(pow(text, d, n))  # prints the decrypted text

string = ''.join(chr(value) for value in ord_values)

print(string)