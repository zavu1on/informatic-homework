for A in range(300):
    count = 0
    for x in range(300):
        for y in range(300):
            f = (x > 7) or (y > 4) or (x ** 2 + 3 * y < A)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 62
        break
