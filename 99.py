# 2 -> 11 -> 26

exclude = [21]


def f(start, stop):
    if start in exclude or start > stop:
        return 0
    if start == stop:
        return 1

    if start % 2 == 0:
        n = start + 2
    else:
        n = start + 1

    return f(start + 1, stop) + f(start + 4, stop) + f(start + n, stop)


print(f(2, 11) * f(11, 26))  # 493