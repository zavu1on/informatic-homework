for A in range(300):
    count = 0
    for x in range(1, 301):
        for y in range(1, 301):
            f = (2 * y + 4 * x != 100) or (A < 9 * x) or (A < 3 * y)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 89
