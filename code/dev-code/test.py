def galois_mult(a, b):
    p = 0  # Result of multiplication
    for _ in range(8):  # Loop over each bit
        if b & 1:  # If the least significant bit of b is set
            p ^= a  # XOR the result with a
        carry = a & 0x80  # Check if the highest bit of a is set
        a = (a << 1) & 0xFF  # Shift a to the left, keep it in one byte
        if carry:  # If carry is set, reduce modulo x^8 + x^4 + x^3 + x + 1 (0x11b)
            a ^= 0x11b
        b >>= 1  # Shift b to the right
    return p

# Test cases
print(hex(galois_mult(0x57, 0x83)))  # Expected: 0xc1
print(hex(galois_mult(0x02, 0x87)))  # Expected: 0x15
print(hex(galois_mult(0x01, 0x80)))  # Expected: 0x80
print(hex(galois_mult(0x53, 0xca)))  # Expected: 0x01
