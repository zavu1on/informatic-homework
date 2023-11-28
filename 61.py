# 4 -> 8 -> 23

exclude = [11, 18]


def f(a, check=False):
    if a in exclude:
        return 0
    if a == 8:
        check = True
    if a == 23 and check:
        return 1
    if a == 23 and not check:
        return 0
    if a > 23:
        return 0

    return f(a + 1, check) + f(a + 2, check) + f(a * 3, check)


print(f(4))  # 400