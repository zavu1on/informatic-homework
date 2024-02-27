for A in range(300):
    count = 0
    for x in range(1, 301):
        for y in range(1, 301):
            f = (y + 4 * x != 120) or (x > A) or (y > A)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 23
