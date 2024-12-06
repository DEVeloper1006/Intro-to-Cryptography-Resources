import sympy
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
        
mod_inv = ModularInverse(4, 11)
print(mod_inv.euler_mod_inverse())  # Output: 3
print((193 * 3) % 11)