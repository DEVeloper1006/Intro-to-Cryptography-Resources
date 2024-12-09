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

n = 697
phi_n = sympy.totient(n)
print(phi_n)

e_1 = 32
e_2 = 49

print()

try:
    d_1 = ModularInverse(e_1, phi_n).eea_mod_inverse()
    d_2 = ModularInverse(e_2, phi_n).eea_mod_inverse()
    print(d_1)
    print(d_2)
except:
    print("Error: unable to find modular inverse")

