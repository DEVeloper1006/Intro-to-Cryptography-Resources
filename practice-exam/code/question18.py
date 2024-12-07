import math

t = (2**(101/2)) * math.sqrt(math.log((1 / (1 - 0.5)), math.e))

seconds = t / (2**30)
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
print(days)


