# 1 -> 10 -> 20
from math import factorial


def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1

    return f(start + 1, stop) + f(start + 4, stop) + f(start + factorial(start), stop)


print(f(1, 10) * f(10, 20))  # 378