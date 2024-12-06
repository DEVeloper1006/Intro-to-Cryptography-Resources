#Author: Dev Mody
#Date: December 5th, 2024
#Description: Implements Elliptic Curves, the Diffie-Hellman Key Exchange in EC, and ECDSA

import sympy
import random
import math
from hashlib import sha256

class EllipticCurveGroup:
    
    def __init__(self, prime, a, b):
        if sympy.isprime(prime) and prime > 3:
            self.prime = prime
        else:
            raise ValueError("Prime must be a prime number greater than 3")
        if (4 * (a ** 3) + 27 * (b ** 2)) % prime != 0:
            self.a = a
            self.b = b
        else:
            raise ValueError("Invalid")
        self.neutral = (None, None)
        self.points = self._generate_points()
        print(self.points)
        self.num_points = len(self.points)
        self.orders = self._find_orders()
        self.primitives = self._find_primitives()
        
    def _generate_points (self):
        points = [self.neutral]  # Include neutral point
        # Loop through every x from 0 to prime-1
        for x in range(self.prime):
            rhs = (x ** 3 + self.a * x + self.b) % self.prime
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
        
        if point1 == self.inverse_point(point2):
            return self.neutral
        
        (x1, y1) = point1
        (x2, y2) = point2
        #s = ((y2 - y1) // (x2 - x1)) % self.prime
        s = ((y2 - y1) * pow (x2 - x1, -1, self.prime)) % self.prime
        x3 = (s ** 2 - x1 - x2) % self.prime
        y3 = (s * (x1 - x3) - y1) % self.prime
        return (x3, y3)
        
    def point_doubling (self, point):
        
        if point not in self.points:
            raise ValueError("Invalid point")
        
        if point == self.neutral:
            return self.neutral
        
        (x1, y1) = point
        #s = ((3 * x1**2 + self.a) // (2 * y1)) % self.prime
        s = ((3 * x1 ** 2 + self.a) * pow (2 * y1, -1, self.prime)) % self.prime
        x3 = (s ** 2 - 2 * x1) % self.prime
        y3 = (s * (x1 - x3) - y1) % self.prime
        return (x3, y3)
    
    def inverse_point (self, point):
        if point not in self.points:
            raise ValueError("Invalid point")
        if point == self.neutral:
            return self.neutral
        (x, y) = point
        return (x, self.prime - y)
    
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
        for i in range(len(binary_n)):
            result = self.point_doubling(result)
            if binary_n[i] == 1:
                result = self.point_adding(result, point)
        return result
    
    def _find_orders (self):
        orders = {}
        for point in self.points:
            count = 1
            current = point
            while current != self.neutral:
                count += 1
                current = self.point_adding(current, point)
            orders[point] = count
        return orders
    
    def _find_primitives (self):
        primitives = []
        for point in self.points:
            if self.orders[point] == self.num_points:
                primitives.append(point)
        return primitives
    
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

class EllipticCurveDiffieHellman:
    
    def __init__ (self, prime, a, b):
        self.group = EllipticCurveGroup(prime, a, b)
        self.prime = prime
        self.alpha = random.choice(self.group.primitives)
        self.numbers = range(2, self.group.num_points)
    
    def create_public_key (self, private):
        if private not in self.numbers:
            raise ValueError("Invalid key")
        return self.group.point_multiplication(self.alpha, private)
    
    def create_shared_key (self, point, private):
        if private not in self.numbers or point not in self.group.points:
            raise ValueError("Invalid key")
        return self.group.point_multiplication(point, private)
    
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
print("Points on curve:", curve.points)
print("Neutral element:", curve.neutral)
print("Orders of points:", curve.orders)
print("Primitive elements:", curve.primitives)
print("Discrete Log of:", curve.ec_discrete_log_problem((0,6), (5,1)))

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

ecdsa = EllipticCurveDSA(23, 11, 1, 1)

# Generate private key d
private_key = random.randint(1, 10)
print(f"Private key: {private_key}")

# Generate public key (B = d * A)
public_key = ecdsa.group.point_multiplication(ecdsa.public[4], private_key)
print(f"Public key: {public_key}")

# Generate a message (x) to sign
x = random.randint(1, 1000)  # Random message
print(f"Message (x): {x}")

# Generate the signature for the message
signature = ecdsa.signature_generation(x)
print(f"Generated signature: {signature}")

# Verify the signature
is_valid = ecdsa.signature_verification(signature)
print(f"Signature valid: {is_valid}")