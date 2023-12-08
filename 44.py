from functools import lru_cache


@lru_cache
def f(n):
    if n < 3:
        return 1
    if n % 2 == 0:
        return f(n - 1) + n - 1
    return f(n - 2) + 2 * n - 2


for i in range(34):
    f(i)

print(f(34))  # 578
