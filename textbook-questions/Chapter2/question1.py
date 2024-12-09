class LetterStreamCipher:
    
    def __init__(self, key):
        self.key = key
        self.alphabet_dict = {
            'a': 0, 'b': 1, 'c': 2,
            'd': 3, 'e': 4, 'f': 5,
            'g': 6, 'h': 7, 'i': 8,
            'j': 9, 'k': 10, 'l': 11,
            'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17,
            's': 18, 't': 19, 'u': 20,
            'v': 21, 'w': 22, 'x': 23,
            'y':24, 'z':25
        }
        self.alphabet = list(self.alphabet_dict.keys())
    
    def encrypt (self, plaintext):
        if len(plaintext) != len(self.key):
            raise ValueError("Key must be the same length as the plaintext")
        ciphertext = ""
        for i in range(len(plaintext)):
            if plaintext[i] not in self.alphabet:
                raise ValueError("Plaintext must only contain letters")
            y_i = (self.alphabet_dict[plaintext[i]] + self.alphabet_dict[self.key[i]]) % 26
            ciphertext += self.alphabet[y_i]
        return ciphertext
    
    def decrypt (self, ciphertext):
        if len(ciphertext) != len(self.key):
            raise ValueError("Key must be the same length as the ciphertext")
        plaintext = ""
        for i in range(len(ciphertext)):
            if ciphertext[i] not in self.alphabet:
                raise ValueError("Ciphertext must only contain letters")
            y_i = (self.alphabet_dict[ciphertext[i]] - self.alphabet_dict[self.key[i]]) % 26
            plaintext += self.alphabet[y_i]
        return plaintext
                                                                    
key = "rsidpy dkawoa".replace(" ", "")

cipher = LetterStreamCipher(key)
ciphertext = "bsasppkkuosr"
plaintext = cipher.decrypt(ciphertext)
print(plaintext)  # Output: "secretmessage"
