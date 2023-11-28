# 3 -> 12 -> 25


def f(a, check=False):
    if a == 12:
        check = True
    if a == 25 and check:
        return 1
    if a == 25 and not check:
        return 0
    if a > 25:
        return 0

    return f(a + 2, check) + f(a + 3, check) + f(int(f'{a}1'), check)


print(f(3))  # 80