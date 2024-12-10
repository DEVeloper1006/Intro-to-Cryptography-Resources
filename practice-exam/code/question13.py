pairs = [(32, 16), (6,415), (53, 83), (112, 45)]
n, e = (493, 205)
for x, s in pairs:
    if pow(s, e, n) == x:
        print((x, s), "Valid")
    
    
# Element a in Zp
# if a^k = len(Zp) then a is a generator
# if it is not, it is not a generator of Zp, but it is a generator in general. If k = 3. Then a is a generator of all subgroups of length 3.
