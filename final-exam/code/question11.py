import random, sympy, math
from hashlib import sha256

# Groups Implementation
class PrimeCyclicGroupMult:
    
    # n should be a prime number
    def __init__ (self, n):
        self.n = n
        self.elements = [num for num in range(1, n)]
        self.orders = self.orders()
        self.primitives = self._find_primitives()
        self.subgroups = self._find_subgroups()
    
    # finds the orders dictionary
    def orders (self):
        orders = dict()
        for i in self.elements:
            orders[i] = self.find_order(i)
        return orders
    
    # Does modular exponentiation until we reach the identity element
    def find_order (self, a):
        if a not in self.elements:
            raise ValueError("Element not in group")
        result = a
        count = 1
        while pow(result, count, self.n) != 1:
            count += 1
        return count
    
    # Finds primitives by identifying which elements have order = len of the group
    def _find_primitives (self):
        primitives = []
        for i in self.elements:
            if self.orders[i] == len(self.elements):
                primitives.append(i)
        return primitives
    
    # FInds subgroups by grouping all orders
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
    
    # Finds modular inverse Extended Euclidean
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
            
p = 31
alpha = 3
beta = 17

group = PrimeCyclicGroupMult(p)
print(group.elements)
print(group.discrete_log_problem(3, 17))
print(group.discrete_log_problem(3, 13))