# 8 -> 96 -> 3456


def f(a, check=False):
    if a == 96:
        check = True
    if a == 3456 and check:
        return 1
    if a == 3456 and not check:
        return 0
    if a > 3456:
        return 0

    return f(a * 2, check) + f(a * 3, check)


print(f(8))  # 18