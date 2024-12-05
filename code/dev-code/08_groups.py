# Author: Dev Mody
# Date: December 4th, 2024
# Description: Implemented Zn^* where n is prime

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
        subgroups = []
        subgroups.append(self.elements)
        marked = set()
        for order in self.orders.values():
            if order != len(self.elements) and order not in marked:
                subgroup = []
                for i in self.elements:
                    if self.orders[i] == order:
                        subgroup.append(i)
                for primitive in self.primitives:
                    subgroup.append(primitive)
                subgroups.append(subgroup)
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
    
    def discrete_log_problem (self, generator, constant):
        if generator not in self.primitives or constant not in self.elements:
            raise ValueError("Elements not in group")
        result = generator
        count = 1
        while (pow(result, count, self.n) != constant):
            count += 1
        return count
        
group = PrimeCyclicGroupMult(11)
print("Order:", group.orders)
print("All Generators:", group.primitives)  # Output: [2, 6, 7, 8]
print("All Subgroups:", group.subgroups)
print(group.is_generator(2))
print(group.derive_new_element(2, 9))
print(group.discrete_log_problem(2, 9))