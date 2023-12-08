from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    if 0 < n <= 10:
        return 1  # f(n - 1)
    if 10 < n < 100:
        return 2.2 * f(n - 3)
    return 1.7 * f(n - 2)


print(sum(map(int, str(int(f(40))))))  # 18
