"""
a = 2
b = 1
while a < 10:
    b = 1
    while b < 10:
        print(a*b)
        b = b + 1
    a = a + 1


a = 2
b = 1
while a < 10:
    b = 1
    while b < 10:
        print("{} x {} = {}". format(a, b, a * b))
        b = b + 1
    a = a + 1

import random
a = []
for i in range (10):
    b = random.randrange(-100, -1)
    a.append(b)
c = a[0]
for j in range(len(a)):
    d = a[j]
    if c < d:
        c = d
print("a", a)
print("c", c)
"""


a = int(input())
b = []
while  a != 1 or a != 0:
    b.append(a%2)
    if a%2 == 0:
        a = a/2
    if a%2 == 1:
        a = a/2 - 0.5
b.append(a)
print(b)
