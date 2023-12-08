from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2) - 1
    return 2 + f(n - 1)


c = 0
for i in range(1001):
    if f(i) == 3:
        c += 1

print(c)  # 174