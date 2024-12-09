class GaloisField:
    def __init__(self, m=8, irreducible_poly=0x11b):
        self.m = m
        self.irreducible_poly = self.num_to_poly(irreducible_poly)
        self.size = 2**m
        self.elements = self._generate_elements()
        
    def num_to_poly(self, num):
        return [int(x) for x in bin(num)[2:].zfill(8)]    
        
    def poly_to_num (self, poly):
        return int("".join(map(str, poly)), 2)
        
    def _generate_elements (self) -> list:
        elements = []
        for value in range(self.size):
            # Convert integer value to bit list of size m
            bit_list = [(value >> i) & 1 for i in reversed(range(self.m))]
            elements.append(bit_list)
        return elements
    
    def add (self, A : list, B : list) -> list:
        if A not in self.elements or B not in self.elements:
            raise ValueError("Both elements must be in the field")
        result = []
        for i in range(self.m):
            result.append((A[i] + B[i]) % 2)
        return result
        
    def multiply (self, A : list, B : list) -> list:
        if A not in self.elements or B not in self.elements:
            raise ValueError("Both elements must be in the field")
        product = [0] * (2 * self.m - 1)

        # Polynomial multiplication
        for i, ai in enumerate(reversed(A)):
            for j, bi in enumerate(reversed(B)):
                product[-(i + j + 1)] ^= ai & bi  # XOR for GF(2)

        # Reduce modulo the irreducible polynomial
        return self._reduce(product)
    
    def _reduce (self, poly : list):
        poly_degree = len(poly) - 1
        while poly_degree >= self.m:
            if poly[0] == 1:  # Leading term is non-zero
                # Subtract the irreducible polynomial shifted to align with poly's degree
                for i in range(len(self.irreducible_poly)):
                    poly[i] ^= self.irreducible_poly[i]
            # Remove the leading zero (shift left)
            poly.pop(0)
            poly_degree -= 1

        # Pad with zeros if necessary
        return [0] * (self.m - len(poly)) + poly
    
    def element_to_str(self, a : list):
        terms = []
        for i, coeff in enumerate(a):
            if coeff:
                power = self.m - i - 1
                if power == 0:
                    terms.append("1")
                elif power == 1:
                    terms.append("x")
                else:
                    terms.append(f"x^{power}")
        return " + ".join(terms) if terms else "0"

gf = GaloisField(3, [1,0,1,1])
for A in gf.elements:
    print()
    for B in gf.elements:
        print(f"{A} * {B} = {gf.multiply(A, B)}")
    print()
        
        
        
        # x (x + 1) = x^2 + x
        # x (x^2 + x) = x^3 + x^2
        # x (x^2 + x + 1) = x^3 + x^2 + x