from collections import Counter

def decrypt_caesar(ciphertext, key):
    """
    Decrypts a ciphertext encrypted with a Caesar cipher using the given key.
    """
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = (ord(char) - key - ord('a')) % 26
            decrypted += chr(shift + ord('a'))
        else:
            decrypted += char
    return decrypted

def frequency_analysis(ciphertext):
    """
    Performs frequency analysis on the ciphertext to determine the most common letter.
    """
    # Count occurrences of each letter
    letter_counts = Counter(ciphertext)
    # Sort letters by frequency in descending order
    sorted_counts = letter_counts.most_common()
    return sorted_counts

# Ciphertext provided
ciphertext = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"

# Perform frequency analysis
frequencies = frequency_analysis(ciphertext)
print("Letter frequencies:", frequencies)

# Assume the most frequent letter corresponds to 'e' (most common letter in English)
most_frequent_letter = frequencies[0][0]  # Most frequent letter in ciphertext
shift_key = (ord(most_frequent_letter) - ord('e')) % 26

print(f"Most frequent letter: {most_frequent_letter}")
print(f"Calculated key: {shift_key}")

# Decrypt the ciphertext using the determined key
plaintext = decrypt_caesar(ciphertext, shift_key)
print(f"Decrypted plaintext: {plaintext}")
