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


for idx, i in enumerate(range(194441, 196501)):
    if is_prime(i) and i % 100 == 93:
        print(idx + 1, i)

"""
753 195193
1053 195493
1153 195593
1453 195893
1753 196193
"""