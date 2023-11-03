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


c = 0
for i in range(3661, 33626):
    k = i ** 0.5
    if k == int(k) and is_prime(k):
        c += 1

print(c)  # 25