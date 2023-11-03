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


for i in range(103_000_000, 104_000_001):
    n = i
    two_count = 0

    while i % 2 == 0:
        i //= 2
        two_count += 1

        if two_count > 2:
            break

    if two_count != 2:
        continue

    k = i ** 0.5
    if k == int(k) and is_prime(k):
        print(n, int(k))

"""
103103716 5077
103266244 5081
103510276 5087
103999204 5099
"""