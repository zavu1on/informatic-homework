from functools import lru_cache


@lru_cache
def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return f(n - 1) + 11 * n
    return 11 * f(n - 2) + n


s = 0
for i in range(35, 51):
    r = f(i)
    if r % 2 == 0:
        s += r

print(len(str(s)))  # 25