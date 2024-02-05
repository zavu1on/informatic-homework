for n in range(100):
    a = n ** 2 + 4 * n + 3
    b = int('25', 6)
    c = (n + 1) ** 2 + 3 * (n + 1) + 8

    if a + b == c:
        print(n)  # 8
