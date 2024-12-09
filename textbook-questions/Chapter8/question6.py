p = 467
alpha = 4

private_keys = [(400, 134), (167, 134)]
for a,b in private_keys:
    A = pow(alpha, a, p)
    B = pow(alpha, b, p)
    print(f"A = {A}, B = {B}")
    shared_A = pow(B, a, p)
    shared_B = pow(A, b, p)
    print(f"Shared A = {shared_A}, Shared B = {shared_B}")
    
    