#Author: Dev Mody
#Date: December 4th 2024
#Description: Uses Euler's Phi Function and EEA

import sympy

# Performs ModularInverse using Euler's Phi Function and Extensive Euclidean Algorithm
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

# Test Cases
a = 1095369562025702556403033673059514719985657846060999038001272754193712036128714475110343472959833158083894277499580078770116751707887313066350958894258
m = 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497897

modInverse = ModularInverse(a, m)
eea_inverse = modInverse.eea_mod_inverse()
euler_inverse = modInverse.euler_mod_inverse()

if euler_inverse is not None and eea_inverse == euler_inverse:
    print(f"The modular inverse of {a} modulo {m} using Euler's Theorem is: {euler_inverse}\nThe modular inverse of {a} modulo {m} using EEA is: {euler_inverse}")
    print((euler_inverse * a) % m == 1)
    print(euler_inverse == 455849832448654918145271645198762680484609121155948527718155116360107376403525283213075123888664381192832794777034012202625978250778619258394374862217)
else:
    print(f"{a} has no modular inverse modulo {m}")
    
print(ModularInverse(13, 39).eea_mod_inverse())