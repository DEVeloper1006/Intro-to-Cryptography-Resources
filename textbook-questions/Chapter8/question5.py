import random, sympy, math
from hashlib import sha256

class PrimeCyclicGroupMult:
    
    def __init__ (self, n):
        self.n = n
        self.elements = [num for num in range(1, n)]
        self.orders = self.orders()
        self.primitives = self._find_primitives()
        self.subgroups = self._find_subgroups()
    
    def orders (self):
        orders = dict()
        for i in self.elements:
            orders[i] = self.find_order(i)
        return orders
    
    def find_order (self, a):
        if a not in self.elements:
            raise ValueError("Element not in group")
        result = a
        count = 1
        while pow(result, count, self.n) != 1:
            count += 1
        return count
    
    def _find_primitives (self):
        primitives = []
        for i in self.elements:
            if self.orders[i] == len(self.elements):
                primitives.append(i)
        return primitives
    
    def _find_subgroups (self):
        subgroups = {}
        subgroups[len(self.elements)] = self.elements
        marked = set()
        for order in self.orders.values():
            if order != len(self.elements) and order not in marked:
                subgroup = []
                for i in self.elements:
                    if self.orders[i] == order:
                        subgroup.append(i)
                for primitive in self.primitives:
                    subgroup.append(primitive)
                subgroups[order] = subgroup
                marked.add(order)
        return subgroups
                
    def print_order (self):
        for i in self.elements:
            print(f"Order of {i} is {self.find_order(i)}")
            
    def is_generator (self, a):
        return a in self.primitives
    
    def derive_new_element (self, a, b):
        if a not in self.elements or b not in self.elements:
            raise ValueError("Elements not in group")
        return (a * b) % self.n
    
    def discrete_log_problem (self, generator, constant): #Very Hard for Large N
        if generator not in self.primitives or constant not in self.elements:
            raise ValueError("Elements not in group")
        result = generator
        count = 1
        while (pow(result, count, self.n) != constant):
            count += 1
        return count
    
    def find_inverse (self, element):
        
        def extended_ea(x, y):
            if y == 0:
                return x, 1, 0
            gcd, s, t = extended_ea(y, x % y)
            return gcd, t, s - (x // y) * t
        
        if element not in self.elements:
            raise ValueError("Element not in group")
        
        gcd, x, _ = extended_ea(element, self.n)
        if gcd != 1:
            raise ValueError(f"No inverse exists for {element} modulo {self.n}")
        return x % self.n

    def print_subgroups (self):
        for order, subgroup in self.subgroups.items():
            print(f"Subgroup of order {order}: {subgroup}")
        
class DiffieHellman:
    
    def __init__ (self, prime):
        if not sympy.isprime(prime):
            self.prime = 5
            self.group = PrimeCyclicGroupMult(self.prime)
        else:
            self.group = PrimeCyclicGroupMult(prime)
            self.prime = prime
        self.alpha = random.choice(self.group.primitives)
    
    def create_public_key (self, private):
        if private not in self.group.elements:
            raise ValueError("Number not in group")
        return pow(self.alpha, private, self.prime)
    
    def create_shared_key (self, num1, private):
        if num1 not in self.group.elements or private not in self.group.elements:
            raise ValueError("Numbers not in group")
        return pow(num1, private, self.prime)
    
p = 467
alpha = 2
group = PrimeCyclicGroupMult(p)
a = 400
b = 134
public_A = pow(alpha, a, p)
public_B = pow(alpha, b, p)
print(f"Public Key A: {public_A}")
print(f"Public Key B: {public_B}")
shared_key_A = pow(public_B, a, p)
shared_key_B = pow(public_A, b, p)
print(f"Shared key A: {shared_key_A}")
print(f"Shared key B: {shared_key_B}")
