# Author: Dev Mody
# Date: December 4th, 2024
# Description: Trying to work out a way to implement Galois Extension Field Multiplication, Modular Inverse, ...
import numpy as np

def number_to_bin_arr (num):
    return np.array([int(b) for b in bin(num)[2:]])

def bin_multiply(a, b):
    result = np.zeros(len(a) + len(b) - 1, dtype=int)
    
    # Multiply and add at the correct index
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
            result[i + j] %= 2  # Keep values in GF(2)
    
    return result

def bin_addition(a, b):
    # Make the arrays the same length by padding with leading zeros if necessary
    max_len = max(len(a), len(b))
    a = np.pad(a, (max_len - len(a), 0), 'constant', constant_values=0)
    b = np.pad(b, (max_len - len(b), 0), 'constant', constant_values=0)
    return np.bitwise_xor(a, b)  # XOR for GF(2) addition

def poly_divide(dividend, divisor):
    # Perform polynomial division of dividend by divisor in GF(2)
    # The degree of dividend and divisor should be considered
    dividend = np.copy(dividend)
    divisor_degree = len(divisor) - 1
    dividend_degree = len(dividend) - 1
    
    # Keep dividing the highest term of dividend by divisor
    while dividend_degree >= divisor_degree:
        # The coefficient of the highest degree term
        if dividend[0] == 1:
            # Shift divisor to align with the highest term of dividend
            shift = dividend_degree - divisor_degree
            # Subtract (XOR) the shifted divisor from the dividend
            divisor_shifted = np.pad(divisor, (shift, 0), 'constant', constant_values=0)
            dividend = bin_addition(dividend, divisor_shifted)
        
        # Update degrees
        dividend_degree = len(dividend) - 1
        # Remove leading zeroes
        dividend = dividend[dividend[0] == 1:]  # Only keep relevant bits
        dividend_degree = len(dividend) - 1
    
    return dividend  # This is the remainder

def overflow_check_and_remainder(a, b, m, irreducible_poly):
    # Step 1: Perform multiplication
    product = bin_multiply(a, b)
    print(f"Initial product: {product}")

    # Step 2: Check for overflow by comparing the degree with m
    if len(product) >= m:
        print(f"Overflow detected. Reducing modulo the irreducible polynomial.")
        remainder = poly_divide(product, irreducible_poly)
        print(f"Remainder after division: {remainder}")
    else:
        print(f"No overflow detected.")
        remainder = product
    
    return remainder

a = 13
b = 6
m = 4  # GF(2^4)

# Convert numbers to binary arrays
a_bin = number_to_bin_arr(a)
b_bin = number_to_bin_arr(b)

# Irreducible polynomial for GF(2^4), e.g., P = x^4 + x + 1
irreducible_poly = np.array([1, 0, 0, 1, 1])  # Represents x^4 + x + 1

# Perform the check and find the remainder
remainder = overflow_check_and_remainder(a_bin, b_bin, m, irreducible_poly)


