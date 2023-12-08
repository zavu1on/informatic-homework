import sys

sys.setrecursionlimit(4000)


def f(n):
    if n == 1:
        return 1
    return 1 + n * f(n - 1)


print(f(1000) // f(997))  # 997002000
