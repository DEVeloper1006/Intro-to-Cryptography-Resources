pairs = [(32, 16), (6,415), (53, 83), (112, 45)]
n, e = (493, 205)
for x, s in pairs:
    if pow(s, e, n) == x:
        print((x, s), "Valid")
    