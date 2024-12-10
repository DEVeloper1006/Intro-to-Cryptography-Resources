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
        s = ((y2 - y1) * sympy.mod_inverse(x2-x1, self.prime)) % self.prime
        x3 = (s ** 2 - x1 - x2) % self.prime
        y3 = (s * (x1 - x3) - y1) % self.prime
        return (x3, y3)
        
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
    
    def _find_orders(self):
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

curve = EllipticCurveGroup(11, 1, 2)
print(curve.orders)
print(curve.orders[(8,4)])

