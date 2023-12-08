from functools import lru_cache


@lru_cache
def f(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 == 1:
        return n

    return f(n - 1) + f(n - 2) + f(n - 3)


for n in range(2255):
    f(n)

print(f(2254) - f(2252))  # 4504
