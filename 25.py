from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 3
    if 0 < n <= 15:
        return 3  # f(n - 1)
    if 10 < n < 100:
        return 2.5 * f(n - 3)
    return 3.3 * f(n - 2)


print(str(f(100)).split('.')[1][0])  # 6