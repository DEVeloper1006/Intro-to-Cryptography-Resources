#Author: Dev Mody
#Date: December 4th 2024
#Description: Performs GCD via EA and EEA

def euclid_gcd (a : int, b : int):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0  # gcd(a, b), x, y
    else:
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
# Example usage
num1 = 987654321987654321
num2 = 123456789123456789

gcd_result = euclid_gcd(num1, num2)
print(f"The gcd of {num1} and {num2} is: {gcd_result}")

num1 = 987654321987654321
num2 = 123456789123456789

gcd_result, x, y = extended_euclid(num1, num2)
print(f"The gcd of {num1} and {num2} is: {gcd_result}")
print(f"The coefficients x and y are: x = {x}, y = {y}")

print(extended_euclid(112, 86))