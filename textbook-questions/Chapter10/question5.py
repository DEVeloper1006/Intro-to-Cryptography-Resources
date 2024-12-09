n, e = 9797, 131

signatures = [(123, 6292), (4333, 4768), (4333, 1424)]

for signature in signatures:
    x, s = signature
    print(pow(s, e, n) == x)