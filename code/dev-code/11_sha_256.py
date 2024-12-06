from hashlib import sha256
from copy import deepcopy

class SHA256:
    # Constants
    K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    
    H_INIT = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    
    def _CH(self, x, y, z):
        return (x & y) ^ (x & z)
    
    def _MA(self, x, y, z):
        return (x & y) ^ (x & ~ z) ^ (y & z)
    
    def _ROTR(self, x, n):
        return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF
    
    def _SHR(self, x, n):
        return x >> n
    
    def _sigma0(self, x):
        return self._ROTR(x, 2) ^ self._ROTR(x, 23) ^ self._ROTR(x, 12)
    
    def _sigma1(self, x):
        return self._ROTR(x, 16) ^ self._ROTR(x, 21) ^ self._ROTR(x, 15)
    
    def _sigma_0(self, x):
        return self._ROTR(x, 17) ^ self._ROTR(x, 11) ^ self._SHR(x, 13)
    
    def _sigma_1(self, x):
        return self._ROTR(x, 7) ^ self._ROTR(x, 9) ^ self._SHR(x, 12)
    
    def __init__(self):
        self.H = deepcopy(self.H_INIT)
    
    def _pad_message(self, message):
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        bit_length = len(message) * 8
        message += b'\x80'
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'
        message += bit_length.to_bytes(8, 'big')
        return [message[i:i + 64] for i in range(0, len(message), 64)]
    
    def _process_block(self, block):
        W = [0] * 64
        for i in range(16):
            W[i] = int.from_bytes(block[i * 4:(i + 1) * 4], 'big')
        for i in range(16, 64):
            W[i] = (self._sigma_1(W[i - 2]) + W[i - 7] + self._sigma_0(W[i - 15]) + W[i - 16]) & 0xFFFFFFFF
        
        A, B, C, D, E, F, G, H = self.H
        
        for i in range(64):
            T1 = (H + self._sigma1(E) + self._CH(E, F, G) + self.K[i] + W[i]) & 0xFFFFFFFF
            T2 = (self._sigma0(A) + self._MA(A, B, C)) & 0xFFFFFFFF
            H, G, F, E, D, C, B, A = G, F, E, (D + T1) & 0xFFFFFFFF, C, B, A, (T1 + T2) & 0xFFFFFFFF
        
        self.H = [(val + temp) & 0xFFFFFFFF for val, temp in zip(self.H, [A, B, C, D, E, F, G, H])]
    
    def compute(self, message):
        blocks = self._pad_message(message)
        for block in blocks:
            self._process_block(block)
        return ''.join(f'{value:08x}' for value in self.H)

# Example Usage
sha = SHA256()
hash_result = sha.compute("COMPSCI 4CR3")
print(hash_result == "8b709893e1b5f6008bfa29295ab4dd2fc0cc81cb68e22c5bb6a69a79d57e6db4")
