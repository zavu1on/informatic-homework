from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return 1 + f(n - 1)
    return f(n // 2)


for i in range(1, 500):
    if f(i) == 4:
        print(i)

# 7 * 2 ** n
# 11 * 2 ** n
# 13 * 2 ** n
