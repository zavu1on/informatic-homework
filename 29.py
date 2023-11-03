from math import sqrt

arr = []


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


for idx, i in enumerate(range(2532000, 2532161)):
    if is_prime(i):
        arr.append((idx + 1, i))

for i in arr[::3]:
    print(*i)
"""
8 2532007
84 2532083
114 2532113
158 2532157
"""
