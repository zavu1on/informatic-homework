for A in range(300):
    count = 0
    for x in range(1, 301):
        for y in range(1, 301):
            f = (5 * y - x > A) or (2 * x + 3 * y < 90) or (y - 2 * x < -50)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 19
