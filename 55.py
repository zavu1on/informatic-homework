from functools import lru_cache


@lru_cache
def f(n):
    if n < 4 or n % 2 == 1:
        return n

    return f(n - 1) + f(n - 2) + f(n - 3)


for n in range(2009):
    f(n)

print(f(2008) - f(2006))  # 4012
