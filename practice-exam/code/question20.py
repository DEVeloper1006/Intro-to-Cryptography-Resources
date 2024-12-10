import sympy

def part_a ():
    print("Key Generation")
    p = 59
    q = 29
    alpha = 3
    d = 23
    beta = pow(alpha, d, p)
    print("Beta:", beta)
    print("Signing Process")
    h_x = 17
    k_e = 25
    k_e_inv = sympy.mod_inverse(k_e, q)
    print("K_E Inverse:", k_e_inv)
    r = pow(alpha, k_e, p) % q
    s = ((h_x + d * r) * k_e_inv) % q
    print("Output:", h_x, (r, s))
    print("Verification Process")
    w = sympy.mod_inverse(s, q)
    print("W:", w)
    u1 = (h_x * w) % q
    u2 = (r * w) % q
    print("U1:", u1)
    print("U2:", u2)
    v = (((alpha ** u1) * (beta ** u2)) % p) % q
    print("V:", v)
    print("Verification:", v % q == r)
    
def part_b ():
    print("Key Generation")
    p = 59
    q = 29
    alpha = 3
    d = 23
    beta = pow(alpha, d, p)
    print("Beta:", beta)
    print("Signing Process")
    h_x = 2
    k_e = 13
    k_e_inv = sympy.mod_inverse(k_e, q)
    print("K_E Inverse:", k_e_inv)
    r = pow(alpha, k_e, p) % q
    s = ((h_x + d * r) * k_e_inv) % q
    print("Output:", h_x, (r, s))
    print("Verification Process")
    w = sympy.mod_inverse(s, q)
    print("W:", w)
    u1 = (h_x * w) % q
    u2 = (r * w) % q
    print("U1:", u1)
    print("U2:", u2)
    v = (((alpha ** u1) * (beta ** u2)) % p) % q
    print("V:", v)
    print("Verification:", v % q == r)
    
print("\nPart A:\n")
part_a()
print("\nPart B:\n")
part_b()
    
