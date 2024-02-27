def D(n, m):
    return n % m == 0


for A in range(1, 300):
    count = 0
    for x in range(1, 301):
        f = ((D(x, 36) and D(x, 42)) <= D(x, A)) and (A * (A - 25) < 25 * (A + 200))

        if f:
            count += 1

    if count == 300:
        print(A)  # 84
