import hashlib

# Function to hash a number using SHA-256
def hash_number(number):
    # Convert the number to a byte representation
    number_bytes = str(number).encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the byte representation of the number
    sha256_hash.update(number_bytes)
    
    # Get the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

# Example usage:
number = 123456789
hashed_number = hash_number(number)
print(f"SHA-256 hash of {number}: {hashed_number}")
