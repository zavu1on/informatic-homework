from functools import lru_cache


@lru_cache
def f(n):
    if n <= 3:
        return n + 3
    if f(n - 1) % 2 == 0:
        return f(n - 2) + n
    return f(n - 2) + 2 * n


s = 0
for i in range(40, 51):
    s += f(i)

print(s)  # 8508