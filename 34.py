for n in range(100):
    a = n ** 2 + 5 * n + 4
    b = int('35', 9)
    c = (n + 1) ** 2 + 7 * (n + 1)

    if a + b == c:
        print(n)  # 7
