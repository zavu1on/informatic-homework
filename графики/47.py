for A in range(300):
    count = 0
    for x in range(1, 301):
        for y in range(1, 301):
            f = ((y - 20 < A) and (10 - x < A)) or (x * (y + 2) > 48)

            if f:
                count += 1

    if count == 300 ** 2:
        print(A)  # 27
        break
