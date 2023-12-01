# 1 -> 15


def f(a, n=0):
    if a > 15:
        return 0
    if a == 15:
        return 1

    if n == 2:
        return f(a + 1) + f(a + 2)

    return f(a + 1) + f(a + 2) + f(a * 2, n + 1)


print(f(1))  # 1736