import random

a = random.randint(100, 1000000)
b = random.randint(100, 1000000)
p = random.randint(100, 1000000)
g = random.randint(100, 1000000)

A = pow(g, a, p)
B = pow(g, b, p)

XA = pow(B, a, p)
XB = pow(A, b, p)

print(A)
print(B)
print(XA)
print(XB)