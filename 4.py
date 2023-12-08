def f(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return f(n // 2) + 1
    return f(n - 3) + 3


c = 0
for i in range(1, 10 ** 5 + 1):
    if f(i) == 12:
        c += 1

print(c)  # 26