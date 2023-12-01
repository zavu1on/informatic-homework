def f(a, s=0, m=0):
    if a == 157:
        if m > s:
            return 1
        return 0
    if a > 157:
        return 0

    return f(a + 1, s + 1, m) + f(a * 2, s, m + 1) + f(a * 3, s, m + 1)


print(f(1))  # 113
