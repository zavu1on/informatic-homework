def f(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return f(n // 2) + 1
    return f(n - 3) + 3


for i in range(5000):
    if f(i) == 31:
        print(i)  # 893
        break