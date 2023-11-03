from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n ** 0.5 == int(n ** 0.5):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


for idx, i in enumerate(range(2532160, 2532000 - 1, -1)):
    if is_prime(i):
        print(161 - idx, i)

"""
158 2532157
144 2532143
138 2532137
114 2532113
110 2532109
108 2532107
84 2532083
72 2532071
68 2532067
8 2532007
"""