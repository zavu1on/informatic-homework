# 101 -> 101110


def f(a):
    if a == 101110:
        return 1
    elif a > 101110:
        return 0

    b = int(f'{a}', 2) + 1
    b = bin(b)[2:]

    return f(int(f'{a}0')) + f(int(f'{a}1')) + f(int(b))


print(f(101))  # 254