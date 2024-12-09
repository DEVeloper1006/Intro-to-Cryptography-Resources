def euclid_gcd (a : int, b : int):
    while b != 0:
        a, b = b, a % b
        print(a, b)
    return a

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0  # gcd(a, b), x, y
    else:
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
A1,B1 = 7469, 2464
print(euclid_gcd(A1, B1))
A2,B2 = 2689, 4001
print(euclid_gcd(A2, B2))
A3,B3 = 286875, 333200
print(euclid_gcd(A3, B3))