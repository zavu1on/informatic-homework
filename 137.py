def f(a):
    if a > 678:
        return 0
    if a == 678:
        return 1

    return f(a + 1) + f(int(f'2{a}'))


print(f(3))  # 616
