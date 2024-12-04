import sympy

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

class PrimeFields:
    
    def __init__(self, p):
        
        self.elements = [x for x in range (p)]
        self.p = p
        self.prime = True
    
    def add (self, a, b):
        if a not in self.elements or b not in self.elements:
            return None
        return (a + b) % self.p

    def multiply (self, a, b):
        if a not in self.elements or b not in self.elements:
            return None
        return (a * b) % self.p
    
    def optimized_inverse (self, a):
        if a not in self.elements:
            return None
        inverseFinder = ModularInverse(a, self.p)
        return inverseFinder.eea_mod_inverse()
    
    def inverse(self, a):
        if a not in self.elements or a == 0:
            return None
        for i in self.elements:
            if (a * i) % self.p == 1:
                return i
        return None
    
    def divide (self, a, b):
        try:
            return self.multiply(a, self.inverse(b))
        except:
            return None

# Create a Prime Field with p = 7
pf = PrimeFields(7)

# Test Cases
print("Field Elements:", pf.elements)

# Addition
print("Addition (3 + 5):", pf.add(3, 5))  # Expected: (3 + 5) % 7 = 1
print("Addition (6 + 2):", pf.add(6, 2))  # Expected: (6 + 2) % 7 = 1
print("Addition (3 + 10):", pf.add(3, 10))  # Expected: None (10 not in field)

# Multiplication
print("Multiplication (3 * 5):", pf.multiply(3, 5))  # Expected: (3 * 5) % 7 = 1
print("Multiplication (6 * 4):", pf.multiply(6, 4))  # Expected: (6 * 4) % 7 = 3
print("Multiplication (3 * 10):", pf.multiply(3, 10))  # Expected: None (10 not in field)

# Inverse
print("Inverse of 3:", pf.optimized_inverse(3))  # Expected: 5 (3 * 5 ≡ 1 mod 7)
print("Inverse of 6:", pf.optimized_inverse(6))  # Expected: 6 (6 * 6 ≡ 1 mod 7)
print("Inverse of 0:", pf.optimized_inverse(0))  # Expected: None (0 has no inverse)

# Division
print("Division (3 / 5):", pf.divide(3, 5))  # Expected: (3 * 5^-1) % 7 = 3 * 3 % 7 = 2
print("Division (4 / 6):", pf.divide(4, 6))  # Expected: (4 * 6^-1) % 7 = 4 * 6 % 7 = 3
try:
    print("Division (3 / 0):", pf.divide(3, 0))  # Expected: ValueError
except ValueError as e:
    print("Division (3 / 0):", e)
