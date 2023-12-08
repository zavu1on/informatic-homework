from functools import lru_cache


@lru_cache
def f(n):
    if n < 3:
        return 1
    if sum(map(int, str(n))) % 2 == 0:
        return f(n - 1) - f(n - 2)
    return f(n - 1) + f(n // 2)


for i in range(100):
    f(i)

print(f(100))  # 23
