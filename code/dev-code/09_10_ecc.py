#Author: Dev Mody
#Date: December 5th, 2024
#Description: Implements Elliptic Curves, the Diffie-Hellman Key Exchange in EC, and ECDSA

import sympy
import random
import math
from hashlib import sha256

# Elliptic Curve Group Implementation
class EllipticCurveGroup:
    
    # Inputs a prime number, a and b numbers
    def __init__(self, prime, a, b):
        if sympy.isprime(prime) and prime > 3:
            self.prime = prime
        else:
            raise ValueError("Prime must be a prime number greater than 3")
        if (4 * (a ** 3) + 27 * (b ** 2)) % prime != 0: # checks if the a and b values are good
            self.a = a
            self.b = b
        else:
            raise ValueError("Invalid")
        self.neutral = (None, None) # Identity Point
        self.points = self._generate_points()
        print(self.points)
        self.num_points = len(self.points)
        self.orders = self._find_orders() # Finds all orders
        self.primitives = self._find_primitives() # Finds all primitives
        
    def _generate_points (self):
        points = [self.neutral]  # Include neutral point
        # Loop through every x from 0 to prime-1
        for x in range(self.prime):
            rhs = (x ** 3 + self.a * x + self.b) % self.prime # generates all points such that y^2 = x^3 + ax + b mod p
            for y in range(self.prime):
                if (y ** 2) % self.prime == rhs:
                    points.append((x, y))
        return points
    
    def point_adding (self, point1, point2):
        if point1 not in self.points or point2 not in self.points:
            raise ValueError("Invalid point")
        
        if point1 == self.neutral:
            return point2
        if point2 == self.neutral:
            return point1
        
        if point1 == point2:
            return self.point_doubling(point1)
        
        if point1 == self.inverse_point(point2): # P + -P = Neutral
            return self.neutral
        
        (x1, y1) = point1
        (x2, y2) = point2
        #s = ((y2 - y1) // (x2 - x1)) % self.prime
        s = ((y2 - y1) * sympy.mod_inverse(x2-x1, self.prime)) % self.prime # Slope
        x3 = (s ** 2 - x1 - x2) % self.prime
        y3 = (s * (x1 - x3) - y1) % self.prime
        return (x3, y3)
        
    # Point Doubling
    def point_doubling (self, point):
        
        if point not in self.points:
            raise ValueError("Invalid point")
        
        if point == self.neutral:
            return self.neutral
        
        (x1, y1) = point
        
        if y1 == 0:
            return self.neutral
        #s = ((3 * x1**2 + self.a) // (2 * y1)) % self.prime
        s = ((3 * x1 ** 2 + self.a) * sympy.mod_inverse(2 * y1, self.prime)) % self.prime
        x3 = (s ** 2 - 2 * x1) % self.prime
        y3 = (s * (x1 - x3) - y1) % self.prime
        return (x3, y3)
    
    # Find the inverse of a point
    def inverse_point (self, point):
        if point not in self.points:
            raise ValueError("Invalid point")
        if point == self.neutral:
            return self.neutral
        (x, y) = point
        return (x, self.prime - y)
    
    # Point Multiplication using the algorithm
    def point_multiplication (self, point, n):
        
        def number_to_binary (number):
            return [int(b) for b in bin(number)[2:]]
        
        if point not in self.points:
            raise ValueError("Invalid point")
        if n == 0:
            return self.neutral
        if n == 1:
            return point
        
        binary_n = number_to_binary(n)
        result = point
        for i in range(len(binary_n) - 1, -1, -1):
            result = self.point_doubling(result)
            if binary_n[i] == 1:
                result = self.point_adding(result, point)
        return result
    
    # Finds the orders
    def _find_orders(self):
        orders = {}
        for point in self.points:
            count = 1
            current = point
            while current != self.neutral:
                count += 1
                current = self.point_adding(current, point) # keeps adding until you reach Neutral
            orders[point] = count
        return orders
    
    # Finds the primitives
    def _find_primitives (self):
        primitives = []
        for point in self.points:
            if self.orders[point] == self.num_points:
                primitives.append(point) #whichever point has order = number of points is a primitive
        return primitives
    
    # DLP for ECC
    def ec_discrete_log_problem (self, primitive, end):
        if primitive not in self.primitives:
            raise ValueError("Invalid primitive")
        if end not in self.points:
            raise ValueError("Invalid end")
        count = 0
        current = primitive
        while current != end:
            count += 1
            current = self.point_adding(current, primitive)
        return count

# ECC Diffie Hellman
class EllipticCurveDiffieHellman:
    
    # Takes in a prime, a and b for the Curve
    def __init__ (self, prime, a, b):
        self.group = EllipticCurveGroup(prime, a, b)
        self.prime = prime
        self.alpha = random.choice(self.group.primitives) # chooses a random primitive
        self.numbers = range(2, self.group.num_points)
    
    def create_public_key (self, private):
        if private not in self.numbers:
            raise ValueError("Invalid key")
        return self.group.point_multiplication(self.alpha, private) # Generates a public key for each party
    
    def create_shared_key (self, point, private):
        if private not in self.numbers or point not in self.group.points:
            raise ValueError("Invalid key")
        return self.group.point_multiplication(point, private) # Generates a private key for each party

# Elliptic Curve DSA Implementation (doesnt work as well as I wanted it to)    
class EllipticCurveDSA:
    
    def __init__(self, p, q, a, b):
        
        self.group = EllipticCurveGroup(p, a, b)
        p = p
        q = q
        A = random.choice(self.group.primitives)
        d = random.randint(0, q)
        B = self.group.point_multiplication(A, d)
        self.public = (p, a, b, q, A, B)
        self.private = d
        self.numbers = range(1, q)
        
    def _hash_number (self, number):
        number_bytes = str(number).encode('utf-8')
        sha256_hash = sha256()
        sha256_hash.update(number_bytes)
        return sha256_hash.hexdigest()
    
    def signature_generation (self, x):
        ephemeral = random.randint(0, self.public[3])
        R = self.group.point_multiplication(self.public[4], ephemeral)
        r = R[0]
        h_x = self._hash_number(x)
        ephemeral_inv = self.group.inverse_point(ephemeral)
        s = ((h_x + self.private * r) * ephemeral_inv) % self.public[3]
        return (h_x, (r, s))
        
    def signature_verification (self, encrypted):
        h_x, (r, s) = encrypted
        s_inv = self.group.inverse_point(s)
        w = s_inv % self.public[3]
        u1 = (h_x * w) % self.public[3]
        u2 = (r * w) % self.public[3]
        point1 = self.group.point_adding(self.group.point_multiplication(self.public[4], u1), self.group.point_multiplication(self.public[5], u2))
        return point1[0] % self.public[3] == r
        
#Tests EC Group
curve = EllipticCurveGroup(17, 2, 2)
print(curve.num_points)
print("Points on curve:", curve.points)
print("Neutral element:", curve.neutral)
print("Orders of points:", curve.orders)
print("Primitive elements:", curve.primitives)

# Example point multiplication
P = (0, 6)
k = 3
print(f"{k} * {P} = {curve.point_multiplication(P, k)}")

#Testing ECDHKE
prime = 17
a = 2
b = 2

# Initialize Diffie-Hellman exchange
dh = EllipticCurveDiffieHellman(prime, a, b)

# Simulate Alice's private and public key
alice_private = random.choice(dh.numbers)
alice_public = dh.create_public_key(alice_private)

# Simulate Bob's private and public key
bob_private = random.choice(dh.numbers)
bob_public = dh.create_public_key(bob_private)

# Alice and Bob generate shared keys
alice_shared_key = dh.create_shared_key(bob_public, alice_private)
bob_shared_key = dh.create_shared_key(alice_public, bob_private)

# Test if the shared keys match (should be the same)
assert alice_shared_key == bob_shared_key, f"Test failed! Alice's shared key: {alice_shared_key}, Bob's shared key: {bob_shared_key}"

print("Test passed! Diffie-Hellman key exchange works correctly.")