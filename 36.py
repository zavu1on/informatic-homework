from math import sqrt
from functools import lru_cache


@lru_cache
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


resp = []
m = 0
for i in range(2, 20001):
    arr = []

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if is_prime(j):
                arr.append(j)
            k = i // j
            if k != j and is_prime(k):
                arr.append(k)

    if len(arr) > m:
        resp = [(i, arr)]
        m = len(arr)
    elif len(arr) == m:
        resp += [(i, arr)]

m = min(resp, key=lambda el: el[0])
print(m[0], len(m[1]))
"""
2310 5
"""