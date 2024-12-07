from math import gcd

def modular_inverse (a, m):
    if gcd(a, m) != 1:
        raise ValueError(f"No Modular Inverse Exists for a={a} and m={m}")
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

class AffineCipher:
    
    def __init__ (self, mult_key, add_key):
        if mult_key < 1 or add_key < 1 or gcd(mult_key, 26) != 1: #mult_key must have a multiplicative inverse
            raise ValueError("Error.")
        self.mult_key = mult_key 
        self.add_key = add_key
        self.m = 26
        self.mod_inv = modular_inverse(mult_key, self.m)
    
    # C = (aP + b) mod m
    def encrypt (self, plaintext):
        return ''.join(chr((self.mult_key * (ord(char) - ord('A')) + self.add_key) % self.m + ord('A')) if char.isalpha() else char for char in plaintext.upper())
    
    # P = ((C - b) * a^-1) mod m
    def decrypt (self, ciphertext):
        return ''.join(chr((self.mod_inv * (ord(char) - ord('A') - self.add_key)) % self.m + ord('A')) if char.isalpha() else char for char in ciphertext.upper())
    
ciphertext = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
cipher = AffineCipher(7, 22)
print(cipher.decrypt(ciphertext)) #falszztysyjzyjky

