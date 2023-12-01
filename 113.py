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


count = 0


def f(a, b, n=0):
    global count

    if n == 5:
        if is_prime(a) and is_prime(b):
            count += 1
        return

    for x in '01':
        for y in '01':
            start = 0
            end = 0
            if x == '0':
                start = a + 3
            elif x == '1':
                start = a * 4

            if y == '0':
                end = b + 5
            elif y == '1':
                end = b * 2

            f(start, end, n + 1)


f(2, 3)
print(count)  # 35