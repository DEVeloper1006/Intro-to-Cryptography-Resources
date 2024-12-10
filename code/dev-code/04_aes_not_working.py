S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

INVERSE_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

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

class AES:
    
    def __init__ (self, key):
        
        if len(key) not in [16, 24, 32]:
            raise ValueError("Key must be 16, 24 or 32 bytes long")
        self.key = key
        self.key_size = len(key)
        self.round_keys = self._organize_key(self._key_expansion())
    
    # def galois_mult(a, b):
    #     p = 0  # Result of multiplication
    #     for _ in range(8):  # Loop over each bit
    #         if b & 1:  # If the least significant bit of b is set
    #             p ^= a  # XOR the result with a
    #         carry = a & 0x80  # Check if the highest bit of a is set
    #         a = (a << 1) & 0xFF  # Shift a to the left, keep it in one byte
    #         if carry:  # If carry is set, reduce modulo x^8 + x^4 + x^3 + x + 1 (0x11b)
    #             a ^= 0x11b
    #         b >>= 1  # Shift b to the right
    #     return p
    
    def _sub_bytes(self, state, inverse=False):
        s_box = INVERSE_S_BOX if inverse else S_BOX
        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] = s_box[state[i][j]]
        return state
    
    def _shift_rows(self, state, inverse=False):
        shifts = [0, 3, 2, 1]
        for i in range(len(state)):
            shift = shifts[i] if not inverse else -shifts[i]
            
            state[i] = state[i][-shift % 4:] + state[i][:-shift % 4]
        
        return state
    
    def _mix_columns(self, state, inverse=False):
        if inverse:
            mix_matrix = [
                [14, 11, 13, 9],
                [9, 14, 11, 13],
                [13, 9, 14, 11],
                [11, 13, 9, 14],
            ]
        else:
            mix_matrix = [
                [2, 3, 1, 1],
                [1, 2, 3, 1],
                [1, 1, 2, 3],
                [3, 1, 1, 2],
            ]
        # Initialize result as a 4x4 matrix
        result = [[0] * 4 for _ in range(4)]
    
        # Perform the mix operation column by column
        for c in range(4):
            for r in range(4):
                # Calculate new value for each element in the column
                gf = GaloisField()
                sum_num = 0
                for i in range(4):
                    A = state[i][c]
                    B = mix_matrix[r][i]
                    sum_num += gf.poly_to_num(gf.multiply(gf.num_to_poly(A), gf.num_to_poly(B)))
                result[r][c] = sum_num & 0xFF
        return result
    
    def _add_round_key(self, state, round_key):
        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] ^= round_key[i][j] & 0xFF
        return state
    
    def _key_expansion(self):
        key_size = len(self.key)  # Key size in bytes (16, 24, or 32 bytes)
        num_rounds = 10 if key_size == 16 else 12 if key_size == 24 else 14
        num_words = key_size // 4  # Words in the original key

        # Initialize the round keys with the original key
        round_keys = [self.key[i:i+4] for i in range(0, len(self.key), 4)]

        for i in range(num_words, (num_rounds + 1) * 4):
            temp = round_keys[-1]  # Last word of the current key schedule
            if i % num_words == 0:
                temp = self._sub_word(self._rotate_word(temp))
                temp[0] ^= Rcon[i // num_words - 1]
            elif key_size == 32 and i % num_words == 4:
                temp = self._sub_word(temp)
            round_keys.append([
                (round_keys[i - num_words][j] ^ temp[j]) & 0xFF for j in range(4)
            ])

        return round_keys
    
    def _organize_key (self, expanded_keys):
        rounds = len(expanded_keys) // 4  # Number of rounds
        keys = [expanded_keys[i * 4: (i + 1) * 4] for i in range(rounds)]
        return keys

    def _sub_word(self, word):
        result = []
        for b in word:
            result.append(S_BOX[b & 0xFF])  # Ensure b is within 0-255
        return result

    def _rotate_word(self, word):
        return word[1:] + [word[0]]
    
    def encrypt_block(self, plaintext):
        state = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]
        
        state = self._add_round_key(state, self.round_keys[0])

        # Rounds 1 to Nr-1
        for i in range(1, len(self.round_keys) - 1):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, self.round_keys[i])

        # Final round
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        state = self._add_round_key(state, self.round_keys[-1])

        result = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                result.append(state[i][j])

        return result
    
    def decrypt_block (self, ciphertext):
        state = [ciphertext[i:i + 4] for i in range(0, len(ciphertext), 4)]
        state = self._add_round_key(state, self.round_keys[-1])

        for i in range(len(self.round_keys) - 2, 0, -1):
            state = self._shift_rows(state, inverse=True)
            state = self._sub_bytes(state, inverse=True)
            state = self._add_round_key(state, self.round_keys[i])
            state = self._mix_columns(state, inverse=True)

        state = self._shift_rows(state, inverse=True)
        state = self._sub_bytes(state, inverse=True)
        state = self._add_round_key(state, self.round_keys[0])

        return [byte for row in state for byte in row]
    
plaintext = [
    0x32, 0x43, 0xf6, 0xa8,
    0x88, 0x5a, 0x30, 0x8d,
    0x31, 0x31, 0x98, 0xa2,
    0xe0, 0x37, 0x07, 0x34
]  # Example plaintext (16 bytes)

key = [
    0x2b, 0x7e, 0x15, 0x16,
    0x28, 0xae, 0xd2, 0xa6,
    0xab, 0xf7, 0xcf, 0x8a,
    0x3c, 0x4f, 0x1d, 0x4f
]  # AES-128 key (16 bytes)

expected_ciphertext = [
    0x39, 0x25, 0x84, 0x1d,
    0x02, 0xdc, 0x09, 0xfb,
    0xdc, 0x11, 0x85, 0x97,
    0x19, 0x6a, 0x0b, 0x32
]  # Expected ciphertext

aes = AES(key)
ciphertext = aes.encrypt_block(plaintext)
print([hex(num) for num in ciphertext])
print([hex(num) for num in aes.decrypt_block(ciphertext)])