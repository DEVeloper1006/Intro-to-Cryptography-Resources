#Author: Dev Mody
#Date: December 3rd 2024
#Description: Uses os.urandom to construct a similar size TRNG-produced key to the plaintext and ciphertext to perform bitwise XORs to encrypt and decrypt

import os

class OneTimePad:
    
    def __init__ (self, key=None):
        self.key = key #sets the key
    
    # Does bitwise XOR with the TRNG produced key to encrypt
    def encrypt (self, plaintext):
        if self.key is None:
            self.key = os.urandom(len(plaintext))
        plaintext_bytes = plaintext.encode('utf-8')
        ciphertext = bytes([p ^ k for p,k in zip(plaintext_bytes, self.key)])
        return ciphertext
    
    # Does bitwise XOR with the TRNG produced key to decrypt
    def decrypt (self, ciphertext):
        if self.key is None:
            raise ValueError("Key not set")
        plaintext_bytes = bytes([c ^ k for c,k in zip(ciphertext, self.key)])
        return plaintext_bytes.decode('utf-8')
    
# Test Cases
otp = OneTimePad()
plaintext = "HELLO OTP"
ciphertext = otp.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted = otp.decrypt(ciphertext)
print("Decrypted text:", decrypted)