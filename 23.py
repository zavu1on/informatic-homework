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


def f(n):
    arr = []
    m = 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if m == 0:
                m = n // i

            arr.append(i)
            if n // i != i:
                arr.append(n // i)

            if len(arr) >= 6:
                break

    arr.sort()

    return arr[:3], m


count = 0
for i in range(100_000_000, 150_000_001):
    arr, m = f(i)

    if len(arr) == 3 and is_prime(arr[0]) and is_prime(arr[1]) and is_prime(arr[2]):
        print(i, m)
        count += 1

        if count == 7:
            break

"""
100000005 33333335
100000021 9090911
100000029 33333343
100000031 353357
100000050 50000025
100000051 636943
100000054 50000027
"""