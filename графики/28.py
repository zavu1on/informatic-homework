for A in range(300):
    count = 0
    for x in range(1, 301):
        for y in range(1, 301):
            f = (3 * y - 4 * x - 29 != 0) or (A < 2 * x ** 2 + 5) or (A < y ** 2 - 1)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 119
