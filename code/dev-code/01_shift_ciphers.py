#Author: Dev Mody
#Date: December 3rd, 2024
#Description: Implements Shift and Affine Cipher from Chapter 1 of the Cryptography Textbook

from math import gcd

def modular_inverse (a, m):
    if gcd(a, m) != 1:
        raise ValueError(f"No Modular Inverse Exists for a={a} and m={m}")
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

#Shift Cipher for the Alphabet
class ShiftCipher:
    
    def __init__(self, shift_key):
        if shift_key < 1:
            raise ValueError("Error.")
        self.shift_key = shift_key #Used as the additive key
        self.m = 26
    
    # C = (P + k) mod m
    def encrypt (self, plaintext):
        return ''.join(chr((ord(char) - ord('A') + self.shift_key) % self.m + ord('A')) if char.isalpha() else char for char in plaintext.upper())
    
    # P = (C - k) mod m
    def decrypt (self, ciphertext):
        return ''.join(chr((ord(char) - ord('A') - self.shift_key) % self.m + ord('A')) if char.isalpha() else char for char in ciphertext.upper())

#Affine Cipher for the Alphabet
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
    
def test_ciphers():
    # Test Shift Cipher
    print("Testing Shift Cipher...")
    shift_key = 3
    shift_cipher = ShiftCipher(shift_key)
    plaintext = "HELLO"
    shift_encrypted = shift_cipher.encrypt(plaintext)
    print(f"Plaintext: {plaintext}")
    print(f"Shift Encrypted (key={shift_key}): {shift_encrypted}")  # Expected: KHOOR
    print(f"Shift Decrypted: {shift_cipher.decrypt(shift_encrypted)}")  # Expected: HELLO
    print()
    
    # Test Affine Cipher
    print("Testing Affine Cipher...")
    mult_key = 5
    add_key = 8
    affine_cipher = AffineCipher(mult_key, add_key)
    plaintext = "CRYPTO"
    affine_encrypted = affine_cipher.encrypt(plaintext)
    print(f"Plaintext: {plaintext}")
    print(f"Affine Encrypted (a={mult_key}, b={add_key}): {affine_encrypted}")  # Example expected: UXJLZT
    print(f"Affine Decrypted: {affine_cipher.decrypt(affine_encrypted)}")  # Expected: CRYPTO

test_ciphers()
