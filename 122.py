# 46 -> 32 -> 12 -> 2


def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1

    if a ** 0.5 % 1 == 0:
        return f(a - 2, b) + f(a - 4, b) + f(a - 2, b) + f(int(a ** 0.5), b)

    return f(a - 2, b) + f(a - 4, b)


print(f(46, 32) * f(32, 12) * f(12, 2))  # 64206