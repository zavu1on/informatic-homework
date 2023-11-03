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


for idx, i in enumerate(range(5336748, 5336835)):
    if is_prime(i):
        print(idx + 1, i)

"""
6 5336753
14 5336761
42 5336789
50 5336797
54 5336801
66 5336813
84 5336831
86 5336833
"""