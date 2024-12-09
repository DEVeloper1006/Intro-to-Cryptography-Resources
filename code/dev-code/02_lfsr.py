#Author: Dev Mody
#Date: December 3rd, 2024
#Description: This code implements the General LFSR from the Textbook and performs a Known-Plaintext Attack given known plaintext, degree and keystream

import numpy as np

class StreamCipherLFSR:
    def __init__(self, coefficients, initial_seed):
        self.coefficients = coefficients
        self.initial_seed = initial_seed
        self.initial_seed.reverse() #s0s1s2...
        self.coefficients.reverse() #p0p1p2...
        
    def generate_key_stream(self, num_bits):
        lfsr = self.initial_seed[:]
        key_stream = []
        print(lfsr)
        for _ in range(num_bits):
            feedback_bit = 0
            for i in range(len(self.initial_seed)):
                if self.coefficients[i] == 1:
                    feedback_bit ^= lfsr[i]
                    print(feedback_bit)
            temp = lfsr.pop(0)
            key_stream.append(temp)# Remove the oldest bit
            lfsr.append(feedback_bit)       # Append the feedback bit to the LFSR
            print(lfsr)
        return key_stream
    
class LFSRAnalyzer:
    
    @staticmethod
    def recover_coeff(key_stream, degree):
        num_equations = degree
        equations = np.zeros((num_equations, degree), dtype=int)
        for i in range(num_equations):
            equations[i] = key_stream[i:i + degree]
        results = np.array(key_stream[degree:], dtype=int)  # Convert to NumPy array

        # Gaussian Elimination Mod 2
        for i in range(degree):
            if equations[i, i] == 0:  # Swap rows if the pivot is zero
                for j in range(i + 1, num_equations):
                    if equations[j, i] == 1:
                        equations[[i, j]] = equations[[j, i]]
                        results[[i, j]] = results[[j, i]]  # NumPy indexing
                        break
            for j in range(i + 1, num_equations):
                if equations[j, i] == 1:
                    equations[j] ^= equations[i]
                    results[j] ^= results[i]

        # Back-substitution
        coefficients = np.zeros(degree, dtype=int)
        for i in range(degree - 1, -1, -1):
            coefficients[i] = results[i]
            for j in range(i + 1, degree):
                coefficients[i] ^= equations[i, j] * coefficients[j]
        return coefficients.tolist()
    
class MatrixValidator:
    @staticmethod
    def construct_matrix_A (key_stream):
        A = [key_stream[i:i + 20][::-1] for i in range(20)]
        b = key_stream[20:40][::-1]
        return np.array(A, dtype=int), np.array(b, dtype=int)
    
def encrypt(plaintext, key_stream):
    if len(plaintext) != len(key_stream): raise ValueError("ERROR.")
    return [plaintext[i] ^ key_stream[i] for i in range(len(plaintext))]

def decrypt(ciphertext, key_stream):
    if len(ciphertext) != len(key_stream): raise ValueError("ERROR.")
    return [ciphertext[i] ^ key_stream[i] for i in range(len(ciphertext))]

# coefficients = [1, 1, 0, 0, 1]
# initial_seed = [0, 1, 0, 1, 1]
# initial_seed.reverse()

coefficients = [1, 0, 1]
initial_seed = [1, 0, 0]

lfsr = StreamCipherLFSR(coefficients, initial_seed)
key_stream = lfsr.generate_key_stream(5)
print(key_stream)  # Should output [1, 0, 0, 1, 0]

# # Define coefficients, initial seed, and plaintext
# coefficients = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
# initial_seed = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
# plain_text = [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0,
#                 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1,
#                 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]

# # Stream cipher instance
# cipher = StreamCipherLFSR(coefficients, initial_seed)
# key_stream = cipher.generate_key_stream(len(plain_text))

# # Encrypt plaintext
# cipher_text =encrypt(plain_text, key_stream)
# print(f"Ciphertext: {cipher_text}")

# # Decrypt ciphertext
# decrypted_text = decrypt(cipher_text, key_stream)
# print(f"Decrypted Text: {decrypted_text}")

# # Validate decryption
# print(f"Decryption successful: {decrypted_text == plain_text}")

# # Known-plaintext attack
# analyzer = LFSRAnalyzer()
# recovered_coefficients = analyzer.recover_coeff(key_stream, len(initial_seed))
# print(f"Recovered Coefficients: {recovered_coefficients}")
# print(f"Correct Coefficients: {recovered_coefficients == coefficients}")

# # Validate matrix construction
# validator = MatrixValidator()
# A, b = validator.construct_matrix_A(key_stream)
# print(f"A matrix:\n{A}")
# print(f"b vector:\n{b}")