from functools import lru_cache
from math import sqrt


@lru_cache
def f(n: int):
    if sqrt(n) % 1 == 0:
        return sqrt(n)

    return f(n + 1) + 1


for n in range(5001):
    f(n)

print(f(4850) + f(5000))  # 232